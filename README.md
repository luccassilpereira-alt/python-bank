## 🚀 Novidades na Versão 2 (V2)

Nesta grande atualização, o sistema do Python Bank foi refatorado e reestruturado para ser mais seguro, organizado e profissional. O fluxo único inicial foi substituído por uma arquitetura modular.

### ✨ Melhorias Implementadas:
* **Autenticação Dupla:** O acesso à conta deixou de ser uma senha fixa e agora exige a validação conjunta do Nome do Titular e a Senha correspondente.
* **Sistema de Bloqueio (Segurança):** Implementação de uma verificação em laço (`while`) que limita o usuário a 3 tentativas de login. Caso exceda o limite, o sistema bloqueia o acesso automaticamente.
* **Modularização de Código:** Separação de responsabilidades em múltiplos arquivos (`main.py` e `login.py`). O uso de funções substituiu o laço `while True` global, deixando o código muito mais limpo, legível e fácil de dar manutenção.
