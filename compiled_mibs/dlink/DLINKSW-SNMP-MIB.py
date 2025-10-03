# SNMP MIB module (DLINKSW-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:51 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,
 SnmpEngineID,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpSecurityModel")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2)
)
if mibBuilder.loadTexts:
    dlinkSwSnmpMIB.setRevisions(
        ("2013-04-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DSnmpMIBNotifications_ObjectIdentity = ObjectIdentity
dSnmpMIBNotifications = _DSnmpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 0)
)
_DSnmpMIBObjects_ObjectIdentity = ObjectIdentity
dSnmpMIBObjects = _DSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1)
)
_DSnmpGeneral_ObjectIdentity = ObjectIdentity
dSnmpGeneral = _DSnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 1)
)
_DSnmpServiceEnabled_Type = TruthValue
_DSnmpServiceEnabled_Object = MibScalar
dSnmpServiceEnabled = _DSnmpServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 1, 1),
    _DSnmpServiceEnabled_Type()
)
dSnmpServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpServiceEnabled.setStatus("current")
_DSnmpServiceUdpPort_Type = Unsigned32
_DSnmpServiceUdpPort_Object = MibScalar
dSnmpServiceUdpPort = _DSnmpServiceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 1, 2),
    _DSnmpServiceUdpPort_Type()
)
dSnmpServiceUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpServiceUdpPort.setStatus("current")
_DSnmpRspBcastRequestEnabled_Type = TruthValue
_DSnmpRspBcastRequestEnabled_Object = MibScalar
dSnmpRspBcastRequestEnabled = _DSnmpRspBcastRequestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 1, 3),
    _DSnmpRspBcastRequestEnabled_Type()
)
dSnmpRspBcastRequestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpRspBcastRequestEnabled.setStatus("current")
_DSnmpLocalEngineID_Type = SnmpEngineID
_DSnmpLocalEngineID_Object = MibScalar
dSnmpLocalEngineID = _DSnmpLocalEngineID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 1, 4),
    _DSnmpLocalEngineID_Type()
)
dSnmpLocalEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpLocalEngineID.setStatus("current")
_DSnmpMIBTrap_ObjectIdentity = ObjectIdentity
dSnmpMIBTrap = _DSnmpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2)
)
_DSnmpTrapGlobalEnabled_Type = TruthValue
_DSnmpTrapGlobalEnabled_Object = MibScalar
dSnmpTrapGlobalEnabled = _DSnmpTrapGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 1),
    _DSnmpTrapGlobalEnabled_Type()
)
dSnmpTrapGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpTrapGlobalEnabled.setStatus("current")


class _DSnmpTrapGlobalNotifyEnable_Type(Bits):
    """Custom type dSnmpTrapGlobalNotifyEnable based on Bits"""
    namedValues = NamedValues(
        *(("linkUp", 0),
          ("linkDown", 1),
          ("coldStart", 2),
          ("warmStart", 3),
          ("authentication", 4))
    )

_DSnmpTrapGlobalNotifyEnable_Type.__name__ = "Bits"
_DSnmpTrapGlobalNotifyEnable_Object = MibScalar
dSnmpTrapGlobalNotifyEnable = _DSnmpTrapGlobalNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 2),
    _DSnmpTrapGlobalNotifyEnable_Type()
)
dSnmpTrapGlobalNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpTrapGlobalNotifyEnable.setStatus("current")
_DSnmpTrapSourceIfIndex_Type = InterfaceIndexOrZero
_DSnmpTrapSourceIfIndex_Object = MibScalar
dSnmpTrapSourceIfIndex = _DSnmpTrapSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 3),
    _DSnmpTrapSourceIfIndex_Type()
)
dSnmpTrapSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpTrapSourceIfIndex.setStatus("current")
_DSnmpTrapIfCtrl_ObjectIdentity = ObjectIdentity
dSnmpTrapIfCtrl = _DSnmpTrapIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 4)
)
_DSnmpTrapIfCfgTable_Object = MibTable
dSnmpTrapIfCfgTable = _DSnmpTrapIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dSnmpTrapIfCfgTable.setStatus("current")
_DSnmpTrapIfCfgEntry_Object = MibTableRow
dSnmpTrapIfCfgEntry = _DSnmpTrapIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 4, 1, 1)
)
dSnmpTrapIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dSnmpTrapIfCfgEntry.setStatus("current")


