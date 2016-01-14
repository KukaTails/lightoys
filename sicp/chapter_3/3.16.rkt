(define (count-pairs x)
  (if (not (pair? x))
      0
      (+ (count-pairs (car x))
         (count-pairs (cdr x))
         1)))

;; three pairs of list

;; ________   ________   _______
;; |   |  |   |   |  |   |   |  |
;; |   |  --->|   |  --->|   |^ |
;; |_|_|__|   |_|_|__|   |_|_|__|
;;   |          |          |
;;   b          c          d

(count-pairs (list 'b 'c 'd))

;; four pairs of list
;; ________   ________   _______
;; |   |  |   |   |  |   |   |  |
;; |   |  --->|   |  ---->   |^ |
;; |   |  |   |   |  | -->   |  |
;; |_|_|__|   |_|_|__| | |_|_|__|
;;   |          |      |   |
;;   b          |------|   d

(define third-list (list 'd))
(define second-list (cons third-list third-list))
(define first-list (cons 'b second-list))
(count-pairs first-list)

;; seven pairs of list
;; ________   ________   _______
;; |   |  |   |   |  |   |   |  |
;; |   |  ----->  |  ---->   |^ |
;; |   |  |   |   |  | -->   |  |
;; |   |  | --->  |  | | |   |  |
;; |_|_|__| | |_|_|__| | |_|_|__|
;;   |      |   |      |   |
;;   |------|   |------|   d

(define third-list (list 'd))
(define second-list (cons third-list third-list))
(define first-list (cons second-list second-list))
(count-pairs first-list)

;; no return
;;    ________   ________   _______
;;    |   |  |   |   |  |   |   |  |
;; |--->  |  ---->   |  --->|   |^ |
;; |  |_|_|__|   |_|_|__|   |_|_|__|
;; |    |          |          |
;; |    b          c          |
;; |---------------------------

(define third-list (list 'any))
(define second-list (cons 'c third-list))
(define first-list (cons 'b second-list))
(set-car! third-list first-list)
(count-pairs first-list)