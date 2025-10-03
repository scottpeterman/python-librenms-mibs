# SNMP MIB module (CISCO-LWAPP-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-LWAPP-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:26:54 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLStringOrEmpty,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLStringOrEmpty")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappWlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512)
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIB.setRevisions(
        ("2018-07-05 00:00",
         "2018-03-07 00:00",
         "2017-07-22 00:00",
         "2016-12-08 00:00",
         "2016-12-08 00:00",
         "2016-04-07 00:00",
         "2015-04-23 00:00",
         "2015-04-17 00:00",
         "2014-11-05 00:00",
         "2013-03-30 00:00",
         "2012-06-21 00:00",
         "2011-03-10 00:00",
         "2010-03-03 00:00",
         "2007-04-02 00:00",
         "2007-02-03 00:00",
         "2006-03-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWlanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWlanMIBNotifs = _CiscoLwappWlanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 0)
)
_CiscoLwappWlanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWlanMIBObjects = _CiscoLwappWlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1)
)
_CiscoLwappWlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWlanConfig = _CiscoLwappWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1)
)
_CLWlanConfigTable_Object = MibTable
cLWlanConfigTable = _CLWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLWlanConfigTable.setStatus("current")
_CLWlanConfigEntry_Object = MibTableRow
cLWlanConfigEntry = _CLWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1)
)
cLWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanConfigEntry.setStatus("current")


class _CLWlanIndex_Type(Unsigned32):
    """Custom type cLWlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 517),
    )


_CLWlanIndex_Type.__name__ = "Unsigned32"
_CLWlanIndex_Object = MibTableColumn
cLWlanIndex = _CLWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 1),
    _CLWlanIndex_Type()
)
cLWlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanIndex.setStatus("current")
_CLWlanRowStatus_Type = RowStatus
_CLWlanRowStatus_Object = MibTableColumn
cLWlanRowStatus = _CLWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 2),
    _CLWlanRowStatus_Type()
)
cLWlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRowStatus.setStatus("current")


class _CLWlanProfileName_Type(SnmpAdminString):
    """Custom type cLWlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLWlanProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanProfileName_Object = MibTableColumn
cLWlanProfileName = _CLWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 3),
    _CLWlanProfileName_Type()
)
cLWlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanProfileName.setStatus("current")


class _CLWlanSsid_Type(OctetString):
    """Custom type cLWlanSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLWlanSsid_Type.__name__ = "OctetString"
_CLWlanSsid_Object = MibTableColumn
cLWlanSsid = _CLWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 4),
    _CLWlanSsid_Type()
)
cLWlanSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanSsid.setStatus("current")


class _CLWlanDiagChan_Type(TruthValue):
    """Custom type cLWlanDiagChan based on TruthValue"""
    defaultValue = 2


_CLWlanDiagChan_Type.__name__ = "TruthValue"
_CLWlanDiagChan_Object = MibTableColumn
cLWlanDiagChan = _CLWlanDiagChan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 5),
    _CLWlanDiagChan_Type()
)
cLWlanDiagChan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanDiagChan.setStatus("current")


class _CLWlanStorageType_Type(StorageType):
    """Custom type cLWlanStorageType based on StorageType"""
    defaultValue = 3


_CLWlanStorageType_Type.__name__ = "StorageType"
_CLWlanStorageType_Object = MibTableColumn
cLWlanStorageType = _CLWlanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 6),
    _CLWlanStorageType_Type()
)
cLWlanStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanStorageType.setStatus("current")
_CLWlanIsWired_Type = TruthValue
_CLWlanIsWired_Object = MibTableColumn
cLWlanIsWired = _CLWlanIsWired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 7),
    _CLWlanIsWired_Type()
)
cLWlanIsWired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanIsWired.setStatus("current")


class _CLWlanIngressInterface_Type(OctetString):
    """Custom type cLWlanIngressInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLWlanIngressInterface_Type.__name__ = "OctetString"
_CLWlanIngressInterface_Object = MibTableColumn
cLWlanIngressInterface = _CLWlanIngressInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 8),
    _CLWlanIngressInterface_Type()
)
cLWlanIngressInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanIngressInterface.setStatus("current")


class _CLWlanNACSupport_Type(TruthValue):
    """Custom type cLWlanNACSupport based on TruthValue"""
    defaultValue = 2


_CLWlanNACSupport_Type.__name__ = "TruthValue"
_CLWlanNACSupport_Object = MibTableColumn
cLWlanNACSupport = _CLWlanNACSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 9),
    _CLWlanNACSupport_Type()
)
cLWlanNACSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanNACSupport.setStatus("current")
_CLWlanWepKeyChange_Type = TimeStamp
_CLWlanWepKeyChange_Object = MibTableColumn
cLWlanWepKeyChange = _CLWlanWepKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 10),
    _CLWlanWepKeyChange_Type()
)
cLWlanWepKeyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWlanWepKeyChange.setStatus("current")


class _CLWlanChdEnable_Type(TruthValue):
    """Custom type cLWlanChdEnable based on TruthValue"""
    defaultValue = 1


_CLWlanChdEnable_Type.__name__ = "TruthValue"
_CLWlanChdEnable_Object = MibTableColumn
cLWlanChdEnable = _CLWlanChdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 11),
    _CLWlanChdEnable_Type()
)
cLWlanChdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanChdEnable.setStatus("current")


class _CLWlan802dot11anDTIM_Type(Unsigned32):
    """Custom type cLWlan802dot11anDTIM based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CLWlan802dot11anDTIM_Type.__name__ = "Unsigned32"
_CLWlan802dot11anDTIM_Object = MibTableColumn
cLWlan802dot11anDTIM = _CLWlan802dot11anDTIM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 12),
    _CLWlan802dot11anDTIM_Type()
)
cLWlan802dot11anDTIM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan802dot11anDTIM.setStatus("current")
if mibBuilder.loadTexts:
    cLWlan802dot11anDTIM.setUnits("Beacon Intervals")


class _CLWlan802dot11bgnDTIM_Type(Unsigned32):
    """Custom type cLWlan802dot11bgnDTIM based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CLWlan802dot11bgnDTIM_Type.__name__ = "Unsigned32"
_CLWlan802dot11bgnDTIM_Object = MibTableColumn
cLWlan802dot11bgnDTIM = _CLWlan802dot11bgnDTIM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 13),
    _CLWlan802dot11bgnDTIM_Type()
)
cLWlan802dot11bgnDTIM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan802dot11bgnDTIM.setStatus("current")
if mibBuilder.loadTexts:
    cLWlan802dot11bgnDTIM.setUnits("Beacon Intervals")


class _CLWlanLoadBalancingEnable_Type(TruthValue):
    """Custom type cLWlanLoadBalancingEnable based on TruthValue"""
    defaultValue = 1


_CLWlanLoadBalancingEnable_Type.__name__ = "TruthValue"
_CLWlanLoadBalancingEnable_Object = MibTableColumn
cLWlanLoadBalancingEnable = _CLWlanLoadBalancingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 14),
    _CLWlanLoadBalancingEnable_Type()
)
cLWlanLoadBalancingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanLoadBalancingEnable.setStatus("current")


class _CLWlanBandSelectEnable_Type(TruthValue):
    """Custom type cLWlanBandSelectEnable based on TruthValue"""
    defaultValue = 1


_CLWlanBandSelectEnable_Type.__name__ = "TruthValue"
_CLWlanBandSelectEnable_Object = MibTableColumn
cLWlanBandSelectEnable = _CLWlanBandSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 15),
    _CLWlanBandSelectEnable_Type()
)
cLWlanBandSelectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanBandSelectEnable.setStatus("current")


class _CLWlanPassiveClientEnable_Type(TruthValue):
    """Custom type cLWlanPassiveClientEnable based on TruthValue"""
    defaultValue = 2


_CLWlanPassiveClientEnable_Type.__name__ = "TruthValue"
_CLWlanPassiveClientEnable_Object = MibTableColumn
cLWlanPassiveClientEnable = _CLWlanPassiveClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 16),
    _CLWlanPassiveClientEnable_Type()
)
cLWlanPassiveClientEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanPassiveClientEnable.setStatus("current")


class _CLWlanReAnchorRoamedVoiceClientsEnable_Type(TruthValue):
    """Custom type cLWlanReAnchorRoamedVoiceClientsEnable based on TruthValue"""
    defaultValue = 2


_CLWlanReAnchorRoamedVoiceClientsEnable_Type.__name__ = "TruthValue"
_CLWlanReAnchorRoamedVoiceClientsEnable_Object = MibTableColumn
cLWlanReAnchorRoamedVoiceClientsEnable = _CLWlanReAnchorRoamedVoiceClientsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 17),
    _CLWlanReAnchorRoamedVoiceClientsEnable_Type()
)
cLWlanReAnchorRoamedVoiceClientsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanReAnchorRoamedVoiceClientsEnable.setStatus("current")


class _CLWlanMulticastInterfaceEnable_Type(TruthValue):
    """Custom type cLWlanMulticastInterfaceEnable based on TruthValue"""
    defaultValue = 2


_CLWlanMulticastInterfaceEnable_Type.__name__ = "TruthValue"
_CLWlanMulticastInterfaceEnable_Object = MibTableColumn
cLWlanMulticastInterfaceEnable = _CLWlanMulticastInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 18),
    _CLWlanMulticastInterfaceEnable_Type()
)
cLWlanMulticastInterfaceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMulticastInterfaceEnable.setStatus("current")


class _CLWlanMulticastInterface_Type(SnmpAdminString):
    """Custom type cLWlanMulticastInterface based on SnmpAdminString"""
    defaultValue = OctetString("default")


_CLWlanMulticastInterface_Type.__name__ = "SnmpAdminString"
_CLWlanMulticastInterface_Object = MibTableColumn
cLWlanMulticastInterface = _CLWlanMulticastInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 19),
    _CLWlanMulticastInterface_Type()
)
cLWlanMulticastInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMulticastInterface.setStatus("current")


class _CLWlanMulticastDirectEnable_Type(TruthValue):
    """Custom type cLWlanMulticastDirectEnable based on TruthValue"""
    defaultValue = 2


_CLWlanMulticastDirectEnable_Type.__name__ = "TruthValue"
_CLWlanMulticastDirectEnable_Object = MibTableColumn
cLWlanMulticastDirectEnable = _CLWlanMulticastDirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 20),
    _CLWlanMulticastDirectEnable_Type()
)
cLWlanMulticastDirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMulticastDirectEnable.setStatus("current")


class _CLWlanNACPostureSupport_Type(TruthValue):
    """Custom type cLWlanNACPostureSupport based on TruthValue"""
    defaultValue = 2


_CLWlanNACPostureSupport_Type.__name__ = "TruthValue"
_CLWlanNACPostureSupport_Object = MibTableColumn
cLWlanNACPostureSupport = _CLWlanNACPostureSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 21),
    _CLWlanNACPostureSupport_Type()
)
cLWlanNACPostureSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanNACPostureSupport.setStatus("current")


class _CLWlanMaxClientsAccepted_Type(Unsigned32):
    """Custom type cLWlanMaxClientsAccepted based on Unsigned32"""
    defaultValue = 0


_CLWlanMaxClientsAccepted_Type.__name__ = "Unsigned32"
_CLWlanMaxClientsAccepted_Object = MibTableColumn
cLWlanMaxClientsAccepted = _CLWlanMaxClientsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 22),
    _CLWlanMaxClientsAccepted_Type()
)
cLWlanMaxClientsAccepted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMaxClientsAccepted.setStatus("current")


class _CLWlanScanDeferPriority_Type(Bits):
    """Custom type cLWlanScanDeferPriority based on Bits"""
    defaultBinValue = "0000011"

    namedValues = NamedValues(
        *(("bit0", 0),
          ("bit1", 1),
          ("bit2", 2),
          ("bit3", 3),
          ("bit4", 4),
          ("bit5", 5),
          ("bit6", 6),
          ("bit7", 7))
    )

_CLWlanScanDeferPriority_Type.__name__ = "Bits"
_CLWlanScanDeferPriority_Object = MibTableColumn
cLWlanScanDeferPriority = _CLWlanScanDeferPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 23),
    _CLWlanScanDeferPriority_Type()
)
cLWlanScanDeferPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanScanDeferPriority.setStatus("current")


class _CLWlanScanDeferTime_Type(Unsigned32):
    """Custom type cLWlanScanDeferTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CLWlanScanDeferTime_Type.__name__ = "Unsigned32"
_CLWlanScanDeferTime_Object = MibTableColumn
cLWlanScanDeferTime = _CLWlanScanDeferTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 24),
    _CLWlanScanDeferTime_Type()
)
cLWlanScanDeferTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanScanDeferTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanScanDeferTime.setUnits("milliseconds")


class _CLWlanLanSubType_Type(Integer32):
    """Custom type cLWlanLanSubType based on Integer32"""
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
        *(("wirelessLan", 1),
          ("guestLan", 2),
          ("remoteLan", 3),
          ("other", 4))
    )


_CLWlanLanSubType_Type.__name__ = "Integer32"
_CLWlanLanSubType_Object = MibTableColumn
cLWlanLanSubType = _CLWlanLanSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 25),
    _CLWlanLanSubType_Type()
)
cLWlanLanSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanLanSubType.setStatus("current")


class _CLWlanWebAuthOnMacFilterFailureEnabled_Type(TruthValue):
    """Custom type cLWlanWebAuthOnMacFilterFailureEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanWebAuthOnMacFilterFailureEnabled_Type.__name__ = "TruthValue"
_CLWlanWebAuthOnMacFilterFailureEnabled_Object = MibTableColumn
cLWlanWebAuthOnMacFilterFailureEnabled = _CLWlanWebAuthOnMacFilterFailureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 26),
    _CLWlanWebAuthOnMacFilterFailureEnabled_Type()
)
cLWlanWebAuthOnMacFilterFailureEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanWebAuthOnMacFilterFailureEnabled.setStatus("current")


class _CLWlanStaticIpTunnelingEnabled_Type(TruthValue):
    """Custom type cLWlanStaticIpTunnelingEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanStaticIpTunnelingEnabled_Type.__name__ = "TruthValue"
_CLWlanStaticIpTunnelingEnabled_Object = MibTableColumn
cLWlanStaticIpTunnelingEnabled = _CLWlanStaticIpTunnelingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 27),
    _CLWlanStaticIpTunnelingEnabled_Type()
)
cLWlanStaticIpTunnelingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanStaticIpTunnelingEnabled.setStatus("current")


class _CLWlanKtsCacSupportEnabled_Type(TruthValue):
    """Custom type cLWlanKtsCacSupportEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanKtsCacSupportEnabled_Type.__name__ = "TruthValue"
_CLWlanKtsCacSupportEnabled_Object = MibTableColumn
cLWlanKtsCacSupportEnabled = _CLWlanKtsCacSupportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 28),
    _CLWlanKtsCacSupportEnabled_Type()
)
cLWlanKtsCacSupportEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanKtsCacSupportEnabled.setStatus("current")


class _CLWlanWifiDirectPolicyStatus_Type(Integer32):
    """Custom type cLWlanWifiDirectPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("allow", 2),
          ("notAllow", 3))
    )


_CLWlanWifiDirectPolicyStatus_Type.__name__ = "Integer32"
_CLWlanWifiDirectPolicyStatus_Object = MibTableColumn
cLWlanWifiDirectPolicyStatus = _CLWlanWifiDirectPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 29),
    _CLWlanWifiDirectPolicyStatus_Type()
)
cLWlanWifiDirectPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanWifiDirectPolicyStatus.setStatus("current")


class _CLWlanWebAuthIPv6AclName_Type(SnmpAdminString):
    """Custom type cLWlanWebAuthIPv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanWebAuthIPv6AclName_Type.__name__ = "SnmpAdminString"
_CLWlanWebAuthIPv6AclName_Object = MibTableColumn
cLWlanWebAuthIPv6AclName = _CLWlanWebAuthIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 30),
    _CLWlanWebAuthIPv6AclName_Type()
)
cLWlanWebAuthIPv6AclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanWebAuthIPv6AclName.setStatus("current")


class _CLWlanHotSpot2Enabled_Type(TruthValue):
    """Custom type cLWlanHotSpot2Enabled based on TruthValue"""
    defaultValue = 2


_CLWlanHotSpot2Enabled_Type.__name__ = "TruthValue"
_CLWlanHotSpot2Enabled_Object = MibTableColumn
cLWlanHotSpot2Enabled = _CLWlanHotSpot2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 31),
    _CLWlanHotSpot2Enabled_Type()
)
cLWlanHotSpot2Enabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2Enabled.setStatus("current")


class _CLWlanMaxClientsAllowedPerRadio_Type(Unsigned32):
    """Custom type cLWlanMaxClientsAllowedPerRadio based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CLWlanMaxClientsAllowedPerRadio_Type.__name__ = "Unsigned32"
_CLWlanMaxClientsAllowedPerRadio_Object = MibTableColumn
cLWlanMaxClientsAllowedPerRadio = _CLWlanMaxClientsAllowedPerRadio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 32),
    _CLWlanMaxClientsAllowedPerRadio_Type()
)
cLWlanMaxClientsAllowedPerRadio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMaxClientsAllowedPerRadio.setStatus("current")


class _CLWlanDhcpDeviceProfiling_Type(TruthValue):
    """Custom type cLWlanDhcpDeviceProfiling based on TruthValue"""
    defaultValue = 2


_CLWlanDhcpDeviceProfiling_Type.__name__ = "TruthValue"
_CLWlanDhcpDeviceProfiling_Object = MibTableColumn
cLWlanDhcpDeviceProfiling = _CLWlanDhcpDeviceProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 33),
    _CLWlanDhcpDeviceProfiling_Type()
)
cLWlanDhcpDeviceProfiling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanDhcpDeviceProfiling.setStatus("current")


class _CLWlanMacAuthOverDot1xEnabled_Type(TruthValue):
    """Custom type cLWlanMacAuthOverDot1xEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanMacAuthOverDot1xEnabled_Type.__name__ = "TruthValue"
_CLWlanMacAuthOverDot1xEnabled_Object = MibTableColumn
cLWlanMacAuthOverDot1xEnabled = _CLWlanMacAuthOverDot1xEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 34),
    _CLWlanMacAuthOverDot1xEnabled_Type()
)
cLWlanMacAuthOverDot1xEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanMacAuthOverDot1xEnabled.setStatus("current")


class _CLWlanUserTimeout_Type(Unsigned32):
    """Custom type cLWlanUserTimeout based on Unsigned32"""
    defaultValue = 300


_CLWlanUserTimeout_Type.__name__ = "Unsigned32"
_CLWlanUserTimeout_Object = MibTableColumn
cLWlanUserTimeout = _CLWlanUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 35),
    _CLWlanUserTimeout_Type()
)
cLWlanUserTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanUserTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanUserTimeout.setUnits("seconds")


class _CLWlanUserIdleThreshold_Type(Unsigned32):
    """Custom type cLWlanUserIdleThreshold based on Unsigned32"""
    defaultValue = 0


_CLWlanUserIdleThreshold_Type.__name__ = "Unsigned32"
_CLWlanUserIdleThreshold_Object = MibTableColumn
cLWlanUserIdleThreshold = _CLWlanUserIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 36),
    _CLWlanUserIdleThreshold_Type()
)
cLWlanUserIdleThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanUserIdleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanUserIdleThreshold.setUnits("bytes")


class _CLWlanHttpDeviceProfiling_Type(TruthValue):
    """Custom type cLWlanHttpDeviceProfiling based on TruthValue"""
    defaultValue = 2


_CLWlanHttpDeviceProfiling_Type.__name__ = "TruthValue"
_CLWlanHttpDeviceProfiling_Object = MibTableColumn
cLWlanHttpDeviceProfiling = _CLWlanHttpDeviceProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 37),
    _CLWlanHttpDeviceProfiling_Type()
)
cLWlanHttpDeviceProfiling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHttpDeviceProfiling.setStatus("current")


