# SNMP MIB module (DLINKSW-ASP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ASP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:41 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwArpSpoofingPreventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76)
)
if mibBuilder.loadTexts:
    dlinkSwArpSpoofingPreventMIB.setRevisions(
        ("2016-07-05 00:00",
         "2013-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DAspMIBNotifications_ObjectIdentity = ObjectIdentity
dAspMIBNotifications = _DAspMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 0)
)
_DAspMIBObjects_ObjectIdentity = ObjectIdentity
dAspMIBObjects = _DAspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1)
)
_DAspGatewayTable_Object = MibTable
dAspGatewayTable = _DAspGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1)
)
if mibBuilder.loadTexts:
    dAspGatewayTable.setStatus("current")
_DAspGatewayEntry_Object = MibTableRow
dAspGatewayEntry = _DAspGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1)
)
dAspGatewayEntry.setIndexNames(
    (0, "DLINKSW-ASP-MIB", "dAspGatewayIP"),
    (0, "DLINKSW-ASP-MIB", "dAspGatewayMAC"),
)
if mibBuilder.loadTexts:
    dAspGatewayEntry.setStatus("current")
_DAspGatewayIP_Type = IpAddress
_DAspGatewayIP_Object = MibTableColumn
dAspGatewayIP = _DAspGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 1),
    _DAspGatewayIP_Type()
)
dAspGatewayIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAspGatewayIP.setStatus("current")
_DAspGatewayMAC_Type = MacAddress
_DAspGatewayMAC_Object = MibTableColumn
dAspGatewayMAC = _DAspGatewayMAC_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 2),
    _DAspGatewayMAC_Type()
)
dAspGatewayMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAspGatewayMAC.setStatus("current")
_DAspActivePortList_Type = PortList
_DAspActivePortList_Object = MibTableColumn
dAspActivePortList = _DAspActivePortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 3),
    _DAspActivePortList_Type()
)
dAspActivePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAspActivePortList.setStatus("current")
_DAspGatewayRowStatus_Type = RowStatus
_DAspGatewayRowStatus_Object = MibTableColumn
dAspGatewayRowStatus = _DAspGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 1, 1, 99),
    _DAspGatewayRowStatus_Type()
)
dAspGatewayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAspGatewayRowStatus.setStatus("current")
_DAspLoggingEnabled_Type = TruthValue
_DAspLoggingEnabled_Object = MibScalar
dAspLoggingEnabled = _DAspLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 1, 2),
    _DAspLoggingEnabled_Type()
)
dAspLoggingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAspLoggingEnabled.setStatus("current")
_DAspMIBConformance_ObjectIdentity = ObjectIdentity
dAspMIBConformance = _DAspMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2)
)
_DAspMIBCompliances_ObjectIdentity = ObjectIdentity
dAspMIBCompliances = _DAspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1)
)
_DAspMIBGroups_ObjectIdentity = ObjectIdentity
dAspMIBGroups = _DAspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2)
)

# Managed Objects groups

dAspMgtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 1)
)
dAspMgtGroup.setObjects(
      *(("DLINKSW-ASP-MIB", "dAspActivePortList"),
        ("DLINKSW-ASP-MIB", "dAspGatewayRowStatus"))
)
if mibBuilder.loadTexts:
    dAspMgtGroup.setStatus("current")

dAspLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 2, 2)
)
dAspLoggingGroup.setObjects(
    ("DLINKSW-ASP-MIB", "dAspLoggingEnabled")
)
if mibBuilder.loadTexts:
    dAspLoggingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dAspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 1)
)
dAspCompliance.setObjects(
    ("DLINKSW-ASP-MIB", "dAspMgtGroup")
)
if mibBuilder.loadTexts:
    dAspCompliance.setStatus(
        "deprecated"
    )

dAspCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 76, 2, 1, 2)
)
dAspCompliance2.setObjects(
      *(("DLINKSW-ASP-MIB", "dAspMgtGroup"),
        ("DLINKSW-ASP-MIB", "dAspLoggingGroup"))
)
if mibBuilder.loadTexts:
    dAspCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ASP-MIB",
    **{"dlinkSwArpSpoofingPreventMIB": dlinkSwArpSpoofingPreventMIB,
       "dAspMIBNotifications": dAspMIBNotifications,
       "dAspMIBObjects": dAspMIBObjects,
       "dAspGatewayTable": dAspGatewayTable,
       "dAspGatewayEntry": dAspGatewayEntry,
       "dAspGatewayIP": dAspGatewayIP,
       "dAspGatewayMAC": dAspGatewayMAC,
       "dAspActivePortList": dAspActivePortList,
       "dAspGatewayRowStatus": dAspGatewayRowStatus,
       "dAspLoggingEnabled": dAspLoggingEnabled,
       "dAspMIBConformance": dAspMIBConformance,
       "dAspMIBCompliances": dAspMIBCompliances,
       "dAspCompliance": dAspCompliance,
       "dAspCompliance2": dAspCompliance2,
       "dAspMIBGroups": dAspMIBGroups,
       "dAspMgtGroup": dAspMgtGroup,
       "dAspLoggingGroup": dAspLoggingGroup}
)
