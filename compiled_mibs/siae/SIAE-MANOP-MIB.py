# SNMP MIB module (SIAE-MANOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-MANOP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:10 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

manualOperation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71)
)
if mibBuilder.loadTexts:
    manualOperation.setRevisions(
        ("2014-03-17 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ManualOpTrap_ObjectIdentity = ObjectIdentity
manualOpTrap = _ManualOpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 0)
)


class _ManualOpMibVersion_Type(Integer32):
    """Custom type manualOpMibVersion based on Integer32"""
    defaultValue = 1


_ManualOpMibVersion_Type.__name__ = "Integer32"
_ManualOpMibVersion_Object = MibScalar
manualOpMibVersion = _ManualOpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 1),
    _ManualOpMibVersion_Type()
)
manualOpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpMibVersion.setStatus("current")
_ManualOpTable_Object = MibTable
manualOpTable = _ManualOpTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2)
)
if mibBuilder.loadTexts:
    manualOpTable.setStatus("current")
_ManualOpRecord_Object = MibTableRow
manualOpRecord = _ManualOpRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1)
)
manualOpRecord.setIndexNames(
    (0, "SIAE-MANOP-MIB", "manualOpId"),
)
if mibBuilder.loadTexts:
    manualOpRecord.setStatus("current")
_ManualOpId_Type = Integer32
_ManualOpId_Object = MibTableColumn
manualOpId = _ManualOpId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 1),
    _ManualOpId_Type()
)
manualOpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpId.setStatus("current")
_ManualOpObjectId_Type = ObjectIdentifier
_ManualOpObjectId_Object = MibTableColumn
manualOpObjectId = _ManualOpObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 2),
    _ManualOpObjectId_Type()
)
manualOpObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpObjectId.setStatus("current")
_ManualOpEventTime_Type = Unsigned32
_ManualOpEventTime_Object = MibTableColumn
manualOpEventTime = _ManualOpEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 3),
    _ManualOpEventTime_Type()
)
manualOpEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpEventTime.setStatus("current")


class _ManualOpValueType_Type(Integer32):
    """Custom type manualOpValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("integer32", 1),
          ("objectId", 2))
    )


_ManualOpValueType_Type.__name__ = "Integer32"
_ManualOpValueType_Object = MibTableColumn
manualOpValueType = _ManualOpValueType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 4),
    _ManualOpValueType_Type()
)
manualOpValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpValueType.setStatus("current")
_ManualOpIntegerVal_Type = Integer32
_ManualOpIntegerVal_Object = MibTableColumn
manualOpIntegerVal = _ManualOpIntegerVal_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 5),
    _ManualOpIntegerVal_Type()
)
manualOpIntegerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpIntegerVal.setStatus("current")
_ManualOpOidVal_Type = ObjectIdentifier
_ManualOpOidVal_Object = MibTableColumn
manualOpOidVal = _ManualOpOidVal_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 6),
    _ManualOpOidVal_Type()
)
manualOpOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpOidVal.setStatus("current")
_ManualOpActive_Type = AlarmStatus
_ManualOpActive_Object = MibScalar
manualOpActive = _ManualOpActive_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 3),
    _ManualOpActive_Type()
)
manualOpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manualOpActive.setStatus("current")


class _ManualOpActiveSeverityCode_Type(AlarmSeverityCode):
    """Custom type manualOpActiveSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_ManualOpActiveSeverityCode_Type.__name__ = "AlarmSeverityCode"
_ManualOpActiveSeverityCode_Object = MibScalar
manualOpActiveSeverityCode = _ManualOpActiveSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 4),
    _ManualOpActiveSeverityCode_Type()
)
manualOpActiveSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualOpActiveSeverityCode.setStatus("current")


class _ManualOpTimeOut_Type(Integer32):
    """Custom type manualOpTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_ManualOpTimeOut_Type.__name__ = "Integer32"
_ManualOpTimeOut_Object = MibScalar
manualOpTimeOut = _ManualOpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 71, 5),
    _ManualOpTimeOut_Type()
)
manualOpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualOpTimeOut.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-MANOP-MIB",
    **{"manualOperation": manualOperation,
       "manualOpTrap": manualOpTrap,
       "manualOpMibVersion": manualOpMibVersion,
       "manualOpTable": manualOpTable,
       "manualOpRecord": manualOpRecord,
       "manualOpId": manualOpId,
       "manualOpObjectId": manualOpObjectId,
       "manualOpEventTime": manualOpEventTime,
       "manualOpValueType": manualOpValueType,
       "manualOpIntegerVal": manualOpIntegerVal,
       "manualOpOidVal": manualOpOidVal,
       "manualOpActive": manualOpActive,
       "manualOpActiveSeverityCode": manualOpActiveSeverityCode,
       "manualOpTimeOut": manualOpTimeOut}
)