class _CLWlanHotSpotClearConfig_Type(Integer32):
    """Custom type cLWlanHotSpotClearConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CLWlanHotSpotClearConfig_Type.__name__ = "Integer32"
_CLWlanHotSpotClearConfig_Object = MibTableColumn
cLWlanHotSpotClearConfig = _CLWlanHotSpotClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 38),
    _CLWlanHotSpotClearConfig_Type()
)
cLWlanHotSpotClearConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpotClearConfig.setStatus("current")


class _CLWlanRadiusAuthFourthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAuthFourthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAuthFourthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAuthFourthServer_Object = MibTableColumn
cLWlanRadiusAuthFourthServer = _CLWlanRadiusAuthFourthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 39),
    _CLWlanRadiusAuthFourthServer_Type()
)
cLWlanRadiusAuthFourthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAuthFourthServer.setStatus("current")


class _CLWlanRadiusAuthFifthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAuthFifthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAuthFifthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAuthFifthServer_Object = MibTableColumn
cLWlanRadiusAuthFifthServer = _CLWlanRadiusAuthFifthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 40),
    _CLWlanRadiusAuthFifthServer_Type()
)
cLWlanRadiusAuthFifthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAuthFifthServer.setStatus("current")


class _CLWlanRadiusAuthSixthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAuthSixthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAuthSixthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAuthSixthServer_Object = MibTableColumn
cLWlanRadiusAuthSixthServer = _CLWlanRadiusAuthSixthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 41),
    _CLWlanRadiusAuthSixthServer_Type()
)
cLWlanRadiusAuthSixthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAuthSixthServer.setStatus("current")


class _CLWlanRadiusAcctFourthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAcctFourthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAcctFourthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAcctFourthServer_Object = MibTableColumn
cLWlanRadiusAcctFourthServer = _CLWlanRadiusAcctFourthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 42),
    _CLWlanRadiusAcctFourthServer_Type()
)
cLWlanRadiusAcctFourthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAcctFourthServer.setStatus("current")


class _CLWlanRadiusAcctFifthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAcctFifthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAcctFifthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAcctFifthServer_Object = MibTableColumn
cLWlanRadiusAcctFifthServer = _CLWlanRadiusAcctFifthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 43),
    _CLWlanRadiusAcctFifthServer_Type()
)
cLWlanRadiusAcctFifthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAcctFifthServer.setStatus("current")


class _CLWlanRadiusAcctSixthServer_Type(DisplayString):
    """Custom type cLWlanRadiusAcctSixthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CLWlanRadiusAcctSixthServer_Type.__name__ = "DisplayString"
_CLWlanRadiusAcctSixthServer_Object = MibTableColumn
cLWlanRadiusAcctSixthServer = _CLWlanRadiusAcctSixthServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 44),
    _CLWlanRadiusAcctSixthServer_Type()
)
cLWlanRadiusAcctSixthServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanRadiusAcctSixthServer.setStatus("current")


class _CLWlanSelfAnchorEnabled_Type(TruthValue):
    """Custom type cLWlanSelfAnchorEnabled based on TruthValue"""
    defaultValue = 2


_CLWlanSelfAnchorEnabled_Type.__name__ = "TruthValue"
_CLWlanSelfAnchorEnabled_Object = MibTableColumn
cLWlanSelfAnchorEnabled = _CLWlanSelfAnchorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 64),
    _CLWlanSelfAnchorEnabled_Type()
)
cLWlanSelfAnchorEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanSelfAnchorEnabled.setStatus("current")


class _CLWlanUniversalAdmin_Type(TruthValue):
    """Custom type cLWlanUniversalAdmin based on TruthValue"""
    defaultValue = 2


_CLWlanUniversalAdmin_Type.__name__ = "TruthValue"
_CLWlanUniversalAdmin_Object = MibTableColumn
cLWlanUniversalAdmin = _CLWlanUniversalAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 65),
    _CLWlanUniversalAdmin_Type()
)
cLWlanUniversalAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanUniversalAdmin.setStatus("current")


class _CLWlan11acMuMimoEnabled_Type(TruthValue):
    """Custom type cLWlan11acMuMimoEnabled based on TruthValue"""
    defaultValue = 2


_CLWlan11acMuMimoEnabled_Type.__name__ = "TruthValue"
_CLWlan11acMuMimoEnabled_Object = MibTableColumn
cLWlan11acMuMimoEnabled = _CLWlan11acMuMimoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 66),
    _CLWlan11acMuMimoEnabled_Type()
)
cLWlan11acMuMimoEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11acMuMimoEnabled.setStatus("current")


class _CLWlan11vDisassocImmiEnable_Type(TruthValue):
    """Custom type cLWlan11vDisassocImmiEnable based on TruthValue"""
    defaultValue = 2


_CLWlan11vDisassocImmiEnable_Type.__name__ = "TruthValue"
_CLWlan11vDisassocImmiEnable_Object = MibTableColumn
cLWlan11vDisassocImmiEnable = _CLWlan11vDisassocImmiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 67),
    _CLWlan11vDisassocImmiEnable_Type()
)
cLWlan11vDisassocImmiEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11vDisassocImmiEnable.setStatus("current")


class _CLWlan11vDisassocTimer_Type(Unsigned32):
    """Custom type cLWlan11vDisassocTimer based on Unsigned32"""
    defaultValue = 200


_CLWlan11vDisassocTimer_Type.__name__ = "Unsigned32"
_CLWlan11vDisassocTimer_Object = MibTableColumn
cLWlan11vDisassocTimer = _CLWlan11vDisassocTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 73),
    _CLWlan11vDisassocTimer_Type()
)
cLWlan11vDisassocTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWlan11vDisassocTimer.setStatus("current")
if mibBuilder.loadTexts:
    cLWlan11vDisassocTimer.setUnits("Target Beacons Transmission Times")


class _CLWlan11vOpRoamDisassocTimer_Type(Unsigned32):
    """Custom type cLWlan11vOpRoamDisassocTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_CLWlan11vOpRoamDisassocTimer_Type.__name__ = "Unsigned32"
_CLWlan11vOpRoamDisassocTimer_Object = MibTableColumn
cLWlan11vOpRoamDisassocTimer = _CLWlan11vOpRoamDisassocTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 74),
    _CLWlan11vOpRoamDisassocTimer_Type()
)
cLWlan11vOpRoamDisassocTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWlan11vOpRoamDisassocTimer.setStatus("current")
if mibBuilder.loadTexts:
    cLWlan11vOpRoamDisassocTimer.setUnits("Target Beacon Transmission Times")


class _CLWlan11vBssTransEnable_Type(TruthValue):
    """Custom type cLWlan11vBssTransEnable based on TruthValue"""
    defaultValue = 2


_CLWlan11vBssTransEnable_Type.__name__ = "TruthValue"
_CLWlan11vBssTransEnable_Object = MibTableColumn
cLWlan11vBssTransEnable = _CLWlan11vBssTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 1, 1, 93),
    _CLWlan11vBssTransEnable_Type()
)
cLWlan11vBssTransEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11vBssTransEnable.setStatus("current")
_CLWlanConfigClientTable_Object = MibTable
cLWlanConfigClientTable = _CLWlanConfigClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLWlanConfigClientTable.setStatus("current")
_CLWlanConfigClientEntry_Object = MibTableRow
cLWlanConfigClientEntry = _CLWlanConfigClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 2, 1)
)
cLWlanConfigClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanConfigClientEntry.setStatus("current")


class _CLWlanClientAclName_Type(DisplayString):
    """Custom type cLWlanClientAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanClientAclName_Type.__name__ = "DisplayString"
_CLWlanClientAclName_Object = MibTableColumn
cLWlanClientAclName = _CLWlanClientAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 2, 1, 1),
    _CLWlanClientAclName_Type()
)
cLWlanClientAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientAclName.setStatus("current")


class _CLWlanP2PBlocking_Type(Integer32):
    """Custom type cLWlanP2PBlocking based on Integer32"""
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
        *(("disable", 1),
          ("drop", 2),
          ("forwardUp", 3),
          ("allowPvtGrp", 4))
    )


_CLWlanP2PBlocking_Type.__name__ = "Integer32"
_CLWlanP2PBlocking_Object = MibTableColumn
cLWlanP2PBlocking = _CLWlanP2PBlocking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 2, 1, 2),
    _CLWlanP2PBlocking_Type()
)
cLWlanP2PBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanP2PBlocking.setStatus("current")


class _CLWlanClientIPv6AclName_Type(DisplayString):
    """Custom type cLWlanClientIPv6AclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanClientIPv6AclName_Type.__name__ = "DisplayString"
_CLWlanClientIPv6AclName_Object = MibTableColumn
cLWlanClientIPv6AclName = _CLWlanClientIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 2, 1, 3),
    _CLWlanClientIPv6AclName_Type()
)
cLWlanClientIPv6AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientIPv6AclName.setStatus("current")
_CLWlanConfigQosTable_Object = MibTable
cLWlanConfigQosTable = _CLWlanConfigQosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLWlanConfigQosTable.setStatus("current")
_CLWlanConfigQosEntry_Object = MibTableRow
cLWlanConfigQosEntry = _CLWlanConfigQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1)
)
cLWlanConfigQosEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanConfigQosEntry.setStatus("current")
_CLWlanClientDSAverageDataRate_Type = Unsigned32
_CLWlanClientDSAverageDataRate_Object = MibTableColumn
cLWlanClientDSAverageDataRate = _CLWlanClientDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 1),
    _CLWlanClientDSAverageDataRate_Type()
)
cLWlanClientDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientDSAverageDataRate.setStatus("current")
_CLWlanClientUSAverageDataRate_Type = Unsigned32
_CLWlanClientUSAverageDataRate_Object = MibTableColumn
cLWlanClientUSAverageDataRate = _CLWlanClientUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 2),
    _CLWlanClientUSAverageDataRate_Type()
)
cLWlanClientUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientUSAverageDataRate.setStatus("current")
_CLWlanClientDSBurstDataRate_Type = Unsigned32
_CLWlanClientDSBurstDataRate_Object = MibTableColumn
cLWlanClientDSBurstDataRate = _CLWlanClientDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 3),
    _CLWlanClientDSBurstDataRate_Type()
)
cLWlanClientDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientDSBurstDataRate.setStatus("current")
_CLWlanClientUSBurstDataRate_Type = Unsigned32
_CLWlanClientUSBurstDataRate_Object = MibTableColumn
cLWlanClientUSBurstDataRate = _CLWlanClientUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 4),
    _CLWlanClientUSBurstDataRate_Type()
)
cLWlanClientUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientUSBurstDataRate.setStatus("current")
_CLWlanClientDSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanClientDSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanClientDSAvgRealTimeDataRate = _CLWlanClientDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 5),
    _CLWlanClientDSAvgRealTimeDataRate_Type()
)
cLWlanClientDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientDSAvgRealTimeDataRate.setStatus("current")
_CLWlanClientUSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanClientUSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanClientUSAvgRealTimeDataRate = _CLWlanClientUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 6),
    _CLWlanClientUSAvgRealTimeDataRate_Type()
)
cLWlanClientUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientUSAvgRealTimeDataRate.setStatus("current")
_CLWlanClientDSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanClientDSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanClientDSBurstRealTimeDataRate = _CLWlanClientDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 7),
    _CLWlanClientDSBurstRealTimeDataRate_Type()
)
cLWlanClientDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientDSBurstRealTimeDataRate.setStatus("current")
_CLWlanClientUSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanClientUSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanClientUSBurstRealTimeDataRate = _CLWlanClientUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 8),
    _CLWlanClientUSBurstRealTimeDataRate_Type()
)
cLWlanClientUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanClientUSBurstRealTimeDataRate.setStatus("current")
_CLWlanSsidDSAverageDataRate_Type = Unsigned32
_CLWlanSsidDSAverageDataRate_Object = MibTableColumn
cLWlanSsidDSAverageDataRate = _CLWlanSsidDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 9),
    _CLWlanSsidDSAverageDataRate_Type()
)
cLWlanSsidDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidDSAverageDataRate.setStatus("current")
_CLWlanSsidUSAverageDataRate_Type = Unsigned32
_CLWlanSsidUSAverageDataRate_Object = MibTableColumn
cLWlanSsidUSAverageDataRate = _CLWlanSsidUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 10),
    _CLWlanSsidUSAverageDataRate_Type()
)
cLWlanSsidUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidUSAverageDataRate.setStatus("current")
_CLWlanSsidDSBurstDataRate_Type = Unsigned32
_CLWlanSsidDSBurstDataRate_Object = MibTableColumn
cLWlanSsidDSBurstDataRate = _CLWlanSsidDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 11),
    _CLWlanSsidDSBurstDataRate_Type()
)
cLWlanSsidDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidDSBurstDataRate.setStatus("current")
_CLWlanSsidUSBurstDataRate_Type = Unsigned32
_CLWlanSsidUSBurstDataRate_Object = MibTableColumn
cLWlanSsidUSBurstDataRate = _CLWlanSsidUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 12),
    _CLWlanSsidUSBurstDataRate_Type()
)
cLWlanSsidUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidUSBurstDataRate.setStatus("current")
_CLWlanSsidDSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanSsidDSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanSsidDSAvgRealTimeDataRate = _CLWlanSsidDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 13),
    _CLWlanSsidDSAvgRealTimeDataRate_Type()
)
cLWlanSsidDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidDSAvgRealTimeDataRate.setStatus("current")
_CLWlanSsidUSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanSsidUSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanSsidUSAvgRealTimeDataRate = _CLWlanSsidUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 14),
    _CLWlanSsidUSAvgRealTimeDataRate_Type()
)
cLWlanSsidUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidUSAvgRealTimeDataRate.setStatus("current")
_CLWlanSsidDSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanSsidDSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanSsidDSBurstRealTimeDataRate = _CLWlanSsidDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 15),
    _CLWlanSsidDSBurstRealTimeDataRate_Type()
)
cLWlanSsidDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidDSBurstRealTimeDataRate.setStatus("current")
_CLWlanSsidUSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanSsidUSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanSsidUSBurstRealTimeDataRate = _CLWlanSsidUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 16),
    _CLWlanSsidUSBurstRealTimeDataRate_Type()
)
cLWlanSsidUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanSsidUSBurstRealTimeDataRate.setStatus("current")
_CLWlanWlanDSAverageDataRate_Type = Unsigned32
_CLWlanWlanDSAverageDataRate_Object = MibTableColumn
cLWlanWlanDSAverageDataRate = _CLWlanWlanDSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 17),
    _CLWlanWlanDSAverageDataRate_Type()
)
cLWlanWlanDSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanDSAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanDSAverageDataRate.setUnits("kbytes")
_CLWlanWlanUSAverageDataRate_Type = Unsigned32
_CLWlanWlanUSAverageDataRate_Object = MibTableColumn
cLWlanWlanUSAverageDataRate = _CLWlanWlanUSAverageDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 18),
    _CLWlanWlanUSAverageDataRate_Type()
)
cLWlanWlanUSAverageDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanUSAverageDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanUSAverageDataRate.setUnits("kbytes")
_CLWlanWlanDSBurstDataRate_Type = Unsigned32
_CLWlanWlanDSBurstDataRate_Object = MibTableColumn
cLWlanWlanDSBurstDataRate = _CLWlanWlanDSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 19),
    _CLWlanWlanDSBurstDataRate_Type()
)
cLWlanWlanDSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanDSBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanDSBurstDataRate.setUnits("kbytes")
_CLWlanWlanUSBurstDataRate_Type = Unsigned32
_CLWlanWlanUSBurstDataRate_Object = MibTableColumn
cLWlanWlanUSBurstDataRate = _CLWlanWlanUSBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 20),
    _CLWlanWlanUSBurstDataRate_Type()
)
cLWlanWlanUSBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanUSBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanUSBurstDataRate.setUnits("kbytes")
_CLWlanWlanDSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanWlanDSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanWlanDSAvgRealTimeDataRate = _CLWlanWlanDSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 21),
    _CLWlanWlanDSAvgRealTimeDataRate_Type()
)
cLWlanWlanDSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanDSAvgRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanDSAvgRealTimeDataRate.setUnits("kbytes")
_CLWlanWlanUSAvgRealTimeDataRate_Type = Unsigned32
_CLWlanWlanUSAvgRealTimeDataRate_Object = MibTableColumn
cLWlanWlanUSAvgRealTimeDataRate = _CLWlanWlanUSAvgRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 22),
    _CLWlanWlanUSAvgRealTimeDataRate_Type()
)
cLWlanWlanUSAvgRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanUSAvgRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanUSAvgRealTimeDataRate.setUnits("kbytes")
_CLWlanWlanDSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanWlanDSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanWlanDSBurstRealTimeDataRate = _CLWlanWlanDSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 23),
    _CLWlanWlanDSBurstRealTimeDataRate_Type()
)
cLWlanWlanDSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanDSBurstRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanDSBurstRealTimeDataRate.setUnits("kbytes")
_CLWlanWlanUSBurstRealTimeDataRate_Type = Unsigned32
_CLWlanWlanUSBurstRealTimeDataRate_Object = MibTableColumn
cLWlanWlanUSBurstRealTimeDataRate = _CLWlanWlanUSBurstRealTimeDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 3, 1, 24),
    _CLWlanWlanUSBurstRealTimeDataRate_Type()
)
cLWlanWlanUSBurstRealTimeDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanWlanUSBurstRealTimeDataRate.setStatus("current")
if mibBuilder.loadTexts:
    cLWlanWlanUSBurstRealTimeDataRate.setUnits("kbytes")
_CLWlanConfigIosTable_Object = MibTable
cLWlanConfigIosTable = _CLWlanConfigIosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cLWlanConfigIosTable.setStatus("current")
_CLWlanConfigIosEntry_Object = MibTableRow
cLWlanConfigIosEntry = _CLWlanConfigIosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1)
)
cLWlanConfigIosEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanConfigIosEntry.setStatus("current")


class _CLWlanIosAccountingMethodListName_Type(SnmpAdminString):
    """Custom type cLWlanIosAccountingMethodListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosAccountingMethodListName_Type.__name__ = "SnmpAdminString"
_CLWlanIosAccountingMethodListName_Object = MibTableColumn
cLWlanIosAccountingMethodListName = _CLWlanIosAccountingMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 1),
    _CLWlanIosAccountingMethodListName_Type()
)
cLWlanIosAccountingMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosAccountingMethodListName.setStatus("current")


class _CLWlanIosAuthenticationMethodListName_Type(SnmpAdminString):
    """Custom type cLWlanIosAuthenticationMethodListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosAuthenticationMethodListName_Type.__name__ = "SnmpAdminString"
_CLWlanIosAuthenticationMethodListName_Object = MibTableColumn
cLWlanIosAuthenticationMethodListName = _CLWlanIosAuthenticationMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 2),
    _CLWlanIosAuthenticationMethodListName_Type()
)
cLWlanIosAuthenticationMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosAuthenticationMethodListName.setStatus("current")


class _CLWlanIosMacFilteringMethodListName_Type(SnmpAdminString):
    """Custom type cLWlanIosMacFilteringMethodListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosMacFilteringMethodListName_Type.__name__ = "SnmpAdminString"
_CLWlanIosMacFilteringMethodListName_Object = MibTableColumn
cLWlanIosMacFilteringMethodListName = _CLWlanIosMacFilteringMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 3),
    _CLWlanIosMacFilteringMethodListName_Type()
)
cLWlanIosMacFilteringMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosMacFilteringMethodListName.setStatus("current")