class _DSnmpTrapIfSendTrapEnabled_Type(TruthValue):
    """Custom type dSnmpTrapIfSendTrapEnabled based on TruthValue"""
    defaultValue = 1


_DSnmpTrapIfSendTrapEnabled_Type.__name__ = "TruthValue"
_DSnmpTrapIfSendTrapEnabled_Object = MibTableColumn
dSnmpTrapIfSendTrapEnabled = _DSnmpTrapIfSendTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 2, 4, 1, 1, 1),
    _DSnmpTrapIfSendTrapEnabled_Type()
)
dSnmpTrapIfSendTrapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSnmpTrapIfSendTrapEnabled.setStatus("current")
_DSnmpAccessCfg_ObjectIdentity = ObjectIdentity
dSnmpAccessCfg = _DSnmpAccessCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3)
)
_DSnmpCommunityTable_Object = MibTable
dSnmpCommunityTable = _DSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dSnmpCommunityTable.setStatus("current")
_DSnmpCommunityEntry_Object = MibTableRow
dSnmpCommunityEntry = _DSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 1, 1)
)
dSnmpCommunityEntry.setIndexNames(
    (0, "DLINKSW-SNMP-MIB", "dSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    dSnmpCommunityEntry.setStatus("current")
_DSnmpCommunityName_Type = SnmpAdminString
_DSnmpCommunityName_Object = MibTableColumn
dSnmpCommunityName = _DSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 1, 1, 1),
    _DSnmpCommunityName_Type()
)
dSnmpCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSnmpCommunityName.setStatus("current")
_DSnmpCommunityAccessListName_Type = DisplayString
_DSnmpCommunityAccessListName_Object = MibTableColumn
dSnmpCommunityAccessListName = _DSnmpCommunityAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 1, 1, 3),
    _DSnmpCommunityAccessListName_Type()
)
dSnmpCommunityAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpCommunityAccessListName.setStatus("current")
_DSnmpGroupTable_Object = MibTable
dSnmpGroupTable = _DSnmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dSnmpGroupTable.setStatus("current")
_DSnmpGroupEntry_Object = MibTableRow
dSnmpGroupEntry = _DSnmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 2, 1)
)
dSnmpGroupEntry.setIndexNames(
    (0, "DLINKSW-SNMP-MIB", "dSnmpGroupName"),
    (0, "DLINKSW-SNMP-MIB", "dSnmpGroupVersion"),
)
if mibBuilder.loadTexts:
    dSnmpGroupEntry.setStatus("current")
_DSnmpGroupName_Type = SnmpAdminString
_DSnmpGroupName_Object = MibTableColumn
dSnmpGroupName = _DSnmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 2, 1, 1),
    _DSnmpGroupName_Type()
)
dSnmpGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSnmpGroupName.setStatus("current")
_DSnmpGroupVersion_Type = SnmpSecurityModel
_DSnmpGroupVersion_Object = MibTableColumn
dSnmpGroupVersion = _DSnmpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 2, 1, 2),
    _DSnmpGroupVersion_Type()
)
dSnmpGroupVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSnmpGroupVersion.setStatus("current")
_DSnmpGroupAccessListName_Type = DisplayString
_DSnmpGroupAccessListName_Object = MibTableColumn
dSnmpGroupAccessListName = _DSnmpGroupAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 2, 1, 3),
    _DSnmpGroupAccessListName_Type()
)
dSnmpGroupAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpGroupAccessListName.setStatus("current")
_DSnmpHostTable_Object = MibTable
dSnmpHostTable = _DSnmpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dSnmpHostTable.setStatus("current")
_DSnmpHostEntry_Object = MibTableRow
dSnmpHostEntry = _DSnmpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 3, 1)
)
dSnmpHostEntry.setIndexNames(
    (0, "DLINKSW-SNMP-MIB", "dSnmpHostAddrName"),
)
if mibBuilder.loadTexts:
    dSnmpHostEntry.setStatus("current")


