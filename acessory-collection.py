    for(int a0 = 0; a0 < T; a0++){
            int L = in.nextInt();
            long A = in.nextInt();
            int N = in.nextInt();
            int D = in.nextInt();

            if (N<D || N>L || A<D){
                System.out.println("SAD");
                continue;
            }

            // Deal with the special case
            if (D==1){
                System.out.println(L*A);
                continue;
            }

            // The number of accessories
            // A : a1
            // A-1 to A-n: a2
            // A-n-1: a3
            long max = 0;
            int a2Max = (N-1)/(D-1);
            // Loop start from maximun a2
            for (int a2=a2Max;a2>=1; a2--){
                // Calculate a1, a3, and n by a2
                long a1 = N + (a2-1) - a2*(D-1);        
                long n = (L-a1)/a2;
                long a3 = (L-a1)%a2;
                // Break when the type of accessories (A) is not enough
                if (n>A-1 || (n==A-1 && a3 > 0)){
                    break;
                }
                // Caclulate cost
                sum = A*a1 + (A-1+A-n)*n/2*a2 + a3 * (A-n-1);
                // Break when cost starts decreasing
                if (sum<=max){
                    break;
                }
                max = sum;                    
            }            
            System.out.println(max==0?"SAD":max);
        }