class _CLWlanIosWebAuthMethodListName_Type(SnmpAdminString):
    """Custom type cLWlanIosWebAuthMethodListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosWebAuthMethodListName_Type.__name__ = "SnmpAdminString"
_CLWlanIosWebAuthMethodListName_Object = MibTableColumn
cLWlanIosWebAuthMethodListName = _CLWlanIosWebAuthMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 4),
    _CLWlanIosWebAuthMethodListName_Type()
)
cLWlanIosWebAuthMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosWebAuthMethodListName.setStatus("current")


class _CLWlanIosQosUpStreamProfileName_Type(SnmpAdminString):
    """Custom type cLWlanIosQosUpStreamProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosQosUpStreamProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanIosQosUpStreamProfileName_Object = MibTableColumn
cLWlanIosQosUpStreamProfileName = _CLWlanIosQosUpStreamProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 5),
    _CLWlanIosQosUpStreamProfileName_Type()
)
cLWlanIosQosUpStreamProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosQosUpStreamProfileName.setStatus("current")


class _CLWlanIosQosDownStreamProfileName_Type(SnmpAdminString):
    """Custom type cLWlanIosQosDownStreamProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosQosDownStreamProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanIosQosDownStreamProfileName_Object = MibTableColumn
cLWlanIosQosDownStreamProfileName = _CLWlanIosQosDownStreamProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 6),
    _CLWlanIosQosDownStreamProfileName_Type()
)
cLWlanIosQosDownStreamProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosQosDownStreamProfileName.setStatus("current")
_CLWlanIngressDHCPOption82Format_Type = Unsigned32
_CLWlanIngressDHCPOption82Format_Object = MibTableColumn
cLWlanIngressDHCPOption82Format = _CLWlanIngressDHCPOption82Format_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 7),
    _CLWlanIngressDHCPOption82Format_Type()
)
cLWlanIngressDHCPOption82Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIngressDHCPOption82Format.setStatus("current")
_CLWlanIngressDHCPOption82Ascii_Type = TruthValue
_CLWlanIngressDHCPOption82Ascii_Object = MibTableColumn
cLWlanIngressDHCPOption82Ascii = _CLWlanIngressDHCPOption82Ascii_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 8),
    _CLWlanIngressDHCPOption82Ascii_Type()
)
cLWlanIngressDHCPOption82Ascii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIngressDHCPOption82Ascii.setStatus("current")
_CLWlanIngressDHCPOption82Rid_Type = TruthValue
_CLWlanIngressDHCPOption82Rid_Object = MibTableColumn
cLWlanIngressDHCPOption82Rid = _CLWlanIngressDHCPOption82Rid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 9),
    _CLWlanIngressDHCPOption82Rid_Type()
)
cLWlanIngressDHCPOption82Rid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIngressDHCPOption82Rid.setStatus("current")
_CLWlanIngressDHCPOption82Enable_Type = TruthValue
_CLWlanIngressDHCPOption82Enable_Object = MibTableColumn
cLWlanIngressDHCPOption82Enable = _CLWlanIngressDHCPOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 10),
    _CLWlanIngressDHCPOption82Enable_Type()
)
cLWlanIngressDHCPOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIngressDHCPOption82Enable.setStatus("current")
_CLWlanIosScanDeferPriority_Type = Unsigned32
_CLWlanIosScanDeferPriority_Object = MibTableColumn
cLWlanIosScanDeferPriority = _CLWlanIosScanDeferPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 11),
    _CLWlanIosScanDeferPriority_Type()
)
cLWlanIosScanDeferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosScanDeferPriority.setStatus("current")
_CLWlanIosWebAuthParameterMapName_Type = SnmpAdminString
_CLWlanIosWebAuthParameterMapName_Object = MibTableColumn
cLWlanIosWebAuthParameterMapName = _CLWlanIosWebAuthParameterMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 12),
    _CLWlanIosWebAuthParameterMapName_Type()
)
cLWlanIosWebAuthParameterMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosWebAuthParameterMapName.setStatus("current")


class _CLWlanIosQosClientUpStreamProfileName_Type(SnmpAdminString):
    """Custom type cLWlanIosQosClientUpStreamProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosQosClientUpStreamProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanIosQosClientUpStreamProfileName_Object = MibTableColumn
cLWlanIosQosClientUpStreamProfileName = _CLWlanIosQosClientUpStreamProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 13),
    _CLWlanIosQosClientUpStreamProfileName_Type()
)
cLWlanIosQosClientUpStreamProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosQosClientUpStreamProfileName.setStatus("current")


class _CLWlanIosQosClientDownStreamProfileName_Type(SnmpAdminString):
    """Custom type cLWlanIosQosClientDownStreamProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLWlanIosQosClientDownStreamProfileName_Type.__name__ = "SnmpAdminString"
_CLWlanIosQosClientDownStreamProfileName_Object = MibTableColumn
cLWlanIosQosClientDownStreamProfileName = _CLWlanIosQosClientDownStreamProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 4, 1, 14),
    _CLWlanIosQosClientDownStreamProfileName_Type()
)
cLWlanIosQosClientDownStreamProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanIosQosClientDownStreamProfileName.setStatus("current")
_CLWlanFlexibleNetflowTable_Object = MibTable
cLWlanFlexibleNetflowTable = _CLWlanFlexibleNetflowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cLWlanFlexibleNetflowTable.setStatus("current")
_CLWlanFlexibleNetflowEntry_Object = MibTableRow
cLWlanFlexibleNetflowEntry = _CLWlanFlexibleNetflowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 5, 1)
)
cLWlanFlexibleNetflowEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanFlexibleNetflowPolicyTypeIndex"),
)
if mibBuilder.loadTexts:
    cLWlanFlexibleNetflowEntry.setStatus("current")


class _CLWlanFlexibleNetflowPolicyTypeIndex_Type(Integer32):
    """Custom type cLWlanFlexibleNetflowPolicyTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipv4InputPolicy", 1),
          ("ipv4OutputPolicy", 2),
          ("ipv6InputPolicy", 3),
          ("ipv6OutputPolicy", 4),
          ("datalinkInputPolicy", 5),
          ("datalinkOutputPolicy", 6))
    )


_CLWlanFlexibleNetflowPolicyTypeIndex_Type.__name__ = "Integer32"
_CLWlanFlexibleNetflowPolicyTypeIndex_Object = MibTableColumn
cLWlanFlexibleNetflowPolicyTypeIndex = _CLWlanFlexibleNetflowPolicyTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 5, 1, 1),
    _CLWlanFlexibleNetflowPolicyTypeIndex_Type()
)
cLWlanFlexibleNetflowPolicyTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanFlexibleNetflowPolicyTypeIndex.setStatus("current")
_CLWlanFlexibleNetflowMonitorName_Type = SnmpAdminString
_CLWlanFlexibleNetflowMonitorName_Object = MibTableColumn
cLWlanFlexibleNetflowMonitorName = _CLWlanFlexibleNetflowMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 5, 1, 2),
    _CLWlanFlexibleNetflowMonitorName_Type()
)
cLWlanFlexibleNetflowMonitorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanFlexibleNetflowMonitorName.setStatus("current")
_CLWlanFlexibleNetflowRowStatus_Type = RowStatus
_CLWlanFlexibleNetflowRowStatus_Object = MibTableColumn
cLWlanFlexibleNetflowRowStatus = _CLWlanFlexibleNetflowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 1, 5, 1, 3),
    _CLWlanFlexibleNetflowRowStatus_Type()
)
cLWlanFlexibleNetflowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanFlexibleNetflowRowStatus.setStatus("current")
_CiscoLwappAPGroupsVlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAPGroupsVlanConfig = _CiscoLwappAPGroupsVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2)
)
_CLAPGroupsVlanConfigTable_Object = MibTable
cLAPGroupsVlanConfigTable = _CLAPGroupsVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLAPGroupsVlanConfigTable.setStatus("current")
_CLAPGroupsVlanConfigEntry_Object = MibTableRow
cLAPGroupsVlanConfigEntry = _CLAPGroupsVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1)
)
cLAPGroupsVlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsVlanConfigEntry.setStatus("current")


class _CLAPGroupName_Type(OctetString):
    """Custom type cLAPGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAPGroupName_Type.__name__ = "OctetString"
_CLAPGroupName_Object = MibTableColumn
cLAPGroupName = _CLAPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 1),
    _CLAPGroupName_Type()
)
cLAPGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAPGroupName.setStatus("current")


class _CLAPGroupsVlanMappingInterfaceName_Type(OctetString):
    """Custom type cLAPGroupsVlanMappingInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLAPGroupsVlanMappingInterfaceName_Type.__name__ = "OctetString"
_CLAPGroupsVlanMappingInterfaceName_Object = MibTableColumn
cLAPGroupsVlanMappingInterfaceName = _CLAPGroupsVlanMappingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 2),
    _CLAPGroupsVlanMappingInterfaceName_Type()
)
cLAPGroupsVlanMappingInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsVlanMappingInterfaceName.setStatus("deprecated")


class _CLAPGroupNACSupport_Type(TruthValue):
    """Custom type cLAPGroupNACSupport based on TruthValue"""
    defaultValue = 2


_CLAPGroupNACSupport_Type.__name__ = "TruthValue"
_CLAPGroupNACSupport_Object = MibTableColumn
cLAPGroupNACSupport = _CLAPGroupNACSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 3),
    _CLAPGroupNACSupport_Type()
)
cLAPGroupNACSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupNACSupport.setStatus("current")
_CLAPGroupsVlanConfigRowStatus_Type = RowStatus
_CLAPGroupsVlanConfigRowStatus_Object = MibTableColumn
cLAPGroupsVlanConfigRowStatus = _CLAPGroupsVlanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 4),
    _CLAPGroupsVlanConfigRowStatus_Type()
)
cLAPGroupsVlanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsVlanConfigRowStatus.setStatus("current")


class _CLAPGroupsVlanConfigStorageType_Type(StorageType):
    """Custom type cLAPGroupsVlanConfigStorageType based on StorageType"""
    defaultValue = 3


_CLAPGroupsVlanConfigStorageType_Type.__name__ = "StorageType"
_CLAPGroupsVlanConfigStorageType_Object = MibTableColumn
cLAPGroupsVlanConfigStorageType = _CLAPGroupsVlanConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 5),
    _CLAPGroupsVlanConfigStorageType_Type()
)
cLAPGroupsVlanConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsVlanConfigStorageType.setStatus("current")
_CLAPGroupsWlanOrderIndex_Type = Unsigned32
_CLAPGroupsWlanOrderIndex_Object = MibTableColumn
cLAPGroupsWlanOrderIndex = _CLAPGroupsWlanOrderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 6),
    _CLAPGroupsWlanOrderIndex_Type()
)
cLAPGroupsWlanOrderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPGroupsWlanOrderIndex.setStatus("current")


class _CLAPGroupsVlanMappingInterfaceNameRev1_Type(OctetString):
    """Custom type cLAPGroupsVlanMappingInterfaceNameRev1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLAPGroupsVlanMappingInterfaceNameRev1_Type.__name__ = "OctetString"
_CLAPGroupsVlanMappingInterfaceNameRev1_Object = MibTableColumn
cLAPGroupsVlanMappingInterfaceNameRev1 = _CLAPGroupsVlanMappingInterfaceNameRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 1, 1, 7),
    _CLAPGroupsVlanMappingInterfaceNameRev1_Type()
)
cLAPGroupsVlanMappingInterfaceNameRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsVlanMappingInterfaceNameRev1.setStatus("current")
_CLAPGroupsVenueConfigTable_Object = MibTable
cLAPGroupsVenueConfigTable = _CLAPGroupsVenueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigTable.setStatus("current")
_CLAPGroupsVenueConfigEntry_Object = MibTableRow
cLAPGroupsVenueConfigEntry = _CLAPGroupsVenueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1)
)
cLAPGroupsVenueConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigEntry.setStatus("current")


class _CLAPGroupsVenueConfigVenueGroup_Type(Integer32):
    """Custom type cLAPGroupsVenueConfigVenueGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("assembly", 2),
          ("business", 3),
          ("educational", 4),
          ("factoryAndIndustrial", 5),
          ("institutional", 6),
          ("mercantile", 7),
          ("residential", 8),
          ("storage", 9),
          ("utilityAndMisc", 10),
          ("vehicular", 11),
          ("outdoor", 12))
    )


_CLAPGroupsVenueConfigVenueGroup_Type.__name__ = "Integer32"
_CLAPGroupsVenueConfigVenueGroup_Object = MibTableColumn
cLAPGroupsVenueConfigVenueGroup = _CLAPGroupsVenueConfigVenueGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1, 1),
    _CLAPGroupsVenueConfigVenueGroup_Type()
)
cLAPGroupsVenueConfigVenueGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigVenueGroup.setStatus("current")


class _CLAPGroupsVenueConfigVenueType_Type(Integer32):
    """Custom type cLAPGroupsVenueConfigVenueType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("unspecifiedAssembly", 2),
          ("arena", 3),
          ("stadium", 4),
          ("passengerTerminal", 5),
          ("amphitheater", 6),
          ("amusementPark", 7),
          ("placeOfWorship", 8),
          ("conventionCenter", 9),
          ("library", 10),
          ("museum", 11),
          ("restaurant", 12),
          ("theater", 13),
          ("bar", 14),
          ("coffeeShop", 15),
          ("zooOrAquarium", 16),
          ("emergencyCoordinationCenter", 17),
          ("unspecifiedBusiness", 18),
          ("doctorOrDentistOffice", 19),
          ("bank", 20),
          ("fireStation", 21),
          ("policeStation", 22),
          ("postOffice", 23),
          ("professionalOffice", 24),
          ("researchAndDevelopmentFacility", 25),
          ("attorneyOffice", 26),
          ("unspecifiedEducational", 27),
          ("schoolPrimary", 28),
          ("schoolSecondary", 29),
          ("universityOrCollege", 30),
          ("unspecifiedFactoryAndIndustrial", 31),
          ("factory", 32),
          ("unspecifiedInstitutional", 33),
          ("hospital", 34),
          ("longTermCareFacility", 35),
          ("alcoholAndDrugRehabilitationCenter", 36),
          ("groupHome", 37),
          ("prisonOrJail", 38),
          ("unspecifiedMercantile", 39),
          ("retailStore", 40),
          ("groceryMarket", 41),
          ("atomotiveServiceStation", 42),
          ("shoppingMall", 43),
          ("gasStation", 44),
          ("unspecifiedResidential", 45),
          ("privateResidence", 46),
          ("hotelOrMotel", 47),
          ("dormitory", 48),
          ("boardingHouse", 49),
          ("unspecifiedStorage", 50),
          ("unspecifiedUtility", 51),
          ("unspecifiedVehicular", 52),
          ("automobileOrTruck", 53),
          ("airplane", 54),
          ("bus", 55),
          ("ferry", 56),
          ("shipOrBoat", 57),
          ("train", 58),
          ("motorBike", 59),
          ("unspecifiedOutdoor", 60),
          ("muniMeshNetwork", 61),
          ("cityPark", 62),
          ("restArea", 63),
          ("trafficControl", 64),
          ("busStop", 65),
          ("kiosk", 66))
    )


_CLAPGroupsVenueConfigVenueType_Type.__name__ = "Integer32"
_CLAPGroupsVenueConfigVenueType_Object = MibTableColumn
cLAPGroupsVenueConfigVenueType = _CLAPGroupsVenueConfigVenueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1, 2),
    _CLAPGroupsVenueConfigVenueType_Type()
)
cLAPGroupsVenueConfigVenueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigVenueType.setStatus("current")


class _CLAPGroupsVenueConfigVenueName_Type(SnmpAdminString):
    """Custom type cLAPGroupsVenueConfigVenueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_CLAPGroupsVenueConfigVenueName_Type.__name__ = "SnmpAdminString"
_CLAPGroupsVenueConfigVenueName_Object = MibTableColumn
cLAPGroupsVenueConfigVenueName = _CLAPGroupsVenueConfigVenueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1, 3),
    _CLAPGroupsVenueConfigVenueName_Type()
)
cLAPGroupsVenueConfigVenueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigVenueName.setStatus("current")


class _CLAPGroupsVenueConfigLanguage_Type(SnmpAdminString):
    """Custom type cLAPGroupsVenueConfigLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CLAPGroupsVenueConfigLanguage_Type.__name__ = "SnmpAdminString"
_CLAPGroupsVenueConfigLanguage_Object = MibTableColumn
cLAPGroupsVenueConfigLanguage = _CLAPGroupsVenueConfigLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1, 4),
    _CLAPGroupsVenueConfigLanguage_Type()
)
cLAPGroupsVenueConfigLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigLanguage.setStatus("current")


class _CLAPGroupsOperatingClass_Type(Bits):
    """Custom type cLAPGroupsOperatingClass based on Bits"""
    namedValues = NamedValues(
        *(("class81", 0),
          ("class83", 1),
          ("class84", 2),
          ("class112", 3),
          ("class113", 4),
          ("class115", 5),
          ("class116", 6),
          ("class117", 7),
          ("class118", 8),
          ("class119", 9),
          ("class120", 10),
          ("class121", 11),
          ("class122", 12),
          ("class123", 13),
          ("class124", 14),
          ("class125", 15),
          ("class126", 16),
          ("class127", 17))
    )

_CLAPGroupsOperatingClass_Type.__name__ = "Bits"
_CLAPGroupsOperatingClass_Object = MibTableColumn
cLAPGroupsOperatingClass = _CLAPGroupsOperatingClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 2, 1, 5),
    _CLAPGroupsOperatingClass_Type()
)
cLAPGroupsOperatingClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsOperatingClass.setStatus("current")
_CLAPGroupsMultipleVenueTable_Object = MibTable
cLAPGroupsMultipleVenueTable = _CLAPGroupsMultipleVenueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueTable.setStatus("current")
_CLAPGroupsMultipleVenueEntry_Object = MibTableRow
cLAPGroupsMultipleVenueEntry = _CLAPGroupsMultipleVenueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 3, 1)
)
cLAPGroupsMultipleVenueEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueLanguage"),
)
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueEntry.setStatus("current")


class _CLAPGroupsMultipleVenueLanguage_Type(SnmpAdminString):
    """Custom type cLAPGroupsMultipleVenueLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CLAPGroupsMultipleVenueLanguage_Type.__name__ = "SnmpAdminString"
_CLAPGroupsMultipleVenueLanguage_Object = MibTableColumn
cLAPGroupsMultipleVenueLanguage = _CLAPGroupsMultipleVenueLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 3, 1, 1),
    _CLAPGroupsMultipleVenueLanguage_Type()
)
cLAPGroupsMultipleVenueLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueLanguage.setStatus("current")


