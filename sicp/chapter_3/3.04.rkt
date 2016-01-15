(define (make-account balance password)
  (define wrong-password-count 0)
  (define wrong-password-limit 7)
  (define (call-the-cops) "Call the cops")
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (dispatch pass op)
    (if (not (eq? pass password))
        (lambda (amount)
          (if (> wrong-password-count wrong-password-limit)
              (call-the-cops)
              (begin (set! wrong-password-count (+ wrong-password-count 1))
                     (error "Incorrect password"))))
        (begin (set! wrong-password-count 0)
               (cond ((eq? op 'withdraw) withdraw)
                     ((eq? op 'deposit) deposit)
                     (else (error "Unknown request -- MAKE-ACCOUNT"
                                  op))))))
  dispatch)


;; testing
(define acc (make-account 100 'secret-password))

((acc 'secret-password 'withdraw) 40)

((acc 'some-other-password 'deposit) 30)