import { createContext } from "react";
import { UserNode, IMeQuery } from "../types/user";
import { useQuery, gql } from "@apollo/client";

interface IAuthContext {
  data: { me: UserNode | null } | undefined;
  loading: boolean;
}

export const AuthContext = createContext<IAuthContext>({ data: undefined, loading: false });

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

  const { data, loading } = useQuery<IMeQuery>(MeQuery);


  return <AuthContext.Provider value={{ data, loading }}>{children}</AuthContext.Provider>;
};
