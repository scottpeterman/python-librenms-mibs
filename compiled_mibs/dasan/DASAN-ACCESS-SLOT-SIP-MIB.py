# SNMP MIB module (DASAN-ACCESS-SLOT-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\DASAN-ACCESS-SLOT-SIP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:57 2025
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

(dasanMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasanMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

dasanAccessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100)
)
if mibBuilder.loadTexts:
    dasanAccessMib.setRevisions(
        ("2005-02-11 21:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DasanAccGatewayMIBObjects_ObjectIdentity = ObjectIdentity
dasanAccGatewayMIBObjects = _DasanAccGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2)
)
_DsAccGwySip_ObjectIdentity = ObjectIdentity
dsAccGwySip = _DsAccGwySip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4)
)
_DsAccGwySipConfiguration_ObjectIdentity = ObjectIdentity
dsAccGwySipConfiguration = _DsAccGwySipConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1)
)
_DsAccGwyConfigSipSlot_ObjectIdentity = ObjectIdentity
dsAccGwyConfigSipSlot = _DsAccGwyConfigSipSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1)
)
_DsAccGwyConfigSipSlotTable_Object = MibTable
dsAccGwyConfigSipSlotTable = _DsAccGwyConfigSipSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSipSlotTable.setStatus("current")
_DsAccGwyConfigSipSlotEntry_Object = MibTableRow
dsAccGwyConfigSipSlotEntry = _DsAccGwyConfigSipSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1)
)
dsAccGwyConfigSipSlotEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-SIP-MIB", "dsSipSlotIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSipSlotEntry.setStatus("current")
_DsSipSlotIndex_Type = Integer32
_DsSipSlotIndex_Object = MibTableColumn
dsSipSlotIndex = _DsSipSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 1),
    _DsSipSlotIndex_Type()
)
dsSipSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSipSlotIndex.setStatus("current")
_DsSipSlotDomain_Type = DisplayString
_DsSipSlotDomain_Object = MibTableColumn
dsSipSlotDomain = _DsSipSlotDomain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 2),
    _DsSipSlotDomain_Type()
)
dsSipSlotDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotDomain.setStatus("current")
_DsSipSlotSockMode_Type = Integer32
_DsSipSlotSockMode_Object = MibTableColumn
dsSipSlotSockMode = _DsSipSlotSockMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 3),
    _DsSipSlotSockMode_Type()
)
dsSipSlotSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotSockMode.setStatus("current")
_DsSipSlotSipPort_Type = Integer32
_DsSipSlotSipPort_Object = MibTableColumn
dsSipSlotSipPort = _DsSipSlotSipPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 4),
    _DsSipSlotSipPort_Type()
)
dsSipSlotSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotSipPort.setStatus("current")
_DsSipSlotProxyAddr1_Type = DisplayString
_DsSipSlotProxyAddr1_Object = MibTableColumn
dsSipSlotProxyAddr1 = _DsSipSlotProxyAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 5),
    _DsSipSlotProxyAddr1_Type()
)
dsSipSlotProxyAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyAddr1.setStatus("current")
_DsSipSlotProxyPort1_Type = Integer32
_DsSipSlotProxyPort1_Object = MibTableColumn
dsSipSlotProxyPort1 = _DsSipSlotProxyPort1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 6),
    _DsSipSlotProxyPort1_Type()
)
dsSipSlotProxyPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyPort1.setStatus("current")
_DsSipSlotProxyAddr2_Type = DisplayString
_DsSipSlotProxyAddr2_Object = MibTableColumn
dsSipSlotProxyAddr2 = _DsSipSlotProxyAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 7),
    _DsSipSlotProxyAddr2_Type()
)
dsSipSlotProxyAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyAddr2.setStatus("current")
_DsSipSlotProxyPort2_Type = Integer32
_DsSipSlotProxyPort2_Object = MibTableColumn
dsSipSlotProxyPort2 = _DsSipSlotProxyPort2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 8),
    _DsSipSlotProxyPort2_Type()
)
dsSipSlotProxyPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyPort2.setStatus("current")
_DsSipSlotProxyAddr3_Type = DisplayString
_DsSipSlotProxyAddr3_Object = MibTableColumn
dsSipSlotProxyAddr3 = _DsSipSlotProxyAddr3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 9),
    _DsSipSlotProxyAddr3_Type()
)
dsSipSlotProxyAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyAddr3.setStatus("current")
_DsSipSlotProxyPort3_Type = Integer32
_DsSipSlotProxyPort3_Object = MibTableColumn
dsSipSlotProxyPort3 = _DsSipSlotProxyPort3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 10),
    _DsSipSlotProxyPort3_Type()
)
dsSipSlotProxyPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotProxyPort3.setStatus("current")
_DsSipSlotHuntMapItem_Type = DisplayString
_DsSipSlotHuntMapItem_Object = MibTableColumn
dsSipSlotHuntMapItem = _DsSipSlotHuntMapItem_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 11),
    _DsSipSlotHuntMapItem_Type()
)
dsSipSlotHuntMapItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotHuntMapItem.setStatus("current")
_DsSipSlotDigitMapItem_Type = DisplayString
_DsSipSlotDigitMapItem_Object = MibTableColumn
dsSipSlotDigitMapItem = _DsSipSlotDigitMapItem_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 12),
    _DsSipSlotDigitMapItem_Type()
)
dsSipSlotDigitMapItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotDigitMapItem.setStatus("current")
_DsSipSlotSigProvisionTO_Type = Integer32
_DsSipSlotSigProvisionTO_Object = MibTableColumn
dsSipSlotSigProvisionTO = _DsSipSlotSigProvisionTO_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 13),
    _DsSipSlotSigProvisionTO_Type()
)
dsSipSlotSigProvisionTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotSigProvisionTO.setStatus("current")
_DsSipSlotSigAleringTO_Type = Integer32
_DsSipSlotSigAleringTO_Object = MibTableColumn
dsSipSlotSigAleringTO = _DsSipSlotSigAleringTO_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 14),
    _DsSipSlotSigAleringTO_Type()
)
dsSipSlotSigAleringTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotSigAleringTO.setStatus("current")
_DsSipSlotSigConnectTO_Type = Integer32
_DsSipSlotSigConnectTO_Object = MibTableColumn
dsSipSlotSigConnectTO = _DsSipSlotSigConnectTO_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 15),
    _DsSipSlotSigConnectTO_Type()
)
dsSipSlotSigConnectTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotSigConnectTO.setStatus("current")
_DsSipSlotHookOffTO_Type = Integer32
_DsSipSlotHookOffTO_Object = MibTableColumn
dsSipSlotHookOffTO = _DsSipSlotHookOffTO_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 16),
    _DsSipSlotHookOffTO_Type()
)
dsSipSlotHookOffTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotHookOffTO.setStatus("current")
_DsSipSlotHookOnTO_Type = Integer32
_DsSipSlotHookOnTO_Object = MibTableColumn
dsSipSlotHookOnTO = _DsSipSlotHookOnTO_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 1, 1, 1, 17),
    _DsSipSlotHookOnTO_Type()
)
dsSipSlotHookOnTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipSlotHookOnTO.setStatus("current")
_DsAccGwyConfigSipPort_ObjectIdentity = ObjectIdentity
dsAccGwyConfigSipPort = _DsAccGwyConfigSipPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2)
)
_DsAccGwyConfigSipPortTable_Object = MibTable
dsAccGwyConfigSipPortTable = _DsAccGwyConfigSipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSipPortTable.setStatus("current")
_DsAccGwyConfigSipPortEntry_Object = MibTableRow
dsAccGwyConfigSipPortEntry = _DsAccGwyConfigSipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1)
)
dsAccGwyConfigSipPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-SIP-MIB", "dsSipPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyConfigSipPortEntry.setStatus("current")
_DsSipPortIndex_Type = Integer32
_DsSipPortIndex_Object = MibTableColumn
dsSipPortIndex = _DsSipPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 1),
    _DsSipPortIndex_Type()
)
dsSipPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSipPortIndex.setStatus("current")
_DsSipPortMyTel_Type = DisplayString
_DsSipPortMyTel_Object = MibTableColumn
dsSipPortMyTel = _DsSipPortMyTel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 2),
    _DsSipPortMyTel_Type()
)
dsSipPortMyTel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortMyTel.setStatus("current")
_DsSipPortURI_Type = DisplayString
_DsSipPortURI_Object = MibTableColumn
dsSipPortURI = _DsSipPortURI_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 3),
    _DsSipPortURI_Type()
)
dsSipPortURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortURI.setStatus("current")
_DsSipPortContactURI_Type = DisplayString
_DsSipPortContactURI_Object = MibTableColumn
dsSipPortContactURI = _DsSipPortContactURI_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 4),
    _DsSipPortContactURI_Type()
)
dsSipPortContactURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortContactURI.setStatus("current")
_DsSipPortDisplayName_Type = DisplayString
_DsSipPortDisplayName_Object = MibTableColumn
dsSipPortDisplayName = _DsSipPortDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 5),
    _DsSipPortDisplayName_Type()
)
dsSipPortDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortDisplayName.setStatus("current")
_DsSipPortUserName_Type = DisplayString
_DsSipPortUserName_Object = MibTableColumn
dsSipPortUserName = _DsSipPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 6),
    _DsSipPortUserName_Type()
)
dsSipPortUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortUserName.setStatus("current")
_DsSipPortUserID_Type = DisplayString
_DsSipPortUserID_Object = MibTableColumn
dsSipPortUserID = _DsSipPortUserID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 7),
    _DsSipPortUserID_Type()
)
dsSipPortUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortUserID.setStatus("current")
_DsSipPortUserPW_Type = DisplayString
_DsSipPortUserPW_Object = MibTableColumn
dsSipPortUserPW = _DsSipPortUserPW_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 8),
    _DsSipPortUserPW_Type()
)
dsSipPortUserPW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortUserPW.setStatus("current")
_DsSipPortRealM_Type = DisplayString
_DsSipPortRealM_Object = MibTableColumn
dsSipPortRealM = _DsSipPortRealM_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 9),
    _DsSipPortRealM_Type()
)
dsSipPortRealM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortRealM.setStatus("current")
_DsSipPortExpiry_Type = Integer32
_DsSipPortExpiry_Object = MibTableColumn
dsSipPortExpiry = _DsSipPortExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 1, 2, 1, 1, 10),
    _DsSipPortExpiry_Type()
)
dsSipPortExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsSipPortExpiry.setStatus("current")
_DsAccGwySipMonitor_ObjectIdentity = ObjectIdentity
dsAccGwySipMonitor = _DsAccGwySipMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2)
)
_DsAccGwyMonitorSipPort_ObjectIdentity = ObjectIdentity
dsAccGwyMonitorSipPort = _DsAccGwyMonitorSipPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2, 1)
)
_DsAccGwyMonitorSipPortTable_Object = MibTable
dsAccGwyMonitorSipPortTable = _DsAccGwyMonitorSipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorSipPortTable.setStatus("current")
_DsAccGwyMonitorSipPortEntry_Object = MibTableRow
dsAccGwyMonitorSipPortEntry = _DsAccGwyMonitorSipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2, 1, 1, 1)
)
dsAccGwyMonitorSipPortEntry.setIndexNames(
    (0, "DASAN-ACCESS-SLOT-SIP-MIB", "dsMonitorSipPortIndex"),
)
if mibBuilder.loadTexts:
    dsAccGwyMonitorSipPortEntry.setStatus("current")
