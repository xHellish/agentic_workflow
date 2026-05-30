import os

skills = {
    'devops-engineer': {
        'role': 'Senior DevOps Engineer',
        'desc': 'Diseña pipelines CI/CD, infraestructura como código (IaC), contenedores y estrategias de despliegue cloud.',
        'responsibilities': ['1. CI/CD Pipeline Design', '2. Infrastructure as Code', '3. Containerization'],
        'triggers': ['dockerize', 'pipeline', 'deployment', 'kubernetes', 'terraform']
    },
    'git-workflow': {
        'role': 'Release Manager',
        'desc': 'Define estrategias de branching, conventional commits, PR templates y automatización de releases.',
        'responsibilities': ['1. Branching Strategy', '2. Conventional Commits', '3. Release Automation'],
        'triggers': ['git flow', 'branching', 'release', 'conventional commits', 'pr template']
    },
    'api-designer': {
        'role': 'API Architect',
        'desc': 'Diseña contratos de API (OpenAPI, GraphQL schemas), estrategias de versionado y arquitecturas contract-first.',
        'responsibilities': ['1. API Contracts', '2. Versioning Strategy', '3. REST/GraphQL Design'],
        'triggers': ['openapi', 'swagger', 'graphql schema', 'api design', 'restful']
    },
    'performance-engineer': {
        'role': 'Performance Engineer',
        'desc': 'Profiling, load testing, benchmarking, caching, APM.',
        'responsibilities': ['1. Profiling', '2. Load Testing', '3. Caching Strategy'],
        'triggers': ['slow', 'bottleneck', 'profiler', 'load test', 'benchmark']
    },
    'database-designer': {
        'role': 'Database Architect',
        'desc': 'ER diagrams, migration strategies, query optimization.',
        'responsibilities': ['1. Schema Design', '2. Query Optimization', '3. Migration Strategy'],
        'triggers': ['schema', 'sql query', 'migration', 'database design', 'er diagram']
    }
}

template = '''---
name: {name}
version: 1.0.0
description: {desc}
---

# {name}

> **Language rule**: Configure in `.agents/config.yaml` → `response_language`. Default: Always respond in Spanish.

You are a {role}. Your role is to {desc}.

## Triggers
{triggers_md}

## When to Use This Skill
- User asks to configure or design related systems
- User wants to optimize or establish patterns in this domain
- User needs guidance on best practices for {name}

## Reference Loading
Before starting any task, read the relevant reference files:
- **Required**: `references/best-practices.md`
- **On demand**: `examples/output.md`

## Core Responsibilities

{resp_md}

## Workflow
1. **Analyze**: Understand current state and requirements.
2. **Design**: Propose architecture or configuration.
3. **Review**: Check against best practices and quality gates.
4. **Implement**: Generate code or configuration.

## Output Format
1. **Análisis**: Contexto.
2. **Propuesta**: Solución detallada.
3. **Implementación**: Archivos y comandos.
4. **Quality Gates Check**: Verificación final.

## Quality Gates
- OBLIGATORIO: El output debe ser ejecutable o sintácticamente válido.
- OBLIGATORIO: Debe incluir justificación técnica de las decisiones.

## Related Skills
- **software-architect**: Para diseño de alto nivel.
- **security-auditor**: Para validaciones de seguridad.

## Guidelines
- Prioritize standard tools and patterns over custom abstractions.
- Provide clear, reproducible instructions.
- Ensure all artifacts meet the required quality gates.
'''

for skill, data in skills.items():
    trigs = '\n'.join([f'- "{t}"' for t in data['triggers']])
    resps = '\n'.join([f'### {r}\nDiseñar y validar este componente con estándares de la industria.' for r in data['responsibilities']])
    content = template.format(name=skill, role=data['role'], desc=data['desc'], triggers_md=trigs, resp_md=resps)
    
    path = os.path.join('.agents', 'skills', skill, 'SKILL.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    os.makedirs(os.path.join('.agents', 'skills', skill, 'references'), exist_ok=True)
    os.makedirs(os.path.join('.agents', 'skills', skill, 'examples'), exist_ok=True)
    
    with open(os.path.join('.agents', 'skills', skill, 'references', 'best-practices.md'), 'w', encoding='utf-8') as f:
        f.write('# Best Practices\n\nInclude industry standard practices here.')
        
    with open(os.path.join('.agents', 'skills', skill, 'examples', 'output.md'), 'w', encoding='utf-8') as f:
        f.write('# Example Output\n\nThis is how output should look.')
        
print('Robustified successfully.')