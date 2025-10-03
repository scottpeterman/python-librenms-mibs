# SNMP MIB module (WRI-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-DEVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:12 2025
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

(wriProducts,
 wriProtocol) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wriProducts",
    "wriProtocol")


# MODULE-IDENTITY


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8




# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"


class RerRingDir(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("west", 0),
          ("east", 1))
    )



class EntryStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )



class VlanIndex(TextualConvention, Unsigned32):
    status = "current"


class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_MsppDev_ObjectIdentity = ObjectIdentity
msppDev = _MsppDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2)
)
_MsppDevGeneral_ObjectIdentity = ObjectIdentity
msppDevGeneral = _MsppDevGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1)
)


class _MsppDevMac_Type(PhysAddress):
    """Custom type msppDevMac based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_MsppDevMac_Type.__name__ = "PhysAddress"
_MsppDevMac_Object = MibScalar
msppDevMac = _MsppDevMac_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 1),
    _MsppDevMac_Type()
)
msppDevMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevMac.setStatus("current")


class _MsppDevDescr_Type(DisplayString):
    """Custom type msppDevDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevDescr_Type.__name__ = "DisplayString"
_MsppDevDescr_Object = MibScalar
msppDevDescr = _MsppDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 2),
    _MsppDevDescr_Type()
)
msppDevDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevDescr.setStatus("current")


class _MsppDevHwVersion_Type(DisplayString):
    """Custom type msppDevHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevHwVersion_Type.__name__ = "DisplayString"
_MsppDevHwVersion_Object = MibScalar
msppDevHwVersion = _MsppDevHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 3),
    _MsppDevHwVersion_Type()
)
msppDevHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevHwVersion.setStatus("current")


class _MsppDevSwVersion_Type(DisplayString):
    """Custom type msppDevSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevSwVersion_Type.__name__ = "DisplayString"
_MsppDevSwVersion_Object = MibScalar
msppDevSwVersion = _MsppDevSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 4),
    _MsppDevSwVersion_Type()
)
msppDevSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevSwVersion.setStatus("current")
_MsppDevCardBits_Type = Counter32
_MsppDevCardBits_Object = MibScalar
msppDevCardBits = _MsppDevCardBits_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 5),
    _MsppDevCardBits_Type()
)
msppDevCardBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevCardBits.setStatus("current")
_MsppDevCardNum_Type = Integer32
_MsppDevCardNum_Object = MibScalar
msppDevCardNum = _MsppDevCardNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 6),
    _MsppDevCardNum_Type()
)
msppDevCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevCardNum.setStatus("current")
_MsppDevLastChange_Type = TimeTicks
_MsppDevLastChange_Object = MibScalar
msppDevLastChange = _MsppDevLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 7),
    _MsppDevLastChange_Type()
)
msppDevLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevLastChange.setStatus("current")
_MsppDevUpTime_Type = TimeTicks
_MsppDevUpTime_Object = MibScalar
msppDevUpTime = _MsppDevUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 8),
    _MsppDevUpTime_Type()
)
msppDevUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevUpTime.setStatus("current")


class _MsppDevTime_Type(DisplayString):
    """Custom type msppDevTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsppDevTime_Type.__name__ = "DisplayString"
_MsppDevTime_Object = MibScalar
msppDevTime = _MsppDevTime_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 9),
    _MsppDevTime_Type()
)
msppDevTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTime.setStatus("current")


class _MsppDevFlushMac_Type(Integer32):
    """Custom type msppDevFlushMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_MsppDevFlushMac_Type.__name__ = "Integer32"
_MsppDevFlushMac_Object = MibScalar
msppDevFlushMac = _MsppDevFlushMac_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 10),
    _MsppDevFlushMac_Type()
)
msppDevFlushMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFlushMac.setStatus("current")


class _MsppDevReboot_Type(Integer32):
    """Custom type msppDevReboot based on Integer32"""
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
        *(("reboot", 1),
          ("writeconfigandreboot", 2),
          ("writeconfigandrebootsys", 3),
          ("eraseconfigandreboot", 4),
          ("eraseconfigandrebootsys", 5))
    )


_MsppDevReboot_Type.__name__ = "Integer32"
_MsppDevReboot_Object = MibScalar
msppDevReboot = _MsppDevReboot_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 11),
    _MsppDevReboot_Type()
)
msppDevReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevReboot.setStatus("current")


