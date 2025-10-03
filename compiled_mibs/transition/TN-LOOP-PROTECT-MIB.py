# SNMP MIB module (TN-LOOP-PROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LOOP-PROTECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:50 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnLoopProtectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22)
)
if mibBuilder.loadTexts:
    tnLoopProtectMIB.setRevisions(
        ("2012-07-25 10:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnLoopProtectNotifications_ObjectIdentity = ObjectIdentity
tnLoopProtectNotifications = _TnLoopProtectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 0)
)
_TnLoopProtectObjects_ObjectIdentity = ObjectIdentity
tnLoopProtectObjects = _TnLoopProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1)
)
_TnLoopProtectMgmt_ObjectIdentity = ObjectIdentity
tnLoopProtectMgmt = _TnLoopProtectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1)
)
_TnLoopProtectBaseTable_Object = MibTable
tnLoopProtectBaseTable = _TnLoopProtectBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnLoopProtectBaseTable.setStatus("current")
_TnLoopProtectBaseEntry_Object = MibTableRow
tnLoopProtectBaseEntry = _TnLoopProtectBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 1, 1)
)
tnLoopProtectBaseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnLoopProtectBaseEntry.setStatus("current")
_TnLoopProtectEnable_Type = TruthValue
_TnLoopProtectEnable_Object = MibTableColumn
tnLoopProtectEnable = _TnLoopProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 1, 1, 1),
    _TnLoopProtectEnable_Type()
)
tnLoopProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectEnable.setStatus("current")


class _TnLoopProtectTxTime_Type(Integer32):
    """Custom type tnLoopProtectTxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnLoopProtectTxTime_Type.__name__ = "Integer32"
_TnLoopProtectTxTime_Object = MibTableColumn
tnLoopProtectTxTime = _TnLoopProtectTxTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 1, 1, 2),
    _TnLoopProtectTxTime_Type()
)
tnLoopProtectTxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectTxTime.setStatus("current")


class _TnLoopProtectShutdownTime_Type(Integer32):
    """Custom type tnLoopProtectShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_TnLoopProtectShutdownTime_Type.__name__ = "Integer32"
_TnLoopProtectShutdownTime_Object = MibTableColumn
tnLoopProtectShutdownTime = _TnLoopProtectShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 1, 1, 3),
    _TnLoopProtectShutdownTime_Type()
)
tnLoopProtectShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectShutdownTime.setStatus("current")
_TnLoopProtectPortTable_Object = MibTable
tnLoopProtectPortTable = _TnLoopProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnLoopProtectPortTable.setStatus("current")
_TnLoopProtectPortEntry_Object = MibTableRow
tnLoopProtectPortEntry = _TnLoopProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1)
)
tnLoopProtectPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnLoopProtectPortEntry.setStatus("current")
_TnLoopProtectPortEnable_Type = TruthValue
_TnLoopProtectPortEnable_Object = MibTableColumn
tnLoopProtectPortEnable = _TnLoopProtectPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 1),
    _TnLoopProtectPortEnable_Type()
)
tnLoopProtectPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectPortEnable.setStatus("current")


class _TnLoopProtectPortAction_Type(Integer32):
    """Custom type tnLoopProtectPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("shutdownAndlog", 2),
          ("log", 3),
          ("trap", 4),
          ("shutdownAndtrap", 5),
          ("logAndtrap", 6),
          ("all", 7))
    )


_TnLoopProtectPortAction_Type.__name__ = "Integer32"
_TnLoopProtectPortAction_Object = MibTableColumn
tnLoopProtectPortAction = _TnLoopProtectPortAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 2),
    _TnLoopProtectPortAction_Type()
)
tnLoopProtectPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectPortAction.setStatus("current")
_TnLoopProtectPortTxModeEnable_Type = TruthValue
_TnLoopProtectPortTxModeEnable_Object = MibTableColumn
tnLoopProtectPortTxModeEnable = _TnLoopProtectPortTxModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 3),
    _TnLoopProtectPortTxModeEnable_Type()
)
tnLoopProtectPortTxModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLoopProtectPortTxModeEnable.setStatus("current")
_TnLoopProtectPortLoopCount_Type = Counter32
_TnLoopProtectPortLoopCount_Object = MibTableColumn
tnLoopProtectPortLoopCount = _TnLoopProtectPortLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 4),
    _TnLoopProtectPortLoopCount_Type()
)
tnLoopProtectPortLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLoopProtectPortLoopCount.setStatus("current")


class _TnLoopProtectPortStatus_Type(Integer32):
    """Custom type tnLoopProtectPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("disable", 3))
    )


_TnLoopProtectPortStatus_Type.__name__ = "Integer32"
_TnLoopProtectPortStatus_Object = MibTableColumn
tnLoopProtectPortStatus = _TnLoopProtectPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 5),
    _TnLoopProtectPortStatus_Type()
)
tnLoopProtectPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLoopProtectPortStatus.setStatus("current")
_TnLoopProtectPortLoopDetected_Type = TruthValue
_TnLoopProtectPortLoopDetected_Object = MibTableColumn
tnLoopProtectPortLoopDetected = _TnLoopProtectPortLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 6),
    _TnLoopProtectPortLoopDetected_Type()
)
tnLoopProtectPortLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLoopProtectPortLoopDetected.setStatus("current")
_TnLoopProtectPortLastLoopTime_Type = DateAndTime
_TnLoopProtectPortLastLoopTime_Object = MibTableColumn
tnLoopProtectPortLastLoopTime = _TnLoopProtectPortLastLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 1, 1, 2, 1, 7),
    _TnLoopProtectPortLastLoopTime_Type()
)
tnLoopProtectPortLastLoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLoopProtectPortLastLoopTime.setStatus("current")

# Managed Objects groups


# Notification objects

tnLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 22, 0, 1)
)
tnLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-LOOP-PROTECT-MIB", "tnLoopProtectPortLoopCount"),
        ("TN-LOOP-PROTECT-MIB", "tnLoopProtectPortAction"))
)
if mibBuilder.loadTexts:
    tnLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LOOP-PROTECT-MIB",
    **{"tnLoopProtectMIB": tnLoopProtectMIB,
       "tnLoopProtectNotifications": tnLoopProtectNotifications,
       "tnLoopProtectLoopDetectedNotification": tnLoopProtectLoopDetectedNotification,
       "tnLoopProtectObjects": tnLoopProtectObjects,
       "tnLoopProtectMgmt": tnLoopProtectMgmt,
       "tnLoopProtectBaseTable": tnLoopProtectBaseTable,
       "tnLoopProtectBaseEntry": tnLoopProtectBaseEntry,
       "tnLoopProtectEnable": tnLoopProtectEnable,
       "tnLoopProtectTxTime": tnLoopProtectTxTime,
       "tnLoopProtectShutdownTime": tnLoopProtectShutdownTime,
       "tnLoopProtectPortTable": tnLoopProtectPortTable,
       "tnLoopProtectPortEntry": tnLoopProtectPortEntry,
       "tnLoopProtectPortEnable": tnLoopProtectPortEnable,
       "tnLoopProtectPortAction": tnLoopProtectPortAction,
       "tnLoopProtectPortTxModeEnable": tnLoopProtectPortTxModeEnable,
       "tnLoopProtectPortLoopCount": tnLoopProtectPortLoopCount,
       "tnLoopProtectPortStatus": tnLoopProtectPortStatus,
       "tnLoopProtectPortLoopDetected": tnLoopProtectPortLoopDetected,
       "tnLoopProtectPortLastLoopTime": tnLoopProtectPortLastLoopTime}
)
