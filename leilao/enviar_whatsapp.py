#!/usr/bin/env python3
"""Envia o relatório diário de leilão via Twilio WhatsApp API (só stdlib).

Variáveis de ambiente (secrets do ambiente cloud):
  TWILIO_ACCOUNT_SID   - SID da conta (AC...)
  TWILIO_AUTH_TOKEN    - Auth token
  TWILIO_WHATSAPP_FROM - número WhatsApp aprovado na Twilio, ex: +16175551234
  WHATSAPP_TO          - destino (padrão: +18572698256)
  TWILIO_CONTENT_SID   - opcional: template aprovado (HX...) para mensagens fora
                         da janela de 24h. Variáveis: {{1}} data, {{2}} resumo.

Uso:
  python3 enviar_whatsapp.py relatorio.txt            # envia
  python3 enviar_whatsapp.py relatorio.txt --dry-run  # só mostra as partes
"""
import base64
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date

LIMITE = 1500  # Twilio aceita 1600 chars por mensagem de WhatsApp; deixa folga


def dividir(texto, limite=LIMITE):
    """Quebra o relatório em partes, preferindo cortar entre blocos de carro."""
    partes, atual = [], ""
    for bloco in texto.split("━━━━━━━━━━━━━━"):
        bloco = bloco.strip("\n")
        if not bloco:
            continue
        candidato = f"{atual}\n━━━━━━━━━━━━━━\n{bloco}" if atual else bloco
        if len(candidato) <= limite:
            atual = candidato
            continue
        if atual:
            partes.append(atual)
        while len(bloco) > limite:
            corte = bloco.rfind("\n", 0, limite)
            corte = corte if corte > 0 else limite
            partes.append(bloco[:corte])
            bloco = bloco[corte:].lstrip("\n")
        atual = bloco
    if atual:
        partes.append(atual)
    total = len(partes)
    return [f"({i}/{total})\n{p}" if total > 1 else p for i, p in enumerate(partes, 1)]


def enviar(campos):
    sid = os.environ["TWILIO_ACCOUNT_SID"]
    token = os.environ["TWILIO_AUTH_TOKEN"]
    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
    req = urllib.request.Request(url, data=urllib.parse.urlencode(campos).encode())
    req.add_header("Authorization", "Basic " + base64.b64encode(f"{sid}:{token}".encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as resp:
        dados = json.load(resp)
    print(f"enviado: {dados.get('sid')} status={dados.get('status')}")
    return dados


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    texto = open(sys.argv[1], encoding="utf-8").read().strip()
    partes = dividir(texto)
    if "--dry-run" in sys.argv:
        for p in partes:
            print(p, f"\n--- {len(p)} chars ---\n")
        return

    base = {
        "From": "whatsapp:" + os.environ["TWILIO_WHATSAPP_FROM"],
        "To": "whatsapp:" + os.environ.get("WHATSAPP_TO", "+18572698256"),
    }
    content_sid = os.environ.get("TWILIO_CONTENT_SID")
    if content_sid:
        # Template aprovado abre a conversa mesmo fora da janela de 24h.
        resumo = " ".join(texto.splitlines()[1:3])[:900]
        enviar({**base, "ContentSid": content_sid,
                "ContentVariables": json.dumps({"1": date.today().strftime("%d/%m"), "2": resumo})})
    for p in partes:
        enviar({**base, "Body": p})


if __name__ == "__main__":
    main()