class _MsppDevCfgFile_Type(DisplayString):
    """Custom type msppDevCfgFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevCfgFile_Type.__name__ = "DisplayString"
_MsppDevCfgFile_Object = MibScalar
msppDevCfgFile = _MsppDevCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 12),
    _MsppDevCfgFile_Type()
)
msppDevCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevCfgFile.setStatus("current")


class _MsppDevCfgAction_Type(Integer32):
    """Custom type msppDevCfgAction based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("write", 1),
          ("erase", 2),
          ("exec", 3),
          ("upgrade", 4),
          ("writestartup", 5),
          ("erasestartup", 6),
          ("execstartup", 7),
          ("upgradestartup", 8),
          ("writebackup", 9),
          ("erasebackup", 10),
          ("execbackup", 11),
          ("upgradebackup", 12),
          ("writeboth", 13),
          ("eraseboth", 14),
          ("upgradeboth", 15),
          ("recoverconfig", 16))
    )


_MsppDevCfgAction_Type.__name__ = "Integer32"
_MsppDevCfgAction_Object = MibScalar
msppDevCfgAction = _MsppDevCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 13),
    _MsppDevCfgAction_Type()
)
msppDevCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevCfgAction.setStatus("current")


class _MsppDevOsFile_Type(DisplayString):
    """Custom type msppDevOsFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevOsFile_Type.__name__ = "DisplayString"
_MsppDevOsFile_Object = MibScalar
msppDevOsFile = _MsppDevOsFile_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 14),
    _MsppDevOsFile_Type()
)
msppDevOsFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevOsFile.setStatus("current")


class _MsppDevOsAction_Type(Integer32):
    """Custom type msppDevOsAction based on Integer32"""
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
        *(("upgradebootos", 1),
          ("upgradebootosandreboot", 2),
          ("upgrademainos", 3),
          ("upgradebakos", 4),
          ("upgradebothos", 5),
          ("recoverbootos", 6))
    )


_MsppDevOsAction_Type.__name__ = "Integer32"
_MsppDevOsAction_Object = MibScalar
msppDevOsAction = _MsppDevOsAction_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 15),
    _MsppDevOsAction_Type()
)
msppDevOsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevOsAction.setStatus("current")


class _MsppDevVer_Type(Integer32):
    """Custom type msppDevVer based on Integer32"""
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
        *(("mspp1", 1),
          ("mspp2EO", 2),
          ("mspp2O", 3),
          ("mspp3", 4))
    )


_MsppDevVer_Type.__name__ = "Integer32"
_MsppDevVer_Object = MibScalar
msppDevVer = _MsppDevVer_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 16),
    _MsppDevVer_Type()
)
msppDevVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevVer.setStatus("current")
_MsppDevErrorBits_Type = Counter32
_MsppDevErrorBits_Object = MibScalar
msppDevErrorBits = _MsppDevErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 17),
    _MsppDevErrorBits_Type()
)
msppDevErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevErrorBits.setStatus("current")
_MsppDevTemperatureLThreshold_Type = Integer32
_MsppDevTemperatureLThreshold_Object = MibScalar
msppDevTemperatureLThreshold = _MsppDevTemperatureLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 18),
    _MsppDevTemperatureLThreshold_Type()
)
msppDevTemperatureLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTemperatureLThreshold.setStatus("current")
_MsppDevTemperatureHThreshold_Type = Integer32
_MsppDevTemperatureHThreshold_Object = MibScalar
msppDevTemperatureHThreshold = _MsppDevTemperatureHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 19),
    _MsppDevTemperatureHThreshold_Type()
)
msppDevTemperatureHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTemperatureHThreshold.setStatus("current")
_MsppDevTemperature_Type = Integer32
_MsppDevTemperature_Object = MibScalar
msppDevTemperature = _MsppDevTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 20),
    _MsppDevTemperature_Type()
)
msppDevTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTemperature.setStatus("current")
_MsppDevTemperatureTrapEnable_Type = Integer32
_MsppDevTemperatureTrapEnable_Object = MibScalar
msppDevTemperatureTrapEnable = _MsppDevTemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 21),
    _MsppDevTemperatureTrapEnable_Type()
)
msppDevTemperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTemperatureTrapEnable.setStatus("current")


class _MsppDevWRED_Type(Integer32):
    """Custom type msppDevWRED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsppDevWRED_Type.__name__ = "Integer32"
