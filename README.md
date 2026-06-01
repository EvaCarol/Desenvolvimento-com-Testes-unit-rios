# Atividade: Desenvolvimento com Testes Unitários

**Aluno:** Evellyn Carolyne Gomes Da Silva  
**Disciplina:** Desenvolvimento com Testes Unitários  
**Cenário Escolhido:** 1. Sistema de Gerenciamento de Notas

---

## 🎯 Objetivo da Atividade

Desenvolver um sistema simples em Python aplicando o conceito de **Testes Unitários** com `pytest`, seguindo o ciclo **TDD (Test-Driven Development)**.

---

## 📋 Funcionalidades Implementadas

- Cadastrar notas com validação
- Calcular média das notas
- Verificar situação do aluno (Aprovado, Recuperação ou Reprovado)

---

## 📌 Regras de Negócio Implementadas

| Média              | Situação       |
|--------------------|----------------|
| ≥ 7.0              | Aprovado       |
| Entre 5.0 e 6.9    | Recuperação    |
| < 5.0              | Reprovado      |

**Validações:**
- Notas devem estar entre 0 e 10
- Rejeitar valores negativos, acima de 10 ou não numéricos

---

## 🧪 Testes Unitários

**Total de testes:** 7  
**Status:** ✅ Todos passando

### Testes Implementados:

1. `test_cadastrar_nota_valida()` — Cadastro de nota válida
2. `test_cadastrar_nota_invalida()` — Validação de notas inválidas
3. `test_calcular_media()` — Cálculo correto da média
4. `test_media_sem_notas()` — Média quando não há notas
5. `test_verificar_situacao_aprovado()` — Situação "Aprovado"
6. `test_verificar_situacao_recuperacao()` — Situação "Recuperação"
7. `test_verificar_situacao_reprovado()` — Situação "Reprovado"

---

## 🚀 Como Executar o Projeto

### 1. Instalar dependências
```bash
pip install pytest