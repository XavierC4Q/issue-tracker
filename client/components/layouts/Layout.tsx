import { Footer } from "../common/Footer";
import { Header } from "../common/Header";

interface ILayout {
  children: React.ReactNode[] | React.ReactNode;
}

export const Layout: React.FC<ILayout> = ({ children }) => {
  return (
    <div>
      <Header />
      {children}
      <Footer />
    </div>
  );
};
