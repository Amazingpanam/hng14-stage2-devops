FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM node:18-alpine

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app /app

ENV PORT=3000
USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget -qO- http://localhost:3000 || exit 1

CMD ["npm", "start"]