class _CLAPGroupsMultipleVenueName_Type(SnmpAdminString):
    """Custom type cLAPGroupsMultipleVenueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_CLAPGroupsMultipleVenueName_Type.__name__ = "SnmpAdminString"
_CLAPGroupsMultipleVenueName_Object = MibTableColumn
cLAPGroupsMultipleVenueName = _CLAPGroupsMultipleVenueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 3, 1, 2),
    _CLAPGroupsMultipleVenueName_Type()
)
cLAPGroupsMultipleVenueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueName.setStatus("current")
_CLAPGroupsMultipleVenueRowStatus_Type = RowStatus
_CLAPGroupsMultipleVenueRowStatus_Object = MibTableColumn
cLAPGroupsMultipleVenueRowStatus = _CLAPGroupsMultipleVenueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 3, 1, 3),
    _CLAPGroupsMultipleVenueRowStatus_Type()
)
cLAPGroupsMultipleVenueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueRowStatus.setStatus("current")
_CLAPGroupsPolicyTable_Object = MibTable
cLAPGroupsPolicyTable = _CLAPGroupsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLAPGroupsPolicyTable.setStatus("current")
_CLAPGroupsPolicyEntry_Object = MibTableRow
cLAPGroupsPolicyEntry = _CLAPGroupsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1)
)
cLAPGroupsPolicyEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPolicyWlanId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPolicyPriIndex"),
)
if mibBuilder.loadTexts:
    cLAPGroupsPolicyEntry.setStatus("current")
_CLAPGroupsPolicyWlanId_Type = Unsigned32
_CLAPGroupsPolicyWlanId_Object = MibTableColumn
cLAPGroupsPolicyWlanId = _CLAPGroupsPolicyWlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1, 1),
    _CLAPGroupsPolicyWlanId_Type()
)
cLAPGroupsPolicyWlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAPGroupsPolicyWlanId.setStatus("current")
_CLAPGroupsPolicyPriIndex_Type = Unsigned32
_CLAPGroupsPolicyPriIndex_Object = MibTableColumn
cLAPGroupsPolicyPriIndex = _CLAPGroupsPolicyPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1, 2),
    _CLAPGroupsPolicyPriIndex_Type()
)
cLAPGroupsPolicyPriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAPGroupsPolicyPriIndex.setStatus("current")
_CLAPGroupsPolicyIndex_Type = Unsigned32
_CLAPGroupsPolicyIndex_Object = MibTableColumn
cLAPGroupsPolicyIndex = _CLAPGroupsPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1, 3),
    _CLAPGroupsPolicyIndex_Type()
)
cLAPGroupsPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsPolicyIndex.setStatus("current")


class _CLAPGroupsPolicyWlanProfile_Type(SnmpAdminString):
    """Custom type cLAPGroupsPolicyWlanProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAPGroupsPolicyWlanProfile_Type.__name__ = "SnmpAdminString"
_CLAPGroupsPolicyWlanProfile_Object = MibTableColumn
cLAPGroupsPolicyWlanProfile = _CLAPGroupsPolicyWlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1, 4),
    _CLAPGroupsPolicyWlanProfile_Type()
)
cLAPGroupsPolicyWlanProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPGroupsPolicyWlanProfile.setStatus("current")
_CLAPGroupsPolicyRowStatus_Type = RowStatus
_CLAPGroupsPolicyRowStatus_Object = MibTableColumn
cLAPGroupsPolicyRowStatus = _CLAPGroupsPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 4, 1, 5),
    _CLAPGroupsPolicyRowStatus_Type()
)
cLAPGroupsPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsPolicyRowStatus.setStatus("current")
_CLAPGroupQinqConfigTable_Object = MibTable
cLAPGroupQinqConfigTable = _CLAPGroupQinqConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLAPGroupQinqConfigTable.setStatus("current")
_CLAPGroupQinqConfigEntry_Object = MibTableRow
cLAPGroupQinqConfigEntry = _CLAPGroupQinqConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 5, 1)
)
cLAPGroupQinqConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupQinqConfigEntry.setStatus("current")
_CLAPGroupTrafficQinqEnabled_Type = TruthValue
_CLAPGroupTrafficQinqEnabled_Object = MibTableColumn
cLAPGroupTrafficQinqEnabled = _CLAPGroupTrafficQinqEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 5, 1, 1),
    _CLAPGroupTrafficQinqEnabled_Type()
)
cLAPGroupTrafficQinqEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupTrafficQinqEnabled.setStatus("current")
_CLAPGroupDhcpQinqEnabled_Type = TruthValue
_CLAPGroupDhcpQinqEnabled_Object = MibTableColumn
cLAPGroupDhcpQinqEnabled = _CLAPGroupDhcpQinqEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 5, 1, 2),
    _CLAPGroupDhcpQinqEnabled_Type()
)
cLAPGroupDhcpQinqEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupDhcpQinqEnabled.setStatus("current")


class _CLAPGroupQinqServiceVlanId_Type(Integer32):
    """Custom type cLAPGroupQinqServiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLAPGroupQinqServiceVlanId_Type.__name__ = "Integer32"
_CLAPGroupQinqServiceVlanId_Object = MibTableColumn
cLAPGroupQinqServiceVlanId = _CLAPGroupQinqServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 5, 1, 3),
    _CLAPGroupQinqServiceVlanId_Type()
)
cLAPGroupQinqServiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupQinqServiceVlanId.setStatus("current")
_CLAPGroupConfigTable_Object = MibTable
cLAPGroupConfigTable = _CLAPGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLAPGroupConfigTable.setStatus("current")
_CLAPGroupConfigEntry_Object = MibTableRow
cLAPGroupConfigEntry = _CLAPGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 6, 1)
)
cLAPGroupConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupConfigEntry.setStatus("current")


class _CLApGroupPreferMode_Type(Integer32):
    """Custom type cLApGroupPreferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("disable", 3))
    )


_CLApGroupPreferMode_Type.__name__ = "Integer32"
_CLApGroupPreferMode_Object = MibTableColumn
cLApGroupPreferMode = _CLApGroupPreferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 6, 1, 1),
    _CLApGroupPreferMode_Type()
)
cLApGroupPreferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGroupPreferMode.setStatus("current")


class _CLApGroupGlobalWebAuthConfig_Type(TruthValue):
    """Custom type cLApGroupGlobalWebAuthConfig based on TruthValue"""
    defaultValue = 2


_CLApGroupGlobalWebAuthConfig_Type.__name__ = "TruthValue"
_CLApGroupGlobalWebAuthConfig_Object = MibTableColumn
cLApGroupGlobalWebAuthConfig = _CLApGroupGlobalWebAuthConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 6, 1, 2),
    _CLApGroupGlobalWebAuthConfig_Type()
)
cLApGroupGlobalWebAuthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGroupGlobalWebAuthConfig.setStatus("current")


class _CLApGroupExternalWebAuthUrl_Type(CiscoURLStringOrEmpty):
    """Custom type cLApGroupExternalWebAuthUrl based on CiscoURLStringOrEmpty"""
    defaultValue = OctetString("")


_CLApGroupExternalWebAuthUrl_Type.__name__ = "CiscoURLStringOrEmpty"
_CLApGroupExternalWebAuthUrl_Object = MibTableColumn
cLApGroupExternalWebAuthUrl = _CLApGroupExternalWebAuthUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 2, 6, 1, 3),
    _CLApGroupExternalWebAuthUrl_Type()
)
cLApGroupExternalWebAuthUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGroupExternalWebAuthUrl.setStatus("current")
_CiscoLwappWlan11uConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWlan11uConfig = _CiscoLwappWlan11uConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3)
)
_CLWlan11uTable_Object = MibTable
cLWlan11uTable = _CLWlan11uTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLWlan11uTable.setStatus("current")
_CLWlan11uEntry_Object = MibTableRow
cLWlan11uEntry = _CLWlan11uEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1)
)
cLWlan11uEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uEntry.setStatus("current")


class _CLWlan11uStatus_Type(TruthValue):
    """Custom type cLWlan11uStatus based on TruthValue"""
    defaultValue = 2


_CLWlan11uStatus_Type.__name__ = "TruthValue"
_CLWlan11uStatus_Object = MibTableColumn
cLWlan11uStatus = _CLWlan11uStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 1),
    _CLWlan11uStatus_Type()
)
cLWlan11uStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uStatus.setStatus("current")


class _CLWlan11uInternetAccess_Type(TruthValue):
    """Custom type cLWlan11uInternetAccess based on TruthValue"""
    defaultValue = 1


_CLWlan11uInternetAccess_Type.__name__ = "TruthValue"
_CLWlan11uInternetAccess_Object = MibTableColumn
cLWlan11uInternetAccess = _CLWlan11uInternetAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 2),
    _CLWlan11uInternetAccess_Type()
)
cLWlan11uInternetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uInternetAccess.setStatus("current")


class _CLWlan11uNetworkType_Type(Integer32):
    """Custom type cLWlan11uNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("private", 2),
          ("privateWithGuestAccess", 3),
          ("chargeablePublicNetwork", 4),
          ("freePublicNetwork", 5),
          ("testOrEquipment", 6),
          ("wildcard", 7),
          ("personnalDeviceNetwork", 8),
          ("emgerencyServiceOnlyNetwork", 9),
          ("notConfigured", 255))
    )


_CLWlan11uNetworkType_Type.__name__ = "Integer32"
_CLWlan11uNetworkType_Object = MibTableColumn
cLWlan11uNetworkType = _CLWlan11uNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 3),
    _CLWlan11uNetworkType_Type()
)
cLWlan11uNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uNetworkType.setStatus("current")


class _CLWlan11uVenueGroup_Type(Integer32):
    """Custom type cLWlan11uVenueGroup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("assembly", 2),
          ("business", 3),
          ("educational", 4),
          ("factoryAndIndustrial", 5),
          ("institutional", 6),
          ("mercantile", 7),
          ("residential", 8),
          ("storage", 9),
          ("utilityAndMisc", 10),
          ("vehicular", 11),
          ("outdoor", 12))
    )


_CLWlan11uVenueGroup_Type.__name__ = "Integer32"
_CLWlan11uVenueGroup_Object = MibTableColumn
cLWlan11uVenueGroup = _CLWlan11uVenueGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 4),
    _CLWlan11uVenueGroup_Type()
)
cLWlan11uVenueGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uVenueGroup.setStatus("deprecated")


class _CLWlan11uVenueType_Type(Integer32):
    """Custom type cLWlan11uVenueType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("assembly", 2),
          ("business", 3),
          ("educational", 4),
          ("factoryAndIndustrial", 5),
          ("institutional", 6),
          ("mercantile", 7),
          ("residential", 8),
          ("storage", 9),
          ("utilityAndMisc", 10),
          ("vehicular", 11),
          ("outdoor", 12))
    )


_CLWlan11uVenueType_Type.__name__ = "Integer32"
_CLWlan11uVenueType_Object = MibTableColumn
cLWlan11uVenueType = _CLWlan11uVenueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 5),
    _CLWlan11uVenueType_Type()
)
cLWlan11uVenueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uVenueType.setStatus("deprecated")


class _CLWlan11uVenueName_Type(SnmpAdminString):
    """Custom type cLWlan11uVenueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLWlan11uVenueName_Type.__name__ = "SnmpAdminString"
_CLWlan11uVenueName_Object = MibTableColumn
cLWlan11uVenueName = _CLWlan11uVenueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 6),
    _CLWlan11uVenueName_Type()
)
cLWlan11uVenueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uVenueName.setStatus("deprecated")
_CLWlan11uHessid_Type = MacAddress
_CLWlan11uHessid_Object = MibTableColumn
cLWlan11uHessid = _CLWlan11uHessid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 8),
    _CLWlan11uHessid_Type()
)
cLWlan11uHessid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uHessid.setStatus("current")


class _CLWlan11uNetworkAuthType_Type(Integer32):
    """Custom type cLWlan11uNetworkAuthType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acceptance", 1),
          ("enrollment", 2),
          ("redirection", 3),
          ("dnsRedirection", 4),
          ("notConfigured", 5))
    )


_CLWlan11uNetworkAuthType_Type.__name__ = "Integer32"
_CLWlan11uNetworkAuthType_Object = MibTableColumn
cLWlan11uNetworkAuthType = _CLWlan11uNetworkAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 9),
    _CLWlan11uNetworkAuthType_Type()
)
cLWlan11uNetworkAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uNetworkAuthType.setStatus("current")


class _CLWlan11uIpAddressAvailIpv4_Type(Integer32):
    """Custom type cLWlan11uIpAddressAvailIpv4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("public", 2),
          ("portRestricted", 3),
          ("singleNATPrivate", 4),
          ("doubleNATPrivate", 5),
          ("portRestrictedAndSingleNATPrivate", 6),
          ("portRestrictedAndDoubleNATPrivate", 7),
          ("unKnown", 8))
    )


_CLWlan11uIpAddressAvailIpv4_Type.__name__ = "Integer32"
_CLWlan11uIpAddressAvailIpv4_Object = MibTableColumn
cLWlan11uIpAddressAvailIpv4 = _CLWlan11uIpAddressAvailIpv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 10),
    _CLWlan11uIpAddressAvailIpv4_Type()
)
cLWlan11uIpAddressAvailIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uIpAddressAvailIpv4.setStatus("current")


class _CLWlan11uIpAddressAvailIpv6_Type(Integer32):
    """Custom type cLWlan11uIpAddressAvailIpv6 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("available", 2),
          ("unKnown", 3))
    )


_CLWlan11uIpAddressAvailIpv6_Type.__name__ = "Integer32"
_CLWlan11uIpAddressAvailIpv6_Object = MibTableColumn
cLWlan11uIpAddressAvailIpv6 = _CLWlan11uIpAddressAvailIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 1, 1, 11),
    _CLWlan11uIpAddressAvailIpv6_Type()
)
cLWlan11uIpAddressAvailIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlan11uIpAddressAvailIpv6.setStatus("current")
_CLWlan11uOuiTable_Object = MibTable
cLWlan11uOuiTable = _CLWlan11uOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLWlan11uOuiTable.setStatus("current")
_CLWlan11uOuiEntry_Object = MibTableRow
cLWlan11uOuiEntry = _CLWlan11uOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1)
)
cLWlan11uOuiEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uOuiEntry.setStatus("current")
_CLWlan11uOuiIndex_Type = Unsigned32
_CLWlan11uOuiIndex_Object = MibTableColumn
cLWlan11uOuiIndex = _CLWlan11uOuiIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1, 1),
    _CLWlan11uOuiIndex_Type()
)
cLWlan11uOuiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11uOuiIndex.setStatus("current")


class _CLWlan11uOui_Type(OctetString):
    """Custom type cLWlan11uOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(10, 10),
    )


_CLWlan11uOui_Type.__name__ = "OctetString"
_CLWlan11uOui_Object = MibTableColumn
cLWlan11uOui = _CLWlan11uOui_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1, 2),
    _CLWlan11uOui_Type()
)
cLWlan11uOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uOui.setStatus("current")


class _CLWlan11uOuiIsBeacon_Type(TruthValue):
    """Custom type cLWlan11uOuiIsBeacon based on TruthValue"""
    defaultValue = 2


_CLWlan11uOuiIsBeacon_Type.__name__ = "TruthValue"
_CLWlan11uOuiIsBeacon_Object = MibTableColumn
cLWlan11uOuiIsBeacon = _CLWlan11uOuiIsBeacon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1, 3),
    _CLWlan11uOuiIsBeacon_Type()
)
cLWlan11uOuiIsBeacon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uOuiIsBeacon.setStatus("current")
_CLWlan11uOuiRowStatus_Type = RowStatus
_CLWlan11uOuiRowStatus_Object = MibTableColumn
cLWlan11uOuiRowStatus = _CLWlan11uOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1, 4),
    _CLWlan11uOuiRowStatus_Type()
)
cLWlan11uOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uOuiRowStatus.setStatus("current")


class _CLWlan11uOuiStorageType_Type(StorageType):
    """Custom type cLWlan11uOuiStorageType based on StorageType"""
    defaultValue = 3


_CLWlan11uOuiStorageType_Type.__name__ = "StorageType"
_CLWlan11uOuiStorageType_Object = MibTableColumn
cLWlan11uOuiStorageType = _CLWlan11uOuiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 2, 1, 5),
    _CLWlan11uOuiStorageType_Type()
)
cLWlan11uOuiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uOuiStorageType.setStatus("current")
_CLWlan11uRealmTable_Object = MibTable
cLWlan11uRealmTable = _CLWlan11uRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLWlan11uRealmTable.setStatus("current")
_CLWlan11uRealmEntry_Object = MibTableRow
cLWlan11uRealmEntry = _CLWlan11uRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 3, 1)
)
cLWlan11uRealmEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uRealmEntry.setStatus("current")


class _CLWlan11uRealmIndex_Type(Unsigned32):
    """Custom type cLWlan11uRealmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CLWlan11uRealmIndex_Type.__name__ = "Unsigned32"
_CLWlan11uRealmIndex_Object = MibTableColumn
cLWlan11uRealmIndex = _CLWlan11uRealmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 3, 1, 1),
    _CLWlan11uRealmIndex_Type()
)
cLWlan11uRealmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11uRealmIndex.setStatus("current")


class _CLWlan11uRealmName_Type(SnmpAdminString):
    """Custom type cLWlan11uRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CLWlan11uRealmName_Type.__name__ = "SnmpAdminString"
_CLWlan11uRealmName_Object = MibTableColumn
cLWlan11uRealmName = _CLWlan11uRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 3, 1, 2),
    _CLWlan11uRealmName_Type()
)
cLWlan11uRealmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmName.setStatus("current")
_CLWlan11uRealmRowStatus_Type = RowStatus
_CLWlan11uRealmRowStatus_Object = MibTableColumn
cLWlan11uRealmRowStatus = _CLWlan11uRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 3, 1, 3),
    _CLWlan11uRealmRowStatus_Type()
)
cLWlan11uRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmRowStatus.setStatus("current")
_CLWlan11uRealmEapTable_Object = MibTable
cLWlan11uRealmEapTable = _CLWlan11uRealmEapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cLWlan11uRealmEapTable.setStatus("current")
_CLWlan11uRealmEapEntry_Object = MibTableRow
cLWlan11uRealmEapEntry = _CLWlan11uRealmEapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 4, 1)
)
cLWlan11uRealmEapEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uRealmEapEntry.setStatus("current")


class _CLWlan11uRealmEapIndex_Type(Unsigned32):
    """Custom type cLWlan11uRealmEapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLWlan11uRealmEapIndex_Type.__name__ = "Unsigned32"
_CLWlan11uRealmEapIndex_Object = MibTableColumn
cLWlan11uRealmEapIndex = _CLWlan11uRealmEapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 4, 1, 1),
    _CLWlan11uRealmEapIndex_Type()
)
cLWlan11uRealmEapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapIndex.setStatus("current")


class _CLWlan11uRealmEapMethod_Type(Integer32):
    """Custom type cLWlan11uRealmEapMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("leap", 2),
          ("peap", 3),
          ("eapTls", 4),
          ("eapFast", 5),
          ("eapSim", 6),
          ("eapTtls", 7),
          ("eapAka", 8))
    )


_CLWlan11uRealmEapMethod_Type.__name__ = "Integer32"
_CLWlan11uRealmEapMethod_Object = MibTableColumn
cLWlan11uRealmEapMethod = _CLWlan11uRealmEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 4, 1, 2),
    _CLWlan11uRealmEapMethod_Type()
)
cLWlan11uRealmEapMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapMethod.setStatus("current")
_CLWlan11uRealmEapRowStatus_Type = RowStatus
_CLWlan11uRealmEapRowStatus_Object = MibTableColumn
cLWlan11uRealmEapRowStatus = _CLWlan11uRealmEapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 4, 1, 3),
    _CLWlan11uRealmEapRowStatus_Type()
)
cLWlan11uRealmEapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapRowStatus.setStatus("current")
_CLWlan11uRealmEapAuthTable_Object = MibTable
cLWlan11uRealmEapAuthTable = _CLWlan11uRealmEapAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthTable.setStatus("current")
_CLWlan11uRealmEapAuthEntry_Object = MibTableRow
cLWlan11uRealmEapAuthEntry = _CLWlan11uRealmEapAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1)
)
cLWlan11uRealmEapAuthEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapAuthIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthEntry.setStatus("current")


