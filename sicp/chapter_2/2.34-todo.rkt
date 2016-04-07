(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial sequence))))


(define (horner-eval x coefficient-sequence)
  (accumulate (lambda (this-coeff higher-terms)
                (+ x (* 
              0
              coefficient-sequence)))))

;; testing
(horner-eval 2 (1 3 0 5 0 1))