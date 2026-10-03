# Rotina diária — o que a sessão agendada faz (seg–sex)

1. Clona `walthamautogallery/folder` (branch `claude/loving-davinci-vhz3e9`) e lê `leilao/PLAYBOOK.md` + `leilao/config.example.json`.
2. **Lê o Gmail** (conector Gmail da rotina) com as buscas de `config.example.json → gmail`:
   - Alertas de buscas salvas (hoje: ADESA "Cris"/"Cris1", ~5h ET; depois ACV/OPENLANE) → lista de VINs do dia (DealerBlock com preço atual + Runlist com data, pátio e Run #).
   - Confirmações de pagamento ADESA Clear → preço que a loja pagou em carros parecidos (âncora de lance).
   - Arbitragens → modelos/defeitos que já deram problema.
   - Complementa com inventário público (web) quando a rede permitir.
3. Para cada candidato: recalls NHTSA (`api.nhtsa.gov`), decodificação VIN (`vpic.nhtsa.dot.gov`), problemas crônicos do modelo, comparáveis de varejo em Greater Boston, estimativa de lance máximo.
4. Monta o relatório em `leilao/relatorio_modelo.md` (máx. 10 carros) e envia com `python3 leilao/enviar_whatsapp.py`.
5. Se algo bloquear (rede, secrets, falta de dados), envia mesmo assim um WhatsApp curto dizendo **o que** bloqueou — nunca falha em silêncio.

## Configurar os alertas por email (uma vez só)

| Leilão | Onde | O que fazer |
|---|---|---|
| **ADESA (DealerBlock/Runlist)** | já ativo | Buscas "Cris" e "Cris1" chegam diariamente. Sugestão: criar mais 1–2 (ex.: "Honda-Toyota-SUV" — CR-V/RAV4/Highlander/Pilot, 2012+, ≤ 130k, ≤ $12k) |
| **ADESA Clear** | app/site Clear → Saved Searches | Salvar as mesmas buscas e ativar notificação **por email** (se o app só oferecer push, avisar — push não chega no Gmail) |
| **ACV Auctions** | app ACV → Saved Searches / Alerts | Ativar alerta diário por email |
| **OPENLANE** | openlane.com → Saved Searches | Ativar "email daily digest" |

Todos os alertas devem chegar em `usaregularma@gmail.com` (que já cai nesta caixa) ou direto em `admin@walthamautogallery.com`.

## Pré-requisitos (uma vez só)

**Secrets do ambiente cloud:** `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_FROM` e (recomendado) `TWILIO_CONTENT_SID`.

**Domínios liberados na rede (Custom → Allowed domains):**
`api.twilio.com`, `adesa.com`, `*.adesa.com`, `openlane.com`, `*.openlane.com`, `acvauctions.com`, `*.acvauctions.com`, `api.nhtsa.gov`, `vpic.nhtsa.dot.gov`, `www.nhtsa.gov`, `www.cargurus.com`, `www.cars.com`, `www.edmunds.com`, `www.kbb.com`, `www.consumerreports.org`

**Template WhatsApp:** mensagem iniciada pela empresa fora da janela de 24h exige template aprovado pela Meta. Criar na Twilio (Content Template Builder), categoria *Utility*, ex.:
> Bom dia! Oportunidades de leilão de {{1}}: {{2}}

e colocar o SID (`HX...`) em `TWILIO_CONTENT_SID`.