_MsppDevWRED_Object = MibScalar
msppDevWRED = _MsppDevWRED_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 22),
    _MsppDevWRED_Type()
)
msppDevWRED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevWRED.setStatus("current")
_MsppDevMirrorToPort_Type = Integer32
_MsppDevMirrorToPort_Object = MibScalar
msppDevMirrorToPort = _MsppDevMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 23),
    _MsppDevMirrorToPort_Type()
)
msppDevMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevMirrorToPort.setStatus("current")
_MsppDevMirrorMode_Type = Integer32
_MsppDevMirrorMode_Object = MibScalar
msppDevMirrorMode = _MsppDevMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 24),
    _MsppDevMirrorMode_Type()
)
msppDevMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevMirrorMode.setStatus("current")
_MsppDevLcd_Type = Integer32
_MsppDevLcd_Object = MibScalar
msppDevLcd = _MsppDevLcd_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 25),
    _MsppDevLcd_Type()
)
msppDevLcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevLcd.setStatus("current")
_MsppDevTDMVlan_Type = Integer32
_MsppDevTDMVlan_Object = MibScalar
msppDevTDMVlan = _MsppDevTDMVlan_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 26),
    _MsppDevTDMVlan_Type()
)
msppDevTDMVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTDMVlan.setStatus("current")
_MsppDevFtpd_Type = Integer32
_MsppDevFtpd_Object = MibScalar
msppDevFtpd = _MsppDevFtpd_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 27),
    _MsppDevFtpd_Type()
)
msppDevFtpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFtpd.setStatus("current")
_MsppDevTelnetd_Type = Integer32
_MsppDevTelnetd_Object = MibScalar
msppDevTelnetd = _MsppDevTelnetd_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 28),
    _MsppDevTelnetd_Type()
)
msppDevTelnetd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTelnetd.setStatus("current")
_MsppDevMirrorToRspanVid_Type = Integer32
_MsppDevMirrorToRspanVid_Object = MibScalar
msppDevMirrorToRspanVid = _MsppDevMirrorToRspanVid_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 29),
    _MsppDevMirrorToRspanVid_Type()
)
msppDevMirrorToRspanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevMirrorToRspanVid.setStatus("current")
_MsppDevMirrorToTpid_Type = Integer32
_MsppDevMirrorToTpid_Object = MibScalar
msppDevMirrorToTpid = _MsppDevMirrorToTpid_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 30),
    _MsppDevMirrorToTpid_Type()
)
msppDevMirrorToTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevMirrorToTpid.setStatus("current")


class _MsppRebootFileMode_Type(Integer32):
    """Custom type msppRebootFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("backup", 1))
    )


_MsppRebootFileMode_Type.__name__ = "Integer32"
_MsppRebootFileMode_Object = MibScalar
msppRebootFileMode = _MsppRebootFileMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 31),
    _MsppRebootFileMode_Type()
)
msppRebootFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppRebootFileMode.setStatus("current")


class _MsppFileExecMode_Type(Integer32):
    """Custom type msppFileExecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("backup", 1))
    )


_MsppFileExecMode_Type.__name__ = "Integer32"
_MsppFileExecMode_Object = MibScalar
msppFileExecMode = _MsppFileExecMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 32),
    _MsppFileExecMode_Type()
)
msppFileExecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppFileExecMode.setStatus("current")


class _MsppUpgradeBkOs_Type(Integer32):
    """Custom type msppUpgradeBkOs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("backup", 1))
    )


_MsppUpgradeBkOs_Type.__name__ = "Integer32"
_MsppUpgradeBkOs_Object = MibScalar
msppUpgradeBkOs = _MsppUpgradeBkOs_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 33),
    _MsppUpgradeBkOs_Type()
)
msppUpgradeBkOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppUpgradeBkOs.setStatus("current")


class _MsppInbandIp_Type(DisplayString):
    """Custom type msppInbandIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MsppInbandIp_Type.__name__ = "DisplayString"
_MsppInbandIp_Object = MibScalar
msppInbandIp = _MsppInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 34),
    _MsppInbandIp_Type()
)
msppInbandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppInbandIp.setStatus("current")


class _MsppOutbandIp_Type(DisplayString):
    """Custom type msppOutbandIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MsppOutbandIp_Type.__name__ = "DisplayString"
_MsppOutbandIp_Object = MibScalar
msppOutbandIp = _MsppOutbandIp_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 35),
    _MsppOutbandIp_Type()
)
msppOutbandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppOutbandIp.setStatus("current")


class _ResetEraseCfg_Type(Integer32):
    """Custom type resetEraseCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ResetEraseCfg_Type.__name__ = "Integer32"
