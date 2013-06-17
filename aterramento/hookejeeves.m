% The following program calculates the minimum point of a multi-variable function using the Hooke-Jeeves directional search method.
% 
% The function hookejeeves has the following input parameters:
% 
% N - number of variables
% X - array of initial guesses
% StepSize - array of search step sizes
% MinStepSize - array of minimum step sizes
% fxToler - tolerance for function
% MaxIter - maximum number of iterations
% myFx - name of the optimized function
% The function generates the following output:
% 
% X - array of optimized variables
% BestF - function value at optimum
% Iters - number of iterations
% Here is a sample session to find the optimum for the following function:
% 
% y = 10 + (X(1) - 2)^2 + (X(2) + 5)^2
% 
% The above function resides in file fx1.m. The search for the optimum 2 variables has the initial guess of [0 0], initial step vector of [0.1 0.1] with a minimum step vector of [1e-5 1e-5]. The search employs a maximum of 1000 iterations and a function tolerance of 1e-7:
% 
% >> [X,BestF,Iters] = hookejeeves(2, [0 0], [.1 .1], [1e-5 1e-5], 1e-7, 1000, 'fx1')
% 
% X =
% 
%     2.0000 -5.0000
% 
% BestF =
% 
%     10
% 
% Iters =
% 
%     15
%
% http://namirshammas.com/MATLAB/Optim_HookeJeeves.htm


function [X,BestF,Iters] = hookejeeves(N, X, StepSize, MinStepSize, Eps_Fx, MaxIter, myFx)
% Function HOOKEJEEVS performs multivariate optimization using the
% Hooke-Jeeves search method.
%
% Input
%
% N - number of variables
% X - array of initial guesses
% StepSize - array of search step sizes
% MinStepSize - array of minimum step sizes
% Eps_Fx - tolerance for difference in successive function values
% MaxIter - maximum number of iterations
% myFx - name of the optimized function
%
% Output
%
% X - array of optimized variables
% BestF - function value at optimum
% Iters - number of iterations
%

Xnew = X;
BestF = feval(myFx, Xnew, N);
LastBestF = 100 * BestF + 100;

bGoOn = true;
Iters = 0;

while bGoOn

  Iters = Iters + 1;
  if Iters > MaxIter
    break;
  end

  X = Xnew;

  for i=1:N
    bMoved(i) = 0;
    bGoOn2 = true;
    while bGoOn2
      xx = Xnew(i);
      Xnew(i) = xx + StepSize(i);
      F = feval(myFx, Xnew, N);
      if F < BestF
        BestF = F;
        bMoved(i) = 1;
      else
        Xnew(i) = xx - StepSize(i);
        F = feval(myFx, Xnew, N);
        if F < BestF
          BestF = F;
          bMoved(i) = 1;
        else
          Xnew(i) = xx;
          bGoOn2 = false;
        end
      end
    end
  end

  bMadeAnyMove = sum(bMoved);

  if bMadeAnyMove > 0
    DeltaX = Xnew - X;
    lambda = 0.5;
    lambda = linsearch(X, N, lambda, DeltaX, myFx);
    Xnew = X + lambda * DeltaX;
  end

  BestF = feval(myFx, Xnew, N);

  % reduce the step size for the dimensions that had no moves
  for i=1:N
    if bMoved(i) == 0
      StepSize(i) = StepSize(i) / 2;
    end
  end

  if abs(BestF - LastBestF) < Eps_Fx
    break
  end

  LastBest = BestF;
  bStop = true;
  for i=1:N
    if StepSize(i) >= MinStepSize(i)
      bStop = false;
    end
  end

  bGoOn = ~bStop;

end

function y = myFxEx(N, X, DeltaX, lambda, myFx)

  X = X + lambda * DeltaX;
  y = feval(myFx, X, N);

% end

function lambda = linsearch(X, N, lambda, D, myFx)

  MaxIt = 100;
  Toler = 0.000001;

  iter = 0;
  bGoOn = true;
  while bGoOn
    iter = iter + 1;
    if iter > MaxIt
      lambda = 0;
      break
    end

    h = 0.01 * (1 + abs(lambda));
    f0 = myFxEx(N, X, D, lambda, myFx);
    fp = myFxEx(N, X, D, lambda+h, myFx);
    fm = myFxEx(N, X, D, lambda-h, myFx);
    deriv1 = (fp - fm) / 2 / h;
    deriv2 = (fp - 2 * f0 + fm) / h ^ 2;
    diff = deriv1 / deriv2;
    lambda = lambda - diff;
    if abs(diff) < Toler
      bGoOn = false;
    end
  end

% end