class _CLWlan11uRealmEapAuthIndex_Type(Unsigned32):
    """Custom type cLWlan11uRealmEapAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLWlan11uRealmEapAuthIndex_Type.__name__ = "Unsigned32"
_CLWlan11uRealmEapAuthIndex_Object = MibTableColumn
cLWlan11uRealmEapAuthIndex = _CLWlan11uRealmEapAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1, 1),
    _CLWlan11uRealmEapAuthIndex_Type()
)
cLWlan11uRealmEapAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthIndex.setStatus("current")


class _CLWlan11uRealmEapAuthMethod_Type(Integer32):
    """Custom type cLWlan11uRealmEapAuthMethod based on Integer32"""
    defaultValue = 1

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
        *(("nonEapInnerAuthType", 1),
          ("innerAuthEapType", 2),
          ("credentialType", 3),
          ("tunneledEapCredentialType", 4))
    )


_CLWlan11uRealmEapAuthMethod_Type.__name__ = "Integer32"
_CLWlan11uRealmEapAuthMethod_Object = MibTableColumn
cLWlan11uRealmEapAuthMethod = _CLWlan11uRealmEapAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1, 2),
    _CLWlan11uRealmEapAuthMethod_Type()
)
cLWlan11uRealmEapAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthMethod.setStatus("current")


class _CLWlan11uRealmEapAuthParam_Type(Integer32):
    """Custom type cLWlan11uRealmEapAuthParam based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pap", 2),
          ("chap", 3),
          ("mschap", 4),
          ("mschapV2", 5),
          ("leap", 6),
          ("peap", 7),
          ("eapTls", 8),
          ("eapFast", 9),
          ("eapSim", 10),
          ("eapTtls", 11),
          ("eapAka", 12),
          ("sim", 13),
          ("usim", 14),
          ("nfcSecure", 15),
          ("hardwareToken", 16),
          ("softToken", 17),
          ("certificate", 18),
          ("usernamePassword", 19),
          ("reserved", 20),
          ("anonynous", 21),
          ("vendorSpecific", 22))
    )


_CLWlan11uRealmEapAuthParam_Type.__name__ = "Integer32"
_CLWlan11uRealmEapAuthParam_Object = MibTableColumn
cLWlan11uRealmEapAuthParam = _CLWlan11uRealmEapAuthParam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1, 3),
    _CLWlan11uRealmEapAuthParam_Type()
)
cLWlan11uRealmEapAuthParam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthParam.setStatus("current")


class _CLWlan11uRealmEapAuthCredentialType_Type(Integer32):
    """Custom type cLWlan11uRealmEapAuthCredentialType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("sim", 1),
          ("usim", 2),
          ("nfcSecure", 3),
          ("hardwareToken", 4),
          ("softToken", 5),
          ("certificate", 6),
          ("usernamePassword", 7),
          ("reserved", 8),
          ("anonynous", 9),
          ("vendorSpecific", 10))
    )


_CLWlan11uRealmEapAuthCredentialType_Type.__name__ = "Integer32"
_CLWlan11uRealmEapAuthCredentialType_Object = MibTableColumn
cLWlan11uRealmEapAuthCredentialType = _CLWlan11uRealmEapAuthCredentialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1, 4),
    _CLWlan11uRealmEapAuthCredentialType_Type()
)
cLWlan11uRealmEapAuthCredentialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthCredentialType.setStatus("current")
_CLWlan11uRealmEapAuthRowStatus_Type = RowStatus
_CLWlan11uRealmEapAuthRowStatus_Object = MibTableColumn
cLWlan11uRealmEapAuthRowStatus = _CLWlan11uRealmEapAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 5, 1, 5),
    _CLWlan11uRealmEapAuthRowStatus_Type()
)
cLWlan11uRealmEapAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uRealmEapAuthRowStatus.setStatus("current")
_CLWlan11uDomainTable_Object = MibTable
cLWlan11uDomainTable = _CLWlan11uDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cLWlan11uDomainTable.setStatus("current")
_CLWlan11uDomainEntry_Object = MibTableRow
cLWlan11uDomainEntry = _CLWlan11uDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 6, 1)
)
cLWlan11uDomainEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11uDomainIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11uDomainEntry.setStatus("current")


class _CLWlan11uDomainIndex_Type(Unsigned32):
    """Custom type cLWlan11uDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWlan11uDomainIndex_Type.__name__ = "Unsigned32"
_CLWlan11uDomainIndex_Object = MibTableColumn
cLWlan11uDomainIndex = _CLWlan11uDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 6, 1, 1),
    _CLWlan11uDomainIndex_Type()
)
cLWlan11uDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11uDomainIndex.setStatus("current")


class _CLWlan11uDomainName_Type(SnmpAdminString):
    """Custom type cLWlan11uDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLWlan11uDomainName_Type.__name__ = "SnmpAdminString"
_CLWlan11uDomainName_Object = MibTableColumn
cLWlan11uDomainName = _CLWlan11uDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 6, 1, 2),
    _CLWlan11uDomainName_Type()
)
cLWlan11uDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uDomainName.setStatus("current")
_CLWlan11uDomainRowStatus_Type = RowStatus
_CLWlan11uDomainRowStatus_Object = MibTableColumn
cLWlan11uDomainRowStatus = _CLWlan11uDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 6, 1, 3),
    _CLWlan11uDomainRowStatus_Type()
)
cLWlan11uDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11uDomainRowStatus.setStatus("current")
_CLWlan11u3gppTable_Object = MibTable
cLWlan11u3gppTable = _CLWlan11u3gppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cLWlan11u3gppTable.setStatus("current")
_CLWlan11u3gppEntry_Object = MibTableRow
cLWlan11u3gppEntry = _CLWlan11u3gppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7, 1)
)
cLWlan11u3gppEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlan11u3gppIndex"),
)
if mibBuilder.loadTexts:
    cLWlan11u3gppEntry.setStatus("current")


class _CLWlan11u3gppIndex_Type(Unsigned32):
    """Custom type cLWlan11u3gppIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWlan11u3gppIndex_Type.__name__ = "Unsigned32"
_CLWlan11u3gppIndex_Object = MibTableColumn
cLWlan11u3gppIndex = _CLWlan11u3gppIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7, 1, 1),
    _CLWlan11u3gppIndex_Type()
)
cLWlan11u3gppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlan11u3gppIndex.setStatus("current")
_CLWlan11u3gppCountryCode_Type = OctetString
_CLWlan11u3gppCountryCode_Object = MibTableColumn
cLWlan11u3gppCountryCode = _CLWlan11u3gppCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7, 1, 2),
    _CLWlan11u3gppCountryCode_Type()
)
cLWlan11u3gppCountryCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11u3gppCountryCode.setStatus("current")
_CLWlan11u3gppNetworkCode_Type = OctetString
_CLWlan11u3gppNetworkCode_Object = MibTableColumn
cLWlan11u3gppNetworkCode = _CLWlan11u3gppNetworkCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7, 1, 3),
    _CLWlan11u3gppNetworkCode_Type()
)
cLWlan11u3gppNetworkCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11u3gppNetworkCode.setStatus("current")
_CLWlan11u3gppRowStatus_Type = RowStatus
_CLWlan11u3gppRowStatus_Object = MibTableColumn
cLWlan11u3gppRowStatus = _CLWlan11u3gppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 3, 7, 1, 4),
    _CLWlan11u3gppRowStatus_Type()
)
cLWlan11u3gppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlan11u3gppRowStatus.setStatus("current")
_CiscoLwappWlanServiceAdvertisementConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWlanServiceAdvertisementConfig = _CiscoLwappWlanServiceAdvertisementConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 4)
)
_CLWlanServiceAdvertisementTable_Object = MibTable
cLWlanServiceAdvertisementTable = _CLWlanServiceAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLWlanServiceAdvertisementTable.setStatus("current")
_CLWlanServiceAdvertisementEntry_Object = MibTableRow
cLWlanServiceAdvertisementEntry = _CLWlanServiceAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 4, 1, 1)
)
cLWlanServiceAdvertisementEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanServiceAdvertisementEntry.setStatus("current")


class _CLWlanServiceAdvertisementStatus_Type(TruthValue):
    """Custom type cLWlanServiceAdvertisementStatus based on TruthValue"""
    defaultValue = 2


_CLWlanServiceAdvertisementStatus_Type.__name__ = "TruthValue"
_CLWlanServiceAdvertisementStatus_Object = MibTableColumn
cLWlanServiceAdvertisementStatus = _CLWlanServiceAdvertisementStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 4, 1, 1, 1),
    _CLWlanServiceAdvertisementStatus_Type()
)
cLWlanServiceAdvertisementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanServiceAdvertisementStatus.setStatus("current")


class _CLWlanServiceAdvertisementMsapServerIndex_Type(Unsigned32):
    """Custom type cLWlanServiceAdvertisementMsapServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLWlanServiceAdvertisementMsapServerIndex_Type.__name__ = "Unsigned32"
_CLWlanServiceAdvertisementMsapServerIndex_Object = MibTableColumn
cLWlanServiceAdvertisementMsapServerIndex = _CLWlanServiceAdvertisementMsapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 4, 1, 1, 5),
    _CLWlanServiceAdvertisementMsapServerIndex_Type()
)
cLWlanServiceAdvertisementMsapServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanServiceAdvertisementMsapServerIndex.setStatus("current")
_CiscoLwappWlanHotSpot2Config_ObjectIdentity = ObjectIdentity
ciscoLwappWlanHotSpot2Config = _CiscoLwappWlanHotSpot2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5)
)
_CLWlanHotSpot2OperatorTable_Object = MibTable
cLWlanHotSpot2OperatorTable = _CLWlanHotSpot2OperatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorTable.setStatus("current")
_CLWlanHotSpot2OperatorEntry_Object = MibTableRow
cLWlanHotSpot2OperatorEntry = _CLWlanHotSpot2OperatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1, 1)
)
cLWlanHotSpot2OperatorEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2OperatorIndex"),
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorEntry.setStatus("current")


class _CLWlanHotSpot2OperatorIndex_Type(Unsigned32):
    """Custom type cLWlanHotSpot2OperatorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWlanHotSpot2OperatorIndex_Type.__name__ = "Unsigned32"
_CLWlanHotSpot2OperatorIndex_Object = MibTableColumn
cLWlanHotSpot2OperatorIndex = _CLWlanHotSpot2OperatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1, 1, 1),
    _CLWlanHotSpot2OperatorIndex_Type()
)
cLWlanHotSpot2OperatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorIndex.setStatus("current")


class _CLWlanHotSpot2OperatorName_Type(SnmpAdminString):
    """Custom type cLWlanHotSpot2OperatorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLWlanHotSpot2OperatorName_Type.__name__ = "SnmpAdminString"
_CLWlanHotSpot2OperatorName_Object = MibTableColumn
cLWlanHotSpot2OperatorName = _CLWlanHotSpot2OperatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1, 1, 2),
    _CLWlanHotSpot2OperatorName_Type()
)
cLWlanHotSpot2OperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorName.setStatus("current")


class _CLWlanHotSpot2OperatorLanguage_Type(SnmpAdminString):
    """Custom type cLWlanHotSpot2OperatorLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_CLWlanHotSpot2OperatorLanguage_Type.__name__ = "SnmpAdminString"
_CLWlanHotSpot2OperatorLanguage_Object = MibTableColumn
cLWlanHotSpot2OperatorLanguage = _CLWlanHotSpot2OperatorLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1, 1, 3),
    _CLWlanHotSpot2OperatorLanguage_Type()
)
cLWlanHotSpot2OperatorLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorLanguage.setStatus("current")
_CLWlanHotSpot2OperatorRowStatus_Type = RowStatus
_CLWlanHotSpot2OperatorRowStatus_Object = MibTableColumn
cLWlanHotSpot2OperatorRowStatus = _CLWlanHotSpot2OperatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 1, 1, 4),
    _CLWlanHotSpot2OperatorRowStatus_Type()
)
cLWlanHotSpot2OperatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2OperatorRowStatus.setStatus("current")
_CLWlanHotSpot2PortConfigTable_Object = MibTable
cLWlanHotSpot2PortConfigTable = _CLWlanHotSpot2PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigTable.setStatus("current")
_CLWlanHotSpot2PortConfigEntry_Object = MibTableRow
cLWlanHotSpot2PortConfigEntry = _CLWlanHotSpot2PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1)
)
cLWlanHotSpot2PortConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2PortConfigIndex"),
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigEntry.setStatus("current")
_CLWlanHotSpot2PortConfigIndex_Type = Unsigned32
_CLWlanHotSpot2PortConfigIndex_Object = MibTableColumn
cLWlanHotSpot2PortConfigIndex = _CLWlanHotSpot2PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1, 1),
    _CLWlanHotSpot2PortConfigIndex_Type()
)
cLWlanHotSpot2PortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigIndex.setStatus("current")


class _CLWlanHotSpot2PortConfigIpProtocol_Type(Integer32):
    """Custom type cLWlanHotSpot2PortConfigIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              50)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("ftp", 6),
          ("ikev2", 17),
          ("esp", 50))
    )


_CLWlanHotSpot2PortConfigIpProtocol_Type.__name__ = "Integer32"
_CLWlanHotSpot2PortConfigIpProtocol_Object = MibTableColumn
cLWlanHotSpot2PortConfigIpProtocol = _CLWlanHotSpot2PortConfigIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1, 2),
    _CLWlanHotSpot2PortConfigIpProtocol_Type()
)
cLWlanHotSpot2PortConfigIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigIpProtocol.setStatus("current")


class _CLWlanHotSpot2PortConfigPortNumber_Type(Integer32):
    """Custom type cLWlanHotSpot2PortConfigPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              20,
              22,
              443,
              500,
              1723,
              4500,
              5060)
        )
    )
    namedValues = NamedValues(
        *(("icmp-esp", 0),
          ("ftp", 20),
          ("ssh", 22),
          ("ttls-vpn", 443),
          ("ikev2", 500),
          ("pptp-vpn", 1723),
          ("ipsec-nat", 4500),
          ("voip", 5060))
    )


_CLWlanHotSpot2PortConfigPortNumber_Type.__name__ = "Integer32"
_CLWlanHotSpot2PortConfigPortNumber_Object = MibTableColumn
cLWlanHotSpot2PortConfigPortNumber = _CLWlanHotSpot2PortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1, 3),
    _CLWlanHotSpot2PortConfigPortNumber_Type()
)
cLWlanHotSpot2PortConfigPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigPortNumber.setStatus("current")


class _CLWlanHotSpot2PortConfigStatus_Type(Integer32):
    """Custom type cLWlanHotSpot2PortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2),
          ("unknown", 3))
    )


_CLWlanHotSpot2PortConfigStatus_Type.__name__ = "Integer32"
_CLWlanHotSpot2PortConfigStatus_Object = MibTableColumn
cLWlanHotSpot2PortConfigStatus = _CLWlanHotSpot2PortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1, 4),
    _CLWlanHotSpot2PortConfigStatus_Type()
)
cLWlanHotSpot2PortConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigStatus.setStatus("current")
_CLWlanHotSpot2PortConfigRowStatus_Type = RowStatus
_CLWlanHotSpot2PortConfigRowStatus_Object = MibTableColumn
cLWlanHotSpot2PortConfigRowStatus = _CLWlanHotSpot2PortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 2, 1, 5),
    _CLWlanHotSpot2PortConfigRowStatus_Type()
)
cLWlanHotSpot2PortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWlanHotSpot2PortConfigRowStatus.setStatus("current")
_CLWlanHotSpot2ConfigTable_Object = MibTable
cLWlanHotSpot2ConfigTable = _CLWlanHotSpot2ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2ConfigTable.setStatus("current")
_CLWlanHotSpot2ConfigEntry_Object = MibTableRow
cLWlanHotSpot2ConfigEntry = _CLWlanHotSpot2ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3, 1)
)
cLWlanHotSpot2ConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWlanHotSpot2ConfigEntry.setStatus("current")


class _CLWlanHotSpot2WanLinkStatus_Type(Integer32):
    """Custom type cLWlanHotSpot2WanLinkStatus based on Integer32"""
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
        *(("linkUp", 1),
          ("linkDown", 2),
          ("linkInTestState", 3),
          ("notConfigured", 4))
    )


_CLWlanHotSpot2WanLinkStatus_Type.__name__ = "Integer32"
_CLWlanHotSpot2WanLinkStatus_Object = MibTableColumn
cLWlanHotSpot2WanLinkStatus = _CLWlanHotSpot2WanLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3, 1, 1),
    _CLWlanHotSpot2WanLinkStatus_Type()
)
cLWlanHotSpot2WanLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanHotSpot2WanLinkStatus.setStatus("current")


class _CLWlanHotSpot2WanSymLinkStatus_Type(Integer32):
    """Custom type cLWlanHotSpot2WanSymLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("different", 1),
          ("same", 2))
    )


_CLWlanHotSpot2WanSymLinkStatus_Type.__name__ = "Integer32"
_CLWlanHotSpot2WanSymLinkStatus_Object = MibTableColumn
cLWlanHotSpot2WanSymLinkStatus = _CLWlanHotSpot2WanSymLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3, 1, 2),
    _CLWlanHotSpot2WanSymLinkStatus_Type()
)
cLWlanHotSpot2WanSymLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanHotSpot2WanSymLinkStatus.setStatus("current")
_CLWlanHotSpot2WanDownLinkSpeed_Type = Unsigned32
_CLWlanHotSpot2WanDownLinkSpeed_Object = MibTableColumn
cLWlanHotSpot2WanDownLinkSpeed = _CLWlanHotSpot2WanDownLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3, 1, 3),
    _CLWlanHotSpot2WanDownLinkSpeed_Type()
)
cLWlanHotSpot2WanDownLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanHotSpot2WanDownLinkSpeed.setStatus("current")
_CLWlanHotSpot2WanUpLinkSpeed_Type = Unsigned32
_CLWlanHotSpot2WanUpLinkSpeed_Object = MibTableColumn
cLWlanHotSpot2WanUpLinkSpeed = _CLWlanHotSpot2WanUpLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 5, 3, 1, 4),
    _CLWlanHotSpot2WanUpLinkSpeed_Type()
)
cLWlanHotSpot2WanUpLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWlanHotSpot2WanUpLinkSpeed.setStatus("current")
_CiscoLwappAPGroupNasIdConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAPGroupNasIdConfig = _CiscoLwappAPGroupNasIdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 6)
)
_CLAPGroupNasIdConfigTable_Object = MibTable
cLAPGroupNasIdConfigTable = _CLAPGroupNasIdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLAPGroupNasIdConfigTable.setStatus("current")
_CLAPGroupNasIdConfigEntry_Object = MibTableRow
cLAPGroupNasIdConfigEntry = _CLAPGroupNasIdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 6, 1, 1)
)
cLAPGroupNasIdConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupNasIdConfigEntry.setStatus("current")
_CLAPGroupNasId_Type = SnmpAdminString
_CLAPGroupNasId_Object = MibTableColumn
cLAPGroupNasId = _CLAPGroupNasId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 6, 1, 1, 1),
    _CLAPGroupNasId_Type()
)
cLAPGroupNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupNasId.setStatus("current")
_CiscoLwappPolicyConfig_ObjectIdentity = ObjectIdentity
ciscoLwappPolicyConfig = _CiscoLwappPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7)
)
_CLPolicyConfigTable_Object = MibTable
cLPolicyConfigTable = _CLPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLPolicyConfigTable.setStatus("current")
_CLPolicyConfigEntry_Object = MibTableRow
cLPolicyConfigEntry = _CLPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1)
)
cLPolicyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyIndex"),
)
if mibBuilder.loadTexts:
    cLPolicyConfigEntry.setStatus("current")
_CLPolicyIndex_Type = Unsigned32
_CLPolicyIndex_Object = MibTableColumn
cLPolicyIndex = _CLPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 1),
    _CLPolicyIndex_Type()
)
cLPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLPolicyIndex.setStatus("current")
_CLPolicyName_Type = SnmpAdminString
_CLPolicyName_Object = MibTableColumn
cLPolicyName = _CLPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 2),
    _CLPolicyName_Type()
)
cLPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyName.setStatus("current")
_CLPolicyRoleName_Type = SnmpAdminString
_CLPolicyRoleName_Object = MibTableColumn
cLPolicyRoleName = _CLPolicyRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 3),
    _CLPolicyRoleName_Type()
)
cLPolicyRoleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyRoleName.setStatus("current")