_ResetEraseCfg_Object = MibScalar
resetEraseCfg = _ResetEraseCfg_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 36),
    _ResetEraseCfg_Type()
)
resetEraseCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetEraseCfg.setStatus("current")


class _MsppDevLicenseEnable_Type(Integer32):
    """Custom type msppDevLicenseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsppDevLicenseEnable_Type.__name__ = "Integer32"
_MsppDevLicenseEnable_Object = MibScalar
msppDevLicenseEnable = _MsppDevLicenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 37),
    _MsppDevLicenseEnable_Type()
)
msppDevLicenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevLicenseEnable.setStatus("current")


class _MsppDevLicenseKey_Type(DisplayString):
    """Custom type msppDevLicenseKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsppDevLicenseKey_Type.__name__ = "DisplayString"
_MsppDevLicenseKey_Object = MibScalar
msppDevLicenseKey = _MsppDevLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 38),
    _MsppDevLicenseKey_Type()
)
msppDevLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevLicenseKey.setStatus("current")


class _MsppDevSerialNum_Type(DisplayString):
    """Custom type msppDevSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsppDevSerialNum_Type.__name__ = "DisplayString"
_MsppDevSerialNum_Object = MibScalar
msppDevSerialNum = _MsppDevSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 39),
    _MsppDevSerialNum_Type()
)
msppDevSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevSerialNum.setStatus("current")
_MsppDevMtu_Type = Unsigned32
_MsppDevMtu_Object = MibScalar
msppDevMtu = _MsppDevMtu_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 40),
    _MsppDevMtu_Type()
)
msppDevMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevMtu.setStatus("current")
_MsppDevFlushDynamicArp_Type = Unsigned32
_MsppDevFlushDynamicArp_Object = MibScalar
msppDevFlushDynamicArp = _MsppDevFlushDynamicArp_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 41),
    _MsppDevFlushDynamicArp_Type()
)
msppDevFlushDynamicArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFlushDynamicArp.setStatus("current")
_MsppDevFlushStaticArp_Type = Unsigned32
_MsppDevFlushStaticArp_Object = MibScalar
msppDevFlushStaticArp = _MsppDevFlushStaticArp_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 42),
    _MsppDevFlushStaticArp_Type()
)
msppDevFlushStaticArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFlushStaticArp.setStatus("current")
_MsppDevFlushAllArp_Type = Unsigned32
_MsppDevFlushAllArp_Object = MibScalar
msppDevFlushAllArp = _MsppDevFlushAllArp_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 43),
    _MsppDevFlushAllArp_Type()
)
msppDevFlushAllArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFlushAllArp.setStatus("current")


class _MsppDevBootOs_Type(Integer32):
    """Custom type msppDevBootOs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("backup", 1))
    )


_MsppDevBootOs_Type.__name__ = "Integer32"
_MsppDevBootOs_Object = MibScalar
msppDevBootOs = _MsppDevBootOs_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 44),
    _MsppDevBootOs_Type()
)
msppDevBootOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevBootOs.setStatus("current")


class _MsppDevBootCfg_Type(Integer32):
    """Custom type msppDevBootCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("backup", 1))
    )


_MsppDevBootCfg_Type.__name__ = "Integer32"
_MsppDevBootCfg_Object = MibScalar
msppDevBootCfg = _MsppDevBootCfg_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 45),
    _MsppDevBootCfg_Type()
)
msppDevBootCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevBootCfg.setStatus("current")


class _Msppl2HashMode_Type(Integer32):
    """Custom type msppl2HashMode based on Integer32"""
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
        *(("crc32-upper", 1),
          ("crc32-lower", 2),
          ("lsb", 3),
          ("crc16-lower", 4),
          ("crc16-upper", 5))
    )


_Msppl2HashMode_Type.__name__ = "Integer32"
_Msppl2HashMode_Object = MibScalar
msppl2HashMode = _Msppl2HashMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 46),
    _Msppl2HashMode_Type()
)
msppl2HashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppl2HashMode.setStatus("current")


class _Msppl3HashMode_Type(Integer32):
    """Custom type msppl3HashMode based on Integer32"""
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
        *(("crc32-upper", 1),
          ("crc32-lower", 2),
          ("lsb", 3),
          ("crc16-lower", 4),
          ("crc16-upper", 5))
    )


_Msppl3HashMode_Type.__name__ = "Integer32"
_Msppl3HashMode_Object = MibScalar
msppl3HashMode = _Msppl3HashMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 47),
    _Msppl3HashMode_Type()
)
msppl3HashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppl3HashMode.setStatus("current")


class _Msppl2AuxHashMode_Type(Integer32):
    """Custom type msppl2AuxHashMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("zero", 0),
          ("crc32-upper", 1),
          ("crc32-lower", 2),
          ("lsb", 3),
          ("crc16-lower", 4),
          ("crc16-upper", 5))
    )


