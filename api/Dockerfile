FROM oven/bun as serve

WORKDIR /app

COPY package.json .
COPY bun.lockb .
RUN bun install --frozen-lockfile --production

COPY src src
COPY tsconfig.json .

ENV NODE_ENV production
CMD ["bun", "src/index.ts"]

EXPOSE 3000
