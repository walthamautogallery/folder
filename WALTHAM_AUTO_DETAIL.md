# 🚗 Waltham Auto Detail — Memória do Projeto

> **Palavra-chave de ativação: "detail"** — quando o usuário disser "detail",
> carregue este arquivo e continue o projeto exatamente de onde parou.
> Última atualização: 2026-08-07 · Owner: admin@walthamautogallery.com

---

## 🎯 O que é

Criar **Waltham Auto Detail** — um negócio de detalhe automotivo, agora como
**empresa separada (nova LLC)**, irmã da **Lehnen & Ristov LLC** (Waltham Auto
Gallery). **EIN, banco, QuickBooks e seguro próprios.**

---

## ✅ Decisões travadas

### Estrutura legal — ⚠️ DECISÃO ALTERADA em 2026-08-07
- ~~Antes: DBA sob a Lehnen & Ristov LLC~~ → **agora: EMPRESA SEPARADA — nova LLC**
  (ex.: **"Waltham Auto Detail LLC"**), irmã da Lehnen & Ristov LLC.
- Passos de formação em Massachusetts:
  1. Checar disponibilidade do nome no banco de corporações do
     **Secretary of the Commonwealth** (corp.sec.state.ma.us).
  2. Registrar o **Certificate of Organization** — taxa **$500** (online +$20).
  3. Tirar **EIN novo** no IRS (grátis, online, sai na hora).
  4. Abrir **conta bancária própria** da nova LLC.
  5. **Apólice de seguro própria** (garage liability/garage keepers) no 39 Felton St.
  6. Lembrar do **Annual Report** de MA: **$500/ano** ($520 online).
  7. Se contratar funcionário: **workers' comp** e payroll próprios.
- Se a LLC se chamar exatamente "Waltham Auto Detail LLC", **não precisa de DBA**;
  DBA no City Clerk só se operar com nome diferente do registrado.
- Trade-off assumido: isola risco e livros da Gallery, em troca de ~$500/ano de
  annual report + QBO próprio + seguro próprio.

### Local — 39 Felton St, Waltham, MA
- Aluguel **$3.000/mês**. **Semipronto + já com permits.** ✅
- Zona **industrial/flex** — correta para detalhe (descarte de água exige isso).
- Tamanho estimado ~1.200–1.450 SF (1–2 baias) pelo comp de mercado (~$25–29/SF/ano).
- **Veredito: bom negócio** (baia permitida e semipronta em Waltham por $3k é justo/barato).
- **Due diligence pendente (amarrar no contrato):**
  1. Os permits cobrem **"motor vehicle detailing/service"** (não só "commercial")?
  2. Existe **separador óleo/água** / dreno ligado ao esgoto? (runoff não pode ir p/ storm drain — regra MassDEP/Waltham).
  3. Elétrica **200A** + água quente (extrator, politriz, compressor, steamer).
- ⚠️ **Concorrência no mesmo corredor:**
  - **A-List Auto Detailing** — 42 Felton St, Unit 3 (porta ao lado!)
  - **JV Auto Detailing** (a da tabela de preços) — Waltham, @jv.autodetailing
  - A R Auto Detailing, Absolute Auto Detail — também Waltham.
  - Campo de batalha = **Google Business Profile + reviews**, mais que o site.

### Nome / marca
- **"Waltham Auto Detail"** — confirmado. Forte p/ **SEO local + GEO**: é o match
  exato da busca "waltham auto detail" e coloca acima dos "X Auto Detail" concorrentes.
- Cola na marca-mãe **Waltham Auto Gallery** (cruzamento de clientes: todo carro
  vendido na Gallery é lead do Detail).

### Site + operação
- **Site feito no GHL (GoHighLevel):** site + agenda + CRM + automações
  (missed-call text-back, lembrete de agendamento, **pedido automático de review**).
- Mapear o domínio **walthamautodetail.com** por cima do GHL.
- Site estático do repo (`index.html` / gerador de folder) fica **opcional**.

### Fluxo do dinheiro
- **QuickBooks = fonte da verdade do dinheiro.** GHL cuida do que **não é** dinheiro.
- Cliente fecha no GHL → **QB cobra** (payment link remoto + **GoPayment** presencial)
  → **GHL↔QBO sincroniza** cliente e status de pago.
- Regra de ouro: **um só sistema cobra**, pra não dobrar receita nos livros.

---

## 💵 Tabela de preços (base JV, corrigida Car < SUV < Truck)

| Serviço        | Car    | SUV    | Truck  |
|----------------|--------|--------|--------|
| Mini Detail    | $160   | $180   | $200   |
| Full Interior  | $300   | $350   | $400   |
| Full Exterior  | $300   | $350   | $400   |
| Full Detail    | $400   | $450   | $500   |
| **Platinum**   | $1.000 | $1.150 | $1.200 |

- **Ceramic Pro:** pacotes de **$599 a $3.500** (sob orçamento por veículo).
- **PPF:** de **$650 a $8.000** (sob orçamento por veículo).

---

## 🧾 QuickBooks — plano de execução

> ⚠️ **Plano antigo (era DBA):** classes `Auto Gallery`/`Auto Detail` no mesmo
> arquivo QB. **DESCARTADO** com a mudança para LLC separada.

**Novo plano (LLC separada):**
1. Quando a LLC existir (EIN em mãos), abrir **assinatura/company QBO NOVA e
   separada** para a Waltham Auto Detail. **Não misturar** com o QB da
   Lehnen & Ristov.
2. Nela: **Products/Services** da tabela de preços → conta de receita
   **"Detailing Revenue"**.
3. Aluguel $3k/mês → despesa **Rent**.
4. Invoices/Estimates + cobrança (payment link remoto e **GoPayment** presencial)
   pelo QBO novo; GHL↔QBO sincroniza cliente e status de pago.
5. O **conector QuickBooks do Claude hoje aponta para a company da Lehnen &
   Ristov** — depois de criar a company nova, reconectar/apontar para ela.

---

## 🌐 Domínio & redes (registrar já)
- **walthamautodetail.com** — sem site ativo (bom sinal). Confirmar disponibilidade
  no GoDaddy/Namecheap e **registrar**. (WHOIS não roda neste ambiente — proxy bloqueia.)
- **@walthamautodetail** no Instagram e Facebook — aparentam livres; garantir os dois.

---

## 📋 Próximos passos (TODO)

- [ ] **Formar a LLC nova** — passo a passo completo em **`LLC_PASSO_A_PASSO.md`**
      (nome → Certificate of Organization $520 → EIN → banco → seguro).
- [ ] Registrar **walthamautodetail.com** + **@walthamautodetail** (IG/FB).
- [ ] Abrir **Google Business Profile** no 39 Felton St → **maior retorno agora**
      (escrever descrição, categorias e serviços com preços — texto a produzir).
- [ ] Criar **company QBO nova** da Detail (pós-EIN) → serviços da tabela +
      reconectar o conector do Claude nela.
- [ ] ~~DBA no City Clerk~~ — só se o nome operacional diferir do nome da LLC.
- [ ] Due diligence do imóvel: permits (uso), separador óleo/água, elétrica 200A.
- [ ] Montar **site no GHL** + mapear domínio.
- [ ] Escrever **texto do Google Business Profile**.

---

## 🔌 Acessos disponíveis nesta conta
GitHub (repo `walthamautogallery/folder`, GitHub Pages) · QuickBooks (Intuit) ·
Buffer (social) · Gmail · Google Calendar · Google Drive · GoHighLevel (externo, do usuário).
