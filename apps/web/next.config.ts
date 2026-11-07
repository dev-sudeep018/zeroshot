import type { NextConfig } from "next";
const config: NextConfig = {
  // Auth emulator checks use a separate development cache, never the release build.
  distDir: process.env.ZEROSHOT_AUTH_TEST === "1" ? ".next-auth" : ".next",
  output: "export",
  trailingSlash: true,
  transpilePackages: ["@zeroshot/problem-schema", "@zeroshot/runner-protocol"],
  images: { unoptimized: true },
  devIndicators: false,
};
export default config;
