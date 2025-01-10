// UnitRepository.java
package com.dormmate.dormmate_backend.repositories;

  import com.dormmate.dormmate_backend.entities.Unit;
  import org.springframework.data.jpa.repository.JpaRepository;
  import org.springframework.stereotype.Repository;

  @Repository
  public interface UnitRepository extends JpaRepository<Unit, Long> {
  }