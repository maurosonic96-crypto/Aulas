# Aula 03 - Conceitos, Funções e Tipos de Sistemas Operacionais

Prof. Me. Deivison S. Takatu  
deivison.takatu@fatec.sp.gov.br

## Sumário

- Introdução aos Sistemas Operacionais
- Tipos de Sistemas Operacionais
- Controle de Versão com Git
- Boas Práticas de Versionamento
- Utilização de IDE
- Atividade

## Sistemas de Grande Porte (Mainframes)

Projetados para alta capacidade de E/S e carga massiva de transações. Operam com processamento em lote e tempo compartilhado para muitos usuários simultâneos.

### Características principais

- Alta confiabilidade e disponibilidade
- Processamento de lotes e transações (TPS)
- Segurança e integridade de dados
- Uso típico: bancos, grandes varejistas, processamento massivo

### Exemplos

- OS/360
- OS/390
- Linux (em ambientes de mainframe)
- Variantes UNIX

Mainframes continuam sendo utilizados, especialmente como:

- Servidores web de grande escala
- Plataformas para e-commerce
- Sistemas bancários de alta criticidade

## Sistemas Operacionais de Servidor

Focados em atender múltiplos usuários e serviços via rede: web, arquivos, bancos de dados e autenticação. Projetados para estabilidade, escalabilidade e compartilhamento de recursos.

### Exemplos

- **Linux** — Ampla adoção em servidores, flexibilidade e vasto ecossistema de serviços.
- **Windows Server** — Integração com Active Directory e serviços empresariais.

## Sistemas de Multiprocessadores

Suportam múltiplas CPUs ou muitos núcleos para processamento paralelo. Requerem mecanismos avançados de escalonamento e sincronização para aproveitar o paralelismo e evitar condições de corrida.

### Desafios e soluções

- Escalonamento: balancear carga entre núcleos
- Sincronização: locks, semáforos, algoritmos lock-free
- Coerência de cache e comunicação entre núcleos
- Aplicações: servidores de alto desempenho, scientific computing

## Sistemas de Computadores Pessoais

Orientados a um único usuário com interface gráfica, suporte a multiprogramação e ampla compatibilidade de aplicações. Foco em usabilidade e suporte multimídia.

### Exemplos

- **Windows** — Ampla compatibilidade com software de produtividade e jogos.
- **macOS** — Integração hardware-software e foco em experiência do usuário.
- **Linux** — Opção para power users e desenvolvimento; personalizável.

## Sistemas Operacionais Portáteis

Principais aspectos:

- Gerenciamento agressivo de energia
- API para sensores (GPS, acelerômetro, câmera)
- Segurança por permissões
- Exemplos: Android, iOS

Forte integração com hardware; distribuição de aplicativos via lojas oficiais; grande foco em segurança e sandboxing.

## Sistemas Embarcados

Executam em dispositivos dedicados com recursos limitados; software frequentemente armazenado em ROM/flash. Usuário normalmente não instala ou altera software.

### Aplicações típicas

- Domésticas: micro-ondas, Smart TVs — resposta imediata e interface simples.
- Automotivo: controle de motor, infotainment; requisitos de segurança críticos.
- Sistemas embarcados sofisticados: Embedded Linux, QNX, VxWorks — quando é necessário mais flexibilidade.

## Sistemas de Nós Sensores

Dispositivos muito pequenos e com bateria limitada, comunicando-se sem fio e orientados a eventos. Projetos priorizam baixo consumo e protocolos leves.

Uso: monitoramento ambiental, vigilância militar, agricultura de precisão. Exemplos de SO: TinyOS, Contiki — otimizados para energia e eventos.

## Sistemas de Tempo Real

### Hard Real-Time

- Falha ao perder prazo pode causar desastre (ex.: controle de voo, segurança)

### Soft Real-Time

- Degradação aceitável (ex.: streaming de mídia, interações multimídia)

## Sistemas de Cartões Inteligentes

### Desafios e características

- Recursos restritos → gerenciamento fino de memória
- Segurança: criptografia, autenticação e resistência a ataques físicos
- Multiprogramação limitada: isolamento por applets

Ao final: diferenciar tipos de SO, reconhecer aplicações e entender exigências de projeto.

## Introdução ao Git

- **O que é Git?** Sistema de controle de versão de arquivos, instalado no computador e utilizado via linha de comando.
- **O que o Git pode fazer?** Sincroniza com repositórios online, registra versões do projeto e permite restaurar versões anteriores.

Fonte: https://github.com/torvalds

## Instalando o Git

Fonte: https://git-scm.com/downloads

1. Escolha a versão do seu sistema operacional
2. Baixe e execute o instalador
3. Siga as etapas "Next > Next > Install"

Para testar a instalação:

```bash
git --version
```

Se aparecer a versão instalada, está correto.

Se solicitado, configure o usuário e e-mail:

```bash
git config --global user.name "<Nome>"
git config --global user.email "<Email>"
```

Abra o VS Code, vá até a aba de Controle de Código-Fonte (terceiro ícone à esquerda) e, se solicitado, instale o Git. Feche e reabra o VS Code.

## Criando um Repositório no VS Code

1. Crie uma pasta no seu computador
2. Abra a pasta no VS Code
3. Crie um arquivo `.md`
4. Vá até a aba de Controle de Código-Fonte
5. Clique em "Inicializar Repositório"
6. Adicione uma mensagem de commit e clique em "Confirmar (Commit)"

## Publicando no GitHub

1. Clique em "Publicar Branch"
2. Faça login no GitHub
3. Escolha entre repositório público ou privado
4. Após a publicação, o código estará acessível no GitHub

## Boas Práticas Git

- Commits pequenos e frequentes: facilita a identificação de problemas e a reversão de mudanças.
- Mensagens de commit claras: descreva o que foi alterado e por quê.
- Uso de branches: mantenha a branch principal estável; use branches para novas funcionalidades e correções.
- Testes automatizados: garanta que o código funcione corretamente antes de fazer merge.

## Atividades

1. Configure integração entre a IDE e a conta do GitHub, garantindo autenticação funcional e reconhecimento do repositório remoto (commit, push, pull).
2. Crie um repositório de teste com ao menos um arquivo inicial, faça alterações, commit, sincronize com o GitHub, apague a pasta local e use `git clone` para restaurar o projeto.
3. Pesquise no GitHub e encontre 5 projetos de outros usuários; use `git clone` para copiá-los e analise o conteúdo.

## Referências

- TANENBAUM, Andrew S.; BOS, Herbert. Sistemas Operacionais Modernos. 4. ed. São Paulo: Pearson, 2016.
- SILBERSCHATZ, Abraham; GALVIN, Peter B.; GAGNE, Greg. Fundamentos de Sistemas Operacionais. 9. ed. Rio de Janeiro: LTC, 2015.
- STALLINGS, William. Sistemas Operacionais: Conceitos e Projetos. 8. ed. São Paulo: Pearson, 2015.
- DENARDIN, G. W.; BARRIQUELLO, C. H. Sistemas Operacionais de Tempo Real e sua Aplicação em Sistemas Embarcados. Porto Alegre: Editora da UFRGS, 2014.
- AWASTHI, A.; RAWAT, V. Ramificação e Tarefas do Sistema Operacional. Edições Nosso Conhecimento, 2023.
- DOWNEY , Allen B. Think OS: A Brief Introduction to Operating Systems. Green Tea Press, 2015.
- RED HAT. Red Hat Enterprise Linux – System Administration Guide. Documentação Oficial.
- DOCKER INC. Docker Documentation. Documentação Oficial. Disponível em: https://docs.docker.com
