# SNMP MIB module (TN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MGMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:42 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 enterprises,
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
    "enterprises",
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

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")

(CpsConnector,
 TNEthPhyMode,
 TNEthernetAutoCross,
 TNEthernetDuplex,
 TNEthernetSpeed,
 TNLoopbackModeCapBits,
 TNLoopbackModes) = mibBuilder.importSymbols(
    "TRANSITION-TC",
    "CpsConnector",
    "TNEthPhyMode",
    "TNEthernetAutoCross",
    "TNEthernetDuplex",
    "TNEthernetSpeed",
    "TNLoopbackModeCapBits",
    "TNLoopbackModes")


# MODULE-IDENTITY

tnMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tnMgmtMIB.setRevisions(
        ("2009-01-08 00:00",
         "2010-07-15 00:00",
         "2010-09-02 00:00",
         "2012-09-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnMgmtNotifications_ObjectIdentity = ObjectIdentity
tnMgmtNotifications = _TnMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0)
)
_TnMgmtObjects_ObjectIdentity = ObjectIdentity
tnMgmtObjects = _TnMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1)
)
_TnDevMgmt_ObjectIdentity = ObjectIdentity
tnDevMgmt = _TnDevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1)
)
_TnDevSysMgmt_ObjectIdentity = ObjectIdentity
tnDevSysMgmt = _TnDevSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1)
)
_TnDevSysCfgTable_Object = MibTable
tnDevSysCfgTable = _TnDevSysCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnDevSysCfgTable.setStatus("current")
_TnDevSysCfgEntry_Object = MibTableRow
tnDevSysCfgEntry = _TnDevSysCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1)
)
tnDevSysCfgEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysCfgEntry.setStatus("current")


class _TnDevSysName_Type(OctetString):
    """Custom type tnDevSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnDevSysName_Type.__name__ = "OctetString"
_TnDevSysName_Object = MibTableColumn
tnDevSysName = _TnDevSysName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 1),
    _TnDevSysName_Type()
)
tnDevSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysName.setStatus("current")
_TnDevSysUptime_Type = TimeTicks
_TnDevSysUptime_Object = MibTableColumn
tnDevSysUptime = _TnDevSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 2),
    _TnDevSysUptime_Type()
)
tnDevSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysUptime.setStatus("current")


class _TnDevSysUptimeReset_Type(Integer32):
    """Custom type tnDevSysUptimeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("doNothing", 2))
    )


_TnDevSysUptimeReset_Type.__name__ = "Integer32"
_TnDevSysUptimeReset_Object = MibTableColumn
tnDevSysUptimeReset = _TnDevSysUptimeReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 3),
    _TnDevSysUptimeReset_Type()
)
tnDevSysUptimeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysUptimeReset.setStatus("current")


class _TnDevSysReset_Type(Integer32):
    """Custom type tnDevSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("coldStart", 2),
          ("warmStart", 3))
    )


_TnDevSysReset_Type.__name__ = "Integer32"
_TnDevSysReset_Object = MibTableColumn
tnDevSysReset = _TnDevSysReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 4),
    _TnDevSysReset_Type()
)
tnDevSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSysReset.setStatus("current")
_TnDevNumOfPorts_Type = Integer32
_TnDevNumOfPorts_Object = MibTableColumn
tnDevNumOfPorts = _TnDevNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 5),
    _TnDevNumOfPorts_Type()
)
tnDevNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevNumOfPorts.setStatus("current")


class _TnDevClearCounters_Type(Integer32):
    """Custom type tnDevClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perform", 1),
          ("doNothing", 2))
    )


_TnDevClearCounters_Type.__name__ = "Integer32"
_TnDevClearCounters_Object = MibTableColumn
tnDevClearCounters = _TnDevClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 6),
    _TnDevClearCounters_Type()
)
tnDevClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevClearCounters.setStatus("current")


class _TnDevResetToFactoryConfig_Type(Integer32):
    """Custom type tnDevResetToFactoryConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perform", 1),
          ("doNothing", 2))
    )


_TnDevResetToFactoryConfig_Type.__name__ = "Integer32"
_TnDevResetToFactoryConfig_Object = MibTableColumn
tnDevResetToFactoryConfig = _TnDevResetToFactoryConfig_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 7),
    _TnDevResetToFactoryConfig_Type()
)
tnDevResetToFactoryConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevResetToFactoryConfig.setStatus("current")


class _TnDevConfigurationMode_Type(Integer32):
    """Custom type tnDevConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("software", 1),
          ("hardware", 2))
    )


_TnDevConfigurationMode_Type.__name__ = "Integer32"
_TnDevConfigurationMode_Object = MibTableColumn
tnDevConfigurationMode = _TnDevConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 8),
    _TnDevConfigurationMode_Type()
)
tnDevConfigurationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevConfigurationMode.setStatus("current")


class _TnDevConsoleAccess_Type(Integer32):
    """Custom type tnDevConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnDevConsoleAccess_Type.__name__ = "Integer32"
_TnDevConsoleAccess_Object = MibTableColumn
tnDevConsoleAccess = _TnDevConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 9),
    _TnDevConsoleAccess_Type()
)
tnDevConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevConsoleAccess.setStatus("current")


class _TnDevSharedPortMode_Type(Integer32):
    """Custom type tnDevSharedPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TnDevSharedPortMode_Type.__name__ = "Integer32"
_TnDevSharedPortMode_Object = MibTableColumn
tnDevSharedPortMode = _TnDevSharedPortMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 1, 1, 10),
    _TnDevSharedPortMode_Type()
)
tnDevSharedPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDevSharedPortMode.setStatus("current")
_TnDevSysHwInforTable_Object = MibTable
tnDevSysHwInforTable = _TnDevSysHwInforTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnDevSysHwInforTable.setStatus("current")
_TnDevSysHwInforEntry_Object = MibTableRow
tnDevSysHwInforEntry = _TnDevSysHwInforEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1)
)
tnDevSysHwInforEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysHwInforEntry.setStatus("current")
_TnDevSysHwInforChipID_Type = Integer32
_TnDevSysHwInforChipID_Object = MibTableColumn
tnDevSysHwInforChipID = _TnDevSysHwInforChipID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1, 1),
    _TnDevSysHwInforChipID_Type()
)
tnDevSysHwInforChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysHwInforChipID.setStatus("current")


class _TnDevSysHwInforBoardRev_Type(OctetString):
    """Custom type tnDevSysHwInforBoardRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnDevSysHwInforBoardRev_Type.__name__ = "OctetString"
_TnDevSysHwInforBoardRev_Object = MibTableColumn
tnDevSysHwInforBoardRev = _TnDevSysHwInforBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1, 2),
    _TnDevSysHwInforBoardRev_Type()
)
tnDevSysHwInforBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysHwInforBoardRev.setStatus("current")


class _TnDevSysHwInforFPGAVer_Type(OctetString):
    """Custom type tnDevSysHwInforFPGAVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnDevSysHwInforFPGAVer_Type.__name__ = "OctetString"
_TnDevSysHwInforFPGAVer_Object = MibTableColumn
tnDevSysHwInforFPGAVer = _TnDevSysHwInforFPGAVer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1, 3),
    _TnDevSysHwInforFPGAVer_Type()
)
tnDevSysHwInforFPGAVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysHwInforFPGAVer.setStatus("current")
_TnDevSysHwInforBoardtmp_Type = Integer32
_TnDevSysHwInforBoardtmp_Object = MibTableColumn
tnDevSysHwInforBoardtmp = _TnDevSysHwInforBoardtmp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1, 4),
    _TnDevSysHwInforBoardtmp_Type()
)
tnDevSysHwInforBoardtmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysHwInforBoardtmp.setStatus("current")
_TnDevSysHwInforCPUtmp_Type = Integer32
_TnDevSysHwInforCPUtmp_Object = MibTableColumn
tnDevSysHwInforCPUtmp = _TnDevSysHwInforCPUtmp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 1, 2, 1, 5),
    _TnDevSysHwInforCPUtmp_Type()
)
tnDevSysHwInforCPUtmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDevSysHwInforCPUtmp.setStatus("current")
_TnDevSysLPT_ObjectIdentity = ObjectIdentity
tnDevSysLPT = _TnDevSysLPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2)
)
_TnDevSysLPTTable_Object = MibTable
tnDevSysLPTTable = _TnDevSysLPTTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnDevSysLPTTable.setStatus("current")
_TnDevSysLPTEntry_Object = MibTableRow
tnDevSysLPTEntry = _TnDevSysLPTEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1)
)
tnDevSysLPTEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysLPTEntry.setStatus("current")


