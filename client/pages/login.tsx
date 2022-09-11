import { useState } from 'react';
import { useMutation, gql } from '@apollo/client';
import { ITokenAuthMutation } from '../types/user';
import { Form } from '../components/forms/Form';
import { Input } from '../components/common/Input';
import { Button } from '../components/common/Button';

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

  const [inputs, setInputs] = useState({ email: '', password: '' });

  const [doTokenAuth, { data, loading, error }] = useMutation<
    ITokenAuthMutation,
    { email: string; password: string }
  >(TokenAuthMutation, {
    variables: { email: inputs.email, password: inputs.password },
  });

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    console.log(event.target)
    setInputs({ ...inputs, [name]: value });
  };

  return (
    <div>
      <Form handleSubmit={() => {}}>
        <h1>Login Here</h1>
        <Input
          id="email"
          name="email"
          value={inputs.email}
          label="Your Email"
          placeholder="Enter email"
          type="email"
          handleInput={handleInput}
        />
        <Input
          id="password"
          name="password"
          value={inputs.password}
          label="Your Password"
          placeholder="Enter password"
          type="password"
          handleInput={handleInput}
        />
        <Button type='button'>Register For Account</Button>
        <Button type="submit">Submit</Button>
      </Form>
    </div>
  );
}
