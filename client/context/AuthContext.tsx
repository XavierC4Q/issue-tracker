import { createContext } from "react";
import { UserNode, IMeQuery } from "../types/user";
import { useQuery, gql } from "@apollo/client";

interface IAuthContext {
  user: UserNode | null;
}

export const AuthContext = createContext<IAuthContext>({ user: null });

interface IAuthProvider {
  children: React.ReactNode[] | React.ReactNode;
}

export const AuthProvider: React.FC<IAuthProvider> = ({ children }) => {
  const MeQuery = gql`
    query MeQuery {
      me {
        uid
        email
      }
    }
  `;

  const { data } = useQuery<IMeQuery>(MeQuery);

  const user = data?.me || null;

  return <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>;
};