class _TnSysLinkPassThro_Type(Integer32):
    """Custom type tnSysLinkPassThro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnSysLinkPassThro_Type.__name__ = "Integer32"
_TnSysLinkPassThro_Object = MibTableColumn
tnSysLinkPassThro = _TnSysLinkPassThro_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1, 1),
    _TnSysLinkPassThro_Type()
)
tnSysLinkPassThro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinkPassThro.setStatus("current")


class _TnSysTransparentLPT_Type(Integer32):
    """Custom type tnSysTransparentLPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnSysTransparentLPT_Type.__name__ = "Integer32"
_TnSysTransparentLPT_Object = MibTableColumn
tnSysTransparentLPT = _TnSysTransparentLPT_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1, 2),
    _TnSysTransparentLPT_Type()
)
tnSysTransparentLPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransparentLPT.setStatus("current")


class _TnSysSelectiveLPT_Type(Integer32):
    """Custom type tnSysSelectiveLPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnSysSelectiveLPT_Type.__name__ = "Integer32"
_TnSysSelectiveLPT_Object = MibTableColumn
tnSysSelectiveLPT = _TnSysSelectiveLPT_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1, 3),
    _TnSysSelectiveLPT_Type()
)
tnSysSelectiveLPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSelectiveLPT.setStatus("current")
_TnSysLPTMonitorPort_Type = InterfaceIndexOrZero
_TnSysLPTMonitorPort_Object = MibTableColumn
tnSysLPTMonitorPort = _TnSysLPTMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1, 4),
    _TnSysLPTMonitorPort_Type()
)
tnSysLPTMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLPTMonitorPort.setStatus("current")


class _TnSysRemoteFaultDetect_Type(Integer32):
    """Custom type tnSysRemoteFaultDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnSysRemoteFaultDetect_Type.__name__ = "Integer32"
_TnSysRemoteFaultDetect_Object = MibTableColumn
tnSysRemoteFaultDetect = _TnSysRemoteFaultDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 2, 1, 1, 5),
    _TnSysRemoteFaultDetect_Type()
)
tnSysRemoteFaultDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRemoteFaultDetect.setStatus("current")
_TnDevSysDyingGasp_ObjectIdentity = ObjectIdentity
tnDevSysDyingGasp = _TnDevSysDyingGasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 3)
)
_TnDevSysDyingGaspTable_Object = MibTable
tnDevSysDyingGaspTable = _TnDevSysDyingGaspTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnDevSysDyingGaspTable.setStatus("current")
_TnDevSysDyingGaspEntry_Object = MibTableRow
tnDevSysDyingGaspEntry = _TnDevSysDyingGaspEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 3, 1, 1)
)
tnDevSysDyingGaspEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysDyingGaspEntry.setStatus("current")


class _TnSysDyingGaspTrap_Type(Integer32):
    """Custom type tnSysDyingGaspTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnSysDyingGaspTrap_Type.__name__ = "Integer32"
_TnSysDyingGaspTrap_Object = MibTableColumn
tnSysDyingGaspTrap = _TnSysDyingGaspTrap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 3, 1, 1, 1),
    _TnSysDyingGaspTrap_Type()
)
tnSysDyingGaspTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDyingGaspTrap.setStatus("current")
_TnDevSysMACLearning_ObjectIdentity = ObjectIdentity
tnDevSysMACLearning = _TnDevSysMACLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 4)
)
_TnDevSysMacLearningTable_Object = MibTable
tnDevSysMacLearningTable = _TnDevSysMacLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnDevSysMacLearningTable.setStatus("current")
_TnDevSysMacLearningEntry_Object = MibTableRow
tnDevSysMacLearningEntry = _TnDevSysMacLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 4, 1, 1)
)
tnDevSysMacLearningEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDevSysMacLearningEntry.setStatus("current")
_TnSysPortMacLearningState_Type = PortList
_TnSysPortMacLearningState_Object = MibTableColumn
tnSysPortMacLearningState = _TnSysPortMacLearningState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 4, 1, 1, 1),
    _TnSysPortMacLearningState_Type()
)
tnSysPortMacLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPortMacLearningState.setStatus("current")
_TnInterfaceMgmt_ObjectIdentity = ObjectIdentity
tnInterfaceMgmt = _TnInterfaceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2)
)
_TnEthInterfaceTable_Object = MibTable
tnEthInterfaceTable = _TnEthInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEthInterfaceTable.setStatus("current")
_TnEthInterfaceEntry_Object = MibTableRow
tnEthInterfaceEntry = _TnEthInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1)
)
tnEthInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnEthInterfaceEntry.setStatus("current")
_TnEthInterfaceSpeed_Type = TNEthernetSpeed
_TnEthInterfaceSpeed_Object = MibTableColumn
tnEthInterfaceSpeed = _TnEthInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 1),
    _TnEthInterfaceSpeed_Type()
)
tnEthInterfaceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthInterfaceSpeed.setStatus("current")
_TnEthInterfaceDuplex_Type = TNEthernetDuplex
_TnEthInterfaceDuplex_Object = MibTableColumn
tnEthInterfaceDuplex = _TnEthInterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 2),
    _TnEthInterfaceDuplex_Type()
)
tnEthInterfaceDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthInterfaceDuplex.setStatus("current")
_TnEthAutoCrossCap_Type = TruthValue
_TnEthAutoCrossCap_Object = MibTableColumn
tnEthAutoCrossCap = _TnEthAutoCrossCap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 3),
    _TnEthAutoCrossCap_Type()
)
tnEthAutoCrossCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthAutoCrossCap.setStatus("current")
_TnEthAutoCrossMode_Type = TNEthernetAutoCross
_TnEthAutoCrossMode_Object = MibTableColumn
tnEthAutoCrossMode = _TnEthAutoCrossMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 4),
    _TnEthAutoCrossMode_Type()
)
tnEthAutoCrossMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthAutoCrossMode.setStatus("current")
_TnEthFarEndFaultCap_Type = TruthValue
_TnEthFarEndFaultCap_Object = MibTableColumn
tnEthFarEndFaultCap = _TnEthFarEndFaultCap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 5),
    _TnEthFarEndFaultCap_Type()
)
tnEthFarEndFaultCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthFarEndFaultCap.setStatus("current")


class _TnEthFarEndFaultMode_Type(Integer32):
    """Custom type tnEthFarEndFaultMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnEthFarEndFaultMode_Type.__name__ = "Integer32"
