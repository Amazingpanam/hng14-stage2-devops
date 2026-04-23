# ---- Build stage ----
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production

COPY . .

# ---- Production stage ----
FROM node:18-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app /app

ENV NODE_ENV=production
ENV PORT=3000

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:3000 || exit 1

CMD ["npm", "start"]
