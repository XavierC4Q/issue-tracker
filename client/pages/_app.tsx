import "../styles/globals.css";
import type { AppProps } from "next/app";
import { ApolloProvider } from "@apollo/client";
import { getApolloClient } from "../lib/apollo-client";
import { AuthProvider } from "../context/AuthContext";
import { Layout } from "../components/layouts/Layout";

const client = getApolloClient();

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ApolloProvider client={client}>
      <AuthProvider>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </AuthProvider>
    </ApolloProvider>
  );
}
export default MyApp;
