# SNMP MIB module (DLINKSW-DDP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DDP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:47 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDdpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161)
)
if mibBuilder.loadTexts:
    dlinkSwDdpClientMIB.setRevisions(
        ("2013-08-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDdpClientNotifications_ObjectIdentity = ObjectIdentity
dDdpClientNotifications = _DDdpClientNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 0)
)
_DDdpClientObjects_ObjectIdentity = ObjectIdentity
dDdpClientObjects = _DDdpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1)
)
_DDdpClientCtrl_ObjectIdentity = ObjectIdentity
dDdpClientCtrl = _DDdpClientCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1)
)


class _DDdpClientGlobalState_Type(TruthValue):
    """Custom type dDdpClientGlobalState based on TruthValue"""
    defaultValue = 1


_DDdpClientGlobalState_Type.__name__ = "TruthValue"
_DDdpClientGlobalState_Object = MibScalar
dDdpClientGlobalState = _DDdpClientGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 1),
    _DDdpClientGlobalState_Type()
)
dDdpClientGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdpClientGlobalState.setStatus("current")


class _DDdpClientReportTimer_Type(Unsigned32):
    """Custom type dDdpClientReportTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_DDdpClientReportTimer_Type.__name__ = "Unsigned32"
_DDdpClientReportTimer_Object = MibScalar
dDdpClientReportTimer = _DDdpClientReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 2),
    _DDdpClientReportTimer_Type()
)
dDdpClientReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdpClientReportTimer.setStatus("current")
if mibBuilder.loadTexts:
    dDdpClientReportTimer.setUnits("second")
_DDdpClientTable_Object = MibTable
dDdpClientTable = _DDdpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dDdpClientTable.setStatus("current")
_DDdpClientEntry_Object = MibTableRow
dDdpClientEntry = _DDdpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1)
)
dDdpClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDdpClientEntry.setStatus("current")


class _DDdpClientPortState_Type(TruthValue):
    """Custom type dDdpClientPortState based on TruthValue"""
    defaultValue = 1


_DDdpClientPortState_Type.__name__ = "TruthValue"
_DDdpClientPortState_Object = MibTableColumn
dDdpClientPortState = _DDdpClientPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 1, 1, 3, 1, 1),
    _DDdpClientPortState_Type()
)
dDdpClientPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDdpClientPortState.setStatus("current")
_DDdpClientConformance_ObjectIdentity = ObjectIdentity
dDdpClientConformance = _DDdpClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 2)
)
_DDdpClientCompliances_ObjectIdentity = ObjectIdentity
dDdpClientCompliances = _DDdpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1)
)
_DDdpClientGroups_ObjectIdentity = ObjectIdentity
dDdpClientGroups = _DDdpClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2)
)

# Managed Objects groups

dDdpClientControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 2, 1)
)
dDdpClientControlGroup.setObjects(
      *(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientGlobalState"),
        ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientPortState"))
)
if mibBuilder.loadTexts:
    dDdpClientControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDdpClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 161, 2, 1, 1)
)
dDdpClientCompliance.setObjects(
      *(("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"),
        ("DLINKSW-DDP-CLIENT-MIB", "dDdpClientControlGroup"))
)
if mibBuilder.loadTexts:
    dDdpClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DDP-CLIENT-MIB",
    **{"dlinkSwDdpClientMIB": dlinkSwDdpClientMIB,
       "dDdpClientNotifications": dDdpClientNotifications,
       "dDdpClientObjects": dDdpClientObjects,
       "dDdpClientCtrl": dDdpClientCtrl,
       "dDdpClientGlobalState": dDdpClientGlobalState,
       "dDdpClientReportTimer": dDdpClientReportTimer,
       "dDdpClientTable": dDdpClientTable,
       "dDdpClientEntry": dDdpClientEntry,
       "dDdpClientPortState": dDdpClientPortState,
       "dDdpClientConformance": dDdpClientConformance,
       "dDdpClientCompliances": dDdpClientCompliances,
       "dDdpClientCompliance": dDdpClientCompliance,
       "dDdpClientGroups": dDdpClientGroups,
       "dDdpClientControlGroup": dDdpClientControlGroup}
)