_Msppl2AuxHashMode_Type.__name__ = "Integer32"
_Msppl2AuxHashMode_Object = MibScalar
msppl2AuxHashMode = _Msppl2AuxHashMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 48),
    _Msppl2AuxHashMode_Type()
)
msppl2AuxHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppl2AuxHashMode.setStatus("current")
_MsppIpv4AddrNum_Type = Integer32
_MsppIpv4AddrNum_Object = MibScalar
msppIpv4AddrNum = _MsppIpv4AddrNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 49),
    _MsppIpv4AddrNum_Type()
)
msppIpv4AddrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppIpv4AddrNum.setStatus("current")


class _MsppDevCode_Type(DisplayString):
    """Custom type msppDevCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsppDevCode_Type.__name__ = "DisplayString"
_MsppDevCode_Object = MibScalar
msppDevCode = _MsppDevCode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 50),
    _MsppDevCode_Type()
)
msppDevCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevCode.setStatus("current")
_MsppCmuState_Type = Integer32
_MsppCmuState_Object = MibScalar
msppCmuState = _MsppCmuState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 51),
    _MsppCmuState_Type()
)
msppCmuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppCmuState.setStatus("current")
_MsppDevTpid_Type = Unsigned32
_MsppDevTpid_Object = MibScalar
msppDevTpid = _MsppDevTpid_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 52),
    _MsppDevTpid_Type()
)
msppDevTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevTpid.setStatus("current")


class _MsppDevLoggingInfo_Type(DisplayString):
    """Custom type msppDevLoggingInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MsppDevLoggingInfo_Type.__name__ = "DisplayString"
_MsppDevLoggingInfo_Object = MibScalar
msppDevLoggingInfo = _MsppDevLoggingInfo_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 53),
    _MsppDevLoggingInfo_Type()
)
msppDevLoggingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppDevLoggingInfo.setStatus("current")
_LoggingTrapObjects_ObjectIdentity = ObjectIdentity
loggingTrapObjects = _LoggingTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 54)
)


class _MsppDevFileName_Type(DisplayString):
    """Custom type msppDevFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsppDevFileName_Type.__name__ = "DisplayString"
_MsppDevFileName_Object = MibScalar
msppDevFileName = _MsppDevFileName_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 55),
    _MsppDevFileName_Type()
)
msppDevFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFileName.setStatus("current")


class _MsppDevFileAction_Type(Integer32):
    """Custom type msppDevFileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delet", 1)
    )


_MsppDevFileAction_Type.__name__ = "Integer32"
_MsppDevFileAction_Object = MibScalar
msppDevFileAction = _MsppDevFileAction_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 56),
    _MsppDevFileAction_Type()
)
msppDevFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppDevFileAction.setStatus("current")


class _MsppShareVlanEn_Type(Integer32):
    """Custom type msppShareVlanEn based on Integer32"""
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


_MsppShareVlanEn_Type.__name__ = "Integer32"
_MsppShareVlanEn_Object = MibScalar
msppShareVlanEn = _MsppShareVlanEn_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 57),
    _MsppShareVlanEn_Type()
)
msppShareVlanEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msppShareVlanEn.setStatus("current")
_MsppUpgradeStatus_Type = Integer32
_MsppUpgradeStatus_Object = MibScalar
msppUpgradeStatus = _MsppUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 58),
    _MsppUpgradeStatus_Type()
)
msppUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppUpgradeStatus.setStatus("current")
_MsppCliVersion_Type = OctetString
_MsppCliVersion_Object = MibScalar
msppCliVersion = _MsppCliVersion_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 59),
    _MsppCliVersion_Type()
)
msppCliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppCliVersion.setStatus("current")
_MsppSnmpVersion_Type = OctetString
_MsppSnmpVersion_Object = MibScalar
msppSnmpVersion = _MsppSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 60),
    _MsppSnmpVersion_Type()
)
msppSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppSnmpVersion.setStatus("current")
_MsppHttpVersion_Type = OctetString
_MsppHttpVersion_Object = MibScalar
msppHttpVersion = _MsppHttpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 61),
    _MsppHttpVersion_Type()
)
msppHttpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msppHttpVersion.setStatus("current")

