# SNMP MIB module (CTRON-TIMED-RESET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-TIMED-RESET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:55 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ctDevice,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDevice")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtTimedResetMIB_ObjectIdentity = ObjectIdentity
ctTimedResetMIB = _CtTimedResetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2)
)


class _CtTimedResetStatus_Type(Integer32):
    """Custom type ctTimedResetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("softEnabled", 1),
          ("hardEnabled", 2))
    )


_CtTimedResetStatus_Type.__name__ = "Integer32"
_CtTimedResetStatus_Object = MibScalar
ctTimedResetStatus = _CtTimedResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 1),
    _CtTimedResetStatus_Type()
)
ctTimedResetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTimedResetStatus.setStatus("deprecated")
_CtTimedResetTimeEntered_Type = Integer32
_CtTimedResetTimeEntered_Object = MibScalar
ctTimedResetTimeEntered = _CtTimedResetTimeEntered_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 2),
    _CtTimedResetTimeEntered_Type()
)
ctTimedResetTimeEntered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTimedResetTimeEntered.setStatus("deprecated")
_CtTimedResetTimeRemaining_Type = Integer32
_CtTimedResetTimeRemaining_Object = MibScalar
ctTimedResetTimeRemaining = _CtTimedResetTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 3),
    _CtTimedResetTimeRemaining_Type()
)
ctTimedResetTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTimedResetTimeRemaining.setStatus("deprecated")


class _CtTimedResetOperationalMode_Type(Integer32):
    """Custom type ctTimedResetOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentMode", 0),
          ("ieee8021Q", 1),
          ("secureFast", 2))
    )


_CtTimedResetOperationalMode_Type.__name__ = "Integer32"
_CtTimedResetOperationalMode_Object = MibScalar
ctTimedResetOperationalMode = _CtTimedResetOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 4),
    _CtTimedResetOperationalMode_Type()
)
ctTimedResetOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTimedResetOperationalMode.setStatus("deprecated")


class _CtTimedResetNVRamReset_Type(Integer32):
    """Custom type ctTimedResetNVRamReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dontResetNVRam", 0),
          ("resetNVRam", 1))
    )


_CtTimedResetNVRamReset_Type.__name__ = "Integer32"
_CtTimedResetNVRamReset_Object = MibScalar
ctTimedResetNVRamReset = _CtTimedResetNVRamReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 5),
    _CtTimedResetNVRamReset_Type()
)
ctTimedResetNVRamReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTimedResetNVRamReset.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-TIMED-RESET-MIB",
    **{"ctTimedResetMIB": ctTimedResetMIB,
       "ctTimedResetStatus": ctTimedResetStatus,
       "ctTimedResetTimeEntered": ctTimedResetTimeEntered,
       "ctTimedResetTimeRemaining": ctTimedResetTimeRemaining,
       "ctTimedResetOperationalMode": ctTimedResetOperationalMode,
       "ctTimedResetNVRamReset": ctTimedResetNVRamReset}
)
