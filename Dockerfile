FROM python:3.13-alpine

LABEL org.opencontainers.image.title="bemvindo-vinia-cinema" \
      org.opencontainers.image.description="Site de boas-vindas com animação de cinema" \
      org.opencontainers.image.source="https://github.com/vsperancin/bemvindo" \
      org.opencontainers.image.licenses="MIT"

# Sem dependências externas — usa só stdlib
# Mantém a imagem bem pequena (~25 MB)

WORKDIR /app

# Cria user não-root por segurança
RUN adduser -D -H -s /sbin/nologin app

# Copia tudo
COPY --chown=app:app server.py ./
COPY --chown=app:app templates/ ./templates/
COPY --chown=app:app static/ ./static/

USER app

ENV PORT=8000 \
    HOST=0.0.0.0

EXPOSE 8000

# Healthcheck simples
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://127.0.0.1:8000/health || exit 1

# Use exec form for proper signal handling
CMD ["python3", "server.py"]