class _CLPolicyEapType_Type(Integer32):
    """Custom type cLPolicyEapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("leap", 2),
          ("eapFast", 3),
          ("eapTls", 4),
          ("peap", 5))
    )


_CLPolicyEapType_Type.__name__ = "Integer32"
_CLPolicyEapType_Object = MibTableColumn
cLPolicyEapType = _CLPolicyEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 4),
    _CLPolicyEapType_Type()
)
cLPolicyEapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyEapType.setStatus("current")
_CLPolicyAclName_Type = SnmpAdminString
_CLPolicyAclName_Object = MibTableColumn
cLPolicyAclName = _CLPolicyAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 5),
    _CLPolicyAclName_Type()
)
cLPolicyAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyAclName.setStatus("current")
_CLPolicyVlanId_Type = Unsigned32
_CLPolicyVlanId_Object = MibTableColumn
cLPolicyVlanId = _CLPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 6),
    _CLPolicyVlanId_Type()
)
cLPolicyVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyVlanId.setStatus("current")


class _CLPolicyQosProfile_Type(Integer32):
    """Custom type cLPolicyQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("silver", 2),
          ("gold", 3),
          ("platinum", 4),
          ("bronze", 5))
    )


_CLPolicyQosProfile_Type.__name__ = "Integer32"
_CLPolicyQosProfile_Object = MibTableColumn
cLPolicyQosProfile = _CLPolicyQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 7),
    _CLPolicyQosProfile_Type()
)
cLPolicyQosProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyQosProfile.setStatus("current")
_CLPolicySessionTimeout_Type = Unsigned32
_CLPolicySessionTimeout_Object = MibTableColumn
cLPolicySessionTimeout = _CLPolicySessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 8),
    _CLPolicySessionTimeout_Type()
)
cLPolicySessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicySessionTimeout.setStatus("current")
_CLPolicySleepTimeout_Type = Unsigned32
_CLPolicySleepTimeout_Object = MibTableColumn
cLPolicySleepTimeout = _CLPolicySleepTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 9),
    _CLPolicySleepTimeout_Type()
)
cLPolicySleepTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicySleepTimeout.setStatus("current")
_CLPolicyRowStatus_Type = RowStatus
_CLPolicyRowStatus_Object = MibTableColumn
cLPolicyRowStatus = _CLPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 10),
    _CLPolicyRowStatus_Type()
)
cLPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyRowStatus.setStatus("current")
_CLPolicyFlexAclName_Type = SnmpAdminString
_CLPolicyFlexAclName_Object = MibTableColumn
cLPolicyFlexAclName = _CLPolicyFlexAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 11),
    _CLPolicyFlexAclName_Type()
)
cLPolicyFlexAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyFlexAclName.setStatus("current")
_CLPolicyAvcProfileName_Type = SnmpAdminString
_CLPolicyAvcProfileName_Object = MibTableColumn
cLPolicyAvcProfileName = _CLPolicyAvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 12),
    _CLPolicyAvcProfileName_Type()
)
cLPolicyAvcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyAvcProfileName.setStatus("current")
_CLPolicyMdnsProfileName_Type = SnmpAdminString
_CLPolicyMdnsProfileName_Object = MibTableColumn
cLPolicyMdnsProfileName = _CLPolicyMdnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 13),
    _CLPolicyMdnsProfileName_Type()
)
cLPolicyMdnsProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyMdnsProfileName.setStatus("current")
_CLPolicyFlexVlanId_Type = Unsigned32
_CLPolicyFlexVlanId_Object = MibTableColumn
cLPolicyFlexVlanId = _CLPolicyFlexVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 14),
    _CLPolicyFlexVlanId_Type()
)
cLPolicyFlexVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyFlexVlanId.setStatus("current")
_CLPolicyUrlAclName_Type = SnmpAdminString
_CLPolicyUrlAclName_Object = MibTableColumn
cLPolicyUrlAclName = _CLPolicyUrlAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 15),
    _CLPolicyUrlAclName_Type()
)
cLPolicyUrlAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyUrlAclName.setStatus("current")
_CLPolicyOpendnsProfileName_Type = SnmpAdminString
_CLPolicyOpendnsProfileName_Object = MibTableColumn
cLPolicyOpendnsProfileName = _CLPolicyOpendnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 1, 1, 16),
    _CLPolicyOpendnsProfileName_Type()
)
cLPolicyOpendnsProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyOpendnsProfileName.setStatus("current")
_CLPolicyDeviceTable_Object = MibTable
cLPolicyDeviceTable = _CLPolicyDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cLPolicyDeviceTable.setStatus("current")
_CLPolicyDeviceEntry_Object = MibTableRow
cLPolicyDeviceEntry = _CLPolicyDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 2, 1)
)
cLPolicyDeviceEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyDeviceIndex"),
)
if mibBuilder.loadTexts:
    cLPolicyDeviceEntry.setStatus("current")
_CLPolicyDeviceIndex_Type = Unsigned32
_CLPolicyDeviceIndex_Object = MibTableColumn
cLPolicyDeviceIndex = _CLPolicyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 2, 1, 1),
    _CLPolicyDeviceIndex_Type()
)
cLPolicyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLPolicyDeviceIndex.setStatus("current")
_CLPolicyDeviceName_Type = SnmpAdminString
_CLPolicyDeviceName_Object = MibTableColumn
cLPolicyDeviceName = _CLPolicyDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 2, 1, 2),
    _CLPolicyDeviceName_Type()
)
cLPolicyDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyDeviceName.setStatus("current")
_CLPolicyDeviceRowStatus_Type = RowStatus
_CLPolicyDeviceRowStatus_Object = MibTableColumn
cLPolicyDeviceRowStatus = _CLPolicyDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 2, 1, 3),
    _CLPolicyDeviceRowStatus_Type()
)
cLPolicyDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyDeviceRowStatus.setStatus("current")
_CLPolicyActiveHoursTable_Object = MibTable
cLPolicyActiveHoursTable = _CLPolicyActiveHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cLPolicyActiveHoursTable.setStatus("current")
_CLPolicyActiveHoursEntry_Object = MibTableRow
cLPolicyActiveHoursEntry = _CLPolicyActiveHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3, 1)
)
cLPolicyActiveHoursEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyActiveDay"),
)
if mibBuilder.loadTexts:
    cLPolicyActiveHoursEntry.setStatus("current")


class _CLPolicyActiveDay_Type(Integer32):
    """Custom type cLPolicyActiveDay based on Integer32"""
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
        *(("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6),
          ("sun", 7))
    )


_CLPolicyActiveDay_Type.__name__ = "Integer32"
_CLPolicyActiveDay_Object = MibTableColumn
cLPolicyActiveDay = _CLPolicyActiveDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3, 1, 1),
    _CLPolicyActiveDay_Type()
)
cLPolicyActiveDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLPolicyActiveDay.setStatus("current")
_CLPolicyActiveStartTime_Type = TimeTicks
_CLPolicyActiveStartTime_Object = MibTableColumn
cLPolicyActiveStartTime = _CLPolicyActiveStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3, 1, 2),
    _CLPolicyActiveStartTime_Type()
)
cLPolicyActiveStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyActiveStartTime.setStatus("current")
_CLPolicyActiveEndTime_Type = TimeTicks
_CLPolicyActiveEndTime_Object = MibTableColumn
cLPolicyActiveEndTime = _CLPolicyActiveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3, 1, 3),
    _CLPolicyActiveEndTime_Type()
)
cLPolicyActiveEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyActiveEndTime.setStatus("current")
_CLPolicyActiveHoursRowStatus_Type = RowStatus
_CLPolicyActiveHoursRowStatus_Object = MibTableColumn
cLPolicyActiveHoursRowStatus = _CLPolicyActiveHoursRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 3, 1, 4),
    _CLPolicyActiveHoursRowStatus_Type()
)
cLPolicyActiveHoursRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyActiveHoursRowStatus.setStatus("current")
_CLPolicyWlanSchedulingTable_Object = MibTable
cLPolicyWlanSchedulingTable = _CLPolicyWlanSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingTable.setStatus("current")
_CLPolicyWlanSchedulingEntry_Object = MibTableRow
cLPolicyWlanSchedulingEntry = _CLPolicyWlanSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1)
)
cLPolicyWlanSchedulingEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyIndex"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLPolicyWlanSchedulingDay"),
)
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingEntry.setStatus("current")


class _CLPolicyWlanSchedulingDay_Type(Integer32):
    """Custom type cLPolicyWlanSchedulingDay based on Integer32"""
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
        *(("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6),
          ("sun", 7))
    )


_CLPolicyWlanSchedulingDay_Type.__name__ = "Integer32"
_CLPolicyWlanSchedulingDay_Object = MibTableColumn
cLPolicyWlanSchedulingDay = _CLPolicyWlanSchedulingDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1, 1),
    _CLPolicyWlanSchedulingDay_Type()
)
cLPolicyWlanSchedulingDay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingDay.setStatus("current")
_CLPolicyWlanSchedulingStatus_Type = TruthValue
_CLPolicyWlanSchedulingStatus_Object = MibTableColumn
cLPolicyWlanSchedulingStatus = _CLPolicyWlanSchedulingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1, 2),
    _CLPolicyWlanSchedulingStatus_Type()
)
cLPolicyWlanSchedulingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingStatus.setStatus("current")
_CLPolicyWlanSchedulingStartTime_Type = TimeTicks
_CLPolicyWlanSchedulingStartTime_Object = MibTableColumn
cLPolicyWlanSchedulingStartTime = _CLPolicyWlanSchedulingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1, 3),
    _CLPolicyWlanSchedulingStartTime_Type()
)
cLPolicyWlanSchedulingStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingStartTime.setStatus("current")
_CLPolicyWlanSchedulingEndTime_Type = TimeTicks
_CLPolicyWlanSchedulingEndTime_Object = MibTableColumn
cLPolicyWlanSchedulingEndTime = _CLPolicyWlanSchedulingEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1, 4),
    _CLPolicyWlanSchedulingEndTime_Type()
)
cLPolicyWlanSchedulingEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingEndTime.setStatus("current")
_CLPolicyWlanSchedulingRowStatus_Type = RowStatus
_CLPolicyWlanSchedulingRowStatus_Object = MibTableColumn
cLPolicyWlanSchedulingRowStatus = _CLPolicyWlanSchedulingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 7, 4, 1, 5),
    _CLPolicyWlanSchedulingRowStatus_Type()
)
cLPolicyWlanSchedulingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPolicyWlanSchedulingRowStatus.setStatus("current")
_CiscoLwappAPGroupsHyperlocationConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAPGroupsHyperlocationConfig = _CiscoLwappAPGroupsHyperlocationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8)
)
_CLAPGroupsHyperlocationConfigTable_Object = MibTable
cLAPGroupsHyperlocationConfigTable = _CLAPGroupsHyperlocationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cLAPGroupsHyperlocationConfigTable.setStatus("current")
_CLAPGroupsHyperlocationConfigEntry_Object = MibTableRow
cLAPGroupsHyperlocationConfigEntry = _CLAPGroupsHyperlocationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1)
)
cLAPGroupsHyperlocationConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsHyperlocationConfigEntry.setStatus("current")


class _CLAPGroupsHyperlocationEnable_Type(TruthValue):
    """Custom type cLAPGroupsHyperlocationEnable based on TruthValue"""
    defaultValue = 2


_CLAPGroupsHyperlocationEnable_Type.__name__ = "TruthValue"
_CLAPGroupsHyperlocationEnable_Object = MibTableColumn
cLAPGroupsHyperlocationEnable = _CLAPGroupsHyperlocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1, 1),
    _CLAPGroupsHyperlocationEnable_Type()
)
cLAPGroupsHyperlocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsHyperlocationEnable.setStatus("current")


class _CLAPGroupsPakRssiThreshold_Type(Integer32):
    """Custom type cLAPGroupsPakRssiThreshold based on Integer32"""
    defaultValue = -100


_CLAPGroupsPakRssiThreshold_Type.__name__ = "Integer32"
_CLAPGroupsPakRssiThreshold_Object = MibTableColumn
cLAPGroupsPakRssiThreshold = _CLAPGroupsPakRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1, 2),
    _CLAPGroupsPakRssiThreshold_Type()
)
cLAPGroupsPakRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsPakRssiThreshold.setStatus("current")


class _CLAPGroupsPakRssiThresholdTrigger_Type(Gauge32):
    """Custom type cLAPGroupsPakRssiThresholdTrigger based on Gauge32"""
    defaultValue = 10

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLAPGroupsPakRssiThresholdTrigger_Type.__name__ = "Gauge32"
_CLAPGroupsPakRssiThresholdTrigger_Object = MibTableColumn
cLAPGroupsPakRssiThresholdTrigger = _CLAPGroupsPakRssiThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1, 3),
    _CLAPGroupsPakRssiThresholdTrigger_Type()
)
cLAPGroupsPakRssiThresholdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsPakRssiThresholdTrigger.setStatus("current")
if mibBuilder.loadTexts:
    cLAPGroupsPakRssiThresholdTrigger.setUnits("dbm")
_CLAPGroupsPakRssiNtpIpAddressType_Type = InetAddressType
_CLAPGroupsPakRssiNtpIpAddressType_Object = MibTableColumn
cLAPGroupsPakRssiNtpIpAddressType = _CLAPGroupsPakRssiNtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1, 4),
    _CLAPGroupsPakRssiNtpIpAddressType_Type()
)
cLAPGroupsPakRssiNtpIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsPakRssiNtpIpAddressType.setStatus("current")
_CLAPGroupsPakRssiNtpAddress_Type = InetAddress
_CLAPGroupsPakRssiNtpAddress_Object = MibTableColumn
cLAPGroupsPakRssiNtpAddress = _CLAPGroupsPakRssiNtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 8, 1, 1, 5),
    _CLAPGroupsPakRssiNtpAddress_Type()
)
cLAPGroupsPakRssiNtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsPakRssiNtpAddress.setStatus("current")
_CiscoLwappAPGroupsPortConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAPGroupsPortConfig = _CiscoLwappAPGroupsPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9)
)
_CLAPGroupsPortConfigTable_Object = MibTable
cLAPGroupsPortConfigTable = _CLAPGroupsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cLAPGroupsPortConfigTable.setStatus("current")
_CLAPGroupsPortConfigEntry_Object = MibTableRow
cLAPGroupsPortConfigEntry = _CLAPGroupsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1)
)
cLAPGroupsPortConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupsLANPortNumber"),
)
if mibBuilder.loadTexts:
    cLAPGroupsPortConfigEntry.setStatus("current")
_CLAPGroupsLANPortNumber_Type = Unsigned32
_CLAPGroupsLANPortNumber_Object = MibTableColumn
cLAPGroupsLANPortNumber = _CLAPGroupsLANPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1, 1),
    _CLAPGroupsLANPortNumber_Type()
)
cLAPGroupsLANPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLAPGroupsLANPortNumber.setStatus("current")


class _CLAPGroupsLANPortStatus_Type(Integer32):
    """Custom type cLAPGroupsLANPortStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLAPGroupsLANPortStatus_Type.__name__ = "Integer32"
_CLAPGroupsLANPortStatus_Object = MibTableColumn
cLAPGroupsLANPortStatus = _CLAPGroupsLANPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1, 2),
    _CLAPGroupsLANPortStatus_Type()
)
cLAPGroupsLANPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsLANPortStatus.setStatus("current")


class _CLAPGroupsLANPortPoeStatus_Type(Integer32):
    """Custom type cLAPGroupsLANPortPoeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_CLAPGroupsLANPortPoeStatus_Type.__name__ = "Integer32"
_CLAPGroupsLANPortPoeStatus_Object = MibTableColumn
cLAPGroupsLANPortPoeStatus = _CLAPGroupsLANPortPoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1, 3),
    _CLAPGroupsLANPortPoeStatus_Type()
)
cLAPGroupsLANPortPoeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsLANPortPoeStatus.setStatus("current")


class _CLAPGroupsLANPortRlanName_Type(SnmpAdminString):
    """Custom type cLAPGroupsLANPortRlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAPGroupsLANPortRlanName_Type.__name__ = "SnmpAdminString"
_CLAPGroupsLANPortRlanName_Object = MibTableColumn
cLAPGroupsLANPortRlanName = _CLAPGroupsLANPortRlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1, 4),
    _CLAPGroupsLANPortRlanName_Type()
)
cLAPGroupsLANPortRlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsLANPortRlanName.setStatus("current")
_CLAPGroupsLANPortRowStatus_Type = RowStatus
_CLAPGroupsLANPortRowStatus_Object = MibTableColumn
cLAPGroupsLANPortRowStatus = _CLAPGroupsLANPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 1, 1, 5),
    _CLAPGroupsLANPortRowStatus_Type()
)
cLAPGroupsLANPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLAPGroupsLANPortRowStatus.setStatus("current")
_CLAPGroupsExtModuleConfigTable_Object = MibTable
cLAPGroupsExtModuleConfigTable = _CLAPGroupsExtModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cLAPGroupsExtModuleConfigTable.setStatus("current")
_CLAPGroupsExtModuleConfigEntry_Object = MibTableRow
cLAPGroupsExtModuleConfigEntry = _CLAPGroupsExtModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 2, 1)
)
cLAPGroupsExtModuleConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLAPGroupName"),
)
if mibBuilder.loadTexts:
    cLAPGroupsExtModuleConfigEntry.setStatus("current")


class _CLAPGroupsExtModuleStatus_Type(Integer32):
    """Custom type cLAPGroupsExtModuleStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CLAPGroupsExtModuleStatus_Type.__name__ = "Integer32"
_CLAPGroupsExtModuleStatus_Object = MibTableColumn
cLAPGroupsExtModuleStatus = _CLAPGroupsExtModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 2, 1, 1),
    _CLAPGroupsExtModuleStatus_Type()
)
cLAPGroupsExtModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsExtModuleStatus.setStatus("current")


