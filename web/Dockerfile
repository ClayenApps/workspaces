FROM oven/bun as build

WORKDIR /app

COPY package.json .
COPY bun.lockb .
RUN bun install --frozen-lockfile --production

COPY . .
RUN bun run build

FROM oven/bun as serve

WORKDIR /app
COPY --from=build /app/build ./build
COPY --from=build /app/node_modules ./node_modules
COPY package.json .
CMD ["bun", "./build"]