_DsMonitorSipPortIndex_Type = Integer32
_DsMonitorSipPortIndex_Object = MibTableColumn
dsMonitorSipPortIndex = _DsMonitorSipPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2, 1, 1, 1, 1),
    _DsMonitorSipPortIndex_Type()
)
dsMonitorSipPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsMonitorSipPortIndex.setStatus("current")
_DsSipPortProxyStatus_Type = Integer32
_DsSipPortProxyStatus_Object = MibTableColumn
dsSipPortProxyStatus = _DsSipPortProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 9, 100, 2, 4, 2, 1, 1, 1, 2),
    _DsSipPortProxyStatus_Type()
)
dsSipPortProxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSipPortProxyStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DASAN-ACCESS-SLOT-SIP-MIB",
    **{"dasanAccessMib": dasanAccessMib,
       "dasanAccGatewayMIBObjects": dasanAccGatewayMIBObjects,
       "dsAccGwySip": dsAccGwySip,
       "dsAccGwySipConfiguration": dsAccGwySipConfiguration,
       "dsAccGwyConfigSipSlot": dsAccGwyConfigSipSlot,
       "dsAccGwyConfigSipSlotTable": dsAccGwyConfigSipSlotTable,
       "dsAccGwyConfigSipSlotEntry": dsAccGwyConfigSipSlotEntry,
       "dsSipSlotIndex": dsSipSlotIndex,
       "dsSipSlotDomain": dsSipSlotDomain,
       "dsSipSlotSockMode": dsSipSlotSockMode,
       "dsSipSlotSipPort": dsSipSlotSipPort,
       "dsSipSlotProxyAddr1": dsSipSlotProxyAddr1,
       "dsSipSlotProxyPort1": dsSipSlotProxyPort1,
       "dsSipSlotProxyAddr2": dsSipSlotProxyAddr2,
       "dsSipSlotProxyPort2": dsSipSlotProxyPort2,
       "dsSipSlotProxyAddr3": dsSipSlotProxyAddr3,
       "dsSipSlotProxyPort3": dsSipSlotProxyPort3,
       "dsSipSlotHuntMapItem": dsSipSlotHuntMapItem,
       "dsSipSlotDigitMapItem": dsSipSlotDigitMapItem,
       "dsSipSlotSigProvisionTO": dsSipSlotSigProvisionTO,
       "dsSipSlotSigAleringTO": dsSipSlotSigAleringTO,
       "dsSipSlotSigConnectTO": dsSipSlotSigConnectTO,
       "dsSipSlotHookOffTO": dsSipSlotHookOffTO,
       "dsSipSlotHookOnTO": dsSipSlotHookOnTO,
       "dsAccGwyConfigSipPort": dsAccGwyConfigSipPort,
       "dsAccGwyConfigSipPortTable": dsAccGwyConfigSipPortTable,
       "dsAccGwyConfigSipPortEntry": dsAccGwyConfigSipPortEntry,
       "dsSipPortIndex": dsSipPortIndex,
       "dsSipPortMyTel": dsSipPortMyTel,
       "dsSipPortURI": dsSipPortURI,
       "dsSipPortContactURI": dsSipPortContactURI,
       "dsSipPortDisplayName": dsSipPortDisplayName,
       "dsSipPortUserName": dsSipPortUserName,
       "dsSipPortUserID": dsSipPortUserID,
       "dsSipPortUserPW": dsSipPortUserPW,
       "dsSipPortRealM": dsSipPortRealM,
       "dsSipPortExpiry": dsSipPortExpiry,
       "dsAccGwySipMonitor": dsAccGwySipMonitor,
       "dsAccGwyMonitorSipPort": dsAccGwyMonitorSipPort,
       "dsAccGwyMonitorSipPortTable": dsAccGwyMonitorSipPortTable,
       "dsAccGwyMonitorSipPortEntry": dsAccGwyMonitorSipPortEntry,
       "dsMonitorSipPortIndex": dsMonitorSipPortIndex,
       "dsSipPortProxyStatus": dsSipPortProxyStatus}
)