_TnEthFarEndFaultMode_Object = MibTableColumn
tnEthFarEndFaultMode = _TnEthFarEndFaultMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 6),
    _TnEthFarEndFaultMode_Type()
)
tnEthFarEndFaultMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthFarEndFaultMode.setStatus("current")
_TnEthPhyModeChangeCap_Type = TruthValue
_TnEthPhyModeChangeCap_Object = MibTableColumn
tnEthPhyModeChangeCap = _TnEthPhyModeChangeCap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 7),
    _TnEthPhyModeChangeCap_Type()
)
tnEthPhyModeChangeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPhyModeChangeCap.setStatus("current")
_TnEthPhyOperMode_Type = TNEthPhyMode
_TnEthPhyOperMode_Object = MibTableColumn
tnEthPhyOperMode = _TnEthPhyOperMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 8),
    _TnEthPhyOperMode_Type()
)
tnEthPhyOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthPhyOperMode.setStatus("current")
_TnEthPhyMode_Type = TNEthPhyMode
_TnEthPhyMode_Object = MibTableColumn
tnEthPhyMode = _TnEthPhyMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 9),
    _TnEthPhyMode_Type()
)
tnEthPhyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthPhyMode.setStatus("current")
_TnEthMaxFrameSize_Type = Integer32
_TnEthMaxFrameSize_Object = MibTableColumn
tnEthMaxFrameSize = _TnEthMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 1, 1, 10),
    _TnEthMaxFrameSize_Type()
)
tnEthMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthMaxFrameSize.setStatus("current")
_TnDMIInfoTable_Object = MibTable
tnDMIInfoTable = _TnDMIInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnDMIInfoTable.setStatus("current")
_TnDMIInfoEntry_Object = MibTableRow
tnDMIInfoEntry = _TnDMIInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1)
)
tnDMIInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnDMIInfoEntry.setStatus("current")
_TnDMIConnectorType_Type = Integer32
_TnDMIConnectorType_Object = MibTableColumn
tnDMIConnectorType = _TnDMIConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 1),
    _TnDMIConnectorType_Type()
)
tnDMIConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIConnectorType.setStatus("current")
_TnDMIBitRate_Type = Integer32
_TnDMIBitRate_Object = MibTableColumn
tnDMIBitRate = _TnDMIBitRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 2),
    _TnDMIBitRate_Type()
)
tnDMIBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIBitRate.setStatus("current")
_TnDMILenFor9x125umKM_Type = Integer32
_TnDMILenFor9x125umKM_Object = MibTableColumn
tnDMILenFor9x125umKM = _TnDMILenFor9x125umKM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 3),
    _TnDMILenFor9x125umKM_Type()
)
tnDMILenFor9x125umKM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILenFor9x125umKM.setStatus("current")
_TnDMILenFor9x125um100M_Type = Integer32
_TnDMILenFor9x125um100M_Object = MibTableColumn
tnDMILenFor9x125um100M = _TnDMILenFor9x125um100M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 4),
    _TnDMILenFor9x125um100M_Type()
)
tnDMILenFor9x125um100M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILenFor9x125um100M.setStatus("current")
_TnDMILenFor50x125um10M_Type = Integer32
_TnDMILenFor50x125um10M_Object = MibTableColumn
tnDMILenFor50x125um10M = _TnDMILenFor50x125um10M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 5),
    _TnDMILenFor50x125um10M_Type()
)
tnDMILenFor50x125um10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILenFor50x125um10M.setStatus("current")
_TnDMILenFor625x125um10M_Type = Integer32
_TnDMILenFor625x125um10M_Object = MibTableColumn
tnDMILenFor625x125um10M = _TnDMILenFor625x125um10M_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 6),
    _TnDMILenFor625x125um10M_Type()
)
tnDMILenFor625x125um10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILenFor625x125um10M.setStatus("current")
_TnDMILenForCopper_Type = Integer32
_TnDMILenForCopper_Object = MibTableColumn
tnDMILenForCopper = _TnDMILenForCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 7),
    _TnDMILenForCopper_Type()
)
tnDMILenForCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILenForCopper.setStatus("current")
_TnDMIId_Type = Integer32
_TnDMIId_Object = MibTableColumn
tnDMIId = _TnDMIId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 8),
    _TnDMIId_Type()
)
tnDMIId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIId.setStatus("current")
_TnDMILaserWavelength_Type = Integer32
_TnDMILaserWavelength_Object = MibTableColumn
tnDMILaserWavelength = _TnDMILaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 9),
    _TnDMILaserWavelength_Type()
)
tnDMILaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMILaserWavelength.setStatus("current")
_TnDMITemperature_Type = Integer32
_TnDMITemperature_Object = MibTableColumn
tnDMITemperature = _TnDMITemperature_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 10),
    _TnDMITemperature_Type()
)
tnDMITemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITemperature.setStatus("current")
_TnDMITempAlarm_Type = Integer32
_TnDMITempAlarm_Object = MibTableColumn
tnDMITempAlarm = _TnDMITempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 11),
    _TnDMITempAlarm_Type()
)
tnDMITempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITempAlarm.setStatus("current")
_TnDMITxBiasCurrent_Type = Integer32
_TnDMITxBiasCurrent_Object = MibTableColumn
tnDMITxBiasCurrent = _TnDMITxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 12),
    _TnDMITxBiasCurrent_Type()
)
tnDMITxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITxBiasCurrent.setStatus("current")


class _TnDMITxBiasAlarm_Type(Integer32):
    """Custom type tnDMITxBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notSupported", 2),
          ("lowWarn", 3),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("highAlarm", 7))
    )


_TnDMITxBiasAlarm_Type.__name__ = "Integer32"
_TnDMITxBiasAlarm_Object = MibTableColumn
tnDMITxBiasAlarm = _TnDMITxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 13),
    _TnDMITxBiasAlarm_Type()
)
tnDMITxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITxBiasAlarm.setStatus("current")
_TnDMITxPowerLevel_Type = Integer32
_TnDMITxPowerLevel_Object = MibTableColumn
tnDMITxPowerLevel = _TnDMITxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 14),
    _TnDMITxPowerLevel_Type()
)
tnDMITxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITxPowerLevel.setStatus("current")


class _TnDMITxPowerAlarm_Type(Integer32):
    """Custom type tnDMITxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notSupported", 2),
          ("lowWarn", 3),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("highAlarm", 7))
    )


_TnDMITxPowerAlarm_Type.__name__ = "Integer32"
_TnDMITxPowerAlarm_Object = MibTableColumn
tnDMITxPowerAlarm = _TnDMITxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 15),
    _TnDMITxPowerAlarm_Type()
)
tnDMITxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMITxPowerAlarm.setStatus("current")
_TnDMIRxPowerLevel_Type = Integer32
_TnDMIRxPowerLevel_Object = MibTableColumn
tnDMIRxPowerLevel = _TnDMIRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 16),
    _TnDMIRxPowerLevel_Type()
)
tnDMIRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIRxPowerLevel.setStatus("current")


class _TnDMIRxPowerAlarm_Type(Integer32):
    """Custom type tnDMIRxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("notSupported", 2),
          ("lowWarn", 3),
          ("highWarn", 4),
          ("lowAlarm", 6),
          ("highAlarm", 7))
    )


_TnDMIRxPowerAlarm_Type.__name__ = "Integer32"
_TnDMIRxPowerAlarm_Object = MibTableColumn
tnDMIRxPowerAlarm = _TnDMIRxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 17),
    _TnDMIRxPowerAlarm_Type()
)
tnDMIRxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIRxPowerAlarm.setStatus("current")


class _TnDMIRxPwrLvlPreset_Type(Integer32):
    """Custom type tnDMIRxPwrLvlPreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnDMIRxPwrLvlPreset_Type.__name__ = "Integer32"
_TnDMIRxPwrLvlPreset_Object = MibTableColumn
tnDMIRxPwrLvlPreset = _TnDMIRxPwrLvlPreset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 18),
    _TnDMIRxPwrLvlPreset_Type()
)
tnDMIRxPwrLvlPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDMIRxPwrLvlPreset.setStatus("current")


class _TnDMIVendorName_Type(OctetString):
    """Custom type tnDMIVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDMIVendorName_Type.__name__ = "OctetString"
_TnDMIVendorName_Object = MibTableColumn
tnDMIVendorName = _TnDMIVendorName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 19),
    _TnDMIVendorName_Type()
)
tnDMIVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIVendorName.setStatus("current")


class _TnDMIVendorOUI_Type(OctetString):
    """Custom type tnDMIVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_TnDMIVendorOUI_Type.__name__ = "OctetString"
_TnDMIVendorOUI_Object = MibTableColumn
tnDMIVendorOUI = _TnDMIVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 20),
    _TnDMIVendorOUI_Type()
)
tnDMIVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIVendorOUI.setStatus("current")


class _TnDMIVendorPartNo_Type(OctetString):
    """Custom type tnDMIVendorPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDMIVendorPartNo_Type.__name__ = "OctetString"
_TnDMIVendorPartNo_Object = MibTableColumn
tnDMIVendorPartNo = _TnDMIVendorPartNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 21),
    _TnDMIVendorPartNo_Type()
)
tnDMIVendorPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIVendorPartNo.setStatus("current")


class _TnDMIVendorRevision_Type(OctetString):
    """Custom type tnDMIVendorRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_TnDMIVendorRevision_Type.__name__ = "OctetString"
_TnDMIVendorRevision_Object = MibTableColumn
tnDMIVendorRevision = _TnDMIVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 22),
    _TnDMIVendorRevision_Type()
)
tnDMIVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIVendorRevision.setStatus("current")


class _TnDMIVendorSerialNo_Type(OctetString):
    """Custom type tnDMIVendorSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnDMIVendorSerialNo_Type.__name__ = "OctetString"
_TnDMIVendorSerialNo_Object = MibTableColumn
tnDMIVendorSerialNo = _TnDMIVendorSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 2, 1, 23),
    _TnDMIVendorSerialNo_Type()
)
tnDMIVendorSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDMIVendorSerialNo.setStatus("current")
_TnIfBWAllocTable_Object = MibTable
tnIfBWAllocTable = _TnIfBWAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnIfBWAllocTable.setStatus("current")
_TnIfBWAllocEntry_Object = MibTableRow
tnIfBWAllocEntry = _TnIfBWAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 3, 1)
)
tnIfBWAllocEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfBWAllocEntry.setStatus("current")


class _TnIfBWAllocType_Type(Integer32):
    """Custom type tnIfBWAllocType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("countAllLayer1", 1),
          ("countAllLayer2", 2),
          ("countAllLayer3", 3))
    )


