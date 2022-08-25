import Head from "next/head";
import { Layout } from "../components/layouts/Layout";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <Layout>
      <div className={styles.container}>
        <h1>Home Page</h1>
      </div>
    </Layout>
  );
}