class _DSnmpHostAddrName_Type(SnmpAdminString):
    """Custom type dSnmpHostAddrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DSnmpHostAddrName_Type.__name__ = "SnmpAdminString"
_DSnmpHostAddrName_Object = MibTableColumn
dSnmpHostAddrName = _DSnmpHostAddrName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 3, 1, 1),
    _DSnmpHostAddrName_Type()
)
dSnmpHostAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSnmpHostAddrName.setStatus("current")
_DSnmpHostVrfName_Type = DisplayString
_DSnmpHostVrfName_Object = MibTableColumn
dSnmpHostVrfName = _DSnmpHostVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 3, 1, 2),
    _DSnmpHostVrfName_Type()
)
dSnmpHostVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpHostVrfName.setStatus("current")


class _DSnmpHostUdpPort_Type(Unsigned32):
    """Custom type dSnmpHostUdpPort based on Unsigned32"""
    defaultValue = 162


_DSnmpHostUdpPort_Type.__name__ = "Unsigned32"
_DSnmpHostUdpPort_Object = MibTableColumn
dSnmpHostUdpPort = _DSnmpHostUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 3, 1, 3),
    _DSnmpHostUdpPort_Type()
)
dSnmpHostUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpHostUdpPort.setStatus("current")
_DSnmpUserTable_Object = MibTable
dSnmpUserTable = _DSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dSnmpUserTable.setStatus("current")
_DSnmpUserEntry_Object = MibTableRow
dSnmpUserEntry = _DSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 4, 1)
)
dSnmpUserEntry.setIndexNames(
    (0, "DLINKSW-SNMP-MIB", "dSnmpUserName"),
)
if mibBuilder.loadTexts:
    dSnmpUserEntry.setStatus("current")


class _DSnmpUserName_Type(SnmpAdminString):
    """Custom type dSnmpUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DSnmpUserName_Type.__name__ = "SnmpAdminString"
_DSnmpUserName_Object = MibTableColumn
dSnmpUserName = _DSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 4, 1, 1),
    _DSnmpUserName_Type()
)
dSnmpUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSnmpUserName.setStatus("current")
_DSnmpUserAccessListName_Type = DisplayString
_DSnmpUserAccessListName_Object = MibTableColumn
dSnmpUserAccessListName = _DSnmpUserAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 1, 3, 4, 1, 2),
    _DSnmpUserAccessListName_Type()
)
dSnmpUserAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSnmpUserAccessListName.setStatus("current")
_DSnmpMIBConformance_ObjectIdentity = ObjectIdentity
dSnmpMIBConformance = _DSnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2)
)
_DSnmpCompliances_ObjectIdentity = ObjectIdentity
dSnmpCompliances = _DSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 1)
)
_DSnmpGroups_ObjectIdentity = ObjectIdentity
dSnmpGroups = _DSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2)
)

# Managed Objects groups

dSnmpSysCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 1)
)
dSnmpSysCfgGroup.setObjects(
      *(("DLINKSW-SNMP-MIB", "dSnmpServiceEnabled"),
        ("DLINKSW-SNMP-MIB", "dSnmpServiceUdpPort"),
        ("DLINKSW-SNMP-MIB", "dSnmpRspBcastRequestEnabled"),
        ("DLINKSW-SNMP-MIB", "dSnmpLocalEngineID"))
)
if mibBuilder.loadTexts:
    dSnmpSysCfgGroup.setStatus("current")

dSnmpTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 2)
)
dSnmpTrapCfgGroup.setObjects(
      *(("DLINKSW-SNMP-MIB", "dSnmpTrapGlobalEnabled"),
        ("DLINKSW-SNMP-MIB", "dSnmpTrapGlobalNotifyEnable"),
        ("DLINKSW-SNMP-MIB", "dSnmpTrapSourceIfIndex"))
)
if mibBuilder.loadTexts:
    dSnmpTrapCfgGroup.setStatus("current")

dSnmpTrapIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 3)
)
dSnmpTrapIfCfgGroup.setObjects(
    ("DLINKSW-SNMP-MIB", "dSnmpTrapIfSendTrapEnabled")
)
if mibBuilder.loadTexts:
    dSnmpTrapIfCfgGroup.setStatus("current")

dSnmpCommunityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 4)
)
dSnmpCommunityExtGroup.setObjects(
    ("DLINKSW-SNMP-MIB", "dSnmpCommunityAccessListName")
)
if mibBuilder.loadTexts:
    dSnmpCommunityExtGroup.setStatus("current")

dSnmpTargetExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 5)
)
dSnmpTargetExtGroup.setObjects(
      *(("DLINKSW-SNMP-MIB", "dSnmpHostVrfName"),
        ("DLINKSW-SNMP-MIB", "dSnmpHostUdpPort"))
)
if mibBuilder.loadTexts:
    dSnmpTargetExtGroup.setStatus("current")

dSnmpVacmExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 2, 6)
)
dSnmpVacmExtGroup.setObjects(
      *(("DLINKSW-SNMP-MIB", "dSnmpGroupAccessListName"),
        ("DLINKSW-SNMP-MIB", "dSnmpUserAccessListName"))
)
if mibBuilder.loadTexts:
    dSnmpVacmExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 2, 2, 1, 1)
)
dSnmpCompliance.setObjects(
      *(("DLINKSW-SNMP-MIB", "dSnmpSysCfgGroup"),
        ("DLINKSW-SNMP-MIB", "dSnmpTrapCfgGroup"),
        ("DLINKSW-SNMP-MIB", "dSnmpTargetExtGroup"),
        ("DLINKSW-SNMP-MIB", "dSnmpTrapIfCfgGroup"))
)
if mibBuilder.loadTexts:
    dSnmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SNMP-MIB",
    **{"dlinkSwSnmpMIB": dlinkSwSnmpMIB,
       "dSnmpMIBNotifications": dSnmpMIBNotifications,
       "dSnmpMIBObjects": dSnmpMIBObjects,
       "dSnmpGeneral": dSnmpGeneral,
       "dSnmpServiceEnabled": dSnmpServiceEnabled,
       "dSnmpServiceUdpPort": dSnmpServiceUdpPort,
       "dSnmpRspBcastRequestEnabled": dSnmpRspBcastRequestEnabled,
       "dSnmpLocalEngineID": dSnmpLocalEngineID,
       "dSnmpMIBTrap": dSnmpMIBTrap,
       "dSnmpTrapGlobalEnabled": dSnmpTrapGlobalEnabled,
       "dSnmpTrapGlobalNotifyEnable": dSnmpTrapGlobalNotifyEnable,
       "dSnmpTrapSourceIfIndex": dSnmpTrapSourceIfIndex,
       "dSnmpTrapIfCtrl": dSnmpTrapIfCtrl,
       "dSnmpTrapIfCfgTable": dSnmpTrapIfCfgTable,
       "dSnmpTrapIfCfgEntry": dSnmpTrapIfCfgEntry,
       "dSnmpTrapIfSendTrapEnabled": dSnmpTrapIfSendTrapEnabled,
       "dSnmpAccessCfg": dSnmpAccessCfg,
       "dSnmpCommunityTable": dSnmpCommunityTable,
       "dSnmpCommunityEntry": dSnmpCommunityEntry,
       "dSnmpCommunityName": dSnmpCommunityName,
       "dSnmpCommunityAccessListName": dSnmpCommunityAccessListName,
       "dSnmpGroupTable": dSnmpGroupTable,
       "dSnmpGroupEntry": dSnmpGroupEntry,
       "dSnmpGroupName": dSnmpGroupName,
       "dSnmpGroupVersion": dSnmpGroupVersion,
       "dSnmpGroupAccessListName": dSnmpGroupAccessListName,
       "dSnmpHostTable": dSnmpHostTable,
       "dSnmpHostEntry": dSnmpHostEntry,
       "dSnmpHostAddrName": dSnmpHostAddrName,
       "dSnmpHostVrfName": dSnmpHostVrfName,
       "dSnmpHostUdpPort": dSnmpHostUdpPort,
       "dSnmpUserTable": dSnmpUserTable,
       "dSnmpUserEntry": dSnmpUserEntry,
       "dSnmpUserName": dSnmpUserName,
       "dSnmpUserAccessListName": dSnmpUserAccessListName,
       "dSnmpMIBConformance": dSnmpMIBConformance,
       "dSnmpCompliances": dSnmpCompliances,
       "dSnmpCompliance": dSnmpCompliance,
       "dSnmpGroups": dSnmpGroups,
       "dSnmpSysCfgGroup": dSnmpSysCfgGroup,
       "dSnmpTrapCfgGroup": dSnmpTrapCfgGroup,
       "dSnmpTrapIfCfgGroup": dSnmpTrapIfCfgGroup,
       "dSnmpCommunityExtGroup": dSnmpCommunityExtGroup,
       "dSnmpTargetExtGroup": dSnmpTargetExtGroup,
       "dSnmpVacmExtGroup": dSnmpVacmExtGroup}
)