_TnIfBWAllocType_Type.__name__ = "Integer32"
_TnIfBWAllocType_Object = MibTableColumn
tnIfBWAllocType = _TnIfBWAllocType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 3, 1, 1),
    _TnIfBWAllocType_Type()
)
tnIfBWAllocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfBWAllocType.setStatus("current")


class _TnIfIngressRateLimit_Type(Integer32):
    """Custom type tnIfIngressRateLimit based on Integer32"""
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
              54)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate64K", 2),
          ("rate128K", 3),
          ("rate192K", 4),
          ("rate256K", 5),
          ("rate320K", 6),
          ("rate384K", 7),
          ("rate512K", 8),
          ("rate768K", 9),
          ("rate1M", 10),
          ("rate2M", 11),
          ("rate3M", 12),
          ("rate4M", 13),
          ("rate6M", 14),
          ("rate8M", 15),
          ("rate10M", 16),
          ("rate20M", 17),
          ("rate30M", 18),
          ("rate40M", 19),
          ("rate50M", 20),
          ("rate60M", 21),
          ("rate70M", 22),
          ("rate80M", 23),
          ("rate100M", 24),
          ("rate200M", 25),
          ("rate300M", 26),
          ("rate400M", 27),
          ("rate500M", 28),
          ("rate600M", 29),
          ("rate700M", 30),
          ("rate800M", 31),
          ("rate900M", 32),
          ("rate5M", 33),
          ("rate7M", 34),
          ("rate9M", 35),
          ("rate90M", 36),
          ("rate15M", 37),
          ("rate25M", 38),
          ("rate35M", 39),
          ("rate45M", 40),
          ("rate55M", 41),
          ("rate65M", 42),
          ("rate75M", 43),
          ("rate85M", 44),
          ("rate95M", 45),
          ("rate150M", 46),
          ("rate250M", 47),
          ("rate350M", 48),
          ("rate450M", 49),
          ("rate550M", 50),
          ("rate650M", 51),
          ("rate750M", 52),
          ("rate850M", 53),
          ("rate950M", 54))
    )


_TnIfIngressRateLimit_Type.__name__ = "Integer32"
_TnIfIngressRateLimit_Object = MibTableColumn
tnIfIngressRateLimit = _TnIfIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 3, 1, 2),
    _TnIfIngressRateLimit_Type()
)
tnIfIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfIngressRateLimit.setStatus("current")


class _TnIfEgressRateLimit_Type(Integer32):
    """Custom type tnIfEgressRateLimit based on Integer32"""
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
              54)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("rate64K", 2),
          ("rate128K", 3),
          ("rate192K", 4),
          ("rate256K", 5),
          ("rate320K", 6),
          ("rate384K", 7),
          ("rate512K", 8),
          ("rate768K", 9),
          ("rate1M", 10),
          ("rate2M", 11),
          ("rate3M", 12),
          ("rate4M", 13),
          ("rate6M", 14),
          ("rate8M", 15),
          ("rate10M", 16),
          ("rate20M", 17),
          ("rate30M", 18),
          ("rate40M", 19),
          ("rate50M", 20),
          ("rate60M", 21),
          ("rate70M", 22),
          ("rate80M", 23),
          ("rate100M", 24),
          ("rate200M", 25),
          ("rate300M", 26),
          ("rate400M", 27),
          ("rate500M", 28),
          ("rate600M", 29),
          ("rate700M", 30),
          ("rate800M", 31),
          ("rate900M", 32),
          ("rate5M", 33),
          ("rate7M", 34),
          ("rate9M", 35),
          ("rate90M", 36),
          ("rate15M", 37),
          ("rate25M", 38),
          ("rate35M", 39),
          ("rate45M", 40),
          ("rate55M", 41),
          ("rate65M", 42),
          ("rate75M", 43),
          ("rate85M", 44),
          ("rate95M", 45),
          ("rate150M", 46),
          ("rate250M", 47),
          ("rate350M", 48),
          ("rate450M", 49),
          ("rate550M", 50),
          ("rate650M", 51),
          ("rate750M", 52),
          ("rate850M", 53),
          ("rate950M", 54))
    )


_TnIfEgressRateLimit_Type.__name__ = "Integer32"
_TnIfEgressRateLimit_Object = MibTableColumn
tnIfEgressRateLimit = _TnIfEgressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 3, 1, 3),
    _TnIfEgressRateLimit_Type()
)
tnIfEgressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfEgressRateLimit.setStatus("current")
_TnIfRedundancyTable_Object = MibTable
tnIfRedundancyTable = _TnIfRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnIfRedundancyTable.setStatus("current")
_TnIfRedundancyEntry_Object = MibTableRow
tnIfRedundancyEntry = _TnIfRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1)
)
tnIfRedundancyEntry.setIndexNames(
    (0, "TN-MGMT-MIB", "tnIfPrimaryPort"),
    (0, "TN-MGMT-MIB", "tnIfSecondaryPort"),
)
if mibBuilder.loadTexts:
    tnIfRedundancyEntry.setStatus("current")


class _TnIfRedundancy_Type(Integer32):
    """Custom type tnIfRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_TnIfRedundancy_Type.__name__ = "Integer32"
_TnIfRedundancy_Object = MibTableColumn
tnIfRedundancy = _TnIfRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1, 1),
    _TnIfRedundancy_Type()
)
tnIfRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfRedundancy.setStatus("current")


class _TnIfRedundRevert_Type(Integer32):
    """Custom type tnIfRedundRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("revert", 1),
          ("noRevert", 2),
          ("notApplicable", 3))
    )


_TnIfRedundRevert_Type.__name__ = "Integer32"
_TnIfRedundRevert_Object = MibTableColumn
tnIfRedundRevert = _TnIfRedundRevert_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1, 2),
    _TnIfRedundRevert_Type()
)
tnIfRedundRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfRedundRevert.setStatus("current")
_TnIfPrimaryPort_Type = InterfaceIndex
_TnIfPrimaryPort_Object = MibTableColumn
tnIfPrimaryPort = _TnIfPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1, 3),
    _TnIfPrimaryPort_Type()
)
tnIfPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfPrimaryPort.setStatus("current")
_TnIfSecondaryPort_Type = InterfaceIndex
_TnIfSecondaryPort_Object = MibTableColumn
tnIfSecondaryPort = _TnIfSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1, 4),
    _TnIfSecondaryPort_Type()
)
tnIfSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfSecondaryPort.setStatus("current")
_TnIfRedundActivePort_Type = InterfaceIndexOrZero
_TnIfRedundActivePort_Object = MibTableColumn
tnIfRedundActivePort = _TnIfRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 4, 1, 5),
    _TnIfRedundActivePort_Type()
)
tnIfRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfRedundActivePort.setStatus("current")
_TnIfFwdPortListTable_Object = MibTable
tnIfFwdPortListTable = _TnIfFwdPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tnIfFwdPortListTable.setStatus("current")
_TnIfFwdPortListEntry_Object = MibTableRow
tnIfFwdPortListEntry = _TnIfFwdPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 5, 1)
)
tnIfFwdPortListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfFwdPortListEntry.setStatus("current")
_TnIfPortifIndextoPortNum_Type = Integer32
_TnIfPortifIndextoPortNum_Object = MibTableColumn
tnIfPortifIndextoPortNum = _TnIfPortifIndextoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 5, 1, 1),
    _TnIfPortifIndextoPortNum_Type()
)
tnIfPortifIndextoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfPortifIndextoPortNum.setStatus("current")
_TnIfFwdPortList_Type = PortList
_TnIfFwdPortList_Object = MibTableColumn
tnIfFwdPortList = _TnIfFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 5, 1, 2),
    _TnIfFwdPortList_Type()
)
tnIfFwdPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfFwdPortList.setStatus("current")
_TnIfL2CPTable_Object = MibTable
tnIfL2CPTable = _TnIfL2CPTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tnIfL2CPTable.setStatus("current")
_TnIfL2CPEntry_Object = MibTableRow
tnIfL2CPEntry = _TnIfL2CPEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1)
)
tnIfL2CPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfL2CPEntry.setStatus("current")


