# SNMP MIB module (JUNIPER-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-BFD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:57 2025
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

(bfdSessIndex,) = mibBuilder.importSymbols(
    "BFD-STD-MIB",
    "bfdSessIndex")

(jnxBfdMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxBfdMibRoot")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxBfdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1)
)
if mibBuilder.loadTexts:
    jnxBfdMib.setRevisions(
        ("2006-10-12 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxBfdNotification_ObjectIdentity = ObjectIdentity
jnxBfdNotification = _JnxBfdNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0)
)
_JnxBfdObjects_ObjectIdentity = ObjectIdentity
jnxBfdObjects = _JnxBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1)
)
_JnxBfdSessTable_Object = MibTable
jnxBfdSessTable = _JnxBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBfdSessTable.setStatus("current")
_JnxBfdSessEntry_Object = MibTableRow
jnxBfdSessEntry = _JnxBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1)
)
jnxBfdSessEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessIndex"),
)
if mibBuilder.loadTexts:
    jnxBfdSessEntry.setStatus("current")
_JnxBfdSessThreshTxInterval_Type = Unsigned32
_JnxBfdSessThreshTxInterval_Object = MibTableColumn
jnxBfdSessThreshTxInterval = _JnxBfdSessThreshTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 1),
    _JnxBfdSessThreshTxInterval_Type()
)
jnxBfdSessThreshTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessThreshTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessThreshTxInterval.setUnits("microseconds")
_JnxBfdSessCurrTxInterval_Type = Unsigned32
_JnxBfdSessCurrTxInterval_Object = MibTableColumn
jnxBfdSessCurrTxInterval = _JnxBfdSessCurrTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 2),
    _JnxBfdSessCurrTxInterval_Type()
)
jnxBfdSessCurrTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessCurrTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessCurrTxInterval.setUnits("microseconds")
_JnxBfdSessThreshDectTime_Type = Unsigned32
_JnxBfdSessThreshDectTime_Object = MibTableColumn
jnxBfdSessThreshDectTime = _JnxBfdSessThreshDectTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 3),
    _JnxBfdSessThreshDectTime_Type()
)
jnxBfdSessThreshDectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessThreshDectTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessThreshDectTime.setUnits("microseconds")
_JnxBfdSessCurrDectTime_Type = Unsigned32
_JnxBfdSessCurrDectTime_Object = MibTableColumn
jnxBfdSessCurrDectTime = _JnxBfdSessCurrDectTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 4),
    _JnxBfdSessCurrDectTime_Type()
)
jnxBfdSessCurrDectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessCurrDectTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessCurrDectTime.setUnits("microseconds")
_JnxBfdSessIntfName_Type = DisplayString
_JnxBfdSessIntfName_Object = MibTableColumn
jnxBfdSessIntfName = _JnxBfdSessIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 5),
    _JnxBfdSessIntfName_Type()
)
jnxBfdSessIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessIntfName.setStatus("current")
_JnxBfdNotifyObjects_ObjectIdentity = ObjectIdentity
jnxBfdNotifyObjects = _JnxBfdNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 2)
)
_JnxBfdSessifName_Type = DisplayString
_JnxBfdSessifName_Object = MibScalar
jnxBfdSessifName = _JnxBfdSessifName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 2, 1),
    _JnxBfdSessifName_Type()
)
jnxBfdSessifName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBfdSessifName.setStatus("current")

# Managed Objects groups


# Notification objects

jnxBfdSessTxIntervalHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0, 1)
)
jnxBfdSessTxIntervalHigh.setObjects(
      *(("JUNIPER-BFD-MIB", "jnxBfdSessThreshTxInterval"),
        ("JUNIPER-BFD-MIB", "jnxBfdSessCurrTxInterval"))
)
if mibBuilder.loadTexts:
    jnxBfdSessTxIntervalHigh.setStatus(
        "current"
    )

jnxBfdSessDetectionTimeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0, 2)
)
jnxBfdSessDetectionTimeHigh.setObjects(
      *(("JUNIPER-BFD-MIB", "jnxBfdSessThreshDectTime"),
        ("JUNIPER-BFD-MIB", "jnxBfdSessCurrDectTime"))
)
if mibBuilder.loadTexts:
    jnxBfdSessDetectionTimeHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-BFD-MIB",
    **{"jnxBfdMib": jnxBfdMib,
       "jnxBfdNotification": jnxBfdNotification,
       "jnxBfdSessTxIntervalHigh": jnxBfdSessTxIntervalHigh,
       "jnxBfdSessDetectionTimeHigh": jnxBfdSessDetectionTimeHigh,
       "jnxBfdObjects": jnxBfdObjects,
       "jnxBfdSessTable": jnxBfdSessTable,
       "jnxBfdSessEntry": jnxBfdSessEntry,
       "jnxBfdSessThreshTxInterval": jnxBfdSessThreshTxInterval,
       "jnxBfdSessCurrTxInterval": jnxBfdSessCurrTxInterval,
       "jnxBfdSessThreshDectTime": jnxBfdSessThreshDectTime,
       "jnxBfdSessCurrDectTime": jnxBfdSessCurrDectTime,
       "jnxBfdSessIntfName": jnxBfdSessIntfName,
       "jnxBfdNotifyObjects": jnxBfdNotifyObjects,
       "jnxBfdSessifName": jnxBfdSessifName}
)
