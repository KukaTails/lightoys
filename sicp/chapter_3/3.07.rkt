(define (call-the-cops)
  (display "calling the cops\n"))

(define (password-protect password subject)
  (let ((num-attempts 0))
    (lambda (provided-password msg)
      (if (eq? provided-password password)
          (begin (set! num-attempts 0)
                 (subject msg))
          (begin (set! num-attempts (+ 1 num-attempts))
                 (if (>= num-attempts 7)
                     (begin (call-the-cops)
                            (lambda (arg . rest)
                              "invalid password"))
                     (lambda (arg . rest)
                       "invalid password")))))))

(define (make-account password balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)

  (define (dispatch msg)
    (cond ((eq? msg 'withdraw) withdraw)
          ((eq? msg 'deposit) deposit)
          (else (error "Unknown request -- MAKE-ACCOUNT"
                       msg))))
  (password-protect password dispatch))

(define (make-joint account old-pass new-pass)
  (define (dispatch msg)
    (account old-pass msg))
  (password-protect new-pass dispatch))

;; testing
(define peter-acc (make-account 'open-sesame 100))

((peter-acc 'open-sesame 'withdraw) 10)

(define paul-acc
  (make-joint peter-acc 'open-sesame 'rosebud))

((paul-acc 'rosebud 'withdraw) 40)