class _TnIfL2CPSTPProtocolsFwd_Type(Integer32):
    """Custom type tnIfL2CPSTPProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPSTPProtocolsFwd_Type.__name__ = "Integer32"
_TnIfL2CPSTPProtocolsFwd_Object = MibTableColumn
tnIfL2CPSTPProtocolsFwd = _TnIfL2CPSTPProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 1),
    _TnIfL2CPSTPProtocolsFwd_Type()
)
tnIfL2CPSTPProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPSTPProtocolsFwd.setStatus("current")


class _TnIfL2CPSlowProtocolsFwd_Type(Integer32):
    """Custom type tnIfL2CPSlowProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPSlowProtocolsFwd_Type.__name__ = "Integer32"
_TnIfL2CPSlowProtocolsFwd_Object = MibTableColumn
tnIfL2CPSlowProtocolsFwd = _TnIfL2CPSlowProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 2),
    _TnIfL2CPSlowProtocolsFwd_Type()
)
tnIfL2CPSlowProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPSlowProtocolsFwd.setStatus("current")


class _TnIfL2CPPortAuthProtocolFwd_Type(Integer32):
    """Custom type tnIfL2CPPortAuthProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPPortAuthProtocolFwd_Type.__name__ = "Integer32"
_TnIfL2CPPortAuthProtocolFwd_Object = MibTableColumn
tnIfL2CPPortAuthProtocolFwd = _TnIfL2CPPortAuthProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 3),
    _TnIfL2CPPortAuthProtocolFwd_Type()
)
tnIfL2CPPortAuthProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPPortAuthProtocolFwd.setStatus("current")


class _TnIfL2CPELMIProtocolFwd_Type(Integer32):
    """Custom type tnIfL2CPELMIProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPELMIProtocolFwd_Type.__name__ = "Integer32"
_TnIfL2CPELMIProtocolFwd_Object = MibTableColumn
tnIfL2CPELMIProtocolFwd = _TnIfL2CPELMIProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 4),
    _TnIfL2CPELMIProtocolFwd_Type()
)
tnIfL2CPELMIProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPELMIProtocolFwd.setStatus("current")


class _TnIfL2CPLLDPProtocolFwd_Type(Integer32):
    """Custom type tnIfL2CPLLDPProtocolFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPLLDPProtocolFwd_Type.__name__ = "Integer32"
_TnIfL2CPLLDPProtocolFwd_Object = MibTableColumn
tnIfL2CPLLDPProtocolFwd = _TnIfL2CPLLDPProtocolFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 5),
    _TnIfL2CPLLDPProtocolFwd_Type()
)
tnIfL2CPLLDPProtocolFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPLLDPProtocolFwd.setStatus("current")


class _TnIfL2CPBridgeMgmtProtocolsFwd_Type(Integer32):
    """Custom type tnIfL2CPBridgeMgmtProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPBridgeMgmtProtocolsFwd_Type.__name__ = "Integer32"
_TnIfL2CPBridgeMgmtProtocolsFwd_Object = MibTableColumn
tnIfL2CPBridgeMgmtProtocolsFwd = _TnIfL2CPBridgeMgmtProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 6),
    _TnIfL2CPBridgeMgmtProtocolsFwd_Type()
)
tnIfL2CPBridgeMgmtProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPBridgeMgmtProtocolsFwd.setStatus("current")


class _TnIfL2CPGARPBlockProtocolsFwd_Type(Integer32):
    """Custom type tnIfL2CPGARPBlockProtocolsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPGARPBlockProtocolsFwd_Type.__name__ = "Integer32"
_TnIfL2CPGARPBlockProtocolsFwd_Object = MibTableColumn
tnIfL2CPGARPBlockProtocolsFwd = _TnIfL2CPGARPBlockProtocolsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 7),
    _TnIfL2CPGARPBlockProtocolsFwd_Type()
)
tnIfL2CPGARPBlockProtocolsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPGARPBlockProtocolsFwd.setStatus("current")


class _TnIfL2CPBridgeBlkOtherMulticastsFwd_Type(Integer32):
    """Custom type tnIfL2CPBridgeBlkOtherMulticastsFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("discard", 2),
          ("notApplicable", 3))
    )


_TnIfL2CPBridgeBlkOtherMulticastsFwd_Type.__name__ = "Integer32"
_TnIfL2CPBridgeBlkOtherMulticastsFwd_Object = MibTableColumn
tnIfL2CPBridgeBlkOtherMulticastsFwd = _TnIfL2CPBridgeBlkOtherMulticastsFwd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 7, 1, 8),
    _TnIfL2CPBridgeBlkOtherMulticastsFwd_Type()
)
tnIfL2CPBridgeBlkOtherMulticastsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfL2CPBridgeBlkOtherMulticastsFwd.setStatus("current")
_TnIfTNDPTable_Object = MibTable
tnIfTNDPTable = _TnIfTNDPTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tnIfTNDPTable.setStatus("current")
_TnIfTNDPEntry_Object = MibTableRow
tnIfTNDPEntry = _TnIfTNDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 8, 1)
)
tnIfTNDPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfTNDPEntry.setStatus("current")


class _TnIfTNDPTxState_Type(Integer32):
    """Custom type tnIfTNDPTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notSupported", 3))
    )


_TnIfTNDPTxState_Type.__name__ = "Integer32"
_TnIfTNDPTxState_Object = MibTableColumn
tnIfTNDPTxState = _TnIfTNDPTxState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 2, 8, 1, 1),
    _TnIfTNDPTxState_Type()
)
tnIfTNDPTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTNDPTxState.setStatus("current")
_TnInterfaceDiagMgmt_ObjectIdentity = ObjectIdentity
tnInterfaceDiagMgmt = _TnInterfaceDiagMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3)
)
_TnIfTDRTestTable_Object = MibTable
tnIfTDRTestTable = _TnIfTDRTestTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnIfTDRTestTable.setStatus("current")
_TnIfTDRTestEntry_Object = MibTableRow
tnIfTDRTestEntry = _TnIfTDRTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1, 1)
)
tnIfTDRTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfTDRTestEntry.setStatus("current")


class _TnIfTDRTestAction_Type(Integer32):
    """Custom type tnIfTDRTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perform", 1),
          ("doNothing", 2))
    )


_TnIfTDRTestAction_Type.__name__ = "Integer32"
_TnIfTDRTestAction_Object = MibTableColumn
tnIfTDRTestAction = _TnIfTDRTestAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1, 1, 1),
    _TnIfTDRTestAction_Type()
)
tnIfTDRTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfTDRTestAction.setStatus("current")


class _TnIfTDRTestStatus_Type(Integer32):
    """Custom type tnIfTDRTestStatus based on Integer32"""
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
        *(("testSuccess", 1),
          ("testFailed", 2),
          ("testAlreadyRunning", 3),
          ("testUnknownState", 4))
    )


_TnIfTDRTestStatus_Type.__name__ = "Integer32"
_TnIfTDRTestStatus_Object = MibTableColumn
tnIfTDRTestStatus = _TnIfTDRTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1, 1, 2),
    _TnIfTDRTestStatus_Type()
)
tnIfTDRTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRTestStatus.setStatus("current")
_TnIfTDRTestInitTime_Type = TimeStamp
_TnIfTDRTestInitTime_Object = MibTableColumn
tnIfTDRTestInitTime = _TnIfTDRTestInitTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1, 1, 3),
    _TnIfTDRTestInitTime_Type()
)
tnIfTDRTestInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRTestInitTime.setStatus("current")
_TnIfTDRTestResultValid_Type = TruthValue
_TnIfTDRTestResultValid_Object = MibTableColumn
tnIfTDRTestResultValid = _TnIfTDRTestResultValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 1, 1, 4),
    _TnIfTDRTestResultValid_Type()
)
tnIfTDRTestResultValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRTestResultValid.setStatus("current")
_TnIfTDRResultTable_Object = MibTable
tnIfTDRResultTable = _TnIfTDRResultTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnIfTDRResultTable.setStatus("current")
_TnIfTDRResultEntry_Object = MibTableRow
tnIfTDRResultEntry = _TnIfTDRResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1)
)
tnIfTDRResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-MGMT-MIB", "tnIfTDRResultPairIndex"),
)
if mibBuilder.loadTexts:
    tnIfTDRResultEntry.setStatus("current")


class _TnIfTDRResultPairIndex_Type(Integer32):
    """Custom type tnIfTDRResultPairIndex based on Integer32"""
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
        *(("pair1to2", 1),
          ("pair3to6", 2),
          ("pair4to5", 3),
          ("pair7to8", 4))
    )


_TnIfTDRResultPairIndex_Type.__name__ = "Integer32"
_TnIfTDRResultPairIndex_Object = MibTableColumn
tnIfTDRResultPairIndex = _TnIfTDRResultPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1, 1),
    _TnIfTDRResultPairIndex_Type()
)
tnIfTDRResultPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnIfTDRResultPairIndex.setStatus("current")


class _TnIfTDRResultPairLength_Type(Integer32):
    """Custom type tnIfTDRResultPairLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TnIfTDRResultPairLength_Type.__name__ = "Integer32"
_TnIfTDRResultPairLength_Object = MibTableColumn
tnIfTDRResultPairLength = _TnIfTDRResultPairLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1, 2),
    _TnIfTDRResultPairLength_Type()
)
tnIfTDRResultPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRResultPairLength.setStatus("current")


class _TnIfTDRResultPairDistToFault_Type(Integer32):
    """Custom type tnIfTDRResultPairDistToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TnIfTDRResultPairDistToFault_Type.__name__ = "Integer32"
_TnIfTDRResultPairDistToFault_Object = MibTableColumn
tnIfTDRResultPairDistToFault = _TnIfTDRResultPairDistToFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1, 3),
    _TnIfTDRResultPairDistToFault_Type()
)
tnIfTDRResultPairDistToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRResultPairDistToFault.setStatus("current")


class _TnIfTDRResultPairLengthUnit_Type(Integer32):
    """Custom type tnIfTDRResultPairLengthUnit based on Integer32"""
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
        *(("unknown", 1),
          ("meter", 2),
          ("centimeter", 3),
          ("kilometer", 4))
    )


_TnIfTDRResultPairLengthUnit_Type.__name__ = "Integer32"
_TnIfTDRResultPairLengthUnit_Object = MibTableColumn
tnIfTDRResultPairLengthUnit = _TnIfTDRResultPairLengthUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1, 4),
    _TnIfTDRResultPairLengthUnit_Type()
)
tnIfTDRResultPairLengthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRResultPairLengthUnit.setStatus("current")


class _TnIfTDRResultPairStatus_Type(Integer32):
    """Custom type tnIfTDRResultPairStatus based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("impedanceMismatch", 3),
          ("shorted", 4),
          ("open", 5))
    )


_TnIfTDRResultPairStatus_Type.__name__ = "Integer32"
_TnIfTDRResultPairStatus_Object = MibTableColumn
tnIfTDRResultPairStatus = _TnIfTDRResultPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 2, 1, 5),
    _TnIfTDRResultPairStatus_Type()
)
tnIfTDRResultPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfTDRResultPairStatus.setStatus("current")
_TnIfLoopbackTable_Object = MibTable
tnIfLoopbackTable = _TnIfLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnIfLoopbackTable.setStatus("current")
_TnIfLoopbackEntry_Object = MibTableRow
tnIfLoopbackEntry = _TnIfLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3, 1)
)
tnIfLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfLoopbackEntry.setStatus("current")
_TnIfLoopbackCapability_Type = TNLoopbackModeCapBits
_TnIfLoopbackCapability_Object = MibTableColumn
tnIfLoopbackCapability = _TnIfLoopbackCapability_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3, 1, 1),
    _TnIfLoopbackCapability_Type()
)
tnIfLoopbackCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfLoopbackCapability.setStatus("current")
_TnIfLoopbackInit_Type = TNLoopbackModes
_TnIfLoopbackInit_Object = MibTableColumn
tnIfLoopbackInit = _TnIfLoopbackInit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3, 1, 2),
    _TnIfLoopbackInit_Type()
)
tnIfLoopbackInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLoopbackInit.setStatus("current")


class _TnIfLoopbackStatus_Type(Integer32):
    """Custom type tnIfLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("intiateLoopback", 2),
          ("terminateLoopback", 3),
          ("inProcess", 4),
          ("localInLoopback", 5),
          ("remoteInLoopback", 6))
    )


_TnIfLoopbackStatus_Type.__name__ = "Integer32"
_TnIfLoopbackStatus_Object = MibTableColumn
tnIfLoopbackStatus = _TnIfLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3, 1, 3),
    _TnIfLoopbackStatus_Type()
)
tnIfLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLoopbackStatus.setStatus("current")


class _TnIfClearCounters_Type(Integer32):
    """Custom type tnIfClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("doNothing", 2))
    )


_TnIfClearCounters_Type.__name__ = "Integer32"
_TnIfClearCounters_Object = MibTableColumn
tnIfClearCounters = _TnIfClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 3, 3, 1, 4),
    _TnIfClearCounters_Type()
)
tnIfClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfClearCounters.setStatus("current")
_TnIfMACSecurityMgmt_ObjectIdentity = ObjectIdentity
tnIfMACSecurityMgmt = _TnIfMACSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4)
)
_TnIfMACSecurityTable_Object = MibTable
tnIfMACSecurityTable = _TnIfMACSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tnIfMACSecurityTable.setStatus("current")
_TnIfMACSecurityEntry_Object = MibTableRow
tnIfMACSecurityEntry = _TnIfMACSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3, 1)
)
tnIfMACSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfMACSecurityEntry.setStatus("current")
_TnIfSourceAddrLock_Type = TruthValue
_TnIfSourceAddrLock_Object = MibTableColumn
tnIfSourceAddrLock = _TnIfSourceAddrLock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3, 1, 1),
    _TnIfSourceAddrLock_Type()
)
tnIfSourceAddrLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfSourceAddrLock.setStatus("current")


class _TnIfSourceAddrLockAction_Type(Integer32):
    """Custom type tnIfSourceAddrLockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("discardAndNotify", 2),
          ("shutdown", 3),
          ("all", 5))
    )


_TnIfSourceAddrLockAction_Type.__name__ = "Integer32"
_TnIfSourceAddrLockAction_Object = MibTableColumn
tnIfSourceAddrLockAction = _TnIfSourceAddrLockAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3, 1, 2),
    _TnIfSourceAddrLockAction_Type()
)
tnIfSourceAddrLockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfSourceAddrLockAction.setStatus("current")
_TnIfFilterUnknownUnicast_Type = TruthValue
_TnIfFilterUnknownUnicast_Object = MibTableColumn
tnIfFilterUnknownUnicast = _TnIfFilterUnknownUnicast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3, 1, 3),
    _TnIfFilterUnknownUnicast_Type()
)
tnIfFilterUnknownUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfFilterUnknownUnicast.setStatus("current")
_TnIfFilterUnknownMulticast_Type = TruthValue
_TnIfFilterUnknownMulticast_Object = MibTableColumn
tnIfFilterUnknownMulticast = _TnIfFilterUnknownMulticast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 3, 1, 4),
    _TnIfFilterUnknownMulticast_Type()
)
tnIfFilterUnknownMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfFilterUnknownMulticast.setStatus("current")
_TnIfLimitDynMACLearningTable_Object = MibTable
tnIfLimitDynMACLearningTable = _TnIfLimitDynMACLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tnIfLimitDynMACLearningTable.setStatus("current")
_TnIfLimitDynMACLearningEntry_Object = MibTableRow
tnIfLimitDynMACLearningEntry = _TnIfLimitDynMACLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1)
)
tnIfLimitDynMACLearningEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnIfLimitDynMACLearningEntry.setStatus("current")
_TnIfLimitDynMACMode_Type = TruthValue
_TnIfLimitDynMACMode_Object = MibTableColumn
tnIfLimitDynMACMode = _TnIfLimitDynMACMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1, 1),
    _TnIfLimitDynMACMode_Type()
)
tnIfLimitDynMACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLimitDynMACMode.setStatus("current")


class _TnIfLimitDynMACMaxCount_Type(Integer32):
    """Custom type tnIfLimitDynMACMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TnIfLimitDynMACMaxCount_Type.__name__ = "Integer32"
_TnIfLimitDynMACMaxCount_Object = MibTableColumn
tnIfLimitDynMACMaxCount = _TnIfLimitDynMACMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1, 2),
    _TnIfLimitDynMACMaxCount_Type()
)
tnIfLimitDynMACMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLimitDynMACMaxCount.setStatus("current")


class _TnIfLimitDynMACAction_Type(Integer32):
    """Custom type tnIfLimitDynMACAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trap", 1),
          ("shutdown", 2),
          ("trapShutdown", 3))
    )


_TnIfLimitDynMACAction_Type.__name__ = "Integer32"
_TnIfLimitDynMACAction_Object = MibTableColumn
tnIfLimitDynMACAction = _TnIfLimitDynMACAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1, 3),
    _TnIfLimitDynMACAction_Type()
)
tnIfLimitDynMACAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLimitDynMACAction.setStatus("current")


