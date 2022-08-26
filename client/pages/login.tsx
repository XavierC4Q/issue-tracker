import { useState } from "react";
import { useMutation, gql } from "@apollo/client";
import { ITokenAuthMutation } from "../types/user";
import { Form } from "../components/forms/Form";

export default function Login() {
  const TokenAuthMutation = gql`
    mutation TokenAuthMutation($email: String!, $password: String!) {
      tokenAuth(email: $email, password: $password) {
        token
        success
        errors
      }
    }
  `;

  const [inputs, setInputs] = useState({ email: "", password: "" });

  const [doTokenAuth, { data, loading, error }] = useMutation<ITokenAuthMutation, { email: string; password: string }>(
    TokenAuthMutation,
    { variables: { email: inputs.email, password: inputs.password } }
  );

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setInputs({ ...inputs, [name]: value });
  };

  return <div>Login Here</div>;
}
