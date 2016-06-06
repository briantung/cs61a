(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)
  ))

(define (caddr s)
  (car (cdr (cdr s))) 
)

(define (sign x)
  (if (< x 0) -1 
    (if (> x 0) 1 0)
    
    )
  
  )

(define (square x) (* x x))

(define (pow b n)
  (if (= n 1) b 
    (if (even? n) (pow (* b b) (/ n 2))
      (* b (pow b (- n 1))) 
    ) 
  
  ))

(define (ordered? s)
  (if (null? (cdr s)) True
    (if (> (car s) (car (cdr s)))
      False
      (ordered? (cdr s))
      )
))

(define (nodots s)
    (display s)
    (newline)
    (if (pair? s) 
      (cons (if (pair? (car s)) (car (nodots (car s))) (car s)) (nodots (cdr s)))
      (cons s nil) 
      ) 
       
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) False)
          ((= (car s) v) True)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
            ((= (car s) v) s)
            ((> (car s) v) (cons v s))
            ((< (car s) v) (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t)))

          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ))


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (cond ((empty? t) false)
          ((= (entry t) v) True)
          ((< (entry t) v) (in? (right t) v))
          ((> (entry t) v) (in? (left t) v))
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

(define (as-list t)
   (define (extend t s)
        (if (empty? t) s
            (extend (left t)
                    (cons (entry t) (extend (right t) s)))))
    (extend t nil)     
    )