class _TnIfLimitDynMACState_Type(Integer32):
    """Custom type tnIfLimitDynMACState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ready", 1),
          ("limitReached", 2),
          ("shutdown", 3))
    )


_TnIfLimitDynMACState_Type.__name__ = "Integer32"
_TnIfLimitDynMACState_Object = MibTableColumn
tnIfLimitDynMACState = _TnIfLimitDynMACState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1, 4),
    _TnIfLimitDynMACState_Type()
)
tnIfLimitDynMACState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLimitDynMACState.setStatus("current")
_TnIfLimitDynMACReopen_Type = TruthValue
_TnIfLimitDynMACReopen_Object = MibTableColumn
tnIfLimitDynMACReopen = _TnIfLimitDynMACReopen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 4, 4, 1, 5),
    _TnIfLimitDynMACReopen_Type()
)
tnIfLimitDynMACReopen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnIfLimitDynMACReopen.setStatus("current")
_TnIfQOSMgmt_ObjectIdentity = ObjectIdentity
tnIfQOSMgmt = _TnIfQOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5)
)
_TnEgressQueueModeMgmt_ObjectIdentity = ObjectIdentity
tnEgressQueueModeMgmt = _TnEgressQueueModeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5, 1)
)
_TnEgressQueueModeTable_Object = MibTable
tnEgressQueueModeTable = _TnEgressQueueModeTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tnEgressQueueModeTable.setStatus("current")
_TnEgressQueueModeEntry_Object = MibTableRow
tnEgressQueueModeEntry = _TnEgressQueueModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5, 1, 1, 1)
)
tnEgressQueueModeEntry.setIndexNames(
    (0, "TN-MGMT-MIB", "tnEgressQueueIfIndex"),
)
if mibBuilder.loadTexts:
    tnEgressQueueModeEntry.setStatus("current")
_TnEgressQueueIfIndex_Type = Integer32
_TnEgressQueueIfIndex_Object = MibTableColumn
tnEgressQueueIfIndex = _TnEgressQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5, 1, 1, 1, 1),
    _TnEgressQueueIfIndex_Type()
)
tnEgressQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEgressQueueIfIndex.setStatus("current")


class _TnEgressQueueMode_Type(Integer32):
    """Custom type tnEgressQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wrr", 1),
          ("strict", 2))
    )


_TnEgressQueueMode_Type.__name__ = "Integer32"
_TnEgressQueueMode_Object = MibTableColumn
tnEgressQueueMode = _TnEgressQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 5, 1, 1, 1, 2),
    _TnEgressQueueMode_Type()
)
tnEgressQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEgressQueueMode.setStatus("current")
_TnMgmtConformance_ObjectIdentity = ObjectIdentity
tnMgmtConformance = _TnMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 2)
)

# Managed Objects groups


# Notification objects

tnDMIRxIntrusionEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 1)
)
tnDMIRxIntrusionEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnDMIRxPwrLvlPreset"),
        ("TN-MGMT-MIB", "tnDMIRxPowerLevel"))
)
if mibBuilder.loadTexts:
    tnDMIRxIntrusionEvt.setStatus(
        "current"
    )

tnDMIRxPowerEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 2)
)
tnDMIRxPowerEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnDMIRxPowerAlarm"),
        ("TN-MGMT-MIB", "tnDMIRxPowerLevel"))
)
if mibBuilder.loadTexts:
    tnDMIRxPowerEvt.setStatus(
        "current"
    )

tnDMITxPowerEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 3)
)
tnDMITxPowerEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnDMITxPowerAlarm"),
        ("TN-MGMT-MIB", "tnDMITxPowerLevel"))
)
if mibBuilder.loadTexts:
    tnDMITxPowerEvt.setStatus(
        "current"
    )

tnDMITxBiasEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 4)
)
tnDMITxBiasEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnDMITxBiasAlarm"),
        ("TN-MGMT-MIB", "tnDMITxBiasCurrent"))
)
if mibBuilder.loadTexts:
    tnDMITxBiasEvt.setStatus(
        "current"
    )

tnDMITemperatureEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 5)
)
tnDMITemperatureEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnDMITempAlarm"),
        ("TN-MGMT-MIB", "tnDMITemperature"))
)
if mibBuilder.loadTexts:
    tnDMITemperatureEvt.setStatus(
        "current"
    )

tnDyingGaspEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 7)
)
if mibBuilder.loadTexts:
    tnDyingGaspEvt.setStatus(
        "current"
    )

tnIfLimitDynMACEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 8)
)
tnIfLimitDynMACEvt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("TN-MGMT-MIB", "tnIfLimitDynMACMaxCount"),
        ("TN-MGMT-MIB", "tnIfLimitDynMACState"))
)
if mibBuilder.loadTexts:
    tnIfLimitDynMACEvt.setStatus(
        "current"
    )

tnMgmtMibBoardTmpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 9)
)
tnMgmtMibBoardTmpNotif.setObjects(
    ("TN-MGMT-MIB", "tnDevSysHwInforBoardtmp")
)
if mibBuilder.loadTexts:
    tnMgmtMibBoardTmpNotif.setStatus(
        "current"
    )

tnMgmtMibCPUTmpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 0, 10)
)
tnMgmtMibCPUTmpNotif.setObjects(
    ("TN-MGMT-MIB", "tnDevSysHwInforCPUtmp")
)
if mibBuilder.loadTexts:
    tnMgmtMibCPUTmpNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MGMT-MIB",
    **{"tnMgmtMIB": tnMgmtMIB,
       "tnMgmtNotifications": tnMgmtNotifications,
       "tnDMIRxIntrusionEvt": tnDMIRxIntrusionEvt,
       "tnDMIRxPowerEvt": tnDMIRxPowerEvt,
       "tnDMITxPowerEvt": tnDMITxPowerEvt,
       "tnDMITxBiasEvt": tnDMITxBiasEvt,
       "tnDMITemperatureEvt": tnDMITemperatureEvt,
       "tnDyingGaspEvt": tnDyingGaspEvt,
       "tnIfLimitDynMACEvt": tnIfLimitDynMACEvt,
       "tnMgmtMibBoardTmpNotif": tnMgmtMibBoardTmpNotif,
       "tnMgmtMibCPUTmpNotif": tnMgmtMibCPUTmpNotif,
       "tnMgmtObjects": tnMgmtObjects,
       "tnDevMgmt": tnDevMgmt,
       "tnDevSysMgmt": tnDevSysMgmt,
       "tnDevSysCfgTable": tnDevSysCfgTable,
       "tnDevSysCfgEntry": tnDevSysCfgEntry,
       "tnDevSysName": tnDevSysName,
       "tnDevSysUptime": tnDevSysUptime,
       "tnDevSysUptimeReset": tnDevSysUptimeReset,
       "tnDevSysReset": tnDevSysReset,
       "tnDevNumOfPorts": tnDevNumOfPorts,
       "tnDevClearCounters": tnDevClearCounters,
       "tnDevResetToFactoryConfig": tnDevResetToFactoryConfig,
       "tnDevConfigurationMode": tnDevConfigurationMode,
       "tnDevConsoleAccess": tnDevConsoleAccess,
       "tnDevSharedPortMode": tnDevSharedPortMode,
       "tnDevSysHwInforTable": tnDevSysHwInforTable,
       "tnDevSysHwInforEntry": tnDevSysHwInforEntry,
       "tnDevSysHwInforChipID": tnDevSysHwInforChipID,
       "tnDevSysHwInforBoardRev": tnDevSysHwInforBoardRev,
       "tnDevSysHwInforFPGAVer": tnDevSysHwInforFPGAVer,
       "tnDevSysHwInforBoardtmp": tnDevSysHwInforBoardtmp,
       "tnDevSysHwInforCPUtmp": tnDevSysHwInforCPUtmp,
       "tnDevSysLPT": tnDevSysLPT,
       "tnDevSysLPTTable": tnDevSysLPTTable,
       "tnDevSysLPTEntry": tnDevSysLPTEntry,
       "tnSysLinkPassThro": tnSysLinkPassThro,
       "tnSysTransparentLPT": tnSysTransparentLPT,
       "tnSysSelectiveLPT": tnSysSelectiveLPT,
       "tnSysLPTMonitorPort": tnSysLPTMonitorPort,
       "tnSysRemoteFaultDetect": tnSysRemoteFaultDetect,
       "tnDevSysDyingGasp": tnDevSysDyingGasp,
       "tnDevSysDyingGaspTable": tnDevSysDyingGaspTable,
       "tnDevSysDyingGaspEntry": tnDevSysDyingGaspEntry,
       "tnSysDyingGaspTrap": tnSysDyingGaspTrap,
       "tnDevSysMACLearning": tnDevSysMACLearning,
       "tnDevSysMacLearningTable": tnDevSysMacLearningTable,
       "tnDevSysMacLearningEntry": tnDevSysMacLearningEntry,
       "tnSysPortMacLearningState": tnSysPortMacLearningState,
       "tnInterfaceMgmt": tnInterfaceMgmt,
       "tnEthInterfaceTable": tnEthInterfaceTable,
       "tnEthInterfaceEntry": tnEthInterfaceEntry,
       "tnEthInterfaceSpeed": tnEthInterfaceSpeed,
       "tnEthInterfaceDuplex": tnEthInterfaceDuplex,
       "tnEthAutoCrossCap": tnEthAutoCrossCap,
       "tnEthAutoCrossMode": tnEthAutoCrossMode,
       "tnEthFarEndFaultCap": tnEthFarEndFaultCap,
       "tnEthFarEndFaultMode": tnEthFarEndFaultMode,
       "tnEthPhyModeChangeCap": tnEthPhyModeChangeCap,
       "tnEthPhyOperMode": tnEthPhyOperMode,
       "tnEthPhyMode": tnEthPhyMode,
       "tnEthMaxFrameSize": tnEthMaxFrameSize,
       "tnDMIInfoTable": tnDMIInfoTable,
       "tnDMIInfoEntry": tnDMIInfoEntry,
       "tnDMIConnectorType": tnDMIConnectorType,
       "tnDMIBitRate": tnDMIBitRate,
       "tnDMILenFor9x125umKM": tnDMILenFor9x125umKM,
       "tnDMILenFor9x125um100M": tnDMILenFor9x125um100M,
       "tnDMILenFor50x125um10M": tnDMILenFor50x125um10M,
       "tnDMILenFor625x125um10M": tnDMILenFor625x125um10M,
       "tnDMILenForCopper": tnDMILenForCopper,
       "tnDMIId": tnDMIId,
       "tnDMILaserWavelength": tnDMILaserWavelength,
       "tnDMITemperature": tnDMITemperature,
       "tnDMITempAlarm": tnDMITempAlarm,
       "tnDMITxBiasCurrent": tnDMITxBiasCurrent,
       "tnDMITxBiasAlarm": tnDMITxBiasAlarm,
       "tnDMITxPowerLevel": tnDMITxPowerLevel,
       "tnDMITxPowerAlarm": tnDMITxPowerAlarm,
       "tnDMIRxPowerLevel": tnDMIRxPowerLevel,
       "tnDMIRxPowerAlarm": tnDMIRxPowerAlarm,
       "tnDMIRxPwrLvlPreset": tnDMIRxPwrLvlPreset,
       "tnDMIVendorName": tnDMIVendorName,
       "tnDMIVendorOUI": tnDMIVendorOUI,
       "tnDMIVendorPartNo": tnDMIVendorPartNo,
       "tnDMIVendorRevision": tnDMIVendorRevision,
       "tnDMIVendorSerialNo": tnDMIVendorSerialNo,
       "tnIfBWAllocTable": tnIfBWAllocTable,
       "tnIfBWAllocEntry": tnIfBWAllocEntry,
       "tnIfBWAllocType": tnIfBWAllocType,
       "tnIfIngressRateLimit": tnIfIngressRateLimit,
       "tnIfEgressRateLimit": tnIfEgressRateLimit,
       "tnIfRedundancyTable": tnIfRedundancyTable,
       "tnIfRedundancyEntry": tnIfRedundancyEntry,
       "tnIfRedundancy": tnIfRedundancy,
       "tnIfRedundRevert": tnIfRedundRevert,
       "tnIfPrimaryPort": tnIfPrimaryPort,
       "tnIfSecondaryPort": tnIfSecondaryPort,
       "tnIfRedundActivePort": tnIfRedundActivePort,
       "tnIfFwdPortListTable": tnIfFwdPortListTable,
       "tnIfFwdPortListEntry": tnIfFwdPortListEntry,
       "tnIfPortifIndextoPortNum": tnIfPortifIndextoPortNum,
       "tnIfFwdPortList": tnIfFwdPortList,
       "tnIfL2CPTable": tnIfL2CPTable,
       "tnIfL2CPEntry": tnIfL2CPEntry,
       "tnIfL2CPSTPProtocolsFwd": tnIfL2CPSTPProtocolsFwd,
       "tnIfL2CPSlowProtocolsFwd": tnIfL2CPSlowProtocolsFwd,
       "tnIfL2CPPortAuthProtocolFwd": tnIfL2CPPortAuthProtocolFwd,
       "tnIfL2CPELMIProtocolFwd": tnIfL2CPELMIProtocolFwd,
       "tnIfL2CPLLDPProtocolFwd": tnIfL2CPLLDPProtocolFwd,
       "tnIfL2CPBridgeMgmtProtocolsFwd": tnIfL2CPBridgeMgmtProtocolsFwd,
       "tnIfL2CPGARPBlockProtocolsFwd": tnIfL2CPGARPBlockProtocolsFwd,
       "tnIfL2CPBridgeBlkOtherMulticastsFwd": tnIfL2CPBridgeBlkOtherMulticastsFwd,
       "tnIfTNDPTable": tnIfTNDPTable,
       "tnIfTNDPEntry": tnIfTNDPEntry,
       "tnIfTNDPTxState": tnIfTNDPTxState,
       "tnInterfaceDiagMgmt": tnInterfaceDiagMgmt,
       "tnIfTDRTestTable": tnIfTDRTestTable,
       "tnIfTDRTestEntry": tnIfTDRTestEntry,
       "tnIfTDRTestAction": tnIfTDRTestAction,
       "tnIfTDRTestStatus": tnIfTDRTestStatus,
       "tnIfTDRTestInitTime": tnIfTDRTestInitTime,
       "tnIfTDRTestResultValid": tnIfTDRTestResultValid,
       "tnIfTDRResultTable": tnIfTDRResultTable,
       "tnIfTDRResultEntry": tnIfTDRResultEntry,
       "tnIfTDRResultPairIndex": tnIfTDRResultPairIndex,
       "tnIfTDRResultPairLength": tnIfTDRResultPairLength,
       "tnIfTDRResultPairDistToFault": tnIfTDRResultPairDistToFault,
       "tnIfTDRResultPairLengthUnit": tnIfTDRResultPairLengthUnit,
       "tnIfTDRResultPairStatus": tnIfTDRResultPairStatus,
       "tnIfLoopbackTable": tnIfLoopbackTable,
       "tnIfLoopbackEntry": tnIfLoopbackEntry,
       "tnIfLoopbackCapability": tnIfLoopbackCapability,
       "tnIfLoopbackInit": tnIfLoopbackInit,
       "tnIfLoopbackStatus": tnIfLoopbackStatus,
       "tnIfClearCounters": tnIfClearCounters,
       "tnIfMACSecurityMgmt": tnIfMACSecurityMgmt,
       "tnIfMACSecurityTable": tnIfMACSecurityTable,
       "tnIfMACSecurityEntry": tnIfMACSecurityEntry,
       "tnIfSourceAddrLock": tnIfSourceAddrLock,
       "tnIfSourceAddrLockAction": tnIfSourceAddrLockAction,
       "tnIfFilterUnknownUnicast": tnIfFilterUnknownUnicast,
       "tnIfFilterUnknownMulticast": tnIfFilterUnknownMulticast,
       "tnIfLimitDynMACLearningTable": tnIfLimitDynMACLearningTable,
       "tnIfLimitDynMACLearningEntry": tnIfLimitDynMACLearningEntry,
       "tnIfLimitDynMACMode": tnIfLimitDynMACMode,
       "tnIfLimitDynMACMaxCount": tnIfLimitDynMACMaxCount,
       "tnIfLimitDynMACAction": tnIfLimitDynMACAction,
       "tnIfLimitDynMACState": tnIfLimitDynMACState,
       "tnIfLimitDynMACReopen": tnIfLimitDynMACReopen,
       "tnIfQOSMgmt": tnIfQOSMgmt,
       "tnEgressQueueModeMgmt": tnEgressQueueModeMgmt,
       "tnEgressQueueModeTable": tnEgressQueueModeTable,
       "tnEgressQueueModeEntry": tnEgressQueueModeEntry,
       "tnEgressQueueIfIndex": tnEgressQueueIfIndex,
       "tnEgressQueueMode": tnEgressQueueMode,
       "tnMgmtConformance": tnMgmtConformance}
)