class _CLAPGroupsExtModuleRlanName_Type(SnmpAdminString):
    """Custom type cLAPGroupsExtModuleRlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLAPGroupsExtModuleRlanName_Type.__name__ = "SnmpAdminString"
_CLAPGroupsExtModuleRlanName_Object = MibTableColumn
cLAPGroupsExtModuleRlanName = _CLAPGroupsExtModuleRlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 1, 9, 2, 1, 2),
    _CLAPGroupsExtModuleRlanName_Type()
)
cLAPGroupsExtModuleRlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPGroupsExtModuleRlanName.setStatus("current")
_CiscoLwappWlanMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappWlanMIBConform = _CiscoLwappWlanMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2)
)
_CiscoLwappWlanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWlanMIBCompliances = _CiscoLwappWlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1)
)
_CiscoLwappWlanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWlanMIBGroups = _CiscoLwappWlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2)
)

# Managed Objects groups

ciscoLwappWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 1)
)
ciscoLwappWlanConfigGroup.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlanRowStatus")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroup.setStatus("deprecated")

ciscoLwappWlanConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 2)
)
ciscoLwappWlanConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsid"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanDiagChan"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanStorageType"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup1.setStatus("current")

ciscoLwappWlanConfigClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 3)
)
ciscoLwappWlanConfigClientGroup.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientAclName")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigClientGroup.setStatus("current")

ciscoLwappWlan11uConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 4)
)
ciscoLwappWlan11uConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlan11uStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uInternetAccess"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uNetworkType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uVenueType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uVenueName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOui"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiIsBeacon"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiStorageType"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlan11uConfigGroup.setStatus("deprecated")

ciscoLwappAPGroupsVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 5)
)
ciscoLwappAPGroupsVlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanMappingInterfaceName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupNACSupport"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanConfigRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanConfigStorageType"))
)
if mibBuilder.loadTexts:
    ciscoLwappAPGroupsVlanConfigGroup.setStatus("deprecated")

ciscoLwappWlanConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 6)
)
ciscoLwappWlanConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanLoadBalancingEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanBandSelectEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanPassiveClientEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIsWired"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIngressInterface"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanNACSupport"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWepKeyChange"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanChdEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan802dot11anDTIM"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan802dot11bgnDTIM"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup2.setStatus("current")

ciscoLwappWlanConfigClientGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 7)
)
ciscoLwappWlanConfigClientGroupSup1.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlanP2PBlocking")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigClientGroupSup1.setStatus("current")

ciscoLwappWlanConfigGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 8)
)
ciscoLwappWlanConfigGroupSup3.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanReAnchorRoamedVoiceClientsEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMulticastInterfaceEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMulticastInterface"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMulticastDirectEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanNACPostureSupport"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMaxClientsAccepted"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanScanDeferPriority"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanScanDeferTime"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanLanSubType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWebAuthOnMacFilterFailureEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanStaticIpTunnelingEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup3.setStatus("current")

ciscoLwappWlan11uConfigGroupsup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 9)
)
ciscoLwappWlan11uConfigGroupsup1.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlan11uStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uInternetAccess"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uNetworkType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uHessid"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uNetworkAuthType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOui"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiIsBeacon"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uOuiStorageType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapMethod"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapAuthMethod"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapAuthParam"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapAuthRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uDomainName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uDomainRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11u3gppCountryCode"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11u3gppNetworkCode"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11u3gppRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uIpAddressAvailIpv4"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uIpAddressAvailIpv6"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlan11uConfigGroupsup1.setStatus("current")

ciscoLwappWlanServiceAdvertisementConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 10)
)
ciscoLwappWlanServiceAdvertisementConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanServiceAdvertisementStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanServiceAdvertisementMsapServerIndex"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanServiceAdvertisementConfigGroup.setStatus("current")

ciscoLwappWlanHotSpot2ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 11)
)
ciscoLwappWlanHotSpot2ConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2OperatorName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2OperatorLanguage"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2OperatorRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2PortConfigIpProtocol"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2PortConfigPortNumber"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2PortConfigStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2PortConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanHotSpot2ConfigGroup.setStatus("current")

ciscoLwappWlanIosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 12)
)
ciscoLwappWlanIosConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanIosAccountingMethodListName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosAuthenticationMethodListName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosMacFilteringMethodListName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosWebAuthMethodListName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosQosUpStreamProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosQosDownStreamProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIngressDHCPOption82Format"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIngressDHCPOption82Ascii"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIngressDHCPOption82Rid"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIngressDHCPOption82Enable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosScanDeferPriority"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosWebAuthParameterMapName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosQosClientUpStreamProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanIosQosClientDownStreamProfileName"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanIosConfigGroup.setStatus("current")

ciscoLwappWlanQosConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 13)
)
ciscoLwappWlanQosConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanClientDSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientUSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientDSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientUSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientUSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidDSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidUSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidDSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidUSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSsidUSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanDSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanUSAverageDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanDSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanUSBurstDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanDSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanUSAvgRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanDSBurstRealTimeDataRate"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWlanUSBurstRealTimeDataRate"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanQosConfigGroup.setStatus("current")

ciscoLwappWlanConfigGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 14)
)
ciscoLwappWlanConfigGroupSup4.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanKtsCacSupportEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWifiDirectPolicyStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWebAuthIPv6AclName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2Enabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMaxClientsAllowedPerRadio"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanDhcpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMacAuthOverDot1xEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanUserTimeout"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpotClearConfig"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthFourthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthFifthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthSixthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctFourthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctFifthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctSixthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSelfAnchorEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup4.setStatus("deprecated")

ciscoLwappWlan11uConfigGroupsup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 15)
)
ciscoLwappWlan11uConfigGroupsup2.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlan11uRealmEapAuthCredentialType")
)
if mibBuilder.loadTexts:
    ciscoLwappWlan11uConfigGroupsup2.setStatus("current")

ciscoLwappWlanHotSpot2ConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 16)
)
ciscoLwappWlanHotSpot2ConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2WanLinkStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2WanSymLinkStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2WanDownLinkSpeed"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2WanUpLinkSpeed"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanHotSpot2ConfigGroupSup1.setStatus("current")

ciscoLwappAPGroupsVlanConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 17)
)
ciscoLwappAPGroupsVlanConfigGroupSup1.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsWlanOrderIndex")
)
if mibBuilder.loadTexts:
    ciscoLwappAPGroupsVlanConfigGroupSup1.setStatus("current")

cLAPGroupsVenueConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 18)
)
cLAPGroupsVenueConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigVenueType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigVenueName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigLanguage"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsOperatingClass"))
)
if mibBuilder.loadTexts:
    cLAPGroupsVenueConfigGroup.setStatus("current")

cLAPGroupsMultipleVenueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 19)
)
cLAPGroupsMultipleVenueGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueRowStatus"))
)
if mibBuilder.loadTexts:
    cLAPGroupsMultipleVenueGroup.setStatus("current")

ciscoLwappWlanConfigClientGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 20)
)
ciscoLwappWlanConfigClientGroupSup2.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlanClientIPv6AclName")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigClientGroupSup2.setStatus("current")

ciscoLwappWlanConfigFlexibleNetflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 21)
)
ciscoLwappWlanConfigFlexibleNetflowGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanFlexibleNetflowMonitorName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanFlexibleNetflowRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigFlexibleNetflowGroup.setStatus("current")

ciscoLwappWlanConfigGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 22)
)
ciscoLwappWlanConfigGroupSup5.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlanKtsCacSupportEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWifiDirectPolicyStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanWebAuthIPv6AclName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpot2Enabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMaxClientsAllowedPerRadio"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanDhcpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanMacAuthOverDot1xEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanUserTimeout"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanUserIdleThreshold"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHttpDeviceProfiling"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanHotSpotClearConfig"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthFourthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthFifthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAuthSixthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctFourthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctFifthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanRadiusAcctSixthServer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanSelfAnchorEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanUniversalAdmin"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup5.setStatus("current")

ciscoLwappAPGroupsVlanConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 23)
)
ciscoLwappAPGroupsVlanConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupNACSupport"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanConfigRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanConfigStorageType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVlanMappingInterfaceNameRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappAPGroupsVlanConfigGroupSup2.setStatus("current")

ciscoLwappWlanConfigGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 24)
)
ciscoLwappWlanConfigGroupSup6.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "cLWlan11acMuMimoEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup6.setStatus("current")

ciscoLwappWlanConfigGroupSup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 25)
)
ciscoLwappWlanConfigGroupSup7.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsHyperlocationEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPakRssiThreshold"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPakRssiThresholdTrigger"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPakRssiNtpIpAddressType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPakRssiNtpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup7.setStatus("current")

ciscoLwappWlanConfigGroupSup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 26)
)
ciscoLwappWlanConfigGroupSup8.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsLANPortStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsLANPortPoeStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsLANPortRlanName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsLANPortRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsExtModuleStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsExtModuleRlanName"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanConfigGroupSup8.setStatus("current")

ciscoLwappWlan11vConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 27)
)
ciscoLwappWlan11vConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLWlan11vBssTransEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11vDisassocImmiEnable"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11vDisassocTimer"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlan11vOpRoamDisassocTimer"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlan11vConfigGroup.setStatus("current")

ciscoLwappApGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 28)
)
ciscoLwappApGroupConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLAPGroupNasId"),
        ("CISCO-LWAPP-WLAN-MIB", "cLApGroupPreferMode"),
        ("CISCO-LWAPP-WLAN-MIB", "cLApGroupGlobalWebAuthConfig"),
        ("CISCO-LWAPP-WLAN-MIB", "cLApGroupExternalWebAuthUrl"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPolicyIndex"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPolicyWlanProfile"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsPolicyRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupTrafficQinqEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupDhcpQinqEnabled"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupQinqServiceVlanId"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupConfigGroup.setStatus("current")

ciscoLwappPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 2, 29)
)
ciscoLwappPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "cLPolicyName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyRoleName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyEapType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyAclName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyVlanId"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyQosProfile"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicySessionTimeout"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicySleepTimeout"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyFlexAclName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyAvcProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyMdnsProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyFlexVlanId"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyUrlAclName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyOpendnsProfileName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyDeviceName"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyDeviceRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyActiveStartTime"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyActiveEndTime"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyActiveHoursRowStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyWlanSchedulingStatus"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyWlanSchedulingStartTime"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyWlanSchedulingEndTime"),
        ("CISCO-LWAPP-WLAN-MIB", "cLPolicyWlanSchedulingRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappPolicyConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappWlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 1)
)
ciscoLwappWlanMIBCompliance.setObjects(
    ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 2)
)
ciscoLwappWlanMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 3)
)
ciscoLwappWlanMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 4)
)
ciscoLwappWlanMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 5)
)
ciscoLwappWlanMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup4"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 6)
)
ciscoLwappWlanMIBComplianceRev5.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup4"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 7)
)
ciscoLwappWlanMIBComplianceRev6.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup4"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup2"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 8)
)
ciscoLwappWlanMIBComplianceRev7.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup4"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup6"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 9)
)
ciscoLwappWlanMIBComplianceRev8.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup4"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup6"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup7"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup8"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev8.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 10)
)
ciscoLwappWlanMIBComplianceRev9.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup5"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup6"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup7"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup8"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11vConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev9.setStatus(
        "deprecated"
    )

ciscoLwappWlanMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 512, 2, 1, 11)
)
ciscoLwappWlanMIBComplianceRev10.setObjects(
      *(("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup3"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanServiceAdvertisementConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanIosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanQosConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11uConfigGroupsup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanHotSpot2ConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup1"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsVenueConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "cLAPGroupsMultipleVenueGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigClientGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigFlexibleNetflowGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup5"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappAPGroupsVlanConfigGroupSup2"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup6"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup7"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlanConfigGroupSup8"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappWlan11vConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappApGroupConfigGroup"),
        ("CISCO-LWAPP-WLAN-MIB", "ciscoLwappPolicyConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanMIBComplianceRev10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    **{"ciscoLwappWlanMIB": ciscoLwappWlanMIB,
       "ciscoLwappWlanMIBNotifs": ciscoLwappWlanMIBNotifs,
       "ciscoLwappWlanMIBObjects": ciscoLwappWlanMIBObjects,
       "ciscoLwappWlanConfig": ciscoLwappWlanConfig,
       "cLWlanConfigTable": cLWlanConfigTable,
       "cLWlanConfigEntry": cLWlanConfigEntry,
       "cLWlanIndex": cLWlanIndex,
       "cLWlanRowStatus": cLWlanRowStatus,
       "cLWlanProfileName": cLWlanProfileName,
       "cLWlanSsid": cLWlanSsid,
       "cLWlanDiagChan": cLWlanDiagChan,
       "cLWlanStorageType": cLWlanStorageType,
       "cLWlanIsWired": cLWlanIsWired,
       "cLWlanIngressInterface": cLWlanIngressInterface,
       "cLWlanNACSupport": cLWlanNACSupport,
       "cLWlanWepKeyChange": cLWlanWepKeyChange,
       "cLWlanChdEnable": cLWlanChdEnable,
       "cLWlan802dot11anDTIM": cLWlan802dot11anDTIM,
       "cLWlan802dot11bgnDTIM": cLWlan802dot11bgnDTIM,
       "cLWlanLoadBalancingEnable": cLWlanLoadBalancingEnable,
       "cLWlanBandSelectEnable": cLWlanBandSelectEnable,
       "cLWlanPassiveClientEnable": cLWlanPassiveClientEnable,
       "cLWlanReAnchorRoamedVoiceClientsEnable": cLWlanReAnchorRoamedVoiceClientsEnable,
       "cLWlanMulticastInterfaceEnable": cLWlanMulticastInterfaceEnable,
       "cLWlanMulticastInterface": cLWlanMulticastInterface,
       "cLWlanMulticastDirectEnable": cLWlanMulticastDirectEnable,
       "cLWlanNACPostureSupport": cLWlanNACPostureSupport,
       "cLWlanMaxClientsAccepted": cLWlanMaxClientsAccepted,
       "cLWlanScanDeferPriority": cLWlanScanDeferPriority,
       "cLWlanScanDeferTime": cLWlanScanDeferTime,
       "cLWlanLanSubType": cLWlanLanSubType,
       "cLWlanWebAuthOnMacFilterFailureEnabled": cLWlanWebAuthOnMacFilterFailureEnabled,
       "cLWlanStaticIpTunnelingEnabled": cLWlanStaticIpTunnelingEnabled,
       "cLWlanKtsCacSupportEnabled": cLWlanKtsCacSupportEnabled,
       "cLWlanWifiDirectPolicyStatus": cLWlanWifiDirectPolicyStatus,
       "cLWlanWebAuthIPv6AclName": cLWlanWebAuthIPv6AclName,
       "cLWlanHotSpot2Enabled": cLWlanHotSpot2Enabled,
       "cLWlanMaxClientsAllowedPerRadio": cLWlanMaxClientsAllowedPerRadio,
       "cLWlanDhcpDeviceProfiling": cLWlanDhcpDeviceProfiling,
       "cLWlanMacAuthOverDot1xEnabled": cLWlanMacAuthOverDot1xEnabled,
       "cLWlanUserTimeout": cLWlanUserTimeout,
       "cLWlanUserIdleThreshold": cLWlanUserIdleThreshold,
       "cLWlanHttpDeviceProfiling": cLWlanHttpDeviceProfiling,
       "cLWlanHotSpotClearConfig": cLWlanHotSpotClearConfig,
       "cLWlanRadiusAuthFourthServer": cLWlanRadiusAuthFourthServer,
       "cLWlanRadiusAuthFifthServer": cLWlanRadiusAuthFifthServer,
       "cLWlanRadiusAuthSixthServer": cLWlanRadiusAuthSixthServer,
       "cLWlanRadiusAcctFourthServer": cLWlanRadiusAcctFourthServer,
       "cLWlanRadiusAcctFifthServer": cLWlanRadiusAcctFifthServer,
       "cLWlanRadiusAcctSixthServer": cLWlanRadiusAcctSixthServer,
       "cLWlanSelfAnchorEnabled": cLWlanSelfAnchorEnabled,
       "cLWlanUniversalAdmin": cLWlanUniversalAdmin,
       "cLWlan11acMuMimoEnabled": cLWlan11acMuMimoEnabled,
       "cLWlan11vDisassocImmiEnable": cLWlan11vDisassocImmiEnable,
       "cLWlan11vDisassocTimer": cLWlan11vDisassocTimer,
       "cLWlan11vOpRoamDisassocTimer": cLWlan11vOpRoamDisassocTimer,
       "cLWlan11vBssTransEnable": cLWlan11vBssTransEnable,
       "cLWlanConfigClientTable": cLWlanConfigClientTable,
       "cLWlanConfigClientEntry": cLWlanConfigClientEntry,
       "cLWlanClientAclName": cLWlanClientAclName,
       "cLWlanP2PBlocking": cLWlanP2PBlocking,
       "cLWlanClientIPv6AclName": cLWlanClientIPv6AclName,
       "cLWlanConfigQosTable": cLWlanConfigQosTable,
       "cLWlanConfigQosEntry": cLWlanConfigQosEntry,
       "cLWlanClientDSAverageDataRate": cLWlanClientDSAverageDataRate,
       "cLWlanClientUSAverageDataRate": cLWlanClientUSAverageDataRate,
       "cLWlanClientDSBurstDataRate": cLWlanClientDSBurstDataRate,
       "cLWlanClientUSBurstDataRate": cLWlanClientUSBurstDataRate,
       "cLWlanClientDSAvgRealTimeDataRate": cLWlanClientDSAvgRealTimeDataRate,
       "cLWlanClientUSAvgRealTimeDataRate": cLWlanClientUSAvgRealTimeDataRate,
       "cLWlanClientDSBurstRealTimeDataRate": cLWlanClientDSBurstRealTimeDataRate,
       "cLWlanClientUSBurstRealTimeDataRate": cLWlanClientUSBurstRealTimeDataRate,
       "cLWlanSsidDSAverageDataRate": cLWlanSsidDSAverageDataRate,
       "cLWlanSsidUSAverageDataRate": cLWlanSsidUSAverageDataRate,
       "cLWlanSsidDSBurstDataRate": cLWlanSsidDSBurstDataRate,
       "cLWlanSsidUSBurstDataRate": cLWlanSsidUSBurstDataRate,
       "cLWlanSsidDSAvgRealTimeDataRate": cLWlanSsidDSAvgRealTimeDataRate,
       "cLWlanSsidUSAvgRealTimeDataRate": cLWlanSsidUSAvgRealTimeDataRate,
       "cLWlanSsidDSBurstRealTimeDataRate": cLWlanSsidDSBurstRealTimeDataRate,
       "cLWlanSsidUSBurstRealTimeDataRate": cLWlanSsidUSBurstRealTimeDataRate,
       "cLWlanWlanDSAverageDataRate": cLWlanWlanDSAverageDataRate,
       "cLWlanWlanUSAverageDataRate": cLWlanWlanUSAverageDataRate,
       "cLWlanWlanDSBurstDataRate": cLWlanWlanDSBurstDataRate,
       "cLWlanWlanUSBurstDataRate": cLWlanWlanUSBurstDataRate,
       "cLWlanWlanDSAvgRealTimeDataRate": cLWlanWlanDSAvgRealTimeDataRate,
       "cLWlanWlanUSAvgRealTimeDataRate": cLWlanWlanUSAvgRealTimeDataRate,
       "cLWlanWlanDSBurstRealTimeDataRate": cLWlanWlanDSBurstRealTimeDataRate,
       "cLWlanWlanUSBurstRealTimeDataRate": cLWlanWlanUSBurstRealTimeDataRate,
       "cLWlanConfigIosTable": cLWlanConfigIosTable,
       "cLWlanConfigIosEntry": cLWlanConfigIosEntry,
       "cLWlanIosAccountingMethodListName": cLWlanIosAccountingMethodListName,
       "cLWlanIosAuthenticationMethodListName": cLWlanIosAuthenticationMethodListName,
       "cLWlanIosMacFilteringMethodListName": cLWlanIosMacFilteringMethodListName,
       "cLWlanIosWebAuthMethodListName": cLWlanIosWebAuthMethodListName,
       "cLWlanIosQosUpStreamProfileName": cLWlanIosQosUpStreamProfileName,
       "cLWlanIosQosDownStreamProfileName": cLWlanIosQosDownStreamProfileName,
       "cLWlanIngressDHCPOption82Format": cLWlanIngressDHCPOption82Format,
       "cLWlanIngressDHCPOption82Ascii": cLWlanIngressDHCPOption82Ascii,
       "cLWlanIngressDHCPOption82Rid": cLWlanIngressDHCPOption82Rid,
       "cLWlanIngressDHCPOption82Enable": cLWlanIngressDHCPOption82Enable,
       "cLWlanIosScanDeferPriority": cLWlanIosScanDeferPriority,
       "cLWlanIosWebAuthParameterMapName": cLWlanIosWebAuthParameterMapName,
       "cLWlanIosQosClientUpStreamProfileName": cLWlanIosQosClientUpStreamProfileName,
       "cLWlanIosQosClientDownStreamProfileName": cLWlanIosQosClientDownStreamProfileName,
       "cLWlanFlexibleNetflowTable": cLWlanFlexibleNetflowTable,
       "cLWlanFlexibleNetflowEntry": cLWlanFlexibleNetflowEntry,
       "cLWlanFlexibleNetflowPolicyTypeIndex": cLWlanFlexibleNetflowPolicyTypeIndex,
       "cLWlanFlexibleNetflowMonitorName": cLWlanFlexibleNetflowMonitorName,
       "cLWlanFlexibleNetflowRowStatus": cLWlanFlexibleNetflowRowStatus,
       "ciscoLwappAPGroupsVlanConfig": ciscoLwappAPGroupsVlanConfig,
       "cLAPGroupsVlanConfigTable": cLAPGroupsVlanConfigTable,
       "cLAPGroupsVlanConfigEntry": cLAPGroupsVlanConfigEntry,
       "cLAPGroupName": cLAPGroupName,
       "cLAPGroupsVlanMappingInterfaceName": cLAPGroupsVlanMappingInterfaceName,
       "cLAPGroupNACSupport": cLAPGroupNACSupport,
       "cLAPGroupsVlanConfigRowStatus": cLAPGroupsVlanConfigRowStatus,
       "cLAPGroupsVlanConfigStorageType": cLAPGroupsVlanConfigStorageType,
       "cLAPGroupsWlanOrderIndex": cLAPGroupsWlanOrderIndex,
       "cLAPGroupsVlanMappingInterfaceNameRev1": cLAPGroupsVlanMappingInterfaceNameRev1,
       "cLAPGroupsVenueConfigTable": cLAPGroupsVenueConfigTable,
       "cLAPGroupsVenueConfigEntry": cLAPGroupsVenueConfigEntry,
       "cLAPGroupsVenueConfigVenueGroup": cLAPGroupsVenueConfigVenueGroup,
       "cLAPGroupsVenueConfigVenueType": cLAPGroupsVenueConfigVenueType,
       "cLAPGroupsVenueConfigVenueName": cLAPGroupsVenueConfigVenueName,
       "cLAPGroupsVenueConfigLanguage": cLAPGroupsVenueConfigLanguage,
       "cLAPGroupsOperatingClass": cLAPGroupsOperatingClass,
       "cLAPGroupsMultipleVenueTable": cLAPGroupsMultipleVenueTable,
       "cLAPGroupsMultipleVenueEntry": cLAPGroupsMultipleVenueEntry,
       "cLAPGroupsMultipleVenueLanguage": cLAPGroupsMultipleVenueLanguage,
       "cLAPGroupsMultipleVenueName": cLAPGroupsMultipleVenueName,
       "cLAPGroupsMultipleVenueRowStatus": cLAPGroupsMultipleVenueRowStatus,
       "cLAPGroupsPolicyTable": cLAPGroupsPolicyTable,
       "cLAPGroupsPolicyEntry": cLAPGroupsPolicyEntry,
       "cLAPGroupsPolicyWlanId": cLAPGroupsPolicyWlanId,
       "cLAPGroupsPolicyPriIndex": cLAPGroupsPolicyPriIndex,
       "cLAPGroupsPolicyIndex": cLAPGroupsPolicyIndex,
       "cLAPGroupsPolicyWlanProfile": cLAPGroupsPolicyWlanProfile,
       "cLAPGroupsPolicyRowStatus": cLAPGroupsPolicyRowStatus,
       "cLAPGroupQinqConfigTable": cLAPGroupQinqConfigTable,
       "cLAPGroupQinqConfigEntry": cLAPGroupQinqConfigEntry,
       "cLAPGroupTrafficQinqEnabled": cLAPGroupTrafficQinqEnabled,
       "cLAPGroupDhcpQinqEnabled": cLAPGroupDhcpQinqEnabled,
       "cLAPGroupQinqServiceVlanId": cLAPGroupQinqServiceVlanId,
       "cLAPGroupConfigTable": cLAPGroupConfigTable,
       "cLAPGroupConfigEntry": cLAPGroupConfigEntry,
       "cLApGroupPreferMode": cLApGroupPreferMode,
       "cLApGroupGlobalWebAuthConfig": cLApGroupGlobalWebAuthConfig,
       "cLApGroupExternalWebAuthUrl": cLApGroupExternalWebAuthUrl,
       "ciscoLwappWlan11uConfig": ciscoLwappWlan11uConfig,
       "cLWlan11uTable": cLWlan11uTable,
       "cLWlan11uEntry": cLWlan11uEntry,
       "cLWlan11uStatus": cLWlan11uStatus,
       "cLWlan11uInternetAccess": cLWlan11uInternetAccess,
       "cLWlan11uNetworkType": cLWlan11uNetworkType,
       "cLWlan11uVenueGroup": cLWlan11uVenueGroup,
       "cLWlan11uVenueType": cLWlan11uVenueType,
       "cLWlan11uVenueName": cLWlan11uVenueName,
       "cLWlan11uHessid": cLWlan11uHessid,
       "cLWlan11uNetworkAuthType": cLWlan11uNetworkAuthType,
       "cLWlan11uIpAddressAvailIpv4": cLWlan11uIpAddressAvailIpv4,
       "cLWlan11uIpAddressAvailIpv6": cLWlan11uIpAddressAvailIpv6,
       "cLWlan11uOuiTable": cLWlan11uOuiTable,
       "cLWlan11uOuiEntry": cLWlan11uOuiEntry,
       "cLWlan11uOuiIndex": cLWlan11uOuiIndex,
       "cLWlan11uOui": cLWlan11uOui,
       "cLWlan11uOuiIsBeacon": cLWlan11uOuiIsBeacon,
       "cLWlan11uOuiRowStatus": cLWlan11uOuiRowStatus,
       "cLWlan11uOuiStorageType": cLWlan11uOuiStorageType,
       "cLWlan11uRealmTable": cLWlan11uRealmTable,
       "cLWlan11uRealmEntry": cLWlan11uRealmEntry,
       "cLWlan11uRealmIndex": cLWlan11uRealmIndex,
       "cLWlan11uRealmName": cLWlan11uRealmName,
       "cLWlan11uRealmRowStatus": cLWlan11uRealmRowStatus,
       "cLWlan11uRealmEapTable": cLWlan11uRealmEapTable,
       "cLWlan11uRealmEapEntry": cLWlan11uRealmEapEntry,
       "cLWlan11uRealmEapIndex": cLWlan11uRealmEapIndex,
       "cLWlan11uRealmEapMethod": cLWlan11uRealmEapMethod,
       "cLWlan11uRealmEapRowStatus": cLWlan11uRealmEapRowStatus,
       "cLWlan11uRealmEapAuthTable": cLWlan11uRealmEapAuthTable,
       "cLWlan11uRealmEapAuthEntry": cLWlan11uRealmEapAuthEntry,
       "cLWlan11uRealmEapAuthIndex": cLWlan11uRealmEapAuthIndex,
       "cLWlan11uRealmEapAuthMethod": cLWlan11uRealmEapAuthMethod,
       "cLWlan11uRealmEapAuthParam": cLWlan11uRealmEapAuthParam,
       "cLWlan11uRealmEapAuthCredentialType": cLWlan11uRealmEapAuthCredentialType,
       "cLWlan11uRealmEapAuthRowStatus": cLWlan11uRealmEapAuthRowStatus,
       "cLWlan11uDomainTable": cLWlan11uDomainTable,
       "cLWlan11uDomainEntry": cLWlan11uDomainEntry,
       "cLWlan11uDomainIndex": cLWlan11uDomainIndex,
       "cLWlan11uDomainName": cLWlan11uDomainName,
       "cLWlan11uDomainRowStatus": cLWlan11uDomainRowStatus,
       "cLWlan11u3gppTable": cLWlan11u3gppTable,
       "cLWlan11u3gppEntry": cLWlan11u3gppEntry,
       "cLWlan11u3gppIndex": cLWlan11u3gppIndex,
       "cLWlan11u3gppCountryCode": cLWlan11u3gppCountryCode,
       "cLWlan11u3gppNetworkCode": cLWlan11u3gppNetworkCode,
       "cLWlan11u3gppRowStatus": cLWlan11u3gppRowStatus,
       "ciscoLwappWlanServiceAdvertisementConfig": ciscoLwappWlanServiceAdvertisementConfig,
       "cLWlanServiceAdvertisementTable": cLWlanServiceAdvertisementTable,
       "cLWlanServiceAdvertisementEntry": cLWlanServiceAdvertisementEntry,
       "cLWlanServiceAdvertisementStatus": cLWlanServiceAdvertisementStatus,
       "cLWlanServiceAdvertisementMsapServerIndex": cLWlanServiceAdvertisementMsapServerIndex,
       "ciscoLwappWlanHotSpot2Config": ciscoLwappWlanHotSpot2Config,
       "cLWlanHotSpot2OperatorTable": cLWlanHotSpot2OperatorTable,
       "cLWlanHotSpot2OperatorEntry": cLWlanHotSpot2OperatorEntry,
       "cLWlanHotSpot2OperatorIndex": cLWlanHotSpot2OperatorIndex,
       "cLWlanHotSpot2OperatorName": cLWlanHotSpot2OperatorName,
       "cLWlanHotSpot2OperatorLanguage": cLWlanHotSpot2OperatorLanguage,
       "cLWlanHotSpot2OperatorRowStatus": cLWlanHotSpot2OperatorRowStatus,
       "cLWlanHotSpot2PortConfigTable": cLWlanHotSpot2PortConfigTable,
       "cLWlanHotSpot2PortConfigEntry": cLWlanHotSpot2PortConfigEntry,
       "cLWlanHotSpot2PortConfigIndex": cLWlanHotSpot2PortConfigIndex,
       "cLWlanHotSpot2PortConfigIpProtocol": cLWlanHotSpot2PortConfigIpProtocol,
       "cLWlanHotSpot2PortConfigPortNumber": cLWlanHotSpot2PortConfigPortNumber,
       "cLWlanHotSpot2PortConfigStatus": cLWlanHotSpot2PortConfigStatus,
       "cLWlanHotSpot2PortConfigRowStatus": cLWlanHotSpot2PortConfigRowStatus,
       "cLWlanHotSpot2ConfigTable": cLWlanHotSpot2ConfigTable,
       "cLWlanHotSpot2ConfigEntry": cLWlanHotSpot2ConfigEntry,
       "cLWlanHotSpot2WanLinkStatus": cLWlanHotSpot2WanLinkStatus,
       "cLWlanHotSpot2WanSymLinkStatus": cLWlanHotSpot2WanSymLinkStatus,
       "cLWlanHotSpot2WanDownLinkSpeed": cLWlanHotSpot2WanDownLinkSpeed,
       "cLWlanHotSpot2WanUpLinkSpeed": cLWlanHotSpot2WanUpLinkSpeed,
       "ciscoLwappAPGroupNasIdConfig": ciscoLwappAPGroupNasIdConfig,
       "cLAPGroupNasIdConfigTable": cLAPGroupNasIdConfigTable,
       "cLAPGroupNasIdConfigEntry": cLAPGroupNasIdConfigEntry,
       "cLAPGroupNasId": cLAPGroupNasId,
       "ciscoLwappPolicyConfig": ciscoLwappPolicyConfig,
       "cLPolicyConfigTable": cLPolicyConfigTable,
       "cLPolicyConfigEntry": cLPolicyConfigEntry,
       "cLPolicyIndex": cLPolicyIndex,
       "cLPolicyName": cLPolicyName,
       "cLPolicyRoleName": cLPolicyRoleName,
       "cLPolicyEapType": cLPolicyEapType,
       "cLPolicyAclName": cLPolicyAclName,
       "cLPolicyVlanId": cLPolicyVlanId,
       "cLPolicyQosProfile": cLPolicyQosProfile,
       "cLPolicySessionTimeout": cLPolicySessionTimeout,
       "cLPolicySleepTimeout": cLPolicySleepTimeout,
       "cLPolicyRowStatus": cLPolicyRowStatus,
       "cLPolicyFlexAclName": cLPolicyFlexAclName,
       "cLPolicyAvcProfileName": cLPolicyAvcProfileName,
       "cLPolicyMdnsProfileName": cLPolicyMdnsProfileName,
       "cLPolicyFlexVlanId": cLPolicyFlexVlanId,
       "cLPolicyUrlAclName": cLPolicyUrlAclName,
       "cLPolicyOpendnsProfileName": cLPolicyOpendnsProfileName,
       "cLPolicyDeviceTable": cLPolicyDeviceTable,
       "cLPolicyDeviceEntry": cLPolicyDeviceEntry,
       "cLPolicyDeviceIndex": cLPolicyDeviceIndex,
       "cLPolicyDeviceName": cLPolicyDeviceName,
       "cLPolicyDeviceRowStatus": cLPolicyDeviceRowStatus,
       "cLPolicyActiveHoursTable": cLPolicyActiveHoursTable,
       "cLPolicyActiveHoursEntry": cLPolicyActiveHoursEntry,
       "cLPolicyActiveDay": cLPolicyActiveDay,
       "cLPolicyActiveStartTime": cLPolicyActiveStartTime,
       "cLPolicyActiveEndTime": cLPolicyActiveEndTime,
       "cLPolicyActiveHoursRowStatus": cLPolicyActiveHoursRowStatus,
       "cLPolicyWlanSchedulingTable": cLPolicyWlanSchedulingTable,
       "cLPolicyWlanSchedulingEntry": cLPolicyWlanSchedulingEntry,
       "cLPolicyWlanSchedulingDay": cLPolicyWlanSchedulingDay,
       "cLPolicyWlanSchedulingStatus": cLPolicyWlanSchedulingStatus,
       "cLPolicyWlanSchedulingStartTime": cLPolicyWlanSchedulingStartTime,
       "cLPolicyWlanSchedulingEndTime": cLPolicyWlanSchedulingEndTime,
       "cLPolicyWlanSchedulingRowStatus": cLPolicyWlanSchedulingRowStatus,
       "ciscoLwappAPGroupsHyperlocationConfig": ciscoLwappAPGroupsHyperlocationConfig,
       "cLAPGroupsHyperlocationConfigTable": cLAPGroupsHyperlocationConfigTable,
       "cLAPGroupsHyperlocationConfigEntry": cLAPGroupsHyperlocationConfigEntry,
       "cLAPGroupsHyperlocationEnable": cLAPGroupsHyperlocationEnable,
       "cLAPGroupsPakRssiThreshold": cLAPGroupsPakRssiThreshold,
       "cLAPGroupsPakRssiThresholdTrigger": cLAPGroupsPakRssiThresholdTrigger,
       "cLAPGroupsPakRssiNtpIpAddressType": cLAPGroupsPakRssiNtpIpAddressType,
       "cLAPGroupsPakRssiNtpAddress": cLAPGroupsPakRssiNtpAddress,
       "ciscoLwappAPGroupsPortConfig": ciscoLwappAPGroupsPortConfig,
       "cLAPGroupsPortConfigTable": cLAPGroupsPortConfigTable,
       "cLAPGroupsPortConfigEntry": cLAPGroupsPortConfigEntry,
       "cLAPGroupsLANPortNumber": cLAPGroupsLANPortNumber,
       "cLAPGroupsLANPortStatus": cLAPGroupsLANPortStatus,
       "cLAPGroupsLANPortPoeStatus": cLAPGroupsLANPortPoeStatus,
       "cLAPGroupsLANPortRlanName": cLAPGroupsLANPortRlanName,
       "cLAPGroupsLANPortRowStatus": cLAPGroupsLANPortRowStatus,
       "cLAPGroupsExtModuleConfigTable": cLAPGroupsExtModuleConfigTable,
       "cLAPGroupsExtModuleConfigEntry": cLAPGroupsExtModuleConfigEntry,
       "cLAPGroupsExtModuleStatus": cLAPGroupsExtModuleStatus,
       "cLAPGroupsExtModuleRlanName": cLAPGroupsExtModuleRlanName,
       "ciscoLwappWlanMIBConform": ciscoLwappWlanMIBConform,
       "ciscoLwappWlanMIBCompliances": ciscoLwappWlanMIBCompliances,
       "ciscoLwappWlanMIBCompliance": ciscoLwappWlanMIBCompliance,
       "ciscoLwappWlanMIBComplianceRev1": ciscoLwappWlanMIBComplianceRev1,
       "ciscoLwappWlanMIBComplianceRev2": ciscoLwappWlanMIBComplianceRev2,
       "ciscoLwappWlanMIBComplianceRev3": ciscoLwappWlanMIBComplianceRev3,
       "ciscoLwappWlanMIBComplianceRev4": ciscoLwappWlanMIBComplianceRev4,
       "ciscoLwappWlanMIBComplianceRev5": ciscoLwappWlanMIBComplianceRev5,
       "ciscoLwappWlanMIBComplianceRev6": ciscoLwappWlanMIBComplianceRev6,
       "ciscoLwappWlanMIBComplianceRev7": ciscoLwappWlanMIBComplianceRev7,
       "ciscoLwappWlanMIBComplianceRev8": ciscoLwappWlanMIBComplianceRev8,
       "ciscoLwappWlanMIBComplianceRev9": ciscoLwappWlanMIBComplianceRev9,
       "ciscoLwappWlanMIBComplianceRev10": ciscoLwappWlanMIBComplianceRev10,
       "ciscoLwappWlanMIBGroups": ciscoLwappWlanMIBGroups,
       "ciscoLwappWlanConfigGroup": ciscoLwappWlanConfigGroup,
       "ciscoLwappWlanConfigGroupSup1": ciscoLwappWlanConfigGroupSup1,
       "ciscoLwappWlanConfigClientGroup": ciscoLwappWlanConfigClientGroup,
       "ciscoLwappWlan11uConfigGroup": ciscoLwappWlan11uConfigGroup,
       "ciscoLwappAPGroupsVlanConfigGroup": ciscoLwappAPGroupsVlanConfigGroup,
       "ciscoLwappWlanConfigGroupSup2": ciscoLwappWlanConfigGroupSup2,
       "ciscoLwappWlanConfigClientGroupSup1": ciscoLwappWlanConfigClientGroupSup1,
       "ciscoLwappWlanConfigGroupSup3": ciscoLwappWlanConfigGroupSup3,
       "ciscoLwappWlan11uConfigGroupsup1": ciscoLwappWlan11uConfigGroupsup1,
       "ciscoLwappWlanServiceAdvertisementConfigGroup": ciscoLwappWlanServiceAdvertisementConfigGroup,
       "ciscoLwappWlanHotSpot2ConfigGroup": ciscoLwappWlanHotSpot2ConfigGroup,
       "ciscoLwappWlanIosConfigGroup": ciscoLwappWlanIosConfigGroup,
       "ciscoLwappWlanQosConfigGroup": ciscoLwappWlanQosConfigGroup,
       "ciscoLwappWlanConfigGroupSup4": ciscoLwappWlanConfigGroupSup4,
       "ciscoLwappWlan11uConfigGroupsup2": ciscoLwappWlan11uConfigGroupsup2,
       "ciscoLwappWlanHotSpot2ConfigGroupSup1": ciscoLwappWlanHotSpot2ConfigGroupSup1,
       "ciscoLwappAPGroupsVlanConfigGroupSup1": ciscoLwappAPGroupsVlanConfigGroupSup1,
       "cLAPGroupsVenueConfigGroup": cLAPGroupsVenueConfigGroup,
       "cLAPGroupsMultipleVenueGroup": cLAPGroupsMultipleVenueGroup,
       "ciscoLwappWlanConfigClientGroupSup2": ciscoLwappWlanConfigClientGroupSup2,
       "ciscoLwappWlanConfigFlexibleNetflowGroup": ciscoLwappWlanConfigFlexibleNetflowGroup,
       "ciscoLwappWlanConfigGroupSup5": ciscoLwappWlanConfigGroupSup5,
       "ciscoLwappAPGroupsVlanConfigGroupSup2": ciscoLwappAPGroupsVlanConfigGroupSup2,
       "ciscoLwappWlanConfigGroupSup6": ciscoLwappWlanConfigGroupSup6,
       "ciscoLwappWlanConfigGroupSup7": ciscoLwappWlanConfigGroupSup7,
       "ciscoLwappWlanConfigGroupSup8": ciscoLwappWlanConfigGroupSup8,
       "ciscoLwappWlan11vConfigGroup": ciscoLwappWlan11vConfigGroup,
       "ciscoLwappApGroupConfigGroup": ciscoLwappApGroupConfigGroup,
       "ciscoLwappPolicyConfigGroup": ciscoLwappPolicyConfigGroup}
)
