# SNMP MIB module (SL-TESTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-TESTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:11 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slTests = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlTestsIfLoop_ObjectIdentity = ObjectIdentity
slTestsIfLoop = _SlTestsIfLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1)
)
_SlTestsIfLoopTable_Object = MibTable
slTestsIfLoopTable = _SlTestsIfLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    slTestsIfLoopTable.setStatus("current")
_SlTestsIfLoopEntry_Object = MibTableRow
slTestsIfLoopEntry = _SlTestsIfLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1)
)
slTestsIfLoopEntry.setIndexNames(
    (0, "SL-TESTS-MIB", "slTestsIfLoopIfIndex"),
)
if mibBuilder.loadTexts:
    slTestsIfLoopEntry.setStatus("current")
_SlTestsIfLoopIfIndex_Type = InterfaceIndex
_SlTestsIfLoopIfIndex_Object = MibTableColumn
slTestsIfLoopIfIndex = _SlTestsIfLoopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 1),
    _SlTestsIfLoopIfIndex_Type()
)
slTestsIfLoopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTestsIfLoopIfIndex.setStatus("current")
_SlTestsIfLoopDuration_Type = Integer32
_SlTestsIfLoopDuration_Object = MibTableColumn
slTestsIfLoopDuration = _SlTestsIfLoopDuration_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 2),
    _SlTestsIfLoopDuration_Type()
)
slTestsIfLoopDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slTestsIfLoopDuration.setStatus("current")


class _SlTestsIfLoopStatus_Type(Integer32):
    """Custom type slTestsIfLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("fail", 3))
    )


_SlTestsIfLoopStatus_Type.__name__ = "Integer32"
_SlTestsIfLoopStatus_Object = MibTableColumn
slTestsIfLoopStatus = _SlTestsIfLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 3),
    _SlTestsIfLoopStatus_Type()
)
slTestsIfLoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slTestsIfLoopStatus.setStatus("current")


class _SlTestsIfLoopType_Type(Integer32):
    """Custom type slTestsIfLoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("terminal", 1),
          ("facility", 2),
          ("prbs", 3),
          ("otnPrbs", 4))
    )


_SlTestsIfLoopType_Type.__name__ = "Integer32"
_SlTestsIfLoopType_Object = MibTableColumn
slTestsIfLoopType = _SlTestsIfLoopType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 5),
    _SlTestsIfLoopType_Type()
)
slTestsIfLoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slTestsIfLoopType.setStatus("current")


class _SlTestsIfLoopMode_Type(Integer32):
    """Custom type slTestsIfLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timeout", 1),
          ("toggle", 2))
    )


_SlTestsIfLoopMode_Type.__name__ = "Integer32"
_SlTestsIfLoopMode_Object = MibTableColumn
slTestsIfLoopMode = _SlTestsIfLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 6),
    _SlTestsIfLoopMode_Type()
)
slTestsIfLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slTestsIfLoopMode.setStatus("current")
_SlTestsIfLoopErrors_Type = Counter32
_SlTestsIfLoopErrors_Object = MibTableColumn
slTestsIfLoopErrors = _SlTestsIfLoopErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 7),
    _SlTestsIfLoopErrors_Type()
)
slTestsIfLoopErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTestsIfLoopErrors.setStatus("current")


class _SlTestsIfLoopResult_Type(Integer32):
    """Custom type slTestsIfLoopResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )


_SlTestsIfLoopResult_Type.__name__ = "Integer32"
_SlTestsIfLoopResult_Object = MibTableColumn
slTestsIfLoopResult = _SlTestsIfLoopResult_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 8),
    _SlTestsIfLoopResult_Type()
)
slTestsIfLoopResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTestsIfLoopResult.setStatus("current")
_SlTestsIfLoopPassedSeconds_Type = Integer32
_SlTestsIfLoopPassedSeconds_Object = MibTableColumn
slTestsIfLoopPassedSeconds = _SlTestsIfLoopPassedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 1, 1, 1, 9),
    _SlTestsIfLoopPassedSeconds_Type()
)
slTestsIfLoopPassedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTestsIfLoopPassedSeconds.setStatus("current")
_SlTestsTraps_ObjectIdentity = ObjectIdentity
slTestsTraps = _SlTestsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2)
)
_SlTestsTraps0_ObjectIdentity = ObjectIdentity
slTestsTraps0 = _SlTestsTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0)
)
_SlTestsTrapsLoopbackActive_Type = TruthValue
_SlTestsTrapsLoopbackActive_Object = MibScalar
slTestsTrapsLoopbackActive = _SlTestsTrapsLoopbackActive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 1),
    _SlTestsTrapsLoopbackActive_Type()
)
slTestsTrapsLoopbackActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTestsTrapsLoopbackActive.setStatus("current")

# Managed Objects groups


# Notification objects

slTestsTrapsLoopbackTableChanged0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 0, 2)
)
slTestsTrapsLoopbackTableChanged0.setObjects(
      *(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"),
        ("SL-TESTS-MIB", "slTestsIfLoopType"),
        ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
)
if mibBuilder.loadTexts:
    slTestsTrapsLoopbackTableChanged0.setStatus(
        "current"
    )

slTestsTrapsLoopbackTableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 13, 2, 2)
)
slTestsTrapsLoopbackTableChanged.setObjects(
      *(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"),
        ("SL-TESTS-MIB", "slTestsIfLoopType"),
        ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
)
if mibBuilder.loadTexts:
    slTestsTrapsLoopbackTableChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-TESTS-MIB",
    **{"slTests": slTests,
       "slTestsIfLoop": slTestsIfLoop,
       "slTestsIfLoopTable": slTestsIfLoopTable,
       "slTestsIfLoopEntry": slTestsIfLoopEntry,
       "slTestsIfLoopIfIndex": slTestsIfLoopIfIndex,
       "slTestsIfLoopDuration": slTestsIfLoopDuration,
       "slTestsIfLoopStatus": slTestsIfLoopStatus,
       "slTestsIfLoopType": slTestsIfLoopType,
       "slTestsIfLoopMode": slTestsIfLoopMode,
       "slTestsIfLoopErrors": slTestsIfLoopErrors,
       "slTestsIfLoopResult": slTestsIfLoopResult,
       "slTestsIfLoopPassedSeconds": slTestsIfLoopPassedSeconds,
       "slTestsTraps": slTestsTraps,
       "slTestsTraps0": slTestsTraps0,
       "slTestsTrapsLoopbackTableChanged0": slTestsTrapsLoopbackTableChanged0,
       "slTestsTrapsLoopbackActive": slTestsTrapsLoopbackActive,
       "slTestsTrapsLoopbackTableChanged": slTestsTrapsLoopbackTableChanged}
)
