import { useContext } from "react";
import { Footer } from "../common/Footer";
import { Header } from "../common/Header";
import { AuthContext } from "../../context/AuthContext";
import { useRouter } from "next/router";

interface ILayout {
  children: React.ReactNode[] | React.ReactNode;
}

export const Layout: React.FC<ILayout> = ({ children }) => {
  const { data, loading } = useContext(AuthContext);
  const user = data?.me;
  const isLoggedIn = !!user;

  const { push, pathname } = useRouter();

  if (loading || !data) return null;

  if (!loading && !user && !pathname.includes("login")) {
    push("/login");
  }

  return (
    <div>
      <Header isLoggedIn={isLoggedIn} />
      {children}
      <Footer isLoggedIn={isLoggedIn} />
    </div>
  );
};
