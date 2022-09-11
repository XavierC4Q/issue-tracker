import { render, screen, fireEvent } from '@testing-library/react';
import { useState } from 'react';
import { Input, inputTestIds } from '../../components/common/Input';

const TestInput = ({
  values,
  inputName,
}: {
  values: { [key: string]: any };
  inputName: string;
}) => {
  const [inputs, setInput] = useState({ ...values });

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setInput({ ...inputs, [name]: value });
  };

  return (
    <Input
      id="test-id"
      label={`I am a label for ${inputName}`}
      name={inputName}
      value={inputs?.email}
      handleInput={handleInput}
    />
  );
};

const setup = (values: { [key: string]: any } = {}, name: string) => {
  const utils = render(<TestInput values={values} inputName={name} />);
  const input = screen.getByTestId(inputTestIds.input as string);

  return {
    ...utils,
    input,
  };
};

describe('Input Component', () => {
  it('Renders an Input correctly', () => {
    const { input } = setup({ email: '' }, 'email');

    screen.getByLabelText(/I am a label/);

    fireEvent.change(input, {
      target: {
        name: 'email',
        value: 'test@email.com',
      },
    });

    expect((input as HTMLInputElement).value).toBe('test@email.com');
  });
});
