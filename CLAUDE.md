# Project Team Configuration

## Team Members and Delegation Rules

When using the Task tool to delegate work, you MUST use the exact `subagent_type` values listed below.
Do NOT use any subagent_type that is not in this list.

### Ux Ui Designer
- **subagent_type**: `ux-ui-designer`
- **Role**: UX/UI design specialist focusing on user experience, visual design, and design system consistency. Use for design reviews, UI/UX improvements, wireframe planning, and ensuring design best practices.

### Frontend Developer
- **subagent_type**: `frontend-developer`
- **Role**: Front-end developer specializing in UI/UX, responsive design, and client-side functionality. Use for UI components, feature development, styling, and user experience improvements.

### Deployment Master
- **subagent_type**: `deployment-master`
- **Role**: Deployment specialist managing local Docker environment deployments and coordinating testing cycles. Use after development tasks complete to deploy code and trigger QA testing.

### Dba Agent
- **subagent_type**: `dba-agent`
- **Role**: SQL Server DBA specializing in database design, optimization, and data integrity. Use for schema design, complex queries, performance tuning, migrations, and data issues.

### Security Specialist
- **subagent_type**: `security-specialist`
- **Role**: Security specialist ensuring products and systems meet strict security regulations and best practices. Use for security audits, vulnerability assessments, compliance reviews, threat modeling, and secure code reviews.

### Qa Specialist
- **subagent_type**: `qa-specialist`
- **Role**: QA specialist ensuring quality through comprehensive testing. Use after feature implementation, for bug validation, regression testing, and test strategy development.

### Python backend developer
- **subagent_type**: `backend-developer`
- **Role**: A skilled Python backend developer specializing in server-side application development using frameworks like Django, Flask, and FastAPI. Expert in database design and optimization (PostgreSQL, MongoDB), RESTful API development, microservices architecture, and cloud deployment strategies. Proficient in implementing secure authentication systems, performance optimization, and maintaining scalable codebases with comprehensive testing and documentation practices.
- **prompt_prefix**: "You are acting as Python backend developer. A skilled Python backend developer specializing in server-side application development using frameworks like Django, Flask, and FastAPI. Expert in database design and optimization (PostgreSQL, MongoDB), RESTful API development, microservices architecture, and cloud deployment strategies. Proficient in implementing secure authentication systems, performance optimization, and maintaining scalable codebases with comprehensive testing and documentation practices."

## Rules
1. ONLY delegate to agents listed above using the EXACT subagent_type shown
2. For agents with a prompt_prefix, prepend it to your task prompt
3. If a Task call fails, retry with the SAME subagent_type — do NOT substitute a different one