# Managed Objects groups


# Notification objects

loggingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 2, 1, 54, 1)
)
loggingTrap.setObjects(
      *(("WRI-DEVICE-MIB", "msppDevMac"),
        ("WRI-DEVICE-MIB", "msppDevDescr"),
        ("WRI-DEVICE-MIB", "msppDevLoggingInfo"))
)
if mibBuilder.loadTexts:
    loggingTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-DEVICE-MIB",
    **{"PortList": PortList,
       "BridgeId": BridgeId,
       "DisplayString": DisplayString,
       "RerRingDir": RerRingDir,
       "EntryStatus": EntryStatus,
       "VlanIndex": VlanIndex,
       "VlanId": VlanId,
       "mspp": mspp,
       "msppChassis": msppChassis,
       "msppDev": msppDev,
       "msppDevGeneral": msppDevGeneral,
       "msppDevMac": msppDevMac,
       "msppDevDescr": msppDevDescr,
       "msppDevHwVersion": msppDevHwVersion,
       "msppDevSwVersion": msppDevSwVersion,
       "msppDevCardBits": msppDevCardBits,
       "msppDevCardNum": msppDevCardNum,
       "msppDevLastChange": msppDevLastChange,
       "msppDevUpTime": msppDevUpTime,
       "msppDevTime": msppDevTime,
       "msppDevFlushMac": msppDevFlushMac,
       "msppDevReboot": msppDevReboot,
       "msppDevCfgFile": msppDevCfgFile,
       "msppDevCfgAction": msppDevCfgAction,
       "msppDevOsFile": msppDevOsFile,
       "msppDevOsAction": msppDevOsAction,
       "msppDevVer": msppDevVer,
       "msppDevErrorBits": msppDevErrorBits,
       "msppDevTemperatureLThreshold": msppDevTemperatureLThreshold,
       "msppDevTemperatureHThreshold": msppDevTemperatureHThreshold,
       "msppDevTemperature": msppDevTemperature,
       "msppDevTemperatureTrapEnable": msppDevTemperatureTrapEnable,
       "msppDevWRED": msppDevWRED,
       "msppDevMirrorToPort": msppDevMirrorToPort,
       "msppDevMirrorMode": msppDevMirrorMode,
       "msppDevLcd": msppDevLcd,
       "msppDevTDMVlan": msppDevTDMVlan,
       "msppDevFtpd": msppDevFtpd,
       "msppDevTelnetd": msppDevTelnetd,
       "msppDevMirrorToRspanVid": msppDevMirrorToRspanVid,
       "msppDevMirrorToTpid": msppDevMirrorToTpid,
       "msppRebootFileMode": msppRebootFileMode,
       "msppFileExecMode": msppFileExecMode,
       "msppUpgradeBkOs": msppUpgradeBkOs,
       "msppInbandIp": msppInbandIp,
       "msppOutbandIp": msppOutbandIp,
       "resetEraseCfg": resetEraseCfg,
       "msppDevLicenseEnable": msppDevLicenseEnable,
       "msppDevLicenseKey": msppDevLicenseKey,
       "msppDevSerialNum": msppDevSerialNum,
       "msppDevMtu": msppDevMtu,
       "msppDevFlushDynamicArp": msppDevFlushDynamicArp,
       "msppDevFlushStaticArp": msppDevFlushStaticArp,
       "msppDevFlushAllArp": msppDevFlushAllArp,
       "msppDevBootOs": msppDevBootOs,
       "msppDevBootCfg": msppDevBootCfg,
       "msppl2HashMode": msppl2HashMode,
       "msppl3HashMode": msppl3HashMode,
       "msppl2AuxHashMode": msppl2AuxHashMode,
       "msppIpv4AddrNum": msppIpv4AddrNum,
       "msppDevCode": msppDevCode,
       "msppCmuState": msppCmuState,
       "msppDevTpid": msppDevTpid,
       "msppDevLoggingInfo": msppDevLoggingInfo,
       "loggingTrapObjects": loggingTrapObjects,
       "loggingTrap": loggingTrap,
       "msppDevFileName": msppDevFileName,
       "msppDevFileAction": msppDevFileAction,
       "msppShareVlanEn": msppShareVlanEn,
       "msppUpgradeStatus": msppUpgradeStatus,
       "msppCliVersion": msppCliVersion,
       "msppSnmpVersion": msppSnmpVersion,
       "msppHttpVersion": msppHttpVersion}
)
