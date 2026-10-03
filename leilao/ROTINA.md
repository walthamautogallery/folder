# Rotina diária — o que a sessão agendada faz (seg–sex)

1. Clona `walthamautogallery/folder` (branch `claude/loving-davinci-vhz3e9`) e lê `leilao/PLAYBOOK.md` + `leilao/config.example.json`.
2. Varre inventário público de ADESA Clear, OPENLANE e ACV (web search/fetch) dentro dos filtros.
3. Para cada candidato: recalls NHTSA (`api.nhtsa.gov`), decodificação VIN (`vpic.nhtsa.dot.gov`), problemas crônicos do modelo, comparáveis de varejo em Greater Boston, estimativa de lance máximo.
4. Monta o relatório em `leilao/relatorio_modelo.md` (máx. 10 carros) e envia com `python3 leilao/enviar_whatsapp.py`.
5. Se algo bloquear (rede, secrets, falta de dados), envia mesmo assim um WhatsApp curto dizendo **o que** bloqueou — nunca falha em silêncio.

## Pré-requisitos (uma vez só)

**Secrets do ambiente cloud:** `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_FROM` e (recomendado) `TWILIO_CONTENT_SID`.

**Domínios liberados na rede (Custom → Allowed domains):**
`api.twilio.com`, `adesa.com`, `*.adesa.com`, `openlane.com`, `*.openlane.com`, `acvauctions.com`, `*.acvauctions.com`, `api.nhtsa.gov`, `vpic.nhtsa.dot.gov`, `www.nhtsa.gov`, `www.cargurus.com`, `www.cars.com`, `www.edmunds.com`, `www.kbb.com`, `www.consumerreports.org`

**Template WhatsApp:** mensagem iniciada pela empresa fora da janela de 24h exige template aprovado pela Meta. Criar na Twilio (Content Template Builder), categoria *Utility*, ex.:
> Bom dia! Oportunidades de leilão de {{1}}: {{2}}

e colocar o SID (`HX...`) em `TWILIO_CONTENT_SID`.
