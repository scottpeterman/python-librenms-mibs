# SNMP MIB module (TROPIC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:10 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TmnxEnabledDisabled,
 TnSwitchID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TmnxEnabledDisabled",
    "TnSwitchID")

(tnSystemMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSystemMIB",
    "tnSystemModules")

(tnEthIfIndex,
 tnNetIfIndex) = mibBuilder.importSymbols(
    "TROPIC-L1SERVICE-MIB",
    "tnEthIfIndex",
    "tnNetIfIndex")

(AluWdmCardCapacity,
 AluWdmDisabledEnabled,
 AluWdmEnabledDisabled,
 AluWdmNewTransferProtocol,
 AluWdmTransferProtocol,
 TnCommand,
 TropicAdminStateType,
 TropicOperationalStateType,
 TropicResetType,
 TropicSourceIpModeValue) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmCardCapacity",
    "AluWdmDisabledEnabled",
    "AluWdmEnabledDisabled",
    "AluWdmNewTransferProtocol",
    "AluWdmTransferProtocol",
    "TnCommand",
    "TropicAdminStateType",
    "TropicOperationalStateType",
    "TropicResetType",
    "TropicSourceIpModeValue")


# MODULE-IDENTITY

tnSystemMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSystemMibModule.setRevisions(
        ("2023-04-07 12:00",
         "2023-03-17 12:00",
         "2023-03-03 12:00",
         "2023-02-17 12:00",
         "2023-02-10 12:00",
         "2023-01-13 12:00",
         "2023-01-06 12:00",
         "2022-12-23 12:00",
         "2022-11-25 12:00",
         "2022-10-14 12:00",
         "2022-09-30 12:00",
         "2022-09-23 12:00",
         "2022-08-26 12:00",
         "2022-08-19 12:00",
         "2022-07-29 12:00",
         "2022-07-22 12:00",
         "2022-07-15 12:00",
         "2022-07-08 12:00",
         "2022-07-01 12:00",
         "2022-05-27 12:00",
         "2022-02-11 12:00",
         "2022-02-04 12:00",
         "2022-01-28 12:00",
         "2022-01-07 12:00",
         "2021-12-31 12:00",
         "2021-12-24 12:00",
         "2021-12-03 12:00",
         "2021-11-26 12:00",
         "2021-10-15 12:00",
         "2021-10-01 12:00",
         "2021-09-24 12:00",
         "2021-09-10 12:00",
         "2021-09-03 12:00",
         "2021-08-27 12:00",
         "2021-08-20 12:00",
         "2021-08-06 12:00",
         "2021-07-16 12:00",
         "2021-07-02 12:00",
         "2021-06-11 12:00",
         "2021-05-28 12:00",
         "2021-05-14 12:00",
         "2021-05-07 12:00",
         "2021-04-23 12:00",
         "2021-04-16 12:00",
         "2021-04-02 12:00",
         "2021-03-26 12:00",
         "2021-03-19 12:00",
         "2021-02-26 12:00",
         "2021-02-19 12:00",
         "2021-02-05 12:00",
         "2021-01-22 12:00",
         "2020-12-04 12:00",
         "2020-11-06 12:00",
         "2020-10-23 12:00",
         "2020-10-09 12:00",
         "2020-08-28 12:00",
         "2020-08-07 12:00",
         "2020-07-24 12:00",
         "2020-05-29 12:00",
         "2020-05-01 12:00",
         "2020-04-10 12:00",
         "2020-04-03 12:00",
         "2020-03-27 12:00",
         "2020-03-20 12:00",
         "2020-03-06 12:00",
         "2020-02-28 12:00",
         "2020-02-21 12:00",
         "2020-02-07 12:00",
         "2020-01-31 12:00",
         "2020-01-24 12:00",
         "2020-01-17 12:00",
         "2020-01-03 12:00",
         "2019-12-06 12:00",
         "2019-11-22 12:00",
         "2019-11-15 12:00",
         "2019-11-01 12:00",
         "2019-10-11 12:00",
         "2019-08-30 12:00",
         "2019-07-19 12:00",
         "2019-07-12 12:00",
         "2019-07-05 12:00",
         "2019-06-28 12:00",
         "2019-06-21 12:00",
         "2019-06-14 12:00",
         "2019-06-07 12:00",
         "2019-05-31 12:00",
         "2019-05-17 12:00",
         "2019-05-03 12:00",
         "2019-04-26 12:00",
         "2019-04-19 12:00",
         "2019-04-05 12:00",
         "2019-03-29 12:00",
         "2019-03-15 12:00",
         "2019-02-15 12:00",
         "2019-02-08 12:00",
         "2019-01-25 12:00",
         "2018-12-21 12:00",
         "2018-12-14 12:00",
         "2018-12-06 12:00",
         "2018-11-30 12:00",
         "2018-10-26 12:00",
         "2018-10-12 12:00",
         "2018-10-10 12:00",
         "2018-09-28 12:00",
         "2018-09-21 12:00",
         "2018-09-14 12:00",
         "2018-09-07 12:00",
         "2018-08-31 12:00",
         "2018-04-27 12:00",
         "2018-03-02 12:00",
         "2018-02-23 12:00",
         "2018-02-16 12:00",
         "2018-01-26 12:00",
         "2017-12-13 12:00",
         "2017-12-08 12:00",
         "2017-12-01 12:00",
         "2017-09-08 12:00",
         "2017-07-07 12:00",
         "2017-04-28 12:00",
         "2017-04-13 12:00",
         "2017-04-07 12:00",
         "2017-03-03 12:00",
         "2017-02-24 12:00",
         "2017-02-17 12:00",
         "2017-02-10 12:00",
         "2017-02-03 12:00",
         "2017-01-27 12:00",
         "2017-01-20 12:00",
         "2017-01-13 12:00",
         "2016-12-28 12:00",
         "2016-12-21 12:00",
         "2016-12-05 12:00",
         "2016-11-29 12:00",
         "2016-11-28 12:00",
         "2016-11-22 12:00",
         "2016-11-18 12:00",
         "2016-11-16 12:00",
         "2016-11-07 12:00",
         "2016-10-20 12:00",
         "2016-09-27 12:00",
         "2016-09-16 12:00",
         "2016-09-09 12:00",
         "2016-07-29 12:00",
         "2016-07-25 12:00",
         "2016-06-23 12:00",
         "2016-06-15 12:00",
         "2016-04-01 12:00",
         "2016-03-30 12:00",
         "2016-03-04 12:00",
         "2016-03-02 12:00",
         "2016-02-26 12:00",
         "2016-02-01 12:00",
         "2016-01-27 12:00",
         "2015-12-17 12:00",
         "2015-12-10 12:00",
         "2015-12-03 12:00",
         "2015-11-17 12:00",
         "2015-09-30 12:00",
         "2015-09-16 12:00",
         "2015-07-13 12:00",
         "2015-07-12 12:00",
         "2015-02-20 12:00",
         "2014-04-23 12:00",
         "2014-03-30 12:00",
         "2014-03-04 12:00",
         "2014-02-26 12:00",
         "2013-11-20 12:00",
         "2013-04-19 12:00",
         "2013-04-17 12:00",
         "2013-03-20 12:00",
         "2013-03-06 12:00",
         "2013-01-31 12:00",
         "2013-01-20 12:00",
         "2013-01-16 12:00",
         "2012-05-18 12:00",
         "2012-02-16 12:00",
         "2012-01-12 12:00",
         "2011-10-24 12:00",
         "2011-09-30 12:00",
         "2011-08-12 12:00",
         "2011-06-21 12:00",
         "2011-06-03 12:00",
         "2011-05-23 12:00",
         "2011-04-25 12:00",
         "2011-03-28 12:00",
         "2011-03-17 12:00",
         "2011-03-15 12:00",
         "2010-11-11 12:00",
         "2010-10-18 12:00",
         "2010-06-22 12:00",
         "2010-01-11 12:00",
         "2010-01-07 12:00",
         "2009-07-22 12:00",
         "2009-05-05 12:00",
         "2009-04-30 12:00",
         "2009-04-28 12:00",
         "2009-04-08 12:00",
         "2009-04-07 12:00",
         "2009-03-03 12:00",
         "2009-02-27 12:00",
         "2008-10-14 12:00",
         "2008-10-10 12:00",
         "2008-05-29 12:00",
         "2008-04-05 12:00",
         "2008-02-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicSysTimingReferenceQuality(TextualConvention, Integer32):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("prs", 2),
          ("stu", 3),
          ("st2", 4),
          ("tnc", 5),
          ("st3e", 6),
          ("st3", 7),
          ("smc", 8),
          ("st4", 9),
          ("dus", 10),
          ("prc", 11),
          ("ssua", 12),
          ("ssub", 13),
          ("sec", 14),
          ("dnu", 15))
    )



class TropicSysTimingReferenceTimingMode(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("external", 2),
          ("line", 3),
          ("through", 4),
          ("loop", 5),
          ("local", 6))
    )



class AluWdmSslOperationStatus(TextualConvention, Integer32):
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("none", 4))
    )



class AluWdmTransferStatus(TextualConvention, Integer32):
    status = "current"
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
          ("completed", 2),
          ("inProgress", 3),
          ("failure", 4),
          ("failTimeout", 5))
    )



class AluWdmOcsLinkStatus(TextualConvention, Integer32):
    status = "current"
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
          ("notConnected", 3))
    )



class NokiaSysBgpMaxPrefixAction(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("alarmOnly", 2),
          ("tearDown", 3),
          ("restartInterval", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnSystemConf_ObjectIdentity = ObjectIdentity
tnSystemConf = _TnSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1)
)
_TnSystemGroups_ObjectIdentity = ObjectIdentity
tnSystemGroups = _TnSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1)
)
_TnSystemCompliances_ObjectIdentity = ObjectIdentity
tnSystemCompliances = _TnSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 2)
)
_TnSystemObjs_ObjectIdentity = ObjectIdentity
tnSystemObjs = _TnSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2)
)
_TnSysBasics_ObjectIdentity = ObjectIdentity
tnSysBasics = _TnSysBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1)
)


class _TnSysDescr_Type(SnmpAdminString):
    """Custom type tnSysDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDescr_Type.__name__ = "SnmpAdminString"
_TnSysDescr_Object = MibScalar
tnSysDescr = _TnSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 1),
    _TnSysDescr_Type()
)
tnSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDescr.setStatus("current")


class _TnSysTelnetPort_Type(Unsigned32):
    """Custom type tnSysTelnetPort based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysTelnetPort_Type.__name__ = "Unsigned32"
_TnSysTelnetPort_Object = MibScalar
tnSysTelnetPort = _TnSysTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 2),
    _TnSysTelnetPort_Type()
)
tnSysTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTelnetPort.setStatus("current")


class _TnSysHttpPort_Type(Unsigned32):
    """Custom type tnSysHttpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysHttpPort_Type.__name__ = "Unsigned32"
_TnSysHttpPort_Object = MibScalar
tnSysHttpPort = _TnSysHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 3),
    _TnSysHttpPort_Type()
)
tnSysHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHttpPort.setStatus("current")
_TnSysDateAndTime_Type = DateAndTime
_TnSysDateAndTime_Object = MibScalar
tnSysDateAndTime = _TnSysDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 4),
    _TnSysDateAndTime_Type()
)
tnSysDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDateAndTime.setStatus("current")


class _TnSysReset_Type(TropicResetType):
    """Custom type tnSysReset based on TropicResetType"""
    defaultValue = 1


_TnSysReset_Type.__name__ = "TropicResetType"
_TnSysReset_Object = MibScalar
tnSysReset = _TnSysReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 5),
    _TnSysReset_Type()
)
tnSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysReset.setStatus("current")


class _TnSysMIBVersion_Type(SnmpAdminString):
    """Custom type tnSysMIBVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysMIBVersion_Type.__name__ = "SnmpAdminString"
_TnSysMIBVersion_Object = MibScalar
tnSysMIBVersion = _TnSysMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 6),
    _TnSysMIBVersion_Type()
)
tnSysMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMIBVersion.setStatus("current")


class _TnSysRingID_Type(Unsigned32):
    """Custom type tnSysRingID based on Unsigned32"""
    defaultValue = 0


_TnSysRingID_Type.__name__ = "Unsigned32"
_TnSysRingID_Object = MibScalar
tnSysRingID = _TnSysRingID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 7),
    _TnSysRingID_Type()
)
tnSysRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRingID.setStatus("current")


class _TnSysNetworkElementID_Type(Unsigned32):
    """Custom type tnSysNetworkElementID based on Unsigned32"""
    defaultValue = 0


_TnSysNetworkElementID_Type.__name__ = "Unsigned32"
_TnSysNetworkElementID_Object = MibScalar
tnSysNetworkElementID = _TnSysNetworkElementID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 8),
    _TnSysNetworkElementID_Type()
)
tnSysNetworkElementID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNetworkElementID.setStatus("current")


class _TnSysAINSDebounceTime_Type(Unsigned32):
    """Custom type tnSysAINSDebounceTime based on Unsigned32"""
    defaultValue = 600


_TnSysAINSDebounceTime_Type.__name__ = "Unsigned32"
_TnSysAINSDebounceTime_Object = MibScalar
tnSysAINSDebounceTime = _TnSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 9),
    _TnSysAINSDebounceTime_Type()
)
tnSysAINSDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysAINSDebounceTime.setUnits("seconds")


class _TnSysSonetSdhMode_Type(Integer32):
    """Custom type tnSysSonetSdhMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_TnSysSonetSdhMode_Type.__name__ = "Integer32"
_TnSysSonetSdhMode_Object = MibScalar
tnSysSonetSdhMode = _TnSysSonetSdhMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 10),
    _TnSysSonetSdhMode_Type()
)
tnSysSonetSdhMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSonetSdhMode.setStatus("current")


class _TnSysAlarmReportingControl_Type(Integer32):
    """Custom type tnSysAlarmReportingControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("released", 2),
          ("indefiniteInhibition", 3))
    )


_TnSysAlarmReportingControl_Type.__name__ = "Integer32"
_TnSysAlarmReportingControl_Object = MibScalar
tnSysAlarmReportingControl = _TnSysAlarmReportingControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 11),
    _TnSysAlarmReportingControl_Type()
)
tnSysAlarmReportingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAlarmReportingControl.setStatus("current")


class _TnSysWavelengthTrackerWaveKeySpace_Type(Unsigned32):
    """Custom type tnSysWavelengthTrackerWaveKeySpace based on Unsigned32"""
    defaultValue = 0


_TnSysWavelengthTrackerWaveKeySpace_Type.__name__ = "Unsigned32"
_TnSysWavelengthTrackerWaveKeySpace_Object = MibScalar
tnSysWavelengthTrackerWaveKeySpace = _TnSysWavelengthTrackerWaveKeySpace_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 12),
    _TnSysWavelengthTrackerWaveKeySpace_Type()
)
tnSysWavelengthTrackerWaveKeySpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysWavelengthTrackerWaveKeySpace.setStatus("current")


class _TnSysSecureMode_Type(Integer32):
    """Custom type tnSysSecureMode based on Integer32"""
    defaultValue = 2

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
          ("nonSecure", 2),
          ("secure", 3),
          ("fips", 4),
          ("anssi", 5))
    )


_TnSysSecureMode_Type.__name__ = "Integer32"
_TnSysSecureMode_Object = MibScalar
tnSysSecureMode = _TnSysSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 13),
    _TnSysSecureMode_Type()
)
tnSysSecureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSecureMode.setStatus("current")


class _TnSysExtendedTemperatureRange_Type(TruthValue):
    """Custom type tnSysExtendedTemperatureRange based on TruthValue"""
    defaultValue = 1


_TnSysExtendedTemperatureRange_Type.__name__ = "TruthValue"
_TnSysExtendedTemperatureRange_Object = MibScalar
tnSysExtendedTemperatureRange = _TnSysExtendedTemperatureRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 16),
    _TnSysExtendedTemperatureRange_Type()
)
tnSysExtendedTemperatureRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysExtendedTemperatureRange.setStatus("current")


class _TnSysTemperatureInCelsius_Type(TruthValue):
    """Custom type tnSysTemperatureInCelsius based on TruthValue"""
    defaultValue = 1


_TnSysTemperatureInCelsius_Type.__name__ = "TruthValue"
_TnSysTemperatureInCelsius_Object = MibScalar
tnSysTemperatureInCelsius = _TnSysTemperatureInCelsius_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 17),
    _TnSysTemperatureInCelsius_Type()
)
tnSysTemperatureInCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTemperatureInCelsius.setStatus("current")


class _TnSysName_Type(SnmpAdminString):
    """Custom type tnSysName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysName_Type.__name__ = "SnmpAdminString"
_TnSysName_Object = MibScalar
tnSysName = _TnSysName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 18),
    _TnSysName_Type()
)
tnSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysName.setStatus("current")


class _TnSysEquipmentControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysEquipmentControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysEquipmentControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysEquipmentControllerCapacity_Object = MibScalar
tnSysEquipmentControllerCapacity = _TnSysEquipmentControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 19),
    _TnSysEquipmentControllerCapacity_Type()
)
tnSysEquipmentControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysEquipmentControllerCapacity.setStatus("current")


class _TnSysFirstLevelControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysFirstLevelControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysFirstLevelControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysFirstLevelControllerCapacity_Object = MibScalar
tnSysFirstLevelControllerCapacity = _TnSysFirstLevelControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 20),
    _TnSysFirstLevelControllerCapacity_Type()
)
tnSysFirstLevelControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFirstLevelControllerCapacity.setStatus("current")


class _TnSysMatrix0CompactCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysMatrix0CompactCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysMatrix0CompactCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysMatrix0CompactCapacity_Object = MibScalar
tnSysMatrix0CompactCapacity = _TnSysMatrix0CompactCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 21),
    _TnSysMatrix0CompactCapacity_Type()
)
tnSysMatrix0CompactCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMatrix0CompactCapacity.setStatus("current")


class _TnSysUniversalMatrixFirstLevelControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysUniversalMatrixFirstLevelControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysUniversalMatrixFirstLevelControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysUniversalMatrixFirstLevelControllerCapacity_Object = MibScalar
tnSysUniversalMatrixFirstLevelControllerCapacity = _TnSysUniversalMatrixFirstLevelControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 22),
    _TnSysUniversalMatrixFirstLevelControllerCapacity_Type()
)
tnSysUniversalMatrixFirstLevelControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysUniversalMatrixFirstLevelControllerCapacity.setStatus("current")


class _TnSysTimeOffsetTimeZone_Type(SnmpAdminString):
    """Custom type tnSysTimeOffsetTimeZone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysTimeOffsetTimeZone_Type.__name__ = "SnmpAdminString"
_TnSysTimeOffsetTimeZone_Object = MibScalar
tnSysTimeOffsetTimeZone = _TnSysTimeOffsetTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 23),
    _TnSysTimeOffsetTimeZone_Type()
)
tnSysTimeOffsetTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimeOffsetTimeZone.setStatus("current")
_TnSysSwitchId_Type = TnSwitchID
_TnSysSwitchId_Object = MibScalar
tnSysSwitchId = _TnSysSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 26),
    _TnSysSwitchId_Type()
)
tnSysSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysSwitchId.setStatus("current")


class _TnSysFipsSquelchMode_Type(Integer32):
    """Custom type tnSysFipsSquelchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonFips", 1),
          ("fips", 2))
    )


_TnSysFipsSquelchMode_Type.__name__ = "Integer32"
_TnSysFipsSquelchMode_Object = MibScalar
tnSysFipsSquelchMode = _TnSysFipsSquelchMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 27),
    _TnSysFipsSquelchMode_Type()
)
tnSysFipsSquelchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFipsSquelchMode.setStatus("current")


class _TnSysOtdrListOfFileNames_Type(SnmpAdminString):
    """Custom type tnSysOtdrListOfFileNames based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_TnSysOtdrListOfFileNames_Type.__name__ = "SnmpAdminString"
_TnSysOtdrListOfFileNames_Object = MibScalar
tnSysOtdrListOfFileNames = _TnSysOtdrListOfFileNames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 28),
    _TnSysOtdrListOfFileNames_Type()
)
tnSysOtdrListOfFileNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrListOfFileNames.setStatus("current")
_TnSysOtdrFileCounts_Type = Unsigned32
_TnSysOtdrFileCounts_Object = MibScalar
tnSysOtdrFileCounts = _TnSysOtdrFileCounts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 29),
    _TnSysOtdrFileCounts_Type()
)
tnSysOtdrFileCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrFileCounts.setStatus("current")


class _TnSysAltitude_Type(Unsigned32):
    """Custom type tnSysAltitude based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_TnSysAltitude_Type.__name__ = "Unsigned32"
_TnSysAltitude_Object = MibScalar
tnSysAltitude = _TnSysAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 30),
    _TnSysAltitude_Type()
)
tnSysAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAltitude.setStatus("current")
if mibBuilder.loadTexts:
    tnSysAltitude.setUnits("meters")


class _TnSysThermalShutdownAutotimer_Type(Integer32):
    """Custom type tnSysThermalShutdownAutotimer based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_TnSysThermalShutdownAutotimer_Type.__name__ = "Integer32"
_TnSysThermalShutdownAutotimer_Object = MibScalar
tnSysThermalShutdownAutotimer = _TnSysThermalShutdownAutotimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 31),
    _TnSysThermalShutdownAutotimer_Type()
)
tnSysThermalShutdownAutotimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysThermalShutdownAutotimer.setStatus("current")
if mibBuilder.loadTexts:
    tnSysThermalShutdownAutotimer.setUnits("seconds")


class _TnSysDisplayShelfLabel_Type(TruthValue):
    """Custom type tnSysDisplayShelfLabel based on TruthValue"""
    defaultValue = 2


_TnSysDisplayShelfLabel_Type.__name__ = "TruthValue"
_TnSysDisplayShelfLabel_Object = MibScalar
tnSysDisplayShelfLabel = _TnSysDisplayShelfLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 32),
    _TnSysDisplayShelfLabel_Type()
)
tnSysDisplayShelfLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDisplayShelfLabel.setStatus("current")


class _TnSysPMFineGranularityControl_Type(Integer32):
    """Custom type tnSysPMFineGranularityControl based on Integer32"""
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


_TnSysPMFineGranularityControl_Type.__name__ = "Integer32"
_TnSysPMFineGranularityControl_Object = MibScalar
tnSysPMFineGranularityControl = _TnSysPMFineGranularityControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 33),
    _TnSysPMFineGranularityControl_Type()
)
tnSysPMFineGranularityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPMFineGranularityControl.setStatus("current")


class _TnSysFmRead_Type(TruthValue):
    """Custom type tnSysFmRead based on TruthValue"""
    defaultValue = 2


_TnSysFmRead_Type.__name__ = "TruthValue"
_TnSysFmRead_Object = MibScalar
tnSysFmRead = _TnSysFmRead_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 34),
    _TnSysFmRead_Type()
)
tnSysFmRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFmRead.setStatus("current")


class _TnSysPMStreamingServerControl_Type(Integer32):
    """Custom type tnSysPMStreamingServerControl based on Integer32"""
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


_TnSysPMStreamingServerControl_Type.__name__ = "Integer32"
_TnSysPMStreamingServerControl_Object = MibScalar
tnSysPMStreamingServerControl = _TnSysPMStreamingServerControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 35),
    _TnSysPMStreamingServerControl_Type()
)
tnSysPMStreamingServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPMStreamingServerControl.setStatus("current")


class _TnSysSlotMigrationControl_Type(Integer32):
    """Custom type tnSysSlotMigrationControl based on Integer32"""
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
        *(("noCmd", 1),
          ("activate", 2),
          ("clear", 3))
    )


_TnSysSlotMigrationControl_Type.__name__ = "Integer32"
_TnSysSlotMigrationControl_Object = MibScalar
tnSysSlotMigrationControl = _TnSysSlotMigrationControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 36),
    _TnSysSlotMigrationControl_Type()
)
tnSysSlotMigrationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSlotMigrationControl.setStatus("current")


class _TnSysFlexGridClusterOcsAddDropEnabled_Type(TruthValue):
    """Custom type tnSysFlexGridClusterOcsAddDropEnabled based on TruthValue"""
    defaultValue = 2


_TnSysFlexGridClusterOcsAddDropEnabled_Type.__name__ = "TruthValue"
_TnSysFlexGridClusterOcsAddDropEnabled_Object = MibScalar
tnSysFlexGridClusterOcsAddDropEnabled = _TnSysFlexGridClusterOcsAddDropEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 37),
    _TnSysFlexGridClusterOcsAddDropEnabled_Type()
)
tnSysFlexGridClusterOcsAddDropEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFlexGridClusterOcsAddDropEnabled.setStatus("current")


class _TnSysFilterCheckTime_Type(Unsigned32):
    """Custom type tnSysFilterCheckTime based on Unsigned32"""
    defaultValue = 0


_TnSysFilterCheckTime_Type.__name__ = "Unsigned32"
_TnSysFilterCheckTime_Object = MibScalar
tnSysFilterCheckTime = _TnSysFilterCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 38),
    _TnSysFilterCheckTime_Type()
)
tnSysFilterCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFilterCheckTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysFilterCheckTime.setUnits("seconds")


class _TnSysCNLinkPhysicalIfIndex_Type(SnmpAdminString):
    """Custom type tnSysCNLinkPhysicalIfIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 168),
    )


_TnSysCNLinkPhysicalIfIndex_Type.__name__ = "SnmpAdminString"
_TnSysCNLinkPhysicalIfIndex_Object = MibScalar
tnSysCNLinkPhysicalIfIndex = _TnSysCNLinkPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 39),
    _TnSysCNLinkPhysicalIfIndex_Type()
)
tnSysCNLinkPhysicalIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysCNLinkPhysicalIfIndex.setStatus("current")


class _TnSysUserlabel_Type(SnmpAdminString):
    """Custom type tnSysUserlabel based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnSysUserlabel_Type.__name__ = "SnmpAdminString"
_TnSysUserlabel_Object = MibScalar
tnSysUserlabel = _TnSysUserlabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 40),
    _TnSysUserlabel_Type()
)
tnSysUserlabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysUserlabel.setStatus("current")


class _TnSysOpenAgentControl_Type(Integer32):
    """Custom type tnSysOpenAgentControl based on Integer32"""
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


_TnSysOpenAgentControl_Type.__name__ = "Integer32"
_TnSysOpenAgentControl_Object = MibScalar
tnSysOpenAgentControl = _TnSysOpenAgentControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 41),
    _TnSysOpenAgentControl_Type()
)
tnSysOpenAgentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOpenAgentControl.setStatus("current")


class _TnSysUnkeyedDanglingOchAddDropEnabled_Type(TruthValue):
    """Custom type tnSysUnkeyedDanglingOchAddDropEnabled based on TruthValue"""
    defaultValue = 2


_TnSysUnkeyedDanglingOchAddDropEnabled_Type.__name__ = "TruthValue"
_TnSysUnkeyedDanglingOchAddDropEnabled_Object = MibScalar
tnSysUnkeyedDanglingOchAddDropEnabled = _TnSysUnkeyedDanglingOchAddDropEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 42),
    _TnSysUnkeyedDanglingOchAddDropEnabled_Type()
)
tnSysUnkeyedDanglingOchAddDropEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysUnkeyedDanglingOchAddDropEnabled.setStatus("current")


class _TnSysNetWorkTraceV3SecurityUser_Type(Integer32):
    """Custom type tnSysNetWorkTraceV3SecurityUser based on Integer32"""
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
        *(("compatibilityMode", 1),
          ("maintenanceMode", 2),
          ("secureMode", 3))
    )


_TnSysNetWorkTraceV3SecurityUser_Type.__name__ = "Integer32"
_TnSysNetWorkTraceV3SecurityUser_Object = MibScalar
tnSysNetWorkTraceV3SecurityUser = _TnSysNetWorkTraceV3SecurityUser_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 43),
    _TnSysNetWorkTraceV3SecurityUser_Type()
)
tnSysNetWorkTraceV3SecurityUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNetWorkTraceV3SecurityUser.setStatus("current")


class _TnSysScotV3SecurityUser_Type(Integer32):
    """Custom type tnSysScotV3SecurityUser based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenanceMode", 1),
          ("secureMode", 2))
    )


_TnSysScotV3SecurityUser_Type.__name__ = "Integer32"
_TnSysScotV3SecurityUser_Object = MibScalar
tnSysScotV3SecurityUser = _TnSysScotV3SecurityUser_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 44),
    _TnSysScotV3SecurityUser_Type()
)
tnSysScotV3SecurityUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysScotV3SecurityUser.setStatus("current")


class _TnSysTL1Enable_Type(TruthValue):
    """Custom type tnSysTL1Enable based on TruthValue"""
    defaultValue = 2


_TnSysTL1Enable_Type.__name__ = "TruthValue"
_TnSysTL1Enable_Object = MibScalar
tnSysTL1Enable = _TnSysTL1Enable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 45),
    _TnSysTL1Enable_Type()
)
tnSysTL1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTL1Enable.setStatus("current")


class _TnSysLMEnabled_Type(TruthValue):
    """Custom type tnSysLMEnabled based on TruthValue"""
    defaultValue = 1


_TnSysLMEnabled_Type.__name__ = "TruthValue"
_TnSysLMEnabled_Object = MibScalar
tnSysLMEnabled = _TnSysLMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 46),
    _TnSysLMEnabled_Type()
)
tnSysLMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLMEnabled.setStatus("current")


class _TnSysAlienChannelLicensingEnabled_Type(TruthValue):
    """Custom type tnSysAlienChannelLicensingEnabled based on TruthValue"""
    defaultValue = 1


_TnSysAlienChannelLicensingEnabled_Type.__name__ = "TruthValue"
_TnSysAlienChannelLicensingEnabled_Object = MibScalar
tnSysAlienChannelLicensingEnabled = _TnSysAlienChannelLicensingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 47),
    _TnSysAlienChannelLicensingEnabled_Type()
)
tnSysAlienChannelLicensingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAlienChannelLicensingEnabled.setStatus("current")


class _TnSysDebug_Type(TruthValue):
    """Custom type tnSysDebug based on TruthValue"""
    defaultValue = 2


_TnSysDebug_Type.__name__ = "TruthValue"
_TnSysDebug_Object = MibScalar
tnSysDebug = _TnSysDebug_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 48),
    _TnSysDebug_Type()
)
tnSysDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebug.setStatus("current")


class _TnSysClusterV3SecurityUser_Type(Integer32):
    """Custom type tnSysClusterV3SecurityUser based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatibilityMode", 1),
          ("secureMode", 2))
    )


_TnSysClusterV3SecurityUser_Type.__name__ = "Integer32"
_TnSysClusterV3SecurityUser_Object = MibScalar
tnSysClusterV3SecurityUser = _TnSysClusterV3SecurityUser_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 49),
    _TnSysClusterV3SecurityUser_Type()
)
tnSysClusterV3SecurityUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysClusterV3SecurityUser.setStatus("current")


class _TnSysSyncMode_Type(Integer32):
    """Custom type tnSysSyncMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("etsi", 2))
    )


_TnSysSyncMode_Type.__name__ = "Integer32"
_TnSysSyncMode_Object = MibScalar
tnSysSyncMode = _TnSysSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 51),
    _TnSysSyncMode_Type()
)
tnSysSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSyncMode.setStatus("current")


class _TnSysPMMode_Type(Integer32):
    """Custom type tnSysPMMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("etsi", 2))
    )


_TnSysPMMode_Type.__name__ = "Integer32"
_TnSysPMMode_Object = MibScalar
tnSysPMMode = _TnSysPMMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 52),
    _TnSysPMMode_Type()
)
tnSysPMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPMMode.setStatus("current")


class _TnSysShelfLatitude_Type(SnmpAdminString):
    """Custom type tnSysShelfLatitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysShelfLatitude_Type.__name__ = "SnmpAdminString"
_TnSysShelfLatitude_Object = MibScalar
tnSysShelfLatitude = _TnSysShelfLatitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 53),
    _TnSysShelfLatitude_Type()
)
tnSysShelfLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysShelfLatitude.setStatus("current")


class _TnSysShelfLongitude_Type(SnmpAdminString):
    """Custom type tnSysShelfLongitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysShelfLongitude_Type.__name__ = "SnmpAdminString"
_TnSysShelfLongitude_Object = MibScalar
tnSysShelfLongitude = _TnSysShelfLongitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 54),
    _TnSysShelfLongitude_Type()
)
tnSysShelfLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysShelfLongitude.setStatus("current")


class _TnSysAlmProfName_Type(OctetString):
    """Custom type tnSysAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnSysAlmProfName_Type.__name__ = "OctetString"
_TnSysAlmProfName_Object = MibScalar
tnSysAlmProfName = _TnSysAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 55),
    _TnSysAlmProfName_Type()
)
tnSysAlmProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAlmProfName.setStatus("current")


class _TnSysBgpAsn_Type(Unsigned32):
    """Custom type tnSysBgpAsn based on Unsigned32"""
    defaultValue = 0


_TnSysBgpAsn_Type.__name__ = "Unsigned32"
_TnSysBgpAsn_Object = MibScalar
tnSysBgpAsn = _TnSysBgpAsn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 56),
    _TnSysBgpAsn_Type()
)
tnSysBgpAsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBgpAsn.setStatus("current")


class _TnSysBgpLocalRouterId_Type(IpAddress):
    """Custom type tnSysBgpLocalRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysBgpLocalRouterId_Type.__name__ = "IpAddress"
_TnSysBgpLocalRouterId_Object = MibScalar
tnSysBgpLocalRouterId = _TnSysBgpLocalRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 57),
    _TnSysBgpLocalRouterId_Type()
)
tnSysBgpLocalRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpLocalRouterId.setStatus("current")


class _TnSysNodeIdLabel_Type(SnmpAdminString):
    """Custom type tnSysNodeIdLabel based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnSysNodeIdLabel_Type.__name__ = "SnmpAdminString"
_TnSysNodeIdLabel_Object = MibScalar
tnSysNodeIdLabel = _TnSysNodeIdLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 58),
    _TnSysNodeIdLabel_Type()
)
tnSysNodeIdLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNodeIdLabel.setStatus("current")


class _TnSysNodeNumber_Type(Integer32):
    """Custom type tnSysNodeNumber based on Integer32"""
    defaultValue = 0


_TnSysNodeNumber_Type.__name__ = "Integer32"
_TnSysNodeNumber_Object = MibScalar
tnSysNodeNumber = _TnSysNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 59),
    _TnSysNodeNumber_Type()
)
tnSysNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNodeNumber.setStatus("current")


class _TnSysNodeCLLI_Type(SnmpAdminString):
    """Custom type tnSysNodeCLLI based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_TnSysNodeCLLI_Type.__name__ = "SnmpAdminString"
_TnSysNodeCLLI_Object = MibScalar
tnSysNodeCLLI = _TnSysNodeCLLI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 60),
    _TnSysNodeCLLI_Type()
)
tnSysNodeCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNodeCLLI.setStatus("current")


class _TnSysNodeTemplate_Type(SnmpAdminString):
    """Custom type tnSysNodeTemplate based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysNodeTemplate_Type.__name__ = "SnmpAdminString"
_TnSysNodeTemplate_Object = MibScalar
tnSysNodeTemplate = _TnSysNodeTemplate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 61),
    _TnSysNodeTemplate_Type()
)
tnSysNodeTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNodeTemplate.setStatus("current")


class _TnSysCustomerApplicationMode_Type(Integer32):
    """Custom type tnSysCustomerApplicationMode based on Integer32"""
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
        *(("uninitialized", 1),
          ("unknown", 2),
          ("generic", 3),
          ("openRoadm", 4))
    )


_TnSysCustomerApplicationMode_Type.__name__ = "Integer32"
_TnSysCustomerApplicationMode_Object = MibScalar
tnSysCustomerApplicationMode = _TnSysCustomerApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 64),
    _TnSysCustomerApplicationMode_Type()
)
tnSysCustomerApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysCustomerApplicationMode.setStatus("current")


class _TnSysMDCli_Type(Integer32):
    """Custom type tnSysMDCli based on Integer32"""
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
        *(("unknown", 1),
          ("enable", 2),
          ("disable", 3))
    )


_TnSysMDCli_Type.__name__ = "Integer32"
_TnSysMDCli_Object = MibScalar
tnSysMDCli = _TnSysMDCli_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 65),
    _TnSysMDCli_Type()
)
tnSysMDCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMDCli.setStatus("current")


class _TnSysMultiShelfMode_Type(Integer32):
    """Custom type tnSysMultiShelfMode based on Integer32"""
    defaultValue = 1

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
        *(("learnModeNone", 1),
          ("learnModeFinal", 2),
          ("learnModeLearn", 3),
          ("learnModeAuto", 4),
          ("learnModeManual", 5),
          ("learnModeMax", 6))
    )


_TnSysMultiShelfMode_Type.__name__ = "Integer32"
_TnSysMultiShelfMode_Object = MibScalar
tnSysMultiShelfMode = _TnSysMultiShelfMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 66),
    _TnSysMultiShelfMode_Type()
)
tnSysMultiShelfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMultiShelfMode.setStatus("current")


class _TnSysMultiShelfConfigList_Type(SnmpAdminString):
    """Custom type tnSysMultiShelfConfigList based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_TnSysMultiShelfConfigList_Type.__name__ = "SnmpAdminString"
_TnSysMultiShelfConfigList_Object = MibScalar
tnSysMultiShelfConfigList = _TnSysMultiShelfConfigList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 67),
    _TnSysMultiShelfConfigList_Type()
)
tnSysMultiShelfConfigList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMultiShelfConfigList.setStatus("current")


class _TnSysMultiShelfUnknownList_Type(SnmpAdminString):
    """Custom type tnSysMultiShelfUnknownList based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_TnSysMultiShelfUnknownList_Type.__name__ = "SnmpAdminString"
_TnSysMultiShelfUnknownList_Object = MibScalar
tnSysMultiShelfUnknownList = _TnSysMultiShelfUnknownList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 68),
    _TnSysMultiShelfUnknownList_Type()
)
tnSysMultiShelfUnknownList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMultiShelfUnknownList.setStatus("current")


class _TnSysMultiShelfMissingList_Type(SnmpAdminString):
    """Custom type tnSysMultiShelfMissingList based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_TnSysMultiShelfMissingList_Type.__name__ = "SnmpAdminString"
_TnSysMultiShelfMissingList_Object = MibScalar
tnSysMultiShelfMissingList = _TnSysMultiShelfMissingList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 69),
    _TnSysMultiShelfMissingList_Type()
)
tnSysMultiShelfMissingList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMultiShelfMissingList.setStatus("current")


class _TnSysPrompt_Type(SnmpAdminString):
    """Custom type tnSysPrompt based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnSysPrompt_Type.__name__ = "SnmpAdminString"
_TnSysPrompt_Object = MibScalar
tnSysPrompt = _TnSysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 70),
    _TnSysPrompt_Type()
)
tnSysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPrompt.setStatus("current")


class _TnSysPromptType_Type(Integer32):
    """Custom type tnSysPromptType based on Integer32"""
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
        *(("tid", 1),
          ("userLabel", 2),
          ("promptText", 3),
          ("unknown", 4))
    )


_TnSysPromptType_Type.__name__ = "Integer32"
_TnSysPromptType_Object = MibScalar
tnSysPromptType = _TnSysPromptType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 71),
    _TnSysPromptType_Type()
)
tnSysPromptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPromptType.setStatus("current")


class _TnSysShelfAltitude_Type(SnmpAdminString):
    """Custom type tnSysShelfAltitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysShelfAltitude_Type.__name__ = "SnmpAdminString"
_TnSysShelfAltitude_Object = MibScalar
tnSysShelfAltitude = _TnSysShelfAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 72),
    _TnSysShelfAltitude_Type()
)
tnSysShelfAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysShelfAltitude.setStatus("current")


class _TnSysTacacsSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysTacacsSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysTacacsSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysTacacsSourceIpMode_Object = MibScalar
tnSysTacacsSourceIpMode = _TnSysTacacsSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 73),
    _TnSysTacacsSourceIpMode_Type()
)
tnSysTacacsSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTacacsSourceIpMode.setStatus("current")


class _TnSysRadiusSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysRadiusSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysRadiusSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysRadiusSourceIpMode_Object = MibScalar
tnSysRadiusSourceIpMode = _TnSysRadiusSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 74),
    _TnSysRadiusSourceIpMode_Type()
)
tnSysRadiusSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRadiusSourceIpMode.setStatus("current")


class _TnSysFtpSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysFtpSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysFtpSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysFtpSourceIpMode_Object = MibScalar
tnSysFtpSourceIpMode = _TnSysFtpSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 75),
    _TnSysFtpSourceIpMode_Type()
)
tnSysFtpSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFtpSourceIpMode.setStatus("current")


class _TnSysSftpSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysSftpSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysSftpSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysSftpSourceIpMode_Object = MibScalar
tnSysSftpSourceIpMode = _TnSysSftpSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 76),
    _TnSysSftpSourceIpMode_Type()
)
tnSysSftpSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSftpSourceIpMode.setStatus("current")


class _TnSysHttpSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysHttpSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysHttpSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysHttpSourceIpMode_Object = MibScalar
tnSysHttpSourceIpMode = _TnSysHttpSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 77),
    _TnSysHttpSourceIpMode_Type()
)
tnSysHttpSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHttpSourceIpMode.setStatus("current")


class _TnSysHttpsSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysHttpsSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysHttpsSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysHttpsSourceIpMode_Object = MibScalar
tnSysHttpsSourceIpMode = _TnSysHttpsSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 78),
    _TnSysHttpsSourceIpMode_Type()
)
tnSysHttpsSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHttpsSourceIpMode.setStatus("current")


class _TnSysSnmpSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysSnmpSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysSnmpSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysSnmpSourceIpMode_Object = MibScalar
tnSysSnmpSourceIpMode = _TnSysSnmpSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 79),
    _TnSysSnmpSourceIpMode_Type()
)
tnSysSnmpSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSnmpSourceIpMode.setStatus("current")


class _TnSysSyslogSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysSyslogSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysSyslogSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysSyslogSourceIpMode_Object = MibScalar
tnSysSyslogSourceIpMode = _TnSysSyslogSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 80),
    _TnSysSyslogSourceIpMode_Type()
)
tnSysSyslogSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSyslogSourceIpMode.setStatus("current")


class _TnSysSshSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysSshSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysSshSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysSshSourceIpMode_Object = MibScalar
tnSysSshSourceIpMode = _TnSysSshSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 81),
    _TnSysSshSourceIpMode_Type()
)
tnSysSshSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshSourceIpMode.setStatus("current")


class _TnSysAutoTurnUpActiveTemplate_Type(SnmpAdminString):
    """Custom type tnSysAutoTurnUpActiveTemplate based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnSysAutoTurnUpActiveTemplate_Type.__name__ = "SnmpAdminString"
_TnSysAutoTurnUpActiveTemplate_Object = MibScalar
tnSysAutoTurnUpActiveTemplate = _TnSysAutoTurnUpActiveTemplate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 82),
    _TnSysAutoTurnUpActiveTemplate_Type()
)
tnSysAutoTurnUpActiveTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAutoTurnUpActiveTemplate.setStatus("current")
_TnSysAuthenticationOrder_Type = Unsigned32
_TnSysAuthenticationOrder_Object = MibScalar
tnSysAuthenticationOrder = _TnSysAuthenticationOrder_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 83),
    _TnSysAuthenticationOrder_Type()
)
tnSysAuthenticationOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAuthenticationOrder.setStatus("current")


class _TnSysAuthRejectOption_Type(Integer32):
    """Custom type tnSysAuthRejectOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyRjectMode", 1),
          ("denyRetryMode", 2))
    )


_TnSysAuthRejectOption_Type.__name__ = "Integer32"
_TnSysAuthRejectOption_Object = MibScalar
tnSysAuthRejectOption = _TnSysAuthRejectOption_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 84),
    _TnSysAuthRejectOption_Type()
)
tnSysAuthRejectOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAuthRejectOption.setStatus("current")
_TnSysAutoTurnUpActiveTemplateForce_Type = TruthValue
_TnSysAutoTurnUpActiveTemplateForce_Object = MibScalar
tnSysAutoTurnUpActiveTemplateForce = _TnSysAutoTurnUpActiveTemplateForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 85),
    _TnSysAutoTurnUpActiveTemplateForce_Type()
)
tnSysAutoTurnUpActiveTemplateForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAutoTurnUpActiveTemplateForce.setStatus("current")


class _TnSysNtpSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysNtpSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysNtpSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysNtpSourceIpMode_Object = MibScalar
tnSysNtpSourceIpMode = _TnSysNtpSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 86),
    _TnSysNtpSourceIpMode_Type()
)
tnSysNtpSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpSourceIpMode.setStatus("current")


class _TnSysFeatureAutoTurnUp_Type(AluWdmDisabledEnabled):
    """Custom type tnSysFeatureAutoTurnUp based on AluWdmDisabledEnabled"""
    defaultValue = 1


_TnSysFeatureAutoTurnUp_Type.__name__ = "AluWdmDisabledEnabled"
_TnSysFeatureAutoTurnUp_Object = MibScalar
tnSysFeatureAutoTurnUp = _TnSysFeatureAutoTurnUp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 87),
    _TnSysFeatureAutoTurnUp_Type()
)
tnSysFeatureAutoTurnUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureAutoTurnUp.setStatus("current")
_TnSysDelayResetNE_Type = Integer32
_TnSysDelayResetNE_Object = MibScalar
tnSysDelayResetNE = _TnSysDelayResetNE_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 88),
    _TnSysDelayResetNE_Type()
)
tnSysDelayResetNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDelayResetNE.setStatus("current")
_TnSysDelayReboot_Type = TruthValue
_TnSysDelayReboot_Object = MibScalar
tnSysDelayReboot = _TnSysDelayReboot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 89),
    _TnSysDelayReboot_Type()
)
tnSysDelayReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDelayReboot.setStatus("current")


class _TnSysNmsUserName_Type(SnmpAdminString):
    """Custom type tnSysNmsUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysNmsUserName_Type.__name__ = "SnmpAdminString"
_TnSysNmsUserName_Object = MibScalar
tnSysNmsUserName = _TnSysNmsUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 90),
    _TnSysNmsUserName_Type()
)
tnSysNmsUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNmsUserName.setStatus("current")
_TnSysVersionPatchId_Type = Integer32
_TnSysVersionPatchId_Object = MibScalar
tnSysVersionPatchId = _TnSysVersionPatchId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 91),
    _TnSysVersionPatchId_Type()
)
tnSysVersionPatchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysVersionPatchId.setStatus("current")


class _TnSysVersionPatchDescr_Type(SnmpAdminString):
    """Custom type tnSysVersionPatchDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSysVersionPatchDescr_Type.__name__ = "SnmpAdminString"
_TnSysVersionPatchDescr_Object = MibScalar
tnSysVersionPatchDescr = _TnSysVersionPatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 92),
    _TnSysVersionPatchDescr_Type()
)
tnSysVersionPatchDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysVersionPatchDescr.setStatus("current")


class _TnSysCustomerLifeCycleState_Type(SnmpAdminString):
    """Custom type tnSysCustomerLifeCycleState based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnSysCustomerLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnSysCustomerLifeCycleState_Object = MibScalar
tnSysCustomerLifeCycleState = _TnSysCustomerLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 93),
    _TnSysCustomerLifeCycleState_Type()
)
tnSysCustomerLifeCycleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysCustomerLifeCycleState.setStatus("current")


class _TnSysUSBInstall_Type(TruthValue):
    """Custom type tnSysUSBInstall based on TruthValue"""
    defaultValue = 2


_TnSysUSBInstall_Type.__name__ = "TruthValue"
_TnSysUSBInstall_Object = MibScalar
tnSysUSBInstall = _TnSysUSBInstall_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 94),
    _TnSysUSBInstall_Type()
)
tnSysUSBInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysUSBInstall.setStatus("current")
_TnSysNmsIpVerifyState_Type = TruthValue
_TnSysNmsIpVerifyState_Object = MibScalar
tnSysNmsIpVerifyState = _TnSysNmsIpVerifyState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 95),
    _TnSysNmsIpVerifyState_Type()
)
tnSysNmsIpVerifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNmsIpVerifyState.setStatus("current")


class _TnSysOcspSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysOcspSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysOcspSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysOcspSourceIpMode_Object = MibScalar
tnSysOcspSourceIpMode = _TnSysOcspSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 96),
    _TnSysOcspSourceIpMode_Type()
)
tnSysOcspSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcspSourceIpMode.setStatus("current")


class _TnSysDnsSourceIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysDnsSourceIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysDnsSourceIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysDnsSourceIpMode_Object = MibScalar
tnSysDnsSourceIpMode = _TnSysDnsSourceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 97),
    _TnSysDnsSourceIpMode_Type()
)
tnSysDnsSourceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDnsSourceIpMode.setStatus("current")


class _TnSysOtcWaitTimeAfterPowerChange_Type(Unsigned32):
    """Custom type tnSysOtcWaitTimeAfterPowerChange based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_TnSysOtcWaitTimeAfterPowerChange_Type.__name__ = "Unsigned32"
_TnSysOtcWaitTimeAfterPowerChange_Object = MibScalar
tnSysOtcWaitTimeAfterPowerChange = _TnSysOtcWaitTimeAfterPowerChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 98),
    _TnSysOtcWaitTimeAfterPowerChange_Type()
)
tnSysOtcWaitTimeAfterPowerChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtcWaitTimeAfterPowerChange.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtcWaitTimeAfterPowerChange.setUnits("seconds")


class _TnSysDHCPClassName_Type(SnmpAdminString):
    """Custom type tnSysDHCPClassName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysDHCPClassName_Type.__name__ = "SnmpAdminString"
_TnSysDHCPClassName_Object = MibScalar
tnSysDHCPClassName = _TnSysDHCPClassName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 99),
    _TnSysDHCPClassName_Type()
)
tnSysDHCPClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDHCPClassName.setStatus("current")


class _TnSysDHCPMatchString_Type(SnmpAdminString):
    """Custom type tnSysDHCPMatchString based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnSysDHCPMatchString_Type.__name__ = "SnmpAdminString"
_TnSysDHCPMatchString_Object = MibScalar
tnSysDHCPMatchString = _TnSysDHCPMatchString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 100),
    _TnSysDHCPMatchString_Type()
)
tnSysDHCPMatchString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDHCPMatchString.setStatus("current")


class _TnSysKeyLicense_Type(SnmpAdminString):
    """Custom type tnSysKeyLicense based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnSysKeyLicense_Type.__name__ = "SnmpAdminString"
_TnSysKeyLicense_Object = MibScalar
tnSysKeyLicense = _TnSysKeyLicense_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 101),
    _TnSysKeyLicense_Type()
)
tnSysKeyLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysKeyLicense.setStatus("current")


class _TnSysHwIfMode_Type(Integer32):
    """Custom type tnSysHwIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nomate", 1),
          ("mate100g", 2))
    )


_TnSysHwIfMode_Type.__name__ = "Integer32"
_TnSysHwIfMode_Object = MibScalar
tnSysHwIfMode = _TnSysHwIfMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 102),
    _TnSysHwIfMode_Type()
)
tnSysHwIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHwIfMode.setStatus("current")
_TnSysIpAclNextIndex_Type = Integer32
_TnSysIpAclNextIndex_Object = MibScalar
tnSysIpAclNextIndex = _TnSysIpAclNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 103),
    _TnSysIpAclNextIndex_Type()
)
tnSysIpAclNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclNextIndex.setStatus("current")
_TnSysIpv6AclNextIndex_Type = Integer32
_TnSysIpv6AclNextIndex_Object = MibScalar
tnSysIpv6AclNextIndex = _TnSysIpv6AclNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 104),
    _TnSysIpv6AclNextIndex_Type()
)
tnSysIpv6AclNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclNextIndex.setStatus("current")


class _TnSysDHCPClass_Type(Integer32):
    """Custom type tnSysDHCPClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_TnSysDHCPClass_Type.__name__ = "Integer32"
_TnSysDHCPClass_Object = MibScalar
tnSysDHCPClass = _TnSysDHCPClass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 105),
    _TnSysDHCPClass_Type()
)
tnSysDHCPClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDHCPClass.setStatus("current")


class _TnSysProtocolIpMode_Type(TropicSourceIpModeValue):
    """Custom type tnSysProtocolIpMode based on TropicSourceIpModeValue"""
    defaultValue = 1


_TnSysProtocolIpMode_Type.__name__ = "TropicSourceIpModeValue"
_TnSysProtocolIpMode_Object = MibScalar
tnSysProtocolIpMode = _TnSysProtocolIpMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 106),
    _TnSysProtocolIpMode_Type()
)
tnSysProtocolIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysProtocolIpMode.setStatus("current")


class _TnSysMultiShelfAvailableList_Type(SnmpAdminString):
    """Custom type tnSysMultiShelfAvailableList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_TnSysMultiShelfAvailableList_Type.__name__ = "SnmpAdminString"
_TnSysMultiShelfAvailableList_Object = MibScalar
tnSysMultiShelfAvailableList = _TnSysMultiShelfAvailableList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 107),
    _TnSysMultiShelfAvailableList_Type()
)
tnSysMultiShelfAvailableList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMultiShelfAvailableList.setStatus("current")
_TnSysPerformanceMemoryTotal_Type = Integer32
_TnSysPerformanceMemoryTotal_Object = MibScalar
tnSysPerformanceMemoryTotal = _TnSysPerformanceMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 108),
    _TnSysPerformanceMemoryTotal_Type()
)
tnSysPerformanceMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPerformanceMemoryTotal.setStatus("current")
_TnSysPerformanceMemoryUsed_Type = Integer32
_TnSysPerformanceMemoryUsed_Object = MibScalar
tnSysPerformanceMemoryUsed = _TnSysPerformanceMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 109),
    _TnSysPerformanceMemoryUsed_Type()
)
tnSysPerformanceMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPerformanceMemoryUsed.setStatus("current")
_TnSysPerformanceMemoryUsedPercentage_Type = Integer32
_TnSysPerformanceMemoryUsedPercentage_Object = MibScalar
tnSysPerformanceMemoryUsedPercentage = _TnSysPerformanceMemoryUsedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 110),
    _TnSysPerformanceMemoryUsedPercentage_Type()
)
tnSysPerformanceMemoryUsedPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPerformanceMemoryUsedPercentage.setStatus("current")


class _TnSysPerformanceTime_Type(SnmpAdminString):
    """Custom type tnSysPerformanceTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysPerformanceTime_Type.__name__ = "SnmpAdminString"
_TnSysPerformanceTime_Object = MibScalar
tnSysPerformanceTime = _TnSysPerformanceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 111),
    _TnSysPerformanceTime_Type()
)
tnSysPerformanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPerformanceTime.setStatus("current")


class _TnSysPerformanceCPUStatsPercentages_Type(SnmpAdminString):
    """Custom type tnSysPerformanceCPUStatsPercentages based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysPerformanceCPUStatsPercentages_Type.__name__ = "SnmpAdminString"
_TnSysPerformanceCPUStatsPercentages_Object = MibScalar
tnSysPerformanceCPUStatsPercentages = _TnSysPerformanceCPUStatsPercentages_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 112),
    _TnSysPerformanceCPUStatsPercentages_Type()
)
tnSysPerformanceCPUStatsPercentages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPerformanceCPUStatsPercentages.setStatus("current")


class _TnSysPower_Type(Integer32):
    """Custom type tnSysPower based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("powerOff", 2))
    )


_TnSysPower_Type.__name__ = "Integer32"
_TnSysPower_Object = MibScalar
tnSysPower = _TnSysPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 113),
    _TnSysPower_Type()
)
tnSysPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPower.setStatus("current")
_TnSysKeyStoreCertExpiration_Type = Unsigned32
_TnSysKeyStoreCertExpiration_Object = MibScalar
tnSysKeyStoreCertExpiration = _TnSysKeyStoreCertExpiration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 114),
    _TnSysKeyStoreCertExpiration_Type()
)
tnSysKeyStoreCertExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertExpiration.setStatus("current")
_TnSysNumOspfV2AreaIndependentLsas_Type = Unsigned32
_TnSysNumOspfV2AreaIndependentLsas_Object = MibScalar
tnSysNumOspfV2AreaIndependentLsas = _TnSysNumOspfV2AreaIndependentLsas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 115),
    _TnSysNumOspfV2AreaIndependentLsas_Type()
)
tnSysNumOspfV2AreaIndependentLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNumOspfV2AreaIndependentLsas.setStatus("current")
_TnSysNumOspfV3AreaIndependentLsas_Type = Unsigned32
_TnSysNumOspfV3AreaIndependentLsas_Object = MibScalar
tnSysNumOspfV3AreaIndependentLsas = _TnSysNumOspfV3AreaIndependentLsas_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 116),
    _TnSysNumOspfV3AreaIndependentLsas_Type()
)
tnSysNumOspfV3AreaIndependentLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNumOspfV3AreaIndependentLsas.setStatus("current")


class _TnSysBgpAdminDistance_Type(Unsigned32):
    """Custom type tnSysBgpAdminDistance based on Unsigned32"""
    defaultValue = 20


_TnSysBgpAdminDistance_Type.__name__ = "Unsigned32"
_TnSysBgpAdminDistance_Object = MibScalar
tnSysBgpAdminDistance = _TnSysBgpAdminDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 117),
    _TnSysBgpAdminDistance_Type()
)
tnSysBgpAdminDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBgpAdminDistance.setStatus("current")
_TnSysControlNetwork_ObjectIdentity = ObjectIdentity
tnSysControlNetwork = _TnSysControlNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2)
)


class _TnSysIpAddress_Type(IpAddress):
    """Custom type tnSysIpAddress based on IpAddress"""
    defaultHexValue = "AC100101"


_TnSysIpAddress_Type.__name__ = "IpAddress"
_TnSysIpAddress_Object = MibScalar
tnSysIpAddress = _TnSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 1),
    _TnSysIpAddress_Type()
)
tnSysIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAddress.setStatus("current")


class _TnSysSubnetMask_Type(IpAddress):
    """Custom type tnSysSubnetMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TnSysSubnetMask_Type.__name__ = "IpAddress"
_TnSysSubnetMask_Object = MibScalar
tnSysSubnetMask = _TnSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 2),
    _TnSysSubnetMask_Type()
)
tnSysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSubnetMask.setStatus("current")


class _TnSysConfiguredIpAddress_Type(IpAddress):
    """Custom type tnSysConfiguredIpAddress based on IpAddress"""
    defaultHexValue = "AC100101"


_TnSysConfiguredIpAddress_Type.__name__ = "IpAddress"
_TnSysConfiguredIpAddress_Object = MibScalar
tnSysConfiguredIpAddress = _TnSysConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 3),
    _TnSysConfiguredIpAddress_Type()
)
tnSysConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredIpAddress.setStatus("current")


class _TnSysConfiguredSubnetMask_Type(IpAddress):
    """Custom type tnSysConfiguredSubnetMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_TnSysConfiguredSubnetMask_Type.__name__ = "IpAddress"
_TnSysConfiguredSubnetMask_Object = MibScalar
tnSysConfiguredSubnetMask = _TnSysConfiguredSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 4),
    _TnSysConfiguredSubnetMask_Type()
)
tnSysConfiguredSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSubnetMask.setStatus("current")


class _TnSysConfiguredSnmpSource_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSource based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSource_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSource_Object = MibScalar
tnSysConfiguredSnmpSource = _TnSysConfiguredSnmpSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 5),
    _TnSysConfiguredSnmpSource_Type()
)
tnSysConfiguredSnmpSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSource.setStatus("current")


class _TnSysConfiguredOcsIpAddress_Type(IpAddress):
    """Custom type tnSysConfiguredOcsIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysConfiguredOcsIpAddress_Type.__name__ = "IpAddress"
_TnSysConfiguredOcsIpAddress_Object = MibScalar
tnSysConfiguredOcsIpAddress = _TnSysConfiguredOcsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 6),
    _TnSysConfiguredOcsIpAddress_Type()
)
tnSysConfiguredOcsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredOcsIpAddress.setStatus("current")


class _TnSysConfiguredOcs2IpAddress_Type(IpAddress):
    """Custom type tnSysConfiguredOcs2IpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysConfiguredOcs2IpAddress_Type.__name__ = "IpAddress"
_TnSysConfiguredOcs2IpAddress_Object = MibScalar
tnSysConfiguredOcs2IpAddress = _TnSysConfiguredOcs2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 7),
    _TnSysConfiguredOcs2IpAddress_Type()
)
tnSysConfiguredOcs2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredOcs2IpAddress.setStatus("current")


class _TnSysConfiguredOcs3IpAddress_Type(IpAddress):
    """Custom type tnSysConfiguredOcs3IpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysConfiguredOcs3IpAddress_Type.__name__ = "IpAddress"
_TnSysConfiguredOcs3IpAddress_Object = MibScalar
tnSysConfiguredOcs3IpAddress = _TnSysConfiguredOcs3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 8),
    _TnSysConfiguredOcs3IpAddress_Type()
)
tnSysConfiguredOcs3IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredOcs3IpAddress.setStatus("current")
_TnSysOcs1LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs1LinkStatus_Object = MibScalar
tnSysOcs1LinkStatus = _TnSysOcs1LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 9),
    _TnSysOcs1LinkStatus_Type()
)
tnSysOcs1LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs1LinkStatus.setStatus("current")
_TnSysOcs2LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs2LinkStatus_Object = MibScalar
tnSysOcs2LinkStatus = _TnSysOcs2LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 10),
    _TnSysOcs2LinkStatus_Type()
)
tnSysOcs2LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs2LinkStatus.setStatus("current")
_TnSysOcs3LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs3LinkStatus_Object = MibScalar
tnSysOcs3LinkStatus = _TnSysOcs3LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 11),
    _TnSysOcs3LinkStatus_Type()
)
tnSysOcs3LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs3LinkStatus.setStatus("current")


class _TnSysConfiguredRadiusSource_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSource based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSource_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSource_Object = MibScalar
tnSysConfiguredRadiusSource = _TnSysConfiguredRadiusSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 12),
    _TnSysConfiguredRadiusSource_Type()
)
tnSysConfiguredRadiusSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSource.setStatus("current")


class _TnSysConfiguredLoopbackIp1_Type(IpAddress):
    """Custom type tnSysConfiguredLoopbackIp1 based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysConfiguredLoopbackIp1_Type.__name__ = "IpAddress"
_TnSysConfiguredLoopbackIp1_Object = MibScalar
tnSysConfiguredLoopbackIp1 = _TnSysConfiguredLoopbackIp1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 13),
    _TnSysConfiguredLoopbackIp1_Type()
)
tnSysConfiguredLoopbackIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredLoopbackIp1.setStatus("current")


class _TnSysConfiguredLoopbackIp1SubnetMask_Type(IpAddress):
    """Custom type tnSysConfiguredLoopbackIp1SubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysConfiguredLoopbackIp1SubnetMask_Type.__name__ = "IpAddress"
_TnSysConfiguredLoopbackIp1SubnetMask_Object = MibScalar
tnSysConfiguredLoopbackIp1SubnetMask = _TnSysConfiguredLoopbackIp1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 14),
    _TnSysConfiguredLoopbackIp1SubnetMask_Type()
)
tnSysConfiguredLoopbackIp1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredLoopbackIp1SubnetMask.setStatus("current")


class _TnSysConfiguredSnmpSource1_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSource1 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSource1_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSource1_Object = MibScalar
tnSysConfiguredSnmpSource1 = _TnSysConfiguredSnmpSource1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 15),
    _TnSysConfiguredSnmpSource1_Type()
)
tnSysConfiguredSnmpSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSource1.setStatus("current")


class _TnSysConfiguredRadiusSource1_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSource1 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSource1_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSource1_Object = MibScalar
tnSysConfiguredRadiusSource1 = _TnSysConfiguredRadiusSource1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 16),
    _TnSysConfiguredRadiusSource1_Type()
)
tnSysConfiguredRadiusSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSource1.setStatus("current")


class _TnSysLoopbackIpAddress1_Type(IpAddress):
    """Custom type tnSysLoopbackIpAddress1 based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysLoopbackIpAddress1_Type.__name__ = "IpAddress"
_TnSysLoopbackIpAddress1_Object = MibScalar
tnSysLoopbackIpAddress1 = _TnSysLoopbackIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 17),
    _TnSysLoopbackIpAddress1_Type()
)
tnSysLoopbackIpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLoopbackIpAddress1.setStatus("current")


class _TnSysLoopbackIp1SubnetMask_Type(IpAddress):
    """Custom type tnSysLoopbackIp1SubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysLoopbackIp1SubnetMask_Type.__name__ = "IpAddress"
_TnSysLoopbackIp1SubnetMask_Object = MibScalar
tnSysLoopbackIp1SubnetMask = _TnSysLoopbackIp1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 18),
    _TnSysLoopbackIp1SubnetMask_Type()
)
tnSysLoopbackIp1SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLoopbackIp1SubnetMask.setStatus("current")


class _TnSysConfiguredInetAddressType_Type(InetAddressType):
    """Custom type tnSysConfiguredInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysConfiguredInetAddressType_Type.__name__ = "InetAddressType"
_TnSysConfiguredInetAddressType_Object = MibScalar
tnSysConfiguredInetAddressType = _TnSysConfiguredInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 19),
    _TnSysConfiguredInetAddressType_Type()
)
tnSysConfiguredInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredInetAddressType.setStatus("current")


class _TnSysConfiguredInetAddress_Type(InetAddress):
    """Custom type tnSysConfiguredInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysConfiguredInetAddress_Type.__name__ = "InetAddress"
_TnSysConfiguredInetAddress_Object = MibScalar
tnSysConfiguredInetAddress = _TnSysConfiguredInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 20),
    _TnSysConfiguredInetAddress_Type()
)
tnSysConfiguredInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredInetAddress.setStatus("current")


class _TnSysConfiguredPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tnSysConfiguredPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TnSysConfiguredPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TnSysConfiguredPrefixLength_Object = MibScalar
tnSysConfiguredPrefixLength = _TnSysConfiguredPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 21),
    _TnSysConfiguredPrefixLength_Type()
)
tnSysConfiguredPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredPrefixLength.setStatus("current")


class _TnSysOcsIp1Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp1Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp1Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp1Password_Object = MibScalar
tnSysOcsIp1Password = _TnSysOcsIp1Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 22),
    _TnSysOcsIp1Password_Type()
)
tnSysOcsIp1Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp1Password.setStatus("current")


class _TnSysOcsIp2Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp2Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp2Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp2Password_Object = MibScalar
tnSysOcsIp2Password = _TnSysOcsIp2Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 23),
    _TnSysOcsIp2Password_Type()
)
tnSysOcsIp2Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp2Password.setStatus("current")


class _TnSysOcsIp3Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp3Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp3Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp3Password_Object = MibScalar
tnSysOcsIp3Password = _TnSysOcsIp3Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 24),
    _TnSysOcsIp3Password_Type()
)
tnSysOcsIp3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp3Password.setStatus("current")


class _TnSysConfiguredSnmpSourceIPv6_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSourceIPv6 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSourceIPv6_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSourceIPv6_Object = MibScalar
tnSysConfiguredSnmpSourceIPv6 = _TnSysConfiguredSnmpSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 25),
    _TnSysConfiguredSnmpSourceIPv6_Type()
)
tnSysConfiguredSnmpSourceIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSourceIPv6.setStatus("current")


class _TnSysConfiguredRadiusSourceIPv6_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSourceIPv6 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSourceIPv6_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSourceIPv6_Object = MibScalar
tnSysConfiguredRadiusSourceIPv6 = _TnSysConfiguredRadiusSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 26),
    _TnSysConfiguredRadiusSourceIPv6_Type()
)
tnSysConfiguredRadiusSourceIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSourceIPv6.setStatus("current")
_TnSysRedundancy_ObjectIdentity = ObjectIdentity
tnSysRedundancy = _TnSysRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3)
)


class _TnSysRedundancyDbSynchState_Type(Integer32):
    """Custom type tnSysRedundancyDbSynchState based on Integer32"""
    defaultValue = 1

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
        *(("notSynched", 1),
          ("synched", 2),
          ("synching", 3),
          ("unSynchable", 4),
          ("synchFailure", 5),
          ("schemaTesting", 6))
    )


_TnSysRedundancyDbSynchState_Type.__name__ = "Integer32"
_TnSysRedundancyDbSynchState_Object = MibScalar
tnSysRedundancyDbSynchState = _TnSysRedundancyDbSynchState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 1),
    _TnSysRedundancyDbSynchState_Type()
)
tnSysRedundancyDbSynchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyDbSynchState.setStatus("current")


class _TnSysRedundancyDbResynch_Type(TnCommand):
    """Custom type tnSysRedundancyDbResynch based on TnCommand"""
    defaultValue = 1


_TnSysRedundancyDbResynch_Type.__name__ = "TnCommand"
_TnSysRedundancyDbResynch_Object = MibScalar
tnSysRedundancyDbResynch = _TnSysRedundancyDbResynch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 2),
    _TnSysRedundancyDbResynch_Type()
)
tnSysRedundancyDbResynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbResynch.setStatus("current")


class _TnSysRedundancyDbAudit_Type(TnCommand):
    """Custom type tnSysRedundancyDbAudit based on TnCommand"""
    defaultValue = 1


_TnSysRedundancyDbAudit_Type.__name__ = "TnCommand"
_TnSysRedundancyDbAudit_Object = MibScalar
tnSysRedundancyDbAudit = _TnSysRedundancyDbAudit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 3),
    _TnSysRedundancyDbAudit_Type()
)
tnSysRedundancyDbAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbAudit.setStatus("current")


class _TnSysRedundancyDbClear_Type(Integer32):
    """Custom type tnSysRedundancyDbClear based on Integer32"""
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
        *(("noCmd", 1),
          ("execute", 2),
          ("executeAndClearSonetSdhMode", 3))
    )


_TnSysRedundancyDbClear_Type.__name__ = "Integer32"
_TnSysRedundancyDbClear_Object = MibScalar
tnSysRedundancyDbClear = _TnSysRedundancyDbClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 4),
    _TnSysRedundancyDbClear_Type()
)
tnSysRedundancyDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbClear.setStatus("current")


class _TnSysRedundancyActiveCCSlot_Type(Unsigned32):
    """Custom type tnSysRedundancyActiveCCSlot based on Unsigned32"""
    defaultValue = 1


_TnSysRedundancyActiveCCSlot_Type.__name__ = "Unsigned32"
_TnSysRedundancyActiveCCSlot_Object = MibScalar
tnSysRedundancyActiveCCSlot = _TnSysRedundancyActiveCCSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 5),
    _TnSysRedundancyActiveCCSlot_Type()
)
tnSysRedundancyActiveCCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyActiveCCSlot.setStatus("current")


class _TnSysRedundancyDbInvalid_Type(TruthValue):
    """Custom type tnSysRedundancyDbInvalid based on TruthValue"""
    defaultValue = 2


_TnSysRedundancyDbInvalid_Type.__name__ = "TruthValue"
_TnSysRedundancyDbInvalid_Object = MibScalar
tnSysRedundancyDbInvalid = _TnSysRedundancyDbInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 6),
    _TnSysRedundancyDbInvalid_Type()
)
tnSysRedundancyDbInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyDbInvalid.setStatus("current")


class _TnSysRedundancyMateCCReadyToProtect_Type(TruthValue):
    """Custom type tnSysRedundancyMateCCReadyToProtect based on TruthValue"""
    defaultValue = 2


_TnSysRedundancyMateCCReadyToProtect_Type.__name__ = "TruthValue"
_TnSysRedundancyMateCCReadyToProtect_Object = MibScalar
tnSysRedundancyMateCCReadyToProtect = _TnSysRedundancyMateCCReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 7),
    _TnSysRedundancyMateCCReadyToProtect_Type()
)
tnSysRedundancyMateCCReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyMateCCReadyToProtect.setStatus("current")
_TnSysDiscovery_ObjectIdentity = ObjectIdentity
tnSysDiscovery = _TnSysDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4)
)


class _TnSysDiscoveryFilename_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryFilename based on SnmpAdminString"""
    defaultValue = OctetString("./remote-file")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDiscoveryFilename_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryFilename_Object = MibScalar
tnSysDiscoveryFilename = _TnSysDiscoveryFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 2),
    _TnSysDiscoveryFilename_Type()
)
tnSysDiscoveryFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryFilename.setStatus("current")


class _TnSysDiscoveryMask_Type(Bits):
    """Custom type tnSysDiscoveryMask based on Bits"""
    defaultBinValue = "00001"

    namedValues = NamedValues(
        *(("stage1", 0),
          ("stage2", 1),
          ("stage3", 2),
          ("stage4", 3),
          ("stage5", 4),
          ("stage6", 5),
          ("stage7", 6))
    )

_TnSysDiscoveryMask_Type.__name__ = "Bits"
_TnSysDiscoveryMask_Object = MibScalar
tnSysDiscoveryMask = _TnSysDiscoveryMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 3),
    _TnSysDiscoveryMask_Type()
)
tnSysDiscoveryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryMask.setStatus("current")


class _TnSysDiscoveryControl_Type(Integer32):
    """Custom type tnSysDiscoveryControl based on Integer32"""
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
        *(("noCmd", 1),
          ("start", 2),
          ("abort", 3))
    )


_TnSysDiscoveryControl_Type.__name__ = "Integer32"
_TnSysDiscoveryControl_Object = MibScalar
tnSysDiscoveryControl = _TnSysDiscoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 4),
    _TnSysDiscoveryControl_Type()
)
tnSysDiscoveryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryControl.setStatus("current")


class _TnSysDiscoveryStatus_Type(Integer32):
    """Custom type tnSysDiscoveryStatus based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnSysDiscoveryStatus_Type.__name__ = "Integer32"
_TnSysDiscoveryStatus_Object = MibScalar
tnSysDiscoveryStatus = _TnSysDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 5),
    _TnSysDiscoveryStatus_Type()
)
tnSysDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDiscoveryStatus.setStatus("current")


class _TnSysDiscoveryErrorCode_Type(Integer32):
    """Custom type tnSysDiscoveryErrorCode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("unknown", 2),
          ("timeout", 3),
          ("serverError", 4),
          ("networkError", 5),
          ("fileSystemError", 6),
          ("statsBinsRolled", 7))
    )


_TnSysDiscoveryErrorCode_Type.__name__ = "Integer32"
_TnSysDiscoveryErrorCode_Object = MibScalar
tnSysDiscoveryErrorCode = _TnSysDiscoveryErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 6),
    _TnSysDiscoveryErrorCode_Type()
)
tnSysDiscoveryErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDiscoveryErrorCode.setStatus("current")


class _TnSysDiscoveryBinnedStatsInterval_Type(Unsigned32):
    """Custom type tnSysDiscoveryBinnedStatsInterval based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryBinnedStatsInterval_Type.__name__ = "Unsigned32"
_TnSysDiscoveryBinnedStatsInterval_Object = MibScalar
tnSysDiscoveryBinnedStatsInterval = _TnSysDiscoveryBinnedStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 8),
    _TnSysDiscoveryBinnedStatsInterval_Type()
)
tnSysDiscoveryBinnedStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryBinnedStatsInterval.setStatus("current")


class _TnSysDiscoveryBinnedStatsBin_Type(Unsigned32):
    """Custom type tnSysDiscoveryBinnedStatsBin based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryBinnedStatsBin_Type.__name__ = "Unsigned32"
_TnSysDiscoveryBinnedStatsBin_Object = MibScalar
tnSysDiscoveryBinnedStatsBin = _TnSysDiscoveryBinnedStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 9),
    _TnSysDiscoveryBinnedStatsBin_Type()
)
tnSysDiscoveryBinnedStatsBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryBinnedStatsBin.setStatus("current")


class _TnSysDiscoveryServerProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysDiscoveryServerProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysDiscoveryServerProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysDiscoveryServerProtocol_Object = MibScalar
tnSysDiscoveryServerProtocol = _TnSysDiscoveryServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 10),
    _TnSysDiscoveryServerProtocol_Type()
)
tnSysDiscoveryServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerProtocol.setStatus("current")


class _TnSysDiscoveryServerIp_Type(IpAddress):
    """Custom type tnSysDiscoveryServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysDiscoveryServerIp_Type.__name__ = "IpAddress"
_TnSysDiscoveryServerIp_Object = MibScalar
tnSysDiscoveryServerIp = _TnSysDiscoveryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 11),
    _TnSysDiscoveryServerIp_Type()
)
tnSysDiscoveryServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerIp.setStatus("current")


class _TnSysDiscoveryServerUserId_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysDiscoveryServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryServerUserId_Object = MibScalar
tnSysDiscoveryServerUserId = _TnSysDiscoveryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 12),
    _TnSysDiscoveryServerUserId_Type()
)
tnSysDiscoveryServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerUserId.setStatus("current")


class _TnSysDiscoveryServerPassword_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysDiscoveryServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryServerPassword_Object = MibScalar
tnSysDiscoveryServerPassword = _TnSysDiscoveryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 13),
    _TnSysDiscoveryServerPassword_Type()
)
tnSysDiscoveryServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerPassword.setStatus("current")


class _TnSysDiscoveryServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysDiscoveryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysDiscoveryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysDiscoveryServerInetAddressType_Object = MibScalar
tnSysDiscoveryServerInetAddressType = _TnSysDiscoveryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 14),
    _TnSysDiscoveryServerInetAddressType_Type()
)
tnSysDiscoveryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerInetAddressType.setStatus("current")


class _TnSysDiscoveryServerInetAddress_Type(InetAddress):
    """Custom type tnSysDiscoveryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysDiscoveryServerInetAddress_Type.__name__ = "InetAddress"
_TnSysDiscoveryServerInetAddress_Object = MibScalar
tnSysDiscoveryServerInetAddress = _TnSysDiscoveryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 15),
    _TnSysDiscoveryServerInetAddress_Type()
)
tnSysDiscoveryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerInetAddress.setStatus("current")


class _TnSysDiscoveryPort_Type(Unsigned32):
    """Custom type tnSysDiscoveryPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysDiscoveryPort_Type.__name__ = "Unsigned32"
_TnSysDiscoveryPort_Object = MibScalar
tnSysDiscoveryPort = _TnSysDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 16),
    _TnSysDiscoveryPort_Type()
)
tnSysDiscoveryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryPort.setStatus("current")


class _TnSysDiscoveryPrevious15minBinFilesTransfer_Type(Unsigned32):
    """Custom type tnSysDiscoveryPrevious15minBinFilesTransfer based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryPrevious15minBinFilesTransfer_Type.__name__ = "Unsigned32"
_TnSysDiscoveryPrevious15minBinFilesTransfer_Object = MibScalar
tnSysDiscoveryPrevious15minBinFilesTransfer = _TnSysDiscoveryPrevious15minBinFilesTransfer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 17),
    _TnSysDiscoveryPrevious15minBinFilesTransfer_Type()
)
tnSysDiscoveryPrevious15minBinFilesTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryPrevious15minBinFilesTransfer.setStatus("current")


class _TnSysDiscoveryPrevious1dayBinFilesTransfer_Type(Unsigned32):
    """Custom type tnSysDiscoveryPrevious1dayBinFilesTransfer based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryPrevious1dayBinFilesTransfer_Type.__name__ = "Unsigned32"
_TnSysDiscoveryPrevious1dayBinFilesTransfer_Object = MibScalar
tnSysDiscoveryPrevious1dayBinFilesTransfer = _TnSysDiscoveryPrevious1dayBinFilesTransfer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 18),
    _TnSysDiscoveryPrevious1dayBinFilesTransfer_Type()
)
tnSysDiscoveryPrevious1dayBinFilesTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryPrevious1dayBinFilesTransfer.setStatus("current")


class _TnSysDiscoveryTransferTimeOffset_Type(Unsigned32):
    """Custom type tnSysDiscoveryTransferTimeOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_TnSysDiscoveryTransferTimeOffset_Type.__name__ = "Unsigned32"
_TnSysDiscoveryTransferTimeOffset_Object = MibScalar
tnSysDiscoveryTransferTimeOffset = _TnSysDiscoveryTransferTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 19),
    _TnSysDiscoveryTransferTimeOffset_Type()
)
tnSysDiscoveryTransferTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryTransferTimeOffset.setStatus("current")


class _TnSysDiscoveryTransferTraps_Type(TruthValue):
    """Custom type tnSysDiscoveryTransferTraps based on TruthValue"""
    defaultValue = 1


_TnSysDiscoveryTransferTraps_Type.__name__ = "TruthValue"
_TnSysDiscoveryTransferTraps_Object = MibScalar
tnSysDiscoveryTransferTraps = _TnSysDiscoveryTransferTraps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 20),
    _TnSysDiscoveryTransferTraps_Type()
)
tnSysDiscoveryTransferTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryTransferTraps.setStatus("current")
_TnSysLogging_ObjectIdentity = ObjectIdentity
tnSysLogging = _TnSysLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5)
)


class _TnSysLoggingCLI_Type(Bits):
    """Custom type tnSysLoggingCLI based on Bits"""
    namedValues = NamedValues(
        *(("disableAllLogging", 0),
          ("level1Read", 1),
          ("level1Write", 2),
          ("level2Read", 3),
          ("level2Write", 4),
          ("level3Read", 5),
          ("level3Write", 6),
          ("level4Read", 7),
          ("level4Write", 8),
          ("level5Read", 9),
          ("level5Write", 10),
          ("level6Read", 11),
          ("level6Write", 12))
    )

_TnSysLoggingCLI_Type.__name__ = "Bits"
_TnSysLoggingCLI_Object = MibScalar
tnSysLoggingCLI = _TnSysLoggingCLI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5, 1),
    _TnSysLoggingCLI_Type()
)
tnSysLoggingCLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLoggingCLI.setStatus("current")


class _TnSysLoggingSNMP_Type(Bits):
    """Custom type tnSysLoggingSNMP based on Bits"""
    namedValues = NamedValues(
        *(("disableAllLogging", 0),
          ("level1Read", 1),
          ("level1Write", 2),
          ("level2Read", 3),
          ("level2Write", 4),
          ("level3Read", 5),
          ("level3Write", 6),
          ("level4Read", 7),
          ("level4Write", 8),
          ("level5Read", 9),
          ("level5Write", 10),
          ("level6Read", 11),
          ("level6Write", 12))
    )

_TnSysLoggingSNMP_Type.__name__ = "Bits"
_TnSysLoggingSNMP_Object = MibScalar
tnSysLoggingSNMP = _TnSysLoggingSNMP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5, 2),
    _TnSysLoggingSNMP_Type()
)
tnSysLoggingSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLoggingSNMP.setStatus("current")
_TnSysBackupAndRestore_ObjectIdentity = ObjectIdentity
tnSysBackupAndRestore = _TnSysBackupAndRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6)
)


class _TnSysBackupAndRestoreCommand_Type(Integer32):
    """Custom type tnSysBackupAndRestoreCommand based on Integer32"""
    defaultValue = 1

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
        *(("noCmd", 1),
          ("backupToRemote", 2),
          ("restoreFromRemote", 3),
          ("restoreForceFromRemote", 4),
          ("backupToLocal", 5))
    )


_TnSysBackupAndRestoreCommand_Type.__name__ = "Integer32"
_TnSysBackupAndRestoreCommand_Object = MibScalar
tnSysBackupAndRestoreCommand = _TnSysBackupAndRestoreCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 1),
    _TnSysBackupAndRestoreCommand_Type()
)
tnSysBackupAndRestoreCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreCommand.setStatus("current")


class _TnSysBackupAndRestoreRemoteHostIp_Type(IpAddress):
    """Custom type tnSysBackupAndRestoreRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysBackupAndRestoreRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysBackupAndRestoreRemoteHostIp_Object = MibScalar
tnSysBackupAndRestoreRemoteHostIp = _TnSysBackupAndRestoreRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 2),
    _TnSysBackupAndRestoreRemoteHostIp_Type()
)
tnSysBackupAndRestoreRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostIp.setStatus("current")


class _TnSysBackupAndRestoreRemotePath_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestoreRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreRemotePath_Object = MibScalar
tnSysBackupAndRestoreRemotePath = _TnSysBackupAndRestoreRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 3),
    _TnSysBackupAndRestoreRemotePath_Type()
)
tnSysBackupAndRestoreRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemotePath.setStatus("current")


class _TnSysBackupAndRestoreStatus_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreStatus based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysBackupAndRestoreStatus_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreStatus_Object = MibScalar
tnSysBackupAndRestoreStatus = _TnSysBackupAndRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 4),
    _TnSysBackupAndRestoreStatus_Type()
)
tnSysBackupAndRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreStatus.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFilename_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreLastBackupFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysBackupAndRestoreLastBackupFilename_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreLastBackupFilename_Object = MibScalar
tnSysBackupAndRestoreLastBackupFilename = _TnSysBackupAndRestoreLastBackupFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 5),
    _TnSysBackupAndRestoreLastBackupFilename_Type()
)
tnSysBackupAndRestoreLastBackupFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFilename.setStatus("current")


class _TnSysBackupAndRestoreLastCommand_Type(Integer32):
    """Custom type tnSysBackupAndRestoreLastCommand based on Integer32"""
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
        *(("noCommand", 1),
          ("unknown", 2),
          ("backupToRemote", 3),
          ("restoreFromRemote", 4))
    )


_TnSysBackupAndRestoreLastCommand_Type.__name__ = "Integer32"
_TnSysBackupAndRestoreLastCommand_Object = MibScalar
tnSysBackupAndRestoreLastCommand = _TnSysBackupAndRestoreLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 6),
    _TnSysBackupAndRestoreLastCommand_Type()
)
tnSysBackupAndRestoreLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastCommand.setStatus("current")


class _TnSysBackupAndRestorePercentCompleted_Type(Unsigned32):
    """Custom type tnSysBackupAndRestorePercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysBackupAndRestorePercentCompleted_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestorePercentCompleted_Object = MibScalar
tnSysBackupAndRestorePercentCompleted = _TnSysBackupAndRestorePercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 7),
    _TnSysBackupAndRestorePercentCompleted_Type()
)
tnSysBackupAndRestorePercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestorePercentCompleted.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFileTimeStamp_Type(Unsigned32):
    """Custom type tnSysBackupAndRestoreLastBackupFileTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysBackupAndRestoreLastBackupFileTimeStamp_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestoreLastBackupFileTimeStamp_Object = MibScalar
tnSysBackupAndRestoreLastBackupFileTimeStamp = _TnSysBackupAndRestoreLastBackupFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 8),
    _TnSysBackupAndRestoreLastBackupFileTimeStamp_Type()
)
tnSysBackupAndRestoreLastBackupFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFileTimeStamp.setStatus("current")


class _TnSysBackupAndRestoreProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysBackupAndRestoreProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysBackupAndRestoreProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysBackupAndRestoreProtocol_Object = MibScalar
tnSysBackupAndRestoreProtocol = _TnSysBackupAndRestoreProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 9),
    _TnSysBackupAndRestoreProtocol_Type()
)
tnSysBackupAndRestoreProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreProtocol.setStatus("current")


class _TnSysBackupAndRestoreUserId_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestoreUserId_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreUserId_Object = MibScalar
tnSysBackupAndRestoreUserId = _TnSysBackupAndRestoreUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 10),
    _TnSysBackupAndRestoreUserId_Type()
)
tnSysBackupAndRestoreUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreUserId.setStatus("current")


class _TnSysBackupAndRestorePassword_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestorePassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestorePassword_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestorePassword_Object = MibScalar
tnSysBackupAndRestorePassword = _TnSysBackupAndRestorePassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 11),
    _TnSysBackupAndRestorePassword_Type()
)
tnSysBackupAndRestorePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestorePassword.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFileCrc_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreLastBackupFileCrc based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysBackupAndRestoreLastBackupFileCrc_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreLastBackupFileCrc_Object = MibScalar
tnSysBackupAndRestoreLastBackupFileCrc = _TnSysBackupAndRestoreLastBackupFileCrc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 12),
    _TnSysBackupAndRestoreLastBackupFileCrc_Type()
)
tnSysBackupAndRestoreLastBackupFileCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFileCrc.setStatus("current")


class _TnSysBackupAndRestoreRemoteHostInetAddressType_Type(InetAddressType):
    """Custom type tnSysBackupAndRestoreRemoteHostInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysBackupAndRestoreRemoteHostInetAddressType_Type.__name__ = "InetAddressType"
_TnSysBackupAndRestoreRemoteHostInetAddressType_Object = MibScalar
tnSysBackupAndRestoreRemoteHostInetAddressType = _TnSysBackupAndRestoreRemoteHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 14),
    _TnSysBackupAndRestoreRemoteHostInetAddressType_Type()
)
tnSysBackupAndRestoreRemoteHostInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostInetAddressType.setStatus("current")


class _TnSysBackupAndRestoreRemoteHostInetAddress_Type(InetAddress):
    """Custom type tnSysBackupAndRestoreRemoteHostInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysBackupAndRestoreRemoteHostInetAddress_Type.__name__ = "InetAddress"
_TnSysBackupAndRestoreRemoteHostInetAddress_Object = MibScalar
tnSysBackupAndRestoreRemoteHostInetAddress = _TnSysBackupAndRestoreRemoteHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 15),
    _TnSysBackupAndRestoreRemoteHostInetAddress_Type()
)
tnSysBackupAndRestoreRemoteHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostInetAddress.setStatus("current")


class _TnSysBackupAndRestoreLocalInfo_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreLocalInfo based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysBackupAndRestoreLocalInfo_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreLocalInfo_Object = MibScalar
tnSysBackupAndRestoreLocalInfo = _TnSysBackupAndRestoreLocalInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 16),
    _TnSysBackupAndRestoreLocalInfo_Type()
)
tnSysBackupAndRestoreLocalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLocalInfo.setStatus("current")


class _TnSysBackupAndRestoreLocalDelete_Type(Integer32):
    """Custom type tnSysBackupAndRestoreLocalDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2))
    )


_TnSysBackupAndRestoreLocalDelete_Type.__name__ = "Integer32"
_TnSysBackupAndRestoreLocalDelete_Object = MibScalar
tnSysBackupAndRestoreLocalDelete = _TnSysBackupAndRestoreLocalDelete_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 18),
    _TnSysBackupAndRestoreLocalDelete_Type()
)
tnSysBackupAndRestoreLocalDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLocalDelete.setStatus("current")


class _TnSysBackupAndRestorePort_Type(Unsigned32):
    """Custom type tnSysBackupAndRestorePort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysBackupAndRestorePort_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestorePort_Object = MibScalar
tnSysBackupAndRestorePort = _TnSysBackupAndRestorePort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 19),
    _TnSysBackupAndRestorePort_Type()
)
tnSysBackupAndRestorePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestorePort.setStatus("current")


class _TnSysBackupAndRestoreFallBackTimeStamp_Type(Unsigned32):
    """Custom type tnSysBackupAndRestoreFallBackTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysBackupAndRestoreFallBackTimeStamp_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestoreFallBackTimeStamp_Object = MibScalar
tnSysBackupAndRestoreFallBackTimeStamp = _TnSysBackupAndRestoreFallBackTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 20),
    _TnSysBackupAndRestoreFallBackTimeStamp_Type()
)
tnSysBackupAndRestoreFallBackTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreFallBackTimeStamp.setStatus("current")
_TnSysNtp_ObjectIdentity = ObjectIdentity
tnSysNtp = _TnSysNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7)
)


class _TnSysNtpEnable_Type(TruthValue):
    """Custom type tnSysNtpEnable based on TruthValue"""
    defaultValue = 2


_TnSysNtpEnable_Type.__name__ = "TruthValue"
_TnSysNtpEnable_Object = MibScalar
tnSysNtpEnable = _TnSysNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 1),
    _TnSysNtpEnable_Type()
)
tnSysNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpEnable.setStatus("current")


class _TnSysNtpSynched_Type(TruthValue):
    """Custom type tnSysNtpSynched based on TruthValue"""
    defaultValue = 2


_TnSysNtpSynched_Type.__name__ = "TruthValue"
_TnSysNtpSynched_Object = MibScalar
tnSysNtpSynched = _TnSysNtpSynched_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 8),
    _TnSysNtpSynched_Type()
)
tnSysNtpSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpSynched.setStatus("current")


class _TnSysNtpServerCurrentIpAddress_Type(IpAddress):
    """Custom type tnSysNtpServerCurrentIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysNtpServerCurrentIpAddress_Type.__name__ = "IpAddress"
_TnSysNtpServerCurrentIpAddress_Object = MibScalar
tnSysNtpServerCurrentIpAddress = _TnSysNtpServerCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 9),
    _TnSysNtpServerCurrentIpAddress_Type()
)
tnSysNtpServerCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentIpAddress.setStatus("current")
_TnSysNtpDriftString_Type = OctetString
_TnSysNtpDriftString_Object = MibScalar
tnSysNtpDriftString = _TnSysNtpDriftString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 11),
    _TnSysNtpDriftString_Type()
)
tnSysNtpDriftString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpDriftString.setStatus("current")
_TnSysNtpTimeOffsetString_Type = OctetString
_TnSysNtpTimeOffsetString_Object = MibScalar
tnSysNtpTimeOffsetString = _TnSysNtpTimeOffsetString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 12),
    _TnSysNtpTimeOffsetString_Type()
)
tnSysNtpTimeOffsetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpTimeOffsetString.setStatus("current")


class _TnSysNtpClockMode_Type(Integer32):
    """Custom type tnSysNtpClockMode based on Integer32"""
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
        *(("freeRun", 1),
          ("holdOver", 2),
          ("sync", 3),
          ("syncRed", 4))
    )


_TnSysNtpClockMode_Type.__name__ = "Integer32"
_TnSysNtpClockMode_Object = MibScalar
tnSysNtpClockMode = _TnSysNtpClockMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 13),
    _TnSysNtpClockMode_Type()
)
tnSysNtpClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpClockMode.setStatus("current")


class _TnSysNtpServerCurrentInetAddressType_Type(InetAddressType):
    """Custom type tnSysNtpServerCurrentInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysNtpServerCurrentInetAddressType_Type.__name__ = "InetAddressType"
_TnSysNtpServerCurrentInetAddressType_Object = MibScalar
tnSysNtpServerCurrentInetAddressType = _TnSysNtpServerCurrentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 14),
    _TnSysNtpServerCurrentInetAddressType_Type()
)
tnSysNtpServerCurrentInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentInetAddressType.setStatus("current")


class _TnSysNtpServerCurrentInetAddress_Type(InetAddress):
    """Custom type tnSysNtpServerCurrentInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysNtpServerCurrentInetAddress_Type.__name__ = "InetAddress"
_TnSysNtpServerCurrentInetAddress_Object = MibScalar
tnSysNtpServerCurrentInetAddress = _TnSysNtpServerCurrentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 15),
    _TnSysNtpServerCurrentInetAddress_Type()
)
tnSysNtpServerCurrentInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentInetAddress.setStatus("current")
_TnSysNtpServers_ObjectIdentity = ObjectIdentity
tnSysNtpServers = _TnSysNtpServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8)
)
_TnSysNtpServerTable_Object = MibTable
tnSysNtpServerTable = _TnSysNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tnSysNtpServerTable.setStatus("current")
_TnSysNtpServerEntry_Object = MibTableRow
tnSysNtpServerEntry = _TnSysNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1)
)
tnSysNtpServerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerEntry.setStatus("current")


class _TnSysNtpServerIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnSysNtpServerIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerIndex_Object = MibTableColumn
tnSysNtpServerIndex = _TnSysNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 1),
    _TnSysNtpServerIndex_Type()
)
tnSysNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerIndex.setStatus("current")
_TnSysNtpServerIpAddress_Type = IpAddress
_TnSysNtpServerIpAddress_Object = MibTableColumn
tnSysNtpServerIpAddress = _TnSysNtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 2),
    _TnSysNtpServerIpAddress_Type()
)
tnSysNtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerIpAddress.setStatus("current")
_TnSysNtpServerRowStatus_Type = RowStatus
_TnSysNtpServerRowStatus_Object = MibTableColumn
tnSysNtpServerRowStatus = _TnSysNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 3),
    _TnSysNtpServerRowStatus_Type()
)
tnSysNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerRowStatus.setStatus("current")


class _TnSysNtpServerKeyIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysNtpServerKeyIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerKeyIndex_Object = MibTableColumn
tnSysNtpServerKeyIndex = _TnSysNtpServerKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 4),
    _TnSysNtpServerKeyIndex_Type()
)
tnSysNtpServerKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerKeyIndex.setStatus("current")


class _TnSysNtpServerInetAddress_Type(InetAddress):
    """Custom type tnSysNtpServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysNtpServerInetAddress_Type.__name__ = "InetAddress"
_TnSysNtpServerInetAddress_Object = MibTableColumn
tnSysNtpServerInetAddress = _TnSysNtpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 5),
    _TnSysNtpServerInetAddress_Type()
)
tnSysNtpServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerInetAddress.setStatus("current")


class _TnSysNtpServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysNtpServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysNtpServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysNtpServerInetAddressType_Object = MibTableColumn
tnSysNtpServerInetAddressType = _TnSysNtpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 6),
    _TnSysNtpServerInetAddressType_Type()
)
tnSysNtpServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerInetAddressType.setStatus("current")
_TnSnmpTargetAddresses_ObjectIdentity = ObjectIdentity
tnSnmpTargetAddresses = _TnSnmpTargetAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9)
)
_TnSnmpTargetAddrTable_Object = MibTable
tnSnmpTargetAddrTable = _TnSnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddrTable.setStatus("current")
_TnSnmpTargetAddrEntry_Object = MibTableRow
tnSnmpTargetAddrEntry = _TnSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddrEntry.setStatus("current")
_TnSnmpTargetAddrNmsStationGroupId_Type = Unsigned32
_TnSnmpTargetAddrNmsStationGroupId_Object = MibTableColumn
tnSnmpTargetAddrNmsStationGroupId = _TnSnmpTargetAddrNmsStationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1, 1),
    _TnSnmpTargetAddrNmsStationGroupId_Type()
)
tnSnmpTargetAddrNmsStationGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSnmpTargetAddrNmsStationGroupId.setStatus("current")


class _TnSnmpTargetAddrTrapGroupId_Type(Integer32):
    """Custom type tnSnmpTargetAddrTrapGroupId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOtherData", 1),
          ("pmData", 2))
    )


_TnSnmpTargetAddrTrapGroupId_Type.__name__ = "Integer32"
_TnSnmpTargetAddrTrapGroupId_Object = MibTableColumn
tnSnmpTargetAddrTrapGroupId = _TnSnmpTargetAddrTrapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1, 2),
    _TnSnmpTargetAddrTrapGroupId_Type()
)
tnSnmpTargetAddrTrapGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSnmpTargetAddrTrapGroupId.setStatus("current")
_TnSnmpTargetAddrDisableTrap_Type = Unsigned32
_TnSnmpTargetAddrDisableTrap_Object = MibTableColumn
tnSnmpTargetAddrDisableTrap = _TnSnmpTargetAddrDisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1, 3),
    _TnSnmpTargetAddrDisableTrap_Type()
)
tnSnmpTargetAddrDisableTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSnmpTargetAddrDisableTrap.setStatus("current")
_TnSyslog_ObjectIdentity = ObjectIdentity
tnSyslog = _TnSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10)
)


class _TnSyslogIpAddress_Type(IpAddress):
    """Custom type tnSyslogIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSyslogIpAddress_Type.__name__ = "IpAddress"
_TnSyslogIpAddress_Object = MibScalar
tnSyslogIpAddress = _TnSyslogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 1),
    _TnSyslogIpAddress_Type()
)
tnSyslogIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogIpAddress.setStatus("current")


class _TnSyslogPort_Type(Unsigned32):
    """Custom type tnSyslogPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSyslogPort_Type.__name__ = "Unsigned32"
_TnSyslogPort_Object = MibScalar
tnSyslogPort = _TnSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 2),
    _TnSyslogPort_Type()
)
tnSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogPort.setStatus("current")


class _TnSyslogFacility_Type(Integer32):
    """Custom type tnSyslogFacility based on Integer32"""
    defaultValue = 13

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kern", 1),
          ("user", 2),
          ("mail", 3),
          ("daemon", 4),
          ("auth", 5),
          ("syslog", 6),
          ("lpr", 7),
          ("news", 8),
          ("uucp", 9),
          ("cron", 10),
          ("authPriv", 11),
          ("ftp", 12),
          ("local0", 13),
          ("local1", 14),
          ("local2", 15),
          ("local3", 16),
          ("local4", 17),
          ("local5", 18),
          ("local6", 19),
          ("local7", 20),
          ("all", 21),
          ("logAudit", 22),
          ("logAlert", 23))
    )


_TnSyslogFacility_Type.__name__ = "Integer32"
_TnSyslogFacility_Object = MibScalar
tnSyslogFacility = _TnSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 3),
    _TnSyslogFacility_Type()
)
tnSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogFacility.setStatus("current")


class _TnSyslogPriority_Type(Integer32):
    """Custom type tnSyslogPriority based on Integer32"""
    defaultValue = 8

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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_TnSyslogPriority_Type.__name__ = "Integer32"
_TnSyslogPriority_Object = MibScalar
tnSyslogPriority = _TnSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 4),
    _TnSyslogPriority_Type()
)
tnSyslogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogPriority.setStatus("current")


class _TnSyslogEnabled_Type(TruthValue):
    """Custom type tnSyslogEnabled based on TruthValue"""
    defaultValue = 2


_TnSyslogEnabled_Type.__name__ = "TruthValue"
_TnSyslogEnabled_Object = MibScalar
tnSyslogEnabled = _TnSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 5),
    _TnSyslogEnabled_Type()
)
tnSyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogEnabled.setStatus("current")


class _TnSyslogInetAddress_Type(InetAddress):
    """Custom type tnSyslogInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSyslogInetAddress_Type.__name__ = "InetAddress"
_TnSyslogInetAddress_Object = MibScalar
tnSyslogInetAddress = _TnSyslogInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 6),
    _TnSyslogInetAddress_Type()
)
tnSyslogInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogInetAddress.setStatus("current")


class _TnSyslogInetAddressType_Type(InetAddressType):
    """Custom type tnSyslogInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSyslogInetAddressType_Type.__name__ = "InetAddressType"
_TnSyslogInetAddressType_Object = MibScalar
tnSyslogInetAddressType = _TnSyslogInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 7),
    _TnSyslogInetAddressType_Type()
)
tnSyslogInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogInetAddressType.setStatus("current")


class _TnSyslogProtocol_Type(Integer32):
    """Custom type tnSyslogProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_TnSyslogProtocol_Type.__name__ = "Integer32"
_TnSyslogProtocol_Object = MibScalar
tnSyslogProtocol = _TnSyslogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 8),
    _TnSyslogProtocol_Type()
)
tnSyslogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogProtocol.setStatus("current")
_TnSysTiming_ObjectIdentity = ObjectIdentity
tnSysTiming = _TnSysTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11)
)


class _TnSysTimingPrimaryReference_Type(Unsigned32):
    """Custom type tnSysTimingPrimaryReference based on Unsigned32"""
    defaultValue = 0


_TnSysTimingPrimaryReference_Type.__name__ = "Unsigned32"
_TnSysTimingPrimaryReference_Object = MibScalar
tnSysTimingPrimaryReference = _TnSysTimingPrimaryReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 1),
    _TnSysTimingPrimaryReference_Type()
)
tnSysTimingPrimaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReference.setStatus("current")


class _TnSysTimingSecondaryReference_Type(Unsigned32):
    """Custom type tnSysTimingSecondaryReference based on Unsigned32"""
    defaultValue = 0


_TnSysTimingSecondaryReference_Type.__name__ = "Unsigned32"
_TnSysTimingSecondaryReference_Object = MibScalar
tnSysTimingSecondaryReference = _TnSysTimingSecondaryReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 2),
    _TnSysTimingSecondaryReference_Type()
)
tnSysTimingSecondaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReference.setStatus("current")


class _TnSysTimingLastSwitchTime_Type(Unsigned32):
    """Custom type tnSysTimingLastSwitchTime based on Unsigned32"""
    defaultValue = 0


_TnSysTimingLastSwitchTime_Type.__name__ = "Unsigned32"
_TnSysTimingLastSwitchTime_Object = MibScalar
tnSysTimingLastSwitchTime = _TnSysTimingLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 3),
    _TnSysTimingLastSwitchTime_Type()
)
tnSysTimingLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingLastSwitchTime.setStatus("current")


class _TnSysTimingControl_Type(Integer32):
    """Custom type tnSysTimingControl based on Integer32"""
    defaultValue = 6

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
        *(("noCmd", 1),
          ("forceToPrimary", 2),
          ("forceToSecondary", 3),
          ("manualToPrimary", 4),
          ("manualToSecondary", 5),
          ("clear", 6))
    )


_TnSysTimingControl_Type.__name__ = "Integer32"
_TnSysTimingControl_Object = MibScalar
tnSysTimingControl = _TnSysTimingControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 4),
    _TnSysTimingControl_Type()
)
tnSysTimingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingControl.setStatus("current")


class _TnSysTimingPrimaryReferenceStatus_Type(Integer32):
    """Custom type tnSysTimingPrimaryReferenceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("manual", 3),
          ("forced", 4),
          ("failed", 5),
          ("failedLOS", 6),
          ("failedLOF", 7),
          ("failedLOC", 8),
          ("failedFreqOffset", 9),
          ("failedAIS", 10),
          ("failedSSM", 11),
          ("qualifying", 12))
    )


_TnSysTimingPrimaryReferenceStatus_Type.__name__ = "Integer32"
_TnSysTimingPrimaryReferenceStatus_Object = MibScalar
tnSysTimingPrimaryReferenceStatus = _TnSysTimingPrimaryReferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 5),
    _TnSysTimingPrimaryReferenceStatus_Type()
)
tnSysTimingPrimaryReferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceStatus.setStatus("current")


class _TnSysTimingSecondaryReferenceStatus_Type(Integer32):
    """Custom type tnSysTimingSecondaryReferenceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("manual", 3),
          ("forced", 4),
          ("failed", 5),
          ("failedLOS", 6),
          ("failedLOF", 7),
          ("failedLOC", 8),
          ("failedFreqOffset", 9),
          ("failedAIS", 10),
          ("failedSSM", 11),
          ("qualifying", 12))
    )


_TnSysTimingSecondaryReferenceStatus_Type.__name__ = "Integer32"
_TnSysTimingSecondaryReferenceStatus_Object = MibScalar
tnSysTimingSecondaryReferenceStatus = _TnSysTimingSecondaryReferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 6),
    _TnSysTimingSecondaryReferenceStatus_Type()
)
tnSysTimingSecondaryReferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceStatus.setStatus("current")


class _TnSysTimingPrimaryReferenceQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingPrimaryReferenceQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingPrimaryReferenceQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingPrimaryReferenceQuality_Object = MibScalar
tnSysTimingPrimaryReferenceQuality = _TnSysTimingPrimaryReferenceQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 7),
    _TnSysTimingPrimaryReferenceQuality_Type()
)
tnSysTimingPrimaryReferenceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceQuality.setStatus("current")


class _TnSysTimingSecondaryReferenceQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingSecondaryReferenceQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingSecondaryReferenceQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingSecondaryReferenceQuality_Object = MibScalar
tnSysTimingSecondaryReferenceQuality = _TnSysTimingSecondaryReferenceQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 8),
    _TnSysTimingSecondaryReferenceQuality_Type()
)
tnSysTimingSecondaryReferenceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceQuality.setStatus("current")


class _TnSysTimingPrimaryReferenceTimingMode_Type(TropicSysTimingReferenceTimingMode):
    """Custom type tnSysTimingPrimaryReferenceTimingMode based on TropicSysTimingReferenceTimingMode"""
    defaultValue = 1


_TnSysTimingPrimaryReferenceTimingMode_Type.__name__ = "TropicSysTimingReferenceTimingMode"
_TnSysTimingPrimaryReferenceTimingMode_Object = MibScalar
tnSysTimingPrimaryReferenceTimingMode = _TnSysTimingPrimaryReferenceTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 9),
    _TnSysTimingPrimaryReferenceTimingMode_Type()
)
tnSysTimingPrimaryReferenceTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceTimingMode.setStatus("current")


class _TnSysTimingSecondaryReferenceTimingMode_Type(TropicSysTimingReferenceTimingMode):
    """Custom type tnSysTimingSecondaryReferenceTimingMode based on TropicSysTimingReferenceTimingMode"""
    defaultValue = 1


_TnSysTimingSecondaryReferenceTimingMode_Type.__name__ = "TropicSysTimingReferenceTimingMode"
_TnSysTimingSecondaryReferenceTimingMode_Object = MibScalar
tnSysTimingSecondaryReferenceTimingMode = _TnSysTimingSecondaryReferenceTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 10),
    _TnSysTimingSecondaryReferenceTimingMode_Type()
)
tnSysTimingSecondaryReferenceTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceTimingMode.setStatus("current")


class _TnSysTimingActiveReference_Type(Integer32):
    """Custom type tnSysTimingActiveReference based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_TnSysTimingActiveReference_Type.__name__ = "Integer32"
_TnSysTimingActiveReference_Object = MibScalar
tnSysTimingActiveReference = _TnSysTimingActiveReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 11),
    _TnSysTimingActiveReference_Type()
)
tnSysTimingActiveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingActiveReference.setStatus("current")


class _TnSysTimingClockingMode_Type(Integer32):
    """Custom type tnSysTimingClockingMode based on Integer32"""
    defaultValue = 1

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
          ("fastStart", 3),
          ("holdOver", 4),
          ("freeRun", 5))
    )


_TnSysTimingClockingMode_Type.__name__ = "Integer32"
_TnSysTimingClockingMode_Object = MibScalar
tnSysTimingClockingMode = _TnSysTimingClockingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 12),
    _TnSysTimingClockingMode_Type()
)
tnSysTimingClockingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingClockingMode.setStatus("current")


class _TnSysTimingSwitchingMode_Type(Integer32):
    """Custom type tnSysTimingSwitchingMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("revertive", 2),
          ("nonRevertive", 3))
    )


_TnSysTimingSwitchingMode_Type.__name__ = "Integer32"
_TnSysTimingSwitchingMode_Object = MibScalar
tnSysTimingSwitchingMode = _TnSysTimingSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 13),
    _TnSysTimingSwitchingMode_Type()
)
tnSysTimingSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingSwitchingMode.setStatus("current")


class _TnSysTimingFreeRunSuppressAlarms_Type(TruthValue):
    """Custom type tnSysTimingFreeRunSuppressAlarms based on TruthValue"""
    defaultValue = 2


_TnSysTimingFreeRunSuppressAlarms_Type.__name__ = "TruthValue"
_TnSysTimingFreeRunSuppressAlarms_Object = MibScalar
tnSysTimingFreeRunSuppressAlarms = _TnSysTimingFreeRunSuppressAlarms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 14),
    _TnSysTimingFreeRunSuppressAlarms_Type()
)
tnSysTimingFreeRunSuppressAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingFreeRunSuppressAlarms.setStatus("current")


class _TnSysTimingDs1FramingMode_Type(Integer32):
    """Custom type tnSysTimingDs1FramingMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sf", 2),
          ("esf", 3))
    )


_TnSysTimingDs1FramingMode_Type.__name__ = "Integer32"
_TnSysTimingDs1FramingMode_Object = MibScalar
tnSysTimingDs1FramingMode = _TnSysTimingDs1FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 15),
    _TnSysTimingDs1FramingMode_Type()
)
tnSysTimingDs1FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1FramingMode.setStatus("current")


class _TnSysTimingDs1LineCoding_Type(Integer32):
    """Custom type tnSysTimingDs1LineCoding based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ami", 2),
          ("b8zs", 3))
    )


_TnSysTimingDs1LineCoding_Type.__name__ = "Integer32"
_TnSysTimingDs1LineCoding_Object = MibScalar
tnSysTimingDs1LineCoding = _TnSysTimingDs1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 16),
    _TnSysTimingDs1LineCoding_Type()
)
tnSysTimingDs1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1LineCoding.setStatus("current")


class _TnSysTimingDs1SsmProcessing_Type(AluWdmEnabledDisabled):
    """Custom type tnSysTimingDs1SsmProcessing based on AluWdmEnabledDisabled"""
    defaultValue = 1


_TnSysTimingDs1SsmProcessing_Type.__name__ = "AluWdmEnabledDisabled"
_TnSysTimingDs1SsmProcessing_Object = MibScalar
tnSysTimingDs1SsmProcessing = _TnSysTimingDs1SsmProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 17),
    _TnSysTimingDs1SsmProcessing_Type()
)
tnSysTimingDs1SsmProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1SsmProcessing.setStatus("current")


class _TnSysTimingBitsAClockQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingBitsAClockQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingBitsAClockQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingBitsAClockQuality_Object = MibScalar
tnSysTimingBitsAClockQuality = _TnSysTimingBitsAClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 18),
    _TnSysTimingBitsAClockQuality_Type()
)
tnSysTimingBitsAClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitsAClockQuality.setStatus("current")


class _TnSysTimingBitsBClockQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingBitsBClockQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingBitsBClockQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingBitsBClockQuality_Object = MibScalar
tnSysTimingBitsBClockQuality = _TnSysTimingBitsBClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 19),
    _TnSysTimingBitsBClockQuality_Type()
)
tnSysTimingBitsBClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitsBClockQuality.setStatus("current")


class _TnSysTimingActiveLineTimingCable_Type(Integer32):
    """Custom type tnSysTimingActiveLineTimingCable based on Integer32"""
    defaultValue = 1

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
          ("notApplicable", 2),
          ("none", 3),
          ("a", 4),
          ("b", 5))
    )


_TnSysTimingActiveLineTimingCable_Type.__name__ = "Integer32"
_TnSysTimingActiveLineTimingCable_Object = MibScalar
tnSysTimingActiveLineTimingCable = _TnSysTimingActiveLineTimingCable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 20),
    _TnSysTimingActiveLineTimingCable_Type()
)
tnSysTimingActiveLineTimingCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingActiveLineTimingCable.setStatus("current")


class _TnSysTimingBitSourceType_Type(Integer32):
    """Custom type tnSysTimingBitSourceType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitSourceType_Type.__name__ = "Integer32"
_TnSysTimingBitSourceType_Object = MibScalar
tnSysTimingBitSourceType = _TnSysTimingBitSourceType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 21),
    _TnSysTimingBitSourceType_Type()
)
tnSysTimingBitSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitSourceType.setStatus("current")


class _TnSysTimingBitsAModuleType_Type(Integer32):
    """Custom type tnSysTimingBitsAModuleType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitsAModuleType_Type.__name__ = "Integer32"
_TnSysTimingBitsAModuleType_Object = MibScalar
tnSysTimingBitsAModuleType = _TnSysTimingBitsAModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 22),
    _TnSysTimingBitsAModuleType_Type()
)
tnSysTimingBitsAModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingBitsAModuleType.setStatus("current")


class _TnSysTimingBitsBModuleType_Type(Integer32):
    """Custom type tnSysTimingBitsBModuleType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitsBModuleType_Type.__name__ = "Integer32"
_TnSysTimingBitsBModuleType_Object = MibScalar
tnSysTimingBitsBModuleType = _TnSysTimingBitsBModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 23),
    _TnSysTimingBitsBModuleType_Type()
)
tnSysTimingBitsBModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingBitsBModuleType.setStatus("current")
_TnSysFeatures_ObjectIdentity = ObjectIdentity
tnSysFeatures = _TnSysFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12)
)


class _TnSysFeatureAutoTopology_Type(TruthValue):
    """Custom type tnSysFeatureAutoTopology based on TruthValue"""
    defaultValue = 2


_TnSysFeatureAutoTopology_Type.__name__ = "TruthValue"
_TnSysFeatureAutoTopology_Object = MibScalar
tnSysFeatureAutoTopology = _TnSysFeatureAutoTopology_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 3),
    _TnSysFeatureAutoTopology_Type()
)
tnSysFeatureAutoTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureAutoTopology.setStatus("current")


class _TnSysFeaturePauseFlowControl_Type(Integer32):
    """Custom type tnSysFeaturePauseFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("negotiated", 2))
    )


_TnSysFeaturePauseFlowControl_Type.__name__ = "Integer32"
_TnSysFeaturePauseFlowControl_Object = MibScalar
tnSysFeaturePauseFlowControl = _TnSysFeaturePauseFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 4),
    _TnSysFeaturePauseFlowControl_Type()
)
tnSysFeaturePauseFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeaturePauseFlowControl.setStatus("current")


class _TnSysFeatureIpUtilitiesRestricted_Type(TruthValue):
    """Custom type tnSysFeatureIpUtilitiesRestricted based on TruthValue"""
    defaultValue = 2


_TnSysFeatureIpUtilitiesRestricted_Type.__name__ = "TruthValue"
_TnSysFeatureIpUtilitiesRestricted_Object = MibScalar
tnSysFeatureIpUtilitiesRestricted = _TnSysFeatureIpUtilitiesRestricted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 5),
    _TnSysFeatureIpUtilitiesRestricted_Type()
)
tnSysFeatureIpUtilitiesRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureIpUtilitiesRestricted.setStatus("current")


class _TnSysFeatureFastServiceSetup_Type(TruthValue):
    """Custom type tnSysFeatureFastServiceSetup based on TruthValue"""
    defaultValue = 2


_TnSysFeatureFastServiceSetup_Type.__name__ = "TruthValue"
_TnSysFeatureFastServiceSetup_Object = MibScalar
tnSysFeatureFastServiceSetup = _TnSysFeatureFastServiceSetup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 6),
    _TnSysFeatureFastServiceSetup_Type()
)
tnSysFeatureFastServiceSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureFastServiceSetup.setStatus("current")
_TnSysFaultCorrelation_ObjectIdentity = ObjectIdentity
tnSysFaultCorrelation = _TnSysFaultCorrelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 13)
)
_TnSysFaultCorrelationTransientSuppression_Type = AluWdmEnabledDisabled
_TnSysFaultCorrelationTransientSuppression_Object = MibScalar
tnSysFaultCorrelationTransientSuppression = _TnSysFaultCorrelationTransientSuppression_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 13, 1),
    _TnSysFaultCorrelationTransientSuppression_Type()
)
tnSysFaultCorrelationTransientSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFaultCorrelationTransientSuppression.setStatus("current")
_TnSysErrorHandling_ObjectIdentity = ObjectIdentity
tnSysErrorHandling = _TnSysErrorHandling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 14)
)


class _TnSysSetRequestErrorMessage_Type(SnmpAdminString):
    """Custom type tnSysSetRequestErrorMessage based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSetRequestErrorMessage_Type.__name__ = "SnmpAdminString"
_TnSysSetRequestErrorMessage_Object = MibScalar
tnSysSetRequestErrorMessage = _TnSysSetRequestErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 14, 1),
    _TnSysSetRequestErrorMessage_Type()
)
tnSysSetRequestErrorMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSetRequestErrorMessage.setStatus("current")
_TnSysSecurity_ObjectIdentity = ObjectIdentity
tnSysSecurity = _TnSysSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15)
)


class _TnSysSecurityMode_Type(Integer32):
    """Custom type tnSysSecurityMode based on Integer32"""
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
        *(("normal", 1),
          ("encrypted", 2),
          ("fips", 3),
          ("anssi", 4))
    )


_TnSysSecurityMode_Type.__name__ = "Integer32"
_TnSysSecurityMode_Object = MibScalar
tnSysSecurityMode = _TnSysSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 1),
    _TnSysSecurityMode_Type()
)
tnSysSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSecurityMode.setStatus("current")
_TnSysSsh_ObjectIdentity = ObjectIdentity
tnSysSsh = _TnSysSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2)
)


class _TnSysSshKeyType_Type(Integer32):
    """Custom type tnSysSshKeyType based on Integer32"""
    defaultValue = 2

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
        *(("dsa", 1),
          ("rsa", 2),
          ("ecdsa", 3),
          ("ed25519", 4),
          ("all", 5))
    )


_TnSysSshKeyType_Type.__name__ = "Integer32"
_TnSysSshKeyType_Object = MibScalar
tnSysSshKeyType = _TnSysSshKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 1),
    _TnSysSshKeyType_Type()
)
tnSysSshKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyType.setStatus("current")


class _TnSysSshKeyModulus_Type(Unsigned32):
    """Custom type tnSysSshKeyModulus based on Unsigned32"""
    defaultValue = 2048


_TnSysSshKeyModulus_Type.__name__ = "Unsigned32"
_TnSysSshKeyModulus_Object = MibScalar
tnSysSshKeyModulus = _TnSysSshKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 2),
    _TnSysSshKeyModulus_Type()
)
tnSysSshKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyModulus.setStatus("current")


class _TnSysSshPublicKey_Type(OctetString):
    """Custom type tnSysSshPublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_TnSysSshPublicKey_Type.__name__ = "OctetString"
_TnSysSshPublicKey_Object = MibScalar
tnSysSshPublicKey = _TnSysSshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 3),
    _TnSysSshPublicKey_Type()
)
tnSysSshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSshPublicKey.setStatus("current")


class _TnSysSshKeyCommand_Type(Integer32):
    """Custom type tnSysSshKeyCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("generate", 2),
          ("delete", 3))
    )


_TnSysSshKeyCommand_Type.__name__ = "Integer32"
_TnSysSshKeyCommand_Object = MibScalar
tnSysSshKeyCommand = _TnSysSshKeyCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 4),
    _TnSysSshKeyCommand_Type()
)
tnSysSshKeyCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyCommand.setStatus("current")


class _TnSysSshKeyGenerationStatus_Type(Integer32):
    """Custom type tnSysSshKeyGenerationStatus based on Integer32"""
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3))
    )


_TnSysSshKeyGenerationStatus_Type.__name__ = "Integer32"
_TnSysSshKeyGenerationStatus_Object = MibScalar
tnSysSshKeyGenerationStatus = _TnSysSshKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 5),
    _TnSysSshKeyGenerationStatus_Type()
)
tnSysSshKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSshKeyGenerationStatus.setStatus("current")
_TnSysSshEcdsaKeyModulus_Type = Unsigned32
_TnSysSshEcdsaKeyModulus_Object = MibScalar
tnSysSshEcdsaKeyModulus = _TnSysSshEcdsaKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 6),
    _TnSysSshEcdsaKeyModulus_Type()
)
tnSysSshEcdsaKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshEcdsaKeyModulus.setStatus("current")
_TnSysSsl_ObjectIdentity = ObjectIdentity
tnSysSsl = _TnSysSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3)
)


class _TnSysSslKeyType_Type(Integer32):
    """Custom type tnSysSslKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 1),
          ("rsa", 2))
    )


_TnSysSslKeyType_Type.__name__ = "Integer32"
_TnSysSslKeyType_Object = MibScalar
tnSysSslKeyType = _TnSysSslKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 1),
    _TnSysSslKeyType_Type()
)
tnSysSslKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyType.setStatus("current")


class _TnSysSslKeyModulus_Type(Unsigned32):
    """Custom type tnSysSslKeyModulus based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_TnSysSslKeyModulus_Type.__name__ = "Unsigned32"
_TnSysSslKeyModulus_Object = MibScalar
tnSysSslKeyModulus = _TnSysSslKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 2),
    _TnSysSslKeyModulus_Type()
)
tnSysSslKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyModulus.setStatus("current")


class _TnSysSslPublicKey_Type(OctetString):
    """Custom type tnSysSslPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSysSslPublicKey_Type.__name__ = "OctetString"
_TnSysSslPublicKey_Object = MibScalar
tnSysSslPublicKey = _TnSysSslPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 3),
    _TnSysSslPublicKey_Type()
)
tnSysSslPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslPublicKey.setStatus("current")


class _TnSysSslKeyCommand_Type(Integer32):
    """Custom type tnSysSslKeyCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("generate", 2))
    )


_TnSysSslKeyCommand_Type.__name__ = "Integer32"
_TnSysSslKeyCommand_Object = MibScalar
tnSysSslKeyCommand = _TnSysSslKeyCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 4),
    _TnSysSslKeyCommand_Type()
)
tnSysSslKeyCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyCommand.setStatus("current")


class _TnSysSslKeyGenerationStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslKeyGenerationStatus based on AluWdmSslOperationStatus"""
    defaultValue = 1


_TnSysSslKeyGenerationStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslKeyGenerationStatus_Object = MibScalar
tnSysSslKeyGenerationStatus = _TnSysSslKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 5),
    _TnSysSslKeyGenerationStatus_Type()
)
tnSysSslKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslKeyGenerationStatus.setStatus("current")


class _TnSysSslCertTransferCommand_Type(Integer32):
    """Custom type tnSysSslCertTransferCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("uploadReq", 2),
          ("downloadCert", 3))
    )


_TnSysSslCertTransferCommand_Type.__name__ = "Integer32"
_TnSysSslCertTransferCommand_Object = MibScalar
tnSysSslCertTransferCommand = _TnSysSslCertTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 6),
    _TnSysSslCertTransferCommand_Type()
)
tnSysSslCertTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferCommand.setStatus("current")


class _TnSysSslCertTransferProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysSslCertTransferProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysSslCertTransferProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysSslCertTransferProtocol_Object = MibScalar
tnSysSslCertTransferProtocol = _TnSysSslCertTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 8),
    _TnSysSslCertTransferProtocol_Type()
)
tnSysSslCertTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferProtocol.setStatus("current")


class _TnSysSslCertTransferRemoteIp_Type(IpAddress):
    """Custom type tnSysSslCertTransferRemoteIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysSslCertTransferRemoteIp_Type.__name__ = "IpAddress"
_TnSysSslCertTransferRemoteIp_Object = MibScalar
tnSysSslCertTransferRemoteIp = _TnSysSslCertTransferRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 9),
    _TnSysSslCertTransferRemoteIp_Type()
)
tnSysSslCertTransferRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemoteIp.setStatus("current")


class _TnSysSslCertTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysSslCertTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemotePath_Object = MibScalar
tnSysSslCertTransferRemotePath = _TnSysSslCertTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 10),
    _TnSysSslCertTransferRemotePath_Type()
)
tnSysSslCertTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemotePath.setStatus("current")


class _TnSysSslCertTransferRemoteUserId_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemoteUserId based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCertTransferRemoteUserId_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemoteUserId_Object = MibScalar
tnSysSslCertTransferRemoteUserId = _TnSysSslCertTransferRemoteUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 11),
    _TnSysSslCertTransferRemoteUserId_Type()
)
tnSysSslCertTransferRemoteUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemoteUserId.setStatus("current")


class _TnSysSslCertTransferRemotePassword_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemotePassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCertTransferRemotePassword_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemotePassword_Object = MibScalar
tnSysSslCertTransferRemotePassword = _TnSysSslCertTransferRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 12),
    _TnSysSslCertTransferRemotePassword_Type()
)
tnSysSslCertTransferRemotePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemotePassword.setStatus("current")


class _TnSysSslCsrCommand_Type(Integer32):
    """Custom type tnSysSslCsrCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("generate", 2))
    )


_TnSysSslCsrCommand_Type.__name__ = "Integer32"
_TnSysSslCsrCommand_Object = MibScalar
tnSysSslCsrCommand = _TnSysSslCsrCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 13),
    _TnSysSslCsrCommand_Type()
)
tnSysSslCsrCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCommand.setStatus("current")


class _TnSysSslCsrCountry_Type(SnmpAdminString):
    """Custom type tnSysSslCsrCountry based on SnmpAdminString"""
    defaultValue = OctetString("IT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TnSysSslCsrCountry_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrCountry_Object = MibScalar
tnSysSslCsrCountry = _TnSysSslCsrCountry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 14),
    _TnSysSslCsrCountry_Type()
)
tnSysSslCsrCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCountry.setStatus("current")


class _TnSysSslCsrState_Type(SnmpAdminString):
    """Custom type tnSysSslCsrState based on SnmpAdminString"""
    defaultValue = OctetString("Italy")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSslCsrState_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrState_Object = MibScalar
tnSysSslCsrState = _TnSysSslCsrState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 15),
    _TnSysSslCsrState_Type()
)
tnSysSslCsrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrState.setStatus("current")


class _TnSysSslCsrLocality_Type(SnmpAdminString):
    """Custom type tnSysSslCsrLocality based on SnmpAdminString"""
    defaultValue = OctetString("Milan")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSslCsrLocality_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrLocality_Object = MibScalar
tnSysSslCsrLocality = _TnSysSslCsrLocality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 16),
    _TnSysSslCsrLocality_Type()
)
tnSysSslCsrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrLocality.setStatus("current")


class _TnSysSslCsrOrganization_Type(SnmpAdminString):
    """Custom type tnSysSslCsrOrganization based on SnmpAdminString"""
    defaultValue = OctetString("Nokia")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrOrganization_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrOrganization_Object = MibScalar
tnSysSslCsrOrganization = _TnSysSslCsrOrganization_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 17),
    _TnSysSslCsrOrganization_Type()
)
tnSysSslCsrOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrOrganization.setStatus("current")


class _TnSysSslCsrOrganizationUnit_Type(SnmpAdminString):
    """Custom type tnSysSslCsrOrganizationUnit based on SnmpAdminString"""
    defaultValue = OctetString("Optics Division")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrOrganizationUnit_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrOrganizationUnit_Object = MibScalar
tnSysSslCsrOrganizationUnit = _TnSysSslCsrOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 18),
    _TnSysSslCsrOrganizationUnit_Type()
)
tnSysSslCsrOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrOrganizationUnit.setStatus("current")


class _TnSysSslCsrCommonName_Type(SnmpAdminString):
    """Custom type tnSysSslCsrCommonName based on SnmpAdminString"""
    defaultValue = OctetString("1830 Domain")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrCommonName_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrCommonName_Object = MibScalar
tnSysSslCsrCommonName = _TnSysSslCsrCommonName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 19),
    _TnSysSslCsrCommonName_Type()
)
tnSysSslCsrCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCommonName.setStatus("current")


class _TnSysSslCsrEmailAddress_Type(SnmpAdminString):
    """Custom type tnSysSslCsrEmailAddress based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCsrEmailAddress_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrEmailAddress_Object = MibScalar
tnSysSslCsrEmailAddress = _TnSysSslCsrEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 20),
    _TnSysSslCsrEmailAddress_Type()
)
tnSysSslCsrEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrEmailAddress.setStatus("current")


class _TnSysSslCertCommand_Type(Integer32):
    """Custom type tnSysSslCertCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("install", 2))
    )


_TnSysSslCertCommand_Type.__name__ = "Integer32"
_TnSysSslCertCommand_Object = MibScalar
tnSysSslCertCommand = _TnSysSslCertCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 21),
    _TnSysSslCertCommand_Type()
)
tnSysSslCertCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertCommand.setStatus("current")


class _TnSysSslCertSignatureAlgorithm_Type(SnmpAdminString):
    """Custom type tnSysSslCertSignatureAlgorithm based on SnmpAdminString"""
    defaultValue = OctetString("md5WithRSAEncryption")


_TnSysSslCertSignatureAlgorithm_Type.__name__ = "SnmpAdminString"
_TnSysSslCertSignatureAlgorithm_Object = MibScalar
tnSysSslCertSignatureAlgorithm = _TnSysSslCertSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 22),
    _TnSysSslCertSignatureAlgorithm_Type()
)
tnSysSslCertSignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertSignatureAlgorithm.setStatus("current")


class _TnSysSslCertValidity_Type(SnmpAdminString):
    """Custom type tnSysSslCertValidity based on SnmpAdminString"""
    defaultValue = OctetString("Apr 14 06:03:04 2011 GMT - Apr 11 06:03:04 2021 GMT")


_TnSysSslCertValidity_Type.__name__ = "SnmpAdminString"
_TnSysSslCertValidity_Object = MibScalar
tnSysSslCertValidity = _TnSysSslCertValidity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 23),
    _TnSysSslCertValidity_Type()
)
tnSysSslCertValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertValidity.setStatus("current")


class _TnSysSslCsrUploadStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCsrUploadStatus based on AluWdmSslOperationStatus"""
    defaultValue = 4


_TnSysSslCsrUploadStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCsrUploadStatus_Object = MibScalar
tnSysSslCsrUploadStatus = _TnSysSslCsrUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 24),
    _TnSysSslCsrUploadStatus_Type()
)
tnSysSslCsrUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCsrUploadStatus.setStatus("current")


class _TnSysSslCertDownloadStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCertDownloadStatus based on AluWdmSslOperationStatus"""
    defaultValue = 4


_TnSysSslCertDownloadStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCertDownloadStatus_Object = MibScalar
tnSysSslCertDownloadStatus = _TnSysSslCertDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 25),
    _TnSysSslCertDownloadStatus_Type()
)
tnSysSslCertDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertDownloadStatus.setStatus("current")


class _TnSysSslCertInstallStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCertInstallStatus based on AluWdmSslOperationStatus"""
    defaultValue = 1


_TnSysSslCertInstallStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCertInstallStatus_Object = MibScalar
tnSysSslCertInstallStatus = _TnSysSslCertInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 26),
    _TnSysSslCertInstallStatus_Type()
)
tnSysSslCertInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertInstallStatus.setStatus("current")


class _TnSysSslCsrGenerationStatus_Type(Integer32):
    """Custom type tnSysSslCsrGenerationStatus based on Integer32"""
    defaultValue = 4

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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("none", 4),
          ("editing", 5))
    )


_TnSysSslCsrGenerationStatus_Type.__name__ = "Integer32"
_TnSysSslCsrGenerationStatus_Object = MibScalar
tnSysSslCsrGenerationStatus = _TnSysSslCsrGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 27),
    _TnSysSslCsrGenerationStatus_Type()
)
tnSysSslCsrGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCsrGenerationStatus.setStatus("current")


class _TnSysSslCertTransferInetAddressType_Type(InetAddressType):
    """Custom type tnSysSslCertTransferInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysSslCertTransferInetAddressType_Type.__name__ = "InetAddressType"
_TnSysSslCertTransferInetAddressType_Object = MibScalar
tnSysSslCertTransferInetAddressType = _TnSysSslCertTransferInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 28),
    _TnSysSslCertTransferInetAddressType_Type()
)
tnSysSslCertTransferInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferInetAddressType.setStatus("current")


class _TnSysSslCertTransferInetAddress_Type(InetAddress):
    """Custom type tnSysSslCertTransferInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysSslCertTransferInetAddress_Type.__name__ = "InetAddress"
_TnSysSslCertTransferInetAddress_Object = MibScalar
tnSysSslCertTransferInetAddress = _TnSysSslCertTransferInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 29),
    _TnSysSslCertTransferInetAddress_Type()
)
tnSysSslCertTransferInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferInetAddress.setStatus("current")


class _TnSysSslCertTransferPort_Type(Unsigned32):
    """Custom type tnSysSslCertTransferPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysSslCertTransferPort_Type.__name__ = "Unsigned32"
_TnSysSslCertTransferPort_Object = MibScalar
tnSysSslCertTransferPort = _TnSysSslCertTransferPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 30),
    _TnSysSslCertTransferPort_Type()
)
tnSysSslCertTransferPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferPort.setStatus("current")


class _TnSysSslCertVerification_Type(TruthValue):
    """Custom type tnSysSslCertVerification based on TruthValue"""
    defaultValue = 2


_TnSysSslCertVerification_Type.__name__ = "TruthValue"
_TnSysSslCertVerification_Object = MibScalar
tnSysSslCertVerification = _TnSysSslCertVerification_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 31),
    _TnSysSslCertVerification_Type()
)
tnSysSslCertVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertVerification.setStatus("current")
_TnSysSslCertExpiration_Type = Unsigned32
_TnSysSslCertExpiration_Object = MibScalar
tnSysSslCertExpiration = _TnSysSslCertExpiration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 32),
    _TnSysSslCertExpiration_Type()
)
tnSysSslCertExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertExpiration.setStatus("current")
_TnSysKey_ObjectIdentity = ObjectIdentity
tnSysKey = _TnSysKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4)
)
_TnSshKeyAttributeTotal_Type = Integer32
_TnSshKeyAttributeTotal_Object = MibScalar
tnSshKeyAttributeTotal = _TnSshKeyAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 1),
    _TnSshKeyAttributeTotal_Type()
)
tnSshKeyAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshKeyAttributeTotal.setStatus("current")
_TnSshKeyTable_Object = MibTable
tnSshKeyTable = _TnSshKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2)
)
if mibBuilder.loadTexts:
    tnSshKeyTable.setStatus("current")
_TnSshKeyEntry_Object = MibTableRow
tnSshKeyEntry = _TnSshKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1)
)
tnSshKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshKeyTypeIndex"),
)
if mibBuilder.loadTexts:
    tnSshKeyEntry.setStatus("current")


class _TnSshKeyTypeIndex_Type(Integer32):
    """Custom type tnSshKeyTypeIndex based on Integer32"""
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
        *(("dsa", 1),
          ("rsa", 2),
          ("ecdsa", 3),
          ("ed25519", 4))
    )


_TnSshKeyTypeIndex_Type.__name__ = "Integer32"
_TnSshKeyTypeIndex_Object = MibTableColumn
tnSshKeyTypeIndex = _TnSshKeyTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 1),
    _TnSshKeyTypeIndex_Type()
)
tnSshKeyTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshKeyTypeIndex.setStatus("current")


class _TnSshPublicKey_Type(OctetString):
    """Custom type tnSshPublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshPublicKey_Type.__name__ = "OctetString"
_TnSshPublicKey_Object = MibTableColumn
tnSshPublicKey = _TnSshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 2),
    _TnSshPublicKey_Type()
)
tnSshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshPublicKey.setStatus("current")


class _TnSshPublicKey1_Type(OctetString):
    """Custom type tnSshPublicKey1 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshPublicKey1_Type.__name__ = "OctetString"
_TnSshPublicKey1_Object = MibTableColumn
tnSshPublicKey1 = _TnSshPublicKey1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 3),
    _TnSshPublicKey1_Type()
)
tnSshPublicKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshPublicKey1.setStatus("current")


class _TnSshEcdsaPublicKey_Type(OctetString):
    """Custom type tnSshEcdsaPublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshEcdsaPublicKey_Type.__name__ = "OctetString"
_TnSshEcdsaPublicKey_Object = MibTableColumn
tnSshEcdsaPublicKey = _TnSshEcdsaPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 4),
    _TnSshEcdsaPublicKey_Type()
)
tnSshEcdsaPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshEcdsaPublicKey.setStatus("current")


class _TnSshEcdsaPublicKey1_Type(OctetString):
    """Custom type tnSshEcdsaPublicKey1 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshEcdsaPublicKey1_Type.__name__ = "OctetString"
_TnSshEcdsaPublicKey1_Object = MibTableColumn
tnSshEcdsaPublicKey1 = _TnSshEcdsaPublicKey1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 5),
    _TnSshEcdsaPublicKey1_Type()
)
tnSshEcdsaPublicKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshEcdsaPublicKey1.setStatus("current")


class _TnSshEd25519PublicKey_Type(OctetString):
    """Custom type tnSshEd25519PublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshEd25519PublicKey_Type.__name__ = "OctetString"
_TnSshEd25519PublicKey_Object = MibTableColumn
tnSshEd25519PublicKey = _TnSshEd25519PublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 6),
    _TnSshEd25519PublicKey_Type()
)
tnSshEd25519PublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshEd25519PublicKey.setStatus("current")


class _TnSshEd25519PublicKey1_Type(OctetString):
    """Custom type tnSshEd25519PublicKey1 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshEd25519PublicKey1_Type.__name__ = "OctetString"
_TnSshEd25519PublicKey1_Object = MibTableColumn
tnSshEd25519PublicKey1 = _TnSshEd25519PublicKey1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 7),
    _TnSshEd25519PublicKey1_Type()
)
tnSshEd25519PublicKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshEd25519PublicKey1.setStatus("current")
_TnSysTransferLog_ObjectIdentity = ObjectIdentity
tnSysTransferLog = _TnSysTransferLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16)
)


class _TnSysTransferLogCommand_Type(Integer32):
    """Custom type tnSysTransferLogCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysTransferLogCommand_Type.__name__ = "Integer32"
_TnSysTransferLogCommand_Object = MibScalar
tnSysTransferLogCommand = _TnSysTransferLogCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 1),
    _TnSysTransferLogCommand_Type()
)
tnSysTransferLogCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogCommand.setStatus("current")


class _TnSysTransferLogRemoteHostIp_Type(IpAddress):
    """Custom type tnSysTransferLogRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysTransferLogRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysTransferLogRemoteHostIp_Object = MibScalar
tnSysTransferLogRemoteHostIp = _TnSysTransferLogRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 2),
    _TnSysTransferLogRemoteHostIp_Type()
)
tnSysTransferLogRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostIp.setStatus("current")


class _TnSysTransferLogRemotePath_Type(SnmpAdminString):
    """Custom type tnSysTransferLogRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTransferLogRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogRemotePath_Object = MibScalar
tnSysTransferLogRemotePath = _TnSysTransferLogRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 3),
    _TnSysTransferLogRemotePath_Type()
)
tnSysTransferLogRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemotePath.setStatus("current")


class _TnSysTransferLogType_Type(Integer32):
    """Custom type tnSysTransferLogType based on Integer32"""
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
        *(("none", 1),
          ("snmp", 2),
          ("ual", 3),
          ("alarm", 4),
          ("user", 5),
          ("secu", 6),
          ("other", 7),
          ("ualPartial", 8))
    )


_TnSysTransferLogType_Type.__name__ = "Integer32"
_TnSysTransferLogType_Object = MibScalar
tnSysTransferLogType = _TnSysTransferLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 4),
    _TnSysTransferLogType_Type()
)
tnSysTransferLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogType.setStatus("current")


class _TnSysTransferLogStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysTransferLogStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysTransferLogStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysTransferLogStatus_Object = MibScalar
tnSysTransferLogStatus = _TnSysTransferLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 5),
    _TnSysTransferLogStatus_Type()
)
tnSysTransferLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogStatus.setStatus("current")


class _TnSysTransferLogLastLogFilename_Type(SnmpAdminString):
    """Custom type tnSysTransferLogLastLogFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTransferLogLastLogFilename_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogLastLogFilename_Object = MibScalar
tnSysTransferLogLastLogFilename = _TnSysTransferLogLastLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 6),
    _TnSysTransferLogLastLogFilename_Type()
)
tnSysTransferLogLastLogFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastLogFilename.setStatus("current")


class _TnSysTransferLogLastCommand_Type(Integer32):
    """Custom type tnSysTransferLogLastCommand based on Integer32"""
    defaultValue = 1

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
        *(("noCommand", 1),
          ("unknown", 2),
          ("ual", 3),
          ("snmp", 4),
          ("ualPartial", 5))
    )


_TnSysTransferLogLastCommand_Type.__name__ = "Integer32"
_TnSysTransferLogLastCommand_Object = MibScalar
tnSysTransferLogLastCommand = _TnSysTransferLogLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 7),
    _TnSysTransferLogLastCommand_Type()
)
tnSysTransferLogLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastCommand.setStatus("current")


class _TnSysTransferLogLastFileTimeStamp_Type(Unsigned32):
    """Custom type tnSysTransferLogLastFileTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogLastFileTimeStamp_Type.__name__ = "Unsigned32"
_TnSysTransferLogLastFileTimeStamp_Object = MibScalar
tnSysTransferLogLastFileTimeStamp = _TnSysTransferLogLastFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 8),
    _TnSysTransferLogLastFileTimeStamp_Type()
)
tnSysTransferLogLastFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastFileTimeStamp.setStatus("current")


class _TnSysTransferLogProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysTransferLogProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysTransferLogProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysTransferLogProtocol_Object = MibScalar
tnSysTransferLogProtocol = _TnSysTransferLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 9),
    _TnSysTransferLogProtocol_Type()
)
tnSysTransferLogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogProtocol.setStatus("current")


class _TnSysTransferLogUserId_Type(SnmpAdminString):
    """Custom type tnSysTransferLogUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysTransferLogUserId_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogUserId_Object = MibScalar
tnSysTransferLogUserId = _TnSysTransferLogUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 10),
    _TnSysTransferLogUserId_Type()
)
tnSysTransferLogUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogUserId.setStatus("current")


class _TnSysTransferLogPassword_Type(SnmpAdminString):
    """Custom type tnSysTransferLogPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysTransferLogPassword_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogPassword_Object = MibScalar
tnSysTransferLogPassword = _TnSysTransferLogPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 11),
    _TnSysTransferLogPassword_Type()
)
tnSysTransferLogPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogPassword.setStatus("current")


class _TnSysTransferLogWindowStart_Type(Unsigned32):
    """Custom type tnSysTransferLogWindowStart based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogWindowStart_Type.__name__ = "Unsigned32"
_TnSysTransferLogWindowStart_Object = MibScalar
tnSysTransferLogWindowStart = _TnSysTransferLogWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 12),
    _TnSysTransferLogWindowStart_Type()
)
tnSysTransferLogWindowStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogWindowStart.setStatus("current")


class _TnSysTransferLogWindowStop_Type(Unsigned32):
    """Custom type tnSysTransferLogWindowStop based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogWindowStop_Type.__name__ = "Unsigned32"
_TnSysTransferLogWindowStop_Object = MibScalar
tnSysTransferLogWindowStop = _TnSysTransferLogWindowStop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 13),
    _TnSysTransferLogWindowStop_Type()
)
tnSysTransferLogWindowStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogWindowStop.setStatus("current")


class _TnSysTransferLogRemoteHostInetAddressType_Type(InetAddressType):
    """Custom type tnSysTransferLogRemoteHostInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysTransferLogRemoteHostInetAddressType_Type.__name__ = "InetAddressType"
_TnSysTransferLogRemoteHostInetAddressType_Object = MibScalar
tnSysTransferLogRemoteHostInetAddressType = _TnSysTransferLogRemoteHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 14),
    _TnSysTransferLogRemoteHostInetAddressType_Type()
)
tnSysTransferLogRemoteHostInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostInetAddressType.setStatus("current")


class _TnSysTransferLogRemoteHostInetAddress_Type(InetAddress):
    """Custom type tnSysTransferLogRemoteHostInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysTransferLogRemoteHostInetAddress_Type.__name__ = "InetAddress"
_TnSysTransferLogRemoteHostInetAddress_Object = MibScalar
tnSysTransferLogRemoteHostInetAddress = _TnSysTransferLogRemoteHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 15),
    _TnSysTransferLogRemoteHostInetAddress_Type()
)
tnSysTransferLogRemoteHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostInetAddress.setStatus("current")


class _TnSysTransferLogPort_Type(Unsigned32):
    """Custom type tnSysTransferLogPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysTransferLogPort_Type.__name__ = "Unsigned32"
_TnSysTransferLogPort_Object = MibScalar
tnSysTransferLogPort = _TnSysTransferLogPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 16),
    _TnSysTransferLogPort_Type()
)
tnSysTransferLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogPort.setStatus("current")
_TnSysAccessControlList_ObjectIdentity = ObjectIdentity
tnSysAccessControlList = _TnSysAccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17)
)
_TnSysIpAclSysDefault_ObjectIdentity = ObjectIdentity
tnSysIpAclSysDefault = _TnSysIpAclSysDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1)
)


class _TnSysIpAclRxAction_Type(Integer32):
    """Custom type tnSysIpAclRxAction based on Integer32"""
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
        *(("pass", 1),
          ("block", 2),
          ("dropAndlog", 3))
    )


_TnSysIpAclRxAction_Type.__name__ = "Integer32"
_TnSysIpAclRxAction_Object = MibScalar
tnSysIpAclRxAction = _TnSysIpAclRxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 1),
    _TnSysIpAclRxAction_Type()
)
tnSysIpAclRxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclRxAction.setStatus("current")


class _TnSysIpAclTxAction_Type(Integer32):
    """Custom type tnSysIpAclTxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclTxAction_Type.__name__ = "Integer32"
_TnSysIpAclTxAction_Object = MibScalar
tnSysIpAclTxAction = _TnSysIpAclTxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 2),
    _TnSysIpAclTxAction_Type()
)
tnSysIpAclTxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclTxAction.setStatus("current")


class _TnSysIpAclSnmpCfgEnable_Type(TruthValue):
    """Custom type tnSysIpAclSnmpCfgEnable based on TruthValue"""
    defaultValue = 2


_TnSysIpAclSnmpCfgEnable_Type.__name__ = "TruthValue"
_TnSysIpAclSnmpCfgEnable_Object = MibScalar
tnSysIpAclSnmpCfgEnable = _TnSysIpAclSnmpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 3),
    _TnSysIpAclSnmpCfgEnable_Type()
)
tnSysIpAclSnmpCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclSnmpCfgEnable.setStatus("current")


class _TnSysIpAclCfgRestoreToDefault_Type(TruthValue):
    """Custom type tnSysIpAclCfgRestoreToDefault based on TruthValue"""
    defaultValue = 2


_TnSysIpAclCfgRestoreToDefault_Type.__name__ = "TruthValue"
_TnSysIpAclCfgRestoreToDefault_Object = MibScalar
tnSysIpAclCfgRestoreToDefault = _TnSysIpAclCfgRestoreToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 4),
    _TnSysIpAclCfgRestoreToDefault_Type()
)
tnSysIpAclCfgRestoreToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclCfgRestoreToDefault.setStatus("current")


class _TnSysIpAclClearCounter_Type(TruthValue):
    """Custom type tnSysIpAclClearCounter based on TruthValue"""
    defaultValue = 2


_TnSysIpAclClearCounter_Type.__name__ = "TruthValue"
_TnSysIpAclClearCounter_Object = MibScalar
tnSysIpAclClearCounter = _TnSysIpAclClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 5),
    _TnSysIpAclClearCounter_Type()
)
tnSysIpAclClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclClearCounter.setStatus("current")
_TnSysIpAclPatternAttributeTotal_Type = Integer32
_TnSysIpAclPatternAttributeTotal_Object = MibScalar
tnSysIpAclPatternAttributeTotal = _TnSysIpAclPatternAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 2),
    _TnSysIpAclPatternAttributeTotal_Type()
)
tnSysIpAclPatternAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclPatternAttributeTotal.setStatus("current")
_TnSysIpAclPatternTable_Object = MibTable
tnSysIpAclPatternTable = _TnSysIpAclPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternTable.setStatus("current")
_TnSysIpAclPatternEntry_Object = MibTableRow
tnSysIpAclPatternEntry = _TnSysIpAclPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1)
)
tnSysIpAclPatternEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclPatternID"),
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternEntry.setStatus("current")


class _TnSysIpAclPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclPatternID_Object = MibTableColumn
tnSysIpAclPatternID = _TnSysIpAclPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 1),
    _TnSysIpAclPatternID_Type()
)
tnSysIpAclPatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclPatternID.setStatus("current")


class _TnSysIpAclPatternAction_Type(Integer32):
    """Custom type tnSysIpAclPatternAction based on Integer32"""
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
          ("block", 2),
          ("log", 3))
    )


_TnSysIpAclPatternAction_Type.__name__ = "Integer32"
_TnSysIpAclPatternAction_Object = MibTableColumn
tnSysIpAclPatternAction = _TnSysIpAclPatternAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 2),
    _TnSysIpAclPatternAction_Type()
)
tnSysIpAclPatternAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternAction.setStatus("current")


class _TnSysIpAclPatternICMPERROR_Type(TruthValue):
    """Custom type tnSysIpAclPatternICMPERROR based on TruthValue"""
    defaultValue = 2


_TnSysIpAclPatternICMPERROR_Type.__name__ = "TruthValue"
_TnSysIpAclPatternICMPERROR_Object = MibTableColumn
tnSysIpAclPatternICMPERROR = _TnSysIpAclPatternICMPERROR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 3),
    _TnSysIpAclPatternICMPERROR_Type()
)
tnSysIpAclPatternICMPERROR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternICMPERROR.setStatus("current")
_TnSysIpAclPatternSrcAddr_Type = IpAddress
_TnSysIpAclPatternSrcAddr_Object = MibTableColumn
tnSysIpAclPatternSrcAddr = _TnSysIpAclPatternSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 4),
    _TnSysIpAclPatternSrcAddr_Type()
)
tnSysIpAclPatternSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcAddr.setStatus("current")


class _TnSysIpAclPatternSrcPrefix_Type(IpAddress):
    """Custom type tnSysIpAclPatternSrcPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysIpAclPatternSrcPrefix_Type.__name__ = "IpAddress"
_TnSysIpAclPatternSrcPrefix_Object = MibTableColumn
tnSysIpAclPatternSrcPrefix = _TnSysIpAclPatternSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 5),
    _TnSysIpAclPatternSrcPrefix_Type()
)
tnSysIpAclPatternSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcPrefix.setStatus("current")
_TnSysIpAclPatternDestAddr_Type = IpAddress
_TnSysIpAclPatternDestAddr_Object = MibTableColumn
tnSysIpAclPatternDestAddr = _TnSysIpAclPatternDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 6),
    _TnSysIpAclPatternDestAddr_Type()
)
tnSysIpAclPatternDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestAddr.setStatus("current")


class _TnSysIpAclPatternDestPrefix_Type(IpAddress):
    """Custom type tnSysIpAclPatternDestPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysIpAclPatternDestPrefix_Type.__name__ = "IpAddress"
_TnSysIpAclPatternDestPrefix_Object = MibTableColumn
tnSysIpAclPatternDestPrefix = _TnSysIpAclPatternDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 7),
    _TnSysIpAclPatternDestPrefix_Type()
)
tnSysIpAclPatternDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestPrefix.setStatus("current")


class _TnSysIpAclPatternDestPort_Type(Integer32):
    """Custom type tnSysIpAclPatternDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternDestPort_Type.__name__ = "Integer32"
_TnSysIpAclPatternDestPort_Object = MibTableColumn
tnSysIpAclPatternDestPort = _TnSysIpAclPatternDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 8),
    _TnSysIpAclPatternDestPort_Type()
)
tnSysIpAclPatternDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestPort.setStatus("current")
_TnSysIpAclPatternIpProtocol_Type = OctetString
_TnSysIpAclPatternIpProtocol_Object = MibTableColumn
tnSysIpAclPatternIpProtocol = _TnSysIpAclPatternIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 9),
    _TnSysIpAclPatternIpProtocol_Type()
)
tnSysIpAclPatternIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIpProtocol.setStatus("current")


class _TnSysIpAclPatternIpFragment_Type(TruthValue):
    """Custom type tnSysIpAclPatternIpFragment based on TruthValue"""
    defaultValue = 2


_TnSysIpAclPatternIpFragment_Type.__name__ = "TruthValue"
_TnSysIpAclPatternIpFragment_Object = MibTableColumn
tnSysIpAclPatternIpFragment = _TnSysIpAclPatternIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 10),
    _TnSysIpAclPatternIpFragment_Type()
)
tnSysIpAclPatternIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIpFragment.setStatus("current")


class _TnSysIpAclPatternIcmpType_Type(Integer32):
    """Custom type tnSysIpAclPatternIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclPatternIcmpType_Type.__name__ = "Integer32"
_TnSysIpAclPatternIcmpType_Object = MibTableColumn
tnSysIpAclPatternIcmpType = _TnSysIpAclPatternIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 11),
    _TnSysIpAclPatternIcmpType_Type()
)
tnSysIpAclPatternIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIcmpType.setStatus("current")


class _TnSysIpAclPatternIcmpCode_Type(Integer32):
    """Custom type tnSysIpAclPatternIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclPatternIcmpCode_Type.__name__ = "Integer32"
_TnSysIpAclPatternIcmpCode_Object = MibTableColumn
tnSysIpAclPatternIcmpCode = _TnSysIpAclPatternIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 12),
    _TnSysIpAclPatternIcmpCode_Type()
)
tnSysIpAclPatternIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIcmpCode.setStatus("current")


class _TnSysIpAclPatternTcpEstablish_Type(Integer32):
    """Custom type tnSysIpAclPatternTcpEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("local", 3))
    )


_TnSysIpAclPatternTcpEstablish_Type.__name__ = "Integer32"
_TnSysIpAclPatternTcpEstablish_Object = MibTableColumn
tnSysIpAclPatternTcpEstablish = _TnSysIpAclPatternTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 13),
    _TnSysIpAclPatternTcpEstablish_Type()
)
tnSysIpAclPatternTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternTcpEstablish.setStatus("current")
_TnSysIpAclPatternRowStatus_Type = RowStatus
_TnSysIpAclPatternRowStatus_Object = MibTableColumn
tnSysIpAclPatternRowStatus = _TnSysIpAclPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 14),
    _TnSysIpAclPatternRowStatus_Type()
)
tnSysIpAclPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternRowStatus.setStatus("current")


class _TnSysIpAclPatternSrcPort_Type(Integer32):
    """Custom type tnSysIpAclPatternSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternSrcPort_Type.__name__ = "Integer32"
_TnSysIpAclPatternSrcPort_Object = MibTableColumn
tnSysIpAclPatternSrcPort = _TnSysIpAclPatternSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 15),
    _TnSysIpAclPatternSrcPort_Type()
)
tnSysIpAclPatternSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcPort.setStatus("current")
_TnSysIpAclPatternSystemDefault_Type = TruthValue
_TnSysIpAclPatternSystemDefault_Object = MibTableColumn
tnSysIpAclPatternSystemDefault = _TnSysIpAclPatternSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 16),
    _TnSysIpAclPatternSystemDefault_Type()
)
tnSysIpAclPatternSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSystemDefault.setStatus("current")


class _TnSysIpAclPatternSrcPortRangeEnd_Type(Integer32):
    """Custom type tnSysIpAclPatternSrcPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternSrcPortRangeEnd_Type.__name__ = "Integer32"
_TnSysIpAclPatternSrcPortRangeEnd_Object = MibTableColumn
tnSysIpAclPatternSrcPortRangeEnd = _TnSysIpAclPatternSrcPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 17),
    _TnSysIpAclPatternSrcPortRangeEnd_Type()
)
tnSysIpAclPatternSrcPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcPortRangeEnd.setStatus("current")


class _TnSysIpAclPatternDestPortRangeEnd_Type(Integer32):
    """Custom type tnSysIpAclPatternDestPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternDestPortRangeEnd_Type.__name__ = "Integer32"
_TnSysIpAclPatternDestPortRangeEnd_Object = MibTableColumn
tnSysIpAclPatternDestPortRangeEnd = _TnSysIpAclPatternDestPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 18),
    _TnSysIpAclPatternDestPortRangeEnd_Type()
)
tnSysIpAclPatternDestPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestPortRangeEnd.setStatus("current")
_TnSysIpAclFilterAttributeTotal_Type = Integer32
_TnSysIpAclFilterAttributeTotal_Object = MibScalar
tnSysIpAclFilterAttributeTotal = _TnSysIpAclFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 4),
    _TnSysIpAclFilterAttributeTotal_Type()
)
tnSysIpAclFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterAttributeTotal.setStatus("current")
_TnSysIpAclFilterTable_Object = MibTable
tnSysIpAclFilterTable = _TnSysIpAclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterTable.setStatus("current")
_TnSysIpAclFilterEntry_Object = MibTableRow
tnSysIpAclFilterEntry = _TnSysIpAclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1)
)
tnSysIpAclFilterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclFilterID"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclFilterPatternIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterEntry.setStatus("current")


class _TnSysIpAclFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclFilterID_Object = MibTableColumn
tnSysIpAclFilterID = _TnSysIpAclFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 1),
    _TnSysIpAclFilterID_Type()
)
tnSysIpAclFilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclFilterID.setStatus("current")


class _TnSysIpAclFilterPatternIndex_Type(Integer32):
    """Custom type tnSysIpAclFilterPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnSysIpAclFilterPatternIndex_Type.__name__ = "Integer32"
_TnSysIpAclFilterPatternIndex_Object = MibTableColumn
tnSysIpAclFilterPatternIndex = _TnSysIpAclFilterPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 2),
    _TnSysIpAclFilterPatternIndex_Type()
)
tnSysIpAclFilterPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclFilterPatternIndex.setStatus("current")


class _TnSysIpAclFilterPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclFilterPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclFilterPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclFilterPatternID_Object = MibTableColumn
tnSysIpAclFilterPatternID = _TnSysIpAclFilterPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 3),
    _TnSysIpAclFilterPatternID_Type()
)
tnSysIpAclFilterPatternID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclFilterPatternID.setStatus("current")
_TnSysIpAclFilterStatCount_Type = Counter32
_TnSysIpAclFilterStatCount_Object = MibTableColumn
tnSysIpAclFilterStatCount = _TnSysIpAclFilterStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 4),
    _TnSysIpAclFilterStatCount_Type()
)
tnSysIpAclFilterStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterStatCount.setStatus("current")
_TnSysIpAclFilterRowStatus_Type = RowStatus
_TnSysIpAclFilterRowStatus_Object = MibTableColumn
tnSysIpAclFilterRowStatus = _TnSysIpAclFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 5),
    _TnSysIpAclFilterRowStatus_Type()
)
tnSysIpAclFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclFilterRowStatus.setStatus("current")
_TnSysIpAclFilterSystemDefault_Type = TruthValue
_TnSysIpAclFilterSystemDefault_Object = MibTableColumn
tnSysIpAclFilterSystemDefault = _TnSysIpAclFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 6),
    _TnSysIpAclFilterSystemDefault_Type()
)
tnSysIpAclFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterSystemDefault.setStatus("current")
_TnSysIpAclInterfaceAttributeTotal_Type = Integer32
_TnSysIpAclInterfaceAttributeTotal_Object = MibScalar
tnSysIpAclInterfaceAttributeTotal = _TnSysIpAclInterfaceAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 6),
    _TnSysIpAclInterfaceAttributeTotal_Type()
)
tnSysIpAclInterfaceAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceAttributeTotal.setStatus("current")
_TnSysIpAclInterfaceTable_Object = MibTable
tnSysIpAclInterfaceTable = _TnSysIpAclInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7)
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceTable.setStatus("current")
_TnSysIpAclInterfaceEntry_Object = MibTableRow
tnSysIpAclInterfaceEntry = _TnSysIpAclInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1)
)
tnSysIpAclInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceEntry.setStatus("current")


class _TnSysIpAclInterfaceFilterDir_Type(Integer32):
    """Custom type tnSysIpAclInterfaceFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclInterfaceFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclInterfaceFilterDir_Object = MibTableColumn
tnSysIpAclInterfaceFilterDir = _TnSysIpAclInterfaceFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 1),
    _TnSysIpAclInterfaceFilterDir_Type()
)
tnSysIpAclInterfaceFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterDir.setStatus("current")


class _TnSysIpAclInterfaceFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclInterfaceFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclInterfaceFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclInterfaceFilterID_Object = MibTableColumn
tnSysIpAclInterfaceFilterID = _TnSysIpAclInterfaceFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 2),
    _TnSysIpAclInterfaceFilterID_Type()
)
tnSysIpAclInterfaceFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterID.setStatus("current")


class _TnSysIpAclInterfaceFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclInterfaceFilterEnable based on Integer32"""
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


_TnSysIpAclInterfaceFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclInterfaceFilterEnable_Object = MibTableColumn
tnSysIpAclInterfaceFilterEnable = _TnSysIpAclInterfaceFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 3),
    _TnSysIpAclInterfaceFilterEnable_Type()
)
tnSysIpAclInterfaceFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterEnable.setStatus("current")
_TnSysIpAclInterfaceFilterRowStatus_Type = RowStatus
_TnSysIpAclInterfaceFilterRowStatus_Object = MibTableColumn
tnSysIpAclInterfaceFilterRowStatus = _TnSysIpAclInterfaceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 4),
    _TnSysIpAclInterfaceFilterRowStatus_Type()
)
tnSysIpAclInterfaceFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterRowStatus.setStatus("current")
_TnSysIpAclInterfaceSystemDefault_Type = TruthValue
_TnSysIpAclInterfaceSystemDefault_Object = MibTableColumn
tnSysIpAclInterfaceSystemDefault = _TnSysIpAclInterfaceSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 5),
    _TnSysIpAclInterfaceSystemDefault_Type()
)
tnSysIpAclInterfaceSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceSystemDefault.setStatus("current")


class _TnSysIpAclInterfaceFilterLog_Type(Integer32):
    """Custom type tnSysIpAclInterfaceFilterLog based on Integer32"""
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


_TnSysIpAclInterfaceFilterLog_Type.__name__ = "Integer32"
_TnSysIpAclInterfaceFilterLog_Object = MibTableColumn
tnSysIpAclInterfaceFilterLog = _TnSysIpAclInterfaceFilterLog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 6),
    _TnSysIpAclInterfaceFilterLog_Type()
)
tnSysIpAclInterfaceFilterLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterLog.setStatus("current")
_TnSysIpAclNetIfFilterAttributeTotal_Type = Integer32
_TnSysIpAclNetIfFilterAttributeTotal_Object = MibScalar
tnSysIpAclNetIfFilterAttributeTotal = _TnSysIpAclNetIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 8),
    _TnSysIpAclNetIfFilterAttributeTotal_Type()
)
tnSysIpAclNetIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterAttributeTotal.setStatus("current")
_TnSysIpAclNetIfFilterTable_Object = MibTable
tnSysIpAclNetIfFilterTable = _TnSysIpAclNetIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9)
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterTable.setStatus("current")
_TnSysIpAclNetIfFilterEntry_Object = MibTableRow
tnSysIpAclNetIfFilterEntry = _TnSysIpAclNetIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1)
)
tnSysIpAclNetIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterEntry.setStatus("current")


class _TnSysIpAclNetIfFilterDir_Type(Integer32):
    """Custom type tnSysIpAclNetIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclNetIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclNetIfFilterDir_Object = MibTableColumn
tnSysIpAclNetIfFilterDir = _TnSysIpAclNetIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 1),
    _TnSysIpAclNetIfFilterDir_Type()
)
tnSysIpAclNetIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterDir.setStatus("current")
_TnSysIpAclNetIfFilterRowStatus_Type = RowStatus
_TnSysIpAclNetIfFilterRowStatus_Object = MibTableColumn
tnSysIpAclNetIfFilterRowStatus = _TnSysIpAclNetIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 2),
    _TnSysIpAclNetIfFilterRowStatus_Type()
)
tnSysIpAclNetIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterRowStatus.setStatus("current")


class _TnSysIpAclNetIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclNetIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclNetIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclNetIfFilterID_Object = MibTableColumn
tnSysIpAclNetIfFilterID = _TnSysIpAclNetIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 3),
    _TnSysIpAclNetIfFilterID_Type()
)
tnSysIpAclNetIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterID.setStatus("current")


class _TnSysIpAclNetIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclNetIfFilterEnable based on Integer32"""
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


_TnSysIpAclNetIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclNetIfFilterEnable_Object = MibTableColumn
tnSysIpAclNetIfFilterEnable = _TnSysIpAclNetIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 4),
    _TnSysIpAclNetIfFilterEnable_Type()
)
tnSysIpAclNetIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterEnable.setStatus("current")
_TnSysIpAclNetIfFilterSystemDefault_Type = TruthValue
_TnSysIpAclNetIfFilterSystemDefault_Object = MibTableColumn
tnSysIpAclNetIfFilterSystemDefault = _TnSysIpAclNetIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 5),
    _TnSysIpAclNetIfFilterSystemDefault_Type()
)
tnSysIpAclNetIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterSystemDefault.setStatus("current")
_TnSysIpAclIpv6PatternAttributeTotal_Type = Integer32
_TnSysIpAclIpv6PatternAttributeTotal_Object = MibScalar
tnSysIpAclIpv6PatternAttributeTotal = _TnSysIpAclIpv6PatternAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 10),
    _TnSysIpAclIpv6PatternAttributeTotal_Type()
)
tnSysIpAclIpv6PatternAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternAttributeTotal.setStatus("current")
_TnSysIpAclIpv6PatternTable_Object = MibTable
tnSysIpAclIpv6PatternTable = _TnSysIpAclIpv6PatternTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternTable.setStatus("current")
_TnSysIpAclIpv6PatternEntry_Object = MibTableRow
tnSysIpAclIpv6PatternEntry = _TnSysIpAclIpv6PatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1)
)
tnSysIpAclIpv6PatternEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternID"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternEntry.setStatus("current")


class _TnSysIpAclIpv6PatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6PatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclIpv6PatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6PatternID_Object = MibTableColumn
tnSysIpAclIpv6PatternID = _TnSysIpAclIpv6PatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 1),
    _TnSysIpAclIpv6PatternID_Type()
)
tnSysIpAclIpv6PatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternID.setStatus("current")


class _TnSysIpAclIpv6PatternAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternAction based on Integer32"""
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
          ("block", 2),
          ("log", 3))
    )


_TnSysIpAclIpv6PatternAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternAction_Object = MibTableColumn
tnSysIpAclIpv6PatternAction = _TnSysIpAclIpv6PatternAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 2),
    _TnSysIpAclIpv6PatternAction_Type()
)
tnSysIpAclIpv6PatternAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternAction.setStatus("current")


class _TnSysIpAclIpv6PatternICMPV6ERROR_Type(TruthValue):
    """Custom type tnSysIpAclIpv6PatternICMPV6ERROR based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6PatternICMPV6ERROR_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6PatternICMPV6ERROR_Object = MibTableColumn
tnSysIpAclIpv6PatternICMPV6ERROR = _TnSysIpAclIpv6PatternICMPV6ERROR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 3),
    _TnSysIpAclIpv6PatternICMPV6ERROR_Type()
)
tnSysIpAclIpv6PatternICMPV6ERROR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternICMPV6ERROR.setStatus("current")
_TnSysIpAclIpv6PatternSrcAddr_Type = InetAddressIPv6
_TnSysIpAclIpv6PatternSrcAddr_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcAddr = _TnSysIpAclIpv6PatternSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 4),
    _TnSysIpAclIpv6PatternSrcAddr_Type()
)
tnSysIpAclIpv6PatternSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcAddr.setStatus("current")
_TnSysIpAclIpv6PatternSrcPrefixLen_Type = InetAddressPrefixLength
_TnSysIpAclIpv6PatternSrcPrefixLen_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcPrefixLen = _TnSysIpAclIpv6PatternSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 5),
    _TnSysIpAclIpv6PatternSrcPrefixLen_Type()
)
tnSysIpAclIpv6PatternSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcPrefixLen.setStatus("current")
_TnSysIpAclIpv6PatternDestAddr_Type = InetAddressIPv6
_TnSysIpAclIpv6PatternDestAddr_Object = MibTableColumn
tnSysIpAclIpv6PatternDestAddr = _TnSysIpAclIpv6PatternDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 6),
    _TnSysIpAclIpv6PatternDestAddr_Type()
)
tnSysIpAclIpv6PatternDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestAddr.setStatus("current")
_TnSysIpAclIpv6PatternDestPrefixLen_Type = InetAddressPrefixLength
_TnSysIpAclIpv6PatternDestPrefixLen_Object = MibTableColumn
tnSysIpAclIpv6PatternDestPrefixLen = _TnSysIpAclIpv6PatternDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 7),
    _TnSysIpAclIpv6PatternDestPrefixLen_Type()
)
tnSysIpAclIpv6PatternDestPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestPrefixLen.setStatus("current")
_TnSysIpAclIpv6PatternIpProtocol_Type = OctetString
_TnSysIpAclIpv6PatternIpProtocol_Object = MibTableColumn
tnSysIpAclIpv6PatternIpProtocol = _TnSysIpAclIpv6PatternIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 8),
    _TnSysIpAclIpv6PatternIpProtocol_Type()
)
tnSysIpAclIpv6PatternIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIpProtocol.setStatus("current")


class _TnSysIpAclIpv6PatternIcmpType_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIpv6PatternIcmpType_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternIcmpType_Object = MibTableColumn
tnSysIpAclIpv6PatternIcmpType = _TnSysIpAclIpv6PatternIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 9),
    _TnSysIpAclIpv6PatternIcmpType_Type()
)
tnSysIpAclIpv6PatternIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIcmpType.setStatus("current")


class _TnSysIpAclIpv6PatternIcmpCode_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIpv6PatternIcmpCode_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternIcmpCode_Object = MibTableColumn
tnSysIpAclIpv6PatternIcmpCode = _TnSysIpAclIpv6PatternIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 10),
    _TnSysIpAclIpv6PatternIcmpCode_Type()
)
tnSysIpAclIpv6PatternIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIcmpCode.setStatus("current")


class _TnSysIpAclIpv6PatternSrcPort_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternSrcPort_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternSrcPort_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcPort = _TnSysIpAclIpv6PatternSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 11),
    _TnSysIpAclIpv6PatternSrcPort_Type()
)
tnSysIpAclIpv6PatternSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcPort.setStatus("current")


class _TnSysIpAclIpv6PatternDestPort_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternDestPort_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternDestPort_Object = MibTableColumn
tnSysIpAclIpv6PatternDestPort = _TnSysIpAclIpv6PatternDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 12),
    _TnSysIpAclIpv6PatternDestPort_Type()
)
tnSysIpAclIpv6PatternDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestPort.setStatus("current")


class _TnSysIpAclIpv6PatternIpFragment_Type(TruthValue):
    """Custom type tnSysIpAclIpv6PatternIpFragment based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6PatternIpFragment_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6PatternIpFragment_Object = MibTableColumn
tnSysIpAclIpv6PatternIpFragment = _TnSysIpAclIpv6PatternIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 13),
    _TnSysIpAclIpv6PatternIpFragment_Type()
)
tnSysIpAclIpv6PatternIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIpFragment.setStatus("current")


class _TnSysIpAclIpv6PatternTcpEstablish_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternTcpEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("local", 3))
    )


_TnSysIpAclIpv6PatternTcpEstablish_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternTcpEstablish_Object = MibTableColumn
tnSysIpAclIpv6PatternTcpEstablish = _TnSysIpAclIpv6PatternTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 14),
    _TnSysIpAclIpv6PatternTcpEstablish_Type()
)
tnSysIpAclIpv6PatternTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternTcpEstablish.setStatus("current")
_TnSysIpAclIpv6PatternSystemDefault_Type = TruthValue
_TnSysIpAclIpv6PatternSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6PatternSystemDefault = _TnSysIpAclIpv6PatternSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 15),
    _TnSysIpAclIpv6PatternSystemDefault_Type()
)
tnSysIpAclIpv6PatternSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSystemDefault.setStatus("current")
_TnSysIpAclIpv6PatternRowStatus_Type = RowStatus
_TnSysIpAclIpv6PatternRowStatus_Object = MibTableColumn
tnSysIpAclIpv6PatternRowStatus = _TnSysIpAclIpv6PatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 16),
    _TnSysIpAclIpv6PatternRowStatus_Type()
)
tnSysIpAclIpv6PatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternRowStatus.setStatus("current")


class _TnSysIpAclIpv6PatternSrcPortRangeEnd_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternSrcPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternSrcPortRangeEnd_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternSrcPortRangeEnd_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcPortRangeEnd = _TnSysIpAclIpv6PatternSrcPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 17),
    _TnSysIpAclIpv6PatternSrcPortRangeEnd_Type()
)
tnSysIpAclIpv6PatternSrcPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcPortRangeEnd.setStatus("current")


class _TnSysIpAclIpv6PatternDestPortRangeEnd_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternDestPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternDestPortRangeEnd_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternDestPortRangeEnd_Object = MibTableColumn
tnSysIpAclIpv6PatternDestPortRangeEnd = _TnSysIpAclIpv6PatternDestPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 18),
    _TnSysIpAclIpv6PatternDestPortRangeEnd_Type()
)
tnSysIpAclIpv6PatternDestPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestPortRangeEnd.setStatus("current")
_TnSysIpAclIpv6FilterAttributeTotal_Type = Integer32
_TnSysIpAclIpv6FilterAttributeTotal_Object = MibScalar
tnSysIpAclIpv6FilterAttributeTotal = _TnSysIpAclIpv6FilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 12),
    _TnSysIpAclIpv6FilterAttributeTotal_Type()
)
tnSysIpAclIpv6FilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterAttributeTotal.setStatus("current")
_TnSysIpAclIpv6FilterTable_Object = MibTable
tnSysIpAclIpv6FilterTable = _TnSysIpAclIpv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterTable.setStatus("current")
_TnSysIpAclIpv6FilterEntry_Object = MibTableRow
tnSysIpAclIpv6FilterEntry = _TnSysIpAclIpv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1)
)
tnSysIpAclIpv6FilterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterID"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterPatternIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterEntry.setStatus("current")


class _TnSysIpAclIpv6FilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6FilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclIpv6FilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6FilterID_Object = MibTableColumn
tnSysIpAclIpv6FilterID = _TnSysIpAclIpv6FilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 1),
    _TnSysIpAclIpv6FilterID_Type()
)
tnSysIpAclIpv6FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterID.setStatus("current")


class _TnSysIpAclIpv6FilterPatternIndex_Type(Integer32):
    """Custom type tnSysIpAclIpv6FilterPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnSysIpAclIpv6FilterPatternIndex_Type.__name__ = "Integer32"
_TnSysIpAclIpv6FilterPatternIndex_Object = MibTableColumn
tnSysIpAclIpv6FilterPatternIndex = _TnSysIpAclIpv6FilterPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 2),
    _TnSysIpAclIpv6FilterPatternIndex_Type()
)
tnSysIpAclIpv6FilterPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterPatternIndex.setStatus("current")


class _TnSysIpAclIpv6FilterPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6FilterPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclIpv6FilterPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6FilterPatternID_Object = MibTableColumn
tnSysIpAclIpv6FilterPatternID = _TnSysIpAclIpv6FilterPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 3),
    _TnSysIpAclIpv6FilterPatternID_Type()
)
tnSysIpAclIpv6FilterPatternID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterPatternID.setStatus("current")
_TnSysIpAclIpv6FilterStatCount_Type = Counter32
_TnSysIpAclIpv6FilterStatCount_Object = MibTableColumn
tnSysIpAclIpv6FilterStatCount = _TnSysIpAclIpv6FilterStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 4),
    _TnSysIpAclIpv6FilterStatCount_Type()
)
tnSysIpAclIpv6FilterStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterStatCount.setStatus("current")
_TnSysIpAclIpv6FilterRowStatus_Type = RowStatus
_TnSysIpAclIpv6FilterRowStatus_Object = MibTableColumn
tnSysIpAclIpv6FilterRowStatus = _TnSysIpAclIpv6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 5),
    _TnSysIpAclIpv6FilterRowStatus_Type()
)
tnSysIpAclIpv6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterRowStatus.setStatus("current")
_TnSysIpAclIpv6FilterSystemDefault_Type = TruthValue
_TnSysIpAclIpv6FilterSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6FilterSystemDefault = _TnSysIpAclIpv6FilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 6),
    _TnSysIpAclIpv6FilterSystemDefault_Type()
)
tnSysIpAclIpv6FilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterSystemDefault.setStatus("current")
_TnSysIpAclIpv6InterfaceAttributeTotal_Type = Integer32
_TnSysIpAclIpv6InterfaceAttributeTotal_Object = MibScalar
tnSysIpAclIpv6InterfaceAttributeTotal = _TnSysIpAclIpv6InterfaceAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 14),
    _TnSysIpAclIpv6InterfaceAttributeTotal_Type()
)
tnSysIpAclIpv6InterfaceAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceAttributeTotal.setStatus("current")
_TnSysIpAclIpv6InterfaceTable_Object = MibTable
tnSysIpAclIpv6InterfaceTable = _TnSysIpAclIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceTable.setStatus("current")
_TnSysIpAclIpv6InterfaceEntry_Object = MibTableRow
tnSysIpAclIpv6InterfaceEntry = _TnSysIpAclIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1)
)
tnSysIpAclIpv6InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceEntry.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterDir_Type(Integer32):
    """Custom type tnSysIpAclIpv6InterfaceFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclIpv6InterfaceFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclIpv6InterfaceFilterDir_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterDir = _TnSysIpAclIpv6InterfaceFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 1),
    _TnSysIpAclIpv6InterfaceFilterDir_Type()
)
tnSysIpAclIpv6InterfaceFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterDir.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6InterfaceFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclIpv6InterfaceFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6InterfaceFilterID_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterID = _TnSysIpAclIpv6InterfaceFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 2),
    _TnSysIpAclIpv6InterfaceFilterID_Type()
)
tnSysIpAclIpv6InterfaceFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterID.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclIpv6InterfaceFilterEnable based on Integer32"""
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


_TnSysIpAclIpv6InterfaceFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclIpv6InterfaceFilterEnable_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterEnable = _TnSysIpAclIpv6InterfaceFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 3),
    _TnSysIpAclIpv6InterfaceFilterEnable_Type()
)
tnSysIpAclIpv6InterfaceFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterEnable.setStatus("current")
_TnSysIpAclIpv6InterfaceFilterRowStatus_Type = RowStatus
_TnSysIpAclIpv6InterfaceFilterRowStatus_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterRowStatus = _TnSysIpAclIpv6InterfaceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 4),
    _TnSysIpAclIpv6InterfaceFilterRowStatus_Type()
)
tnSysIpAclIpv6InterfaceFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterRowStatus.setStatus("current")
_TnSysIpAclIpv6InterfaceSystemDefault_Type = TruthValue
_TnSysIpAclIpv6InterfaceSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6InterfaceSystemDefault = _TnSysIpAclIpv6InterfaceSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 5),
    _TnSysIpAclIpv6InterfaceSystemDefault_Type()
)
tnSysIpAclIpv6InterfaceSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceSystemDefault.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterLog_Type(Integer32):
    """Custom type tnSysIpAclIpv6InterfaceFilterLog based on Integer32"""
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


_TnSysIpAclIpv6InterfaceFilterLog_Type.__name__ = "Integer32"
_TnSysIpAclIpv6InterfaceFilterLog_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterLog = _TnSysIpAclIpv6InterfaceFilterLog_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 6),
    _TnSysIpAclIpv6InterfaceFilterLog_Type()
)
tnSysIpAclIpv6InterfaceFilterLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterLog.setStatus("current")
_TnSysIpv6AclNetIfFilterAttributeTotal_Type = Integer32
_TnSysIpv6AclNetIfFilterAttributeTotal_Object = MibScalar
tnSysIpv6AclNetIfFilterAttributeTotal = _TnSysIpv6AclNetIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 16),
    _TnSysIpv6AclNetIfFilterAttributeTotal_Type()
)
tnSysIpv6AclNetIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterAttributeTotal.setStatus("current")
_TnSysIpv6AclNetIfFilterTable_Object = MibTable
tnSysIpv6AclNetIfFilterTable = _TnSysIpv6AclNetIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17)
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterTable.setStatus("current")
_TnSysIpv6AclNetIfFilterEntry_Object = MibTableRow
tnSysIpv6AclNetIfFilterEntry = _TnSysIpv6AclNetIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1)
)
tnSysIpv6AclNetIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterEntry.setStatus("current")


class _TnSysIpv6AclNetIfFilterDir_Type(Integer32):
    """Custom type tnSysIpv6AclNetIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpv6AclNetIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpv6AclNetIfFilterDir_Object = MibTableColumn
tnSysIpv6AclNetIfFilterDir = _TnSysIpv6AclNetIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 1),
    _TnSysIpv6AclNetIfFilterDir_Type()
)
tnSysIpv6AclNetIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterDir.setStatus("current")
_TnSysIpv6AclNetIfFilterRowStatus_Type = RowStatus
_TnSysIpv6AclNetIfFilterRowStatus_Object = MibTableColumn
tnSysIpv6AclNetIfFilterRowStatus = _TnSysIpv6AclNetIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 2),
    _TnSysIpv6AclNetIfFilterRowStatus_Type()
)
tnSysIpv6AclNetIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterRowStatus.setStatus("current")


class _TnSysIpv6AclNetIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclNetIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpv6AclNetIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclNetIfFilterID_Object = MibTableColumn
tnSysIpv6AclNetIfFilterID = _TnSysIpv6AclNetIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 3),
    _TnSysIpv6AclNetIfFilterID_Type()
)
tnSysIpv6AclNetIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterID.setStatus("current")


class _TnSysIpv6AclNetIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpv6AclNetIfFilterEnable based on Integer32"""
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


_TnSysIpv6AclNetIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpv6AclNetIfFilterEnable_Object = MibTableColumn
tnSysIpv6AclNetIfFilterEnable = _TnSysIpv6AclNetIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 4),
    _TnSysIpv6AclNetIfFilterEnable_Type()
)
tnSysIpv6AclNetIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterEnable.setStatus("current")
_TnSysIpv6AclNetIfFilterSystemDefault_Type = TruthValue
_TnSysIpv6AclNetIfFilterSystemDefault_Object = MibTableColumn
tnSysIpv6AclNetIfFilterSystemDefault = _TnSysIpv6AclNetIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 5),
    _TnSysIpv6AclNetIfFilterSystemDefault_Type()
)
tnSysIpv6AclNetIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterSystemDefault.setStatus("current")
_TnSysIpAclEthIfFilterAttributeTotal_Type = Integer32
_TnSysIpAclEthIfFilterAttributeTotal_Object = MibScalar
tnSysIpAclEthIfFilterAttributeTotal = _TnSysIpAclEthIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 18),
    _TnSysIpAclEthIfFilterAttributeTotal_Type()
)
tnSysIpAclEthIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterAttributeTotal.setStatus("current")
_TnSysIpAclEthIfFilterTable_Object = MibTable
tnSysIpAclEthIfFilterTable = _TnSysIpAclEthIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19)
)
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterTable.setStatus("current")
_TnSysIpAclEthIfFilterEntry_Object = MibTableRow
tnSysIpAclEthIfFilterEntry = _TnSysIpAclEthIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1)
)
tnSysIpAclEthIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnEthIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterEntry.setStatus("current")


class _TnSysIpAclEthIfFilterDir_Type(Integer32):
    """Custom type tnSysIpAclEthIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclEthIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclEthIfFilterDir_Object = MibTableColumn
tnSysIpAclEthIfFilterDir = _TnSysIpAclEthIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1, 1),
    _TnSysIpAclEthIfFilterDir_Type()
)
tnSysIpAclEthIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterDir.setStatus("current")
_TnSysIpAclEthIfFilterRowStatus_Type = RowStatus
_TnSysIpAclEthIfFilterRowStatus_Object = MibTableColumn
tnSysIpAclEthIfFilterRowStatus = _TnSysIpAclEthIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1, 2),
    _TnSysIpAclEthIfFilterRowStatus_Type()
)
tnSysIpAclEthIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterRowStatus.setStatus("current")


class _TnSysIpAclEthIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclEthIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclEthIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclEthIfFilterID_Object = MibTableColumn
tnSysIpAclEthIfFilterID = _TnSysIpAclEthIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1, 3),
    _TnSysIpAclEthIfFilterID_Type()
)
tnSysIpAclEthIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterID.setStatus("current")


class _TnSysIpAclEthIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclEthIfFilterEnable based on Integer32"""
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


_TnSysIpAclEthIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclEthIfFilterEnable_Object = MibTableColumn
tnSysIpAclEthIfFilterEnable = _TnSysIpAclEthIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1, 4),
    _TnSysIpAclEthIfFilterEnable_Type()
)
tnSysIpAclEthIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterEnable.setStatus("current")
_TnSysIpAclEthIfFilterSystemDefault_Type = TruthValue
_TnSysIpAclEthIfFilterSystemDefault_Object = MibTableColumn
tnSysIpAclEthIfFilterSystemDefault = _TnSysIpAclEthIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 19, 1, 5),
    _TnSysIpAclEthIfFilterSystemDefault_Type()
)
tnSysIpAclEthIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterSystemDefault.setStatus("current")
_TnSysIpv6AclEthIfFilterAttributeTotal_Type = Integer32
_TnSysIpv6AclEthIfFilterAttributeTotal_Object = MibScalar
tnSysIpv6AclEthIfFilterAttributeTotal = _TnSysIpv6AclEthIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 20),
    _TnSysIpv6AclEthIfFilterAttributeTotal_Type()
)
tnSysIpv6AclEthIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterAttributeTotal.setStatus("current")
_TnSysIpv6AclEthIfFilterTable_Object = MibTable
tnSysIpv6AclEthIfFilterTable = _TnSysIpv6AclEthIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21)
)
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterTable.setStatus("current")
_TnSysIpv6AclEthIfFilterEntry_Object = MibTableRow
tnSysIpv6AclEthIfFilterEntry = _TnSysIpv6AclEthIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1)
)
tnSysIpv6AclEthIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnEthIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterEntry.setStatus("current")


class _TnSysIpv6AclEthIfFilterDir_Type(Integer32):
    """Custom type tnSysIpv6AclEthIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpv6AclEthIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpv6AclEthIfFilterDir_Object = MibTableColumn
tnSysIpv6AclEthIfFilterDir = _TnSysIpv6AclEthIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1, 1),
    _TnSysIpv6AclEthIfFilterDir_Type()
)
tnSysIpv6AclEthIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterDir.setStatus("current")
_TnSysIpv6AclEthIfFilterRowStatus_Type = RowStatus
_TnSysIpv6AclEthIfFilterRowStatus_Object = MibTableColumn
tnSysIpv6AclEthIfFilterRowStatus = _TnSysIpv6AclEthIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1, 2),
    _TnSysIpv6AclEthIfFilterRowStatus_Type()
)
tnSysIpv6AclEthIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterRowStatus.setStatus("current")


class _TnSysIpv6AclEthIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclEthIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpv6AclEthIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclEthIfFilterID_Object = MibTableColumn
tnSysIpv6AclEthIfFilterID = _TnSysIpv6AclEthIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1, 3),
    _TnSysIpv6AclEthIfFilterID_Type()
)
tnSysIpv6AclEthIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterID.setStatus("current")


class _TnSysIpv6AclEthIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpv6AclEthIfFilterEnable based on Integer32"""
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


_TnSysIpv6AclEthIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpv6AclEthIfFilterEnable_Object = MibTableColumn
tnSysIpv6AclEthIfFilterEnable = _TnSysIpv6AclEthIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1, 4),
    _TnSysIpv6AclEthIfFilterEnable_Type()
)
tnSysIpv6AclEthIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterEnable.setStatus("current")
_TnSysIpv6AclEthIfFilterSystemDefault_Type = TruthValue
_TnSysIpv6AclEthIfFilterSystemDefault_Object = MibTableColumn
tnSysIpv6AclEthIfFilterSystemDefault = _TnSysIpv6AclEthIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 21, 1, 5),
    _TnSysIpv6AclEthIfFilterSystemDefault_Type()
)
tnSysIpv6AclEthIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterSystemDefault.setStatus("current")
_TnSysIpAclAttributeTotal_Type = Integer32
_TnSysIpAclAttributeTotal_Object = MibScalar
tnSysIpAclAttributeTotal = _TnSysIpAclAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 22),
    _TnSysIpAclAttributeTotal_Type()
)
tnSysIpAclAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclAttributeTotal.setStatus("current")
_TnSysIpAclTable_Object = MibTable
tnSysIpAclTable = _TnSysIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23)
)
if mibBuilder.loadTexts:
    tnSysIpAclTable.setStatus("current")
_TnSysIpAclEntry_Object = MibTableRow
tnSysIpAclEntry = _TnSysIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1)
)
tnSysIpAclEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpAclEntry.setStatus("current")
_TnSysIpAclIndex_Type = Integer32
_TnSysIpAclIndex_Object = MibTableColumn
tnSysIpAclIndex = _TnSysIpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 1),
    _TnSysIpAclIndex_Type()
)
tnSysIpAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIndex.setStatus("current")


class _TnSysIpAclDesc_Type(SnmpAdminString):
    """Custom type tnSysIpAclDesc based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysIpAclDesc_Type.__name__ = "SnmpAdminString"
_TnSysIpAclDesc_Object = MibTableColumn
tnSysIpAclDesc = _TnSysIpAclDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 2),
    _TnSysIpAclDesc_Type()
)
tnSysIpAclDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclDesc.setStatus("current")


class _TnSysIpAclAccessID_Type(SnmpAdminString):
    """Custom type tnSysIpAclAccessID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclAccessID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclAccessID_Object = MibTableColumn
tnSysIpAclAccessID = _TnSysIpAclAccessID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 3),
    _TnSysIpAclAccessID_Type()
)
tnSysIpAclAccessID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclAccessID.setStatus("current")


class _TnSysIpAclInterface_Type(Unsigned32):
    """Custom type tnSysIpAclInterface based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TnSysIpAclInterface_Type.__name__ = "Unsigned32"
_TnSysIpAclInterface_Object = MibTableColumn
tnSysIpAclInterface = _TnSysIpAclInterface_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 4),
    _TnSysIpAclInterface_Type()
)
tnSysIpAclInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterface.setStatus("current")


class _TnSysIpAclAction_Type(Integer32):
    """Custom type tnSysIpAclAction based on Integer32"""
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
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3),
          ("log", 4))
    )


_TnSysIpAclAction_Type.__name__ = "Integer32"
_TnSysIpAclAction_Object = MibTableColumn
tnSysIpAclAction = _TnSysIpAclAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 5),
    _TnSysIpAclAction_Type()
)
tnSysIpAclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclAction.setStatus("current")


class _TnSysIpAclSrcPort_Type(SnmpAdminString):
    """Custom type tnSysIpAclSrcPort based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpAclSrcPort_Type.__name__ = "SnmpAdminString"
_TnSysIpAclSrcPort_Object = MibTableColumn
tnSysIpAclSrcPort = _TnSysIpAclSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 6),
    _TnSysIpAclSrcPort_Type()
)
tnSysIpAclSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclSrcPort.setStatus("current")


class _TnSysIpAclDestPort_Type(SnmpAdminString):
    """Custom type tnSysIpAclDestPort based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpAclDestPort_Type.__name__ = "SnmpAdminString"
_TnSysIpAclDestPort_Object = MibTableColumn
tnSysIpAclDestPort = _TnSysIpAclDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 7),
    _TnSysIpAclDestPort_Type()
)
tnSysIpAclDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclDestPort.setStatus("current")


class _TnSysIpAclIcmpType_Type(Integer32):
    """Custom type tnSysIpAclIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIcmpType_Type.__name__ = "Integer32"
_TnSysIpAclIcmpType_Object = MibTableColumn
tnSysIpAclIcmpType = _TnSysIpAclIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 8),
    _TnSysIpAclIcmpType_Type()
)
tnSysIpAclIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIcmpType.setStatus("current")


class _TnSysIpAclIcmpCode_Type(Integer32):
    """Custom type tnSysIpAclIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIcmpCode_Type.__name__ = "Integer32"
_TnSysIpAclIcmpCode_Object = MibTableColumn
tnSysIpAclIcmpCode = _TnSysIpAclIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 9),
    _TnSysIpAclIcmpCode_Type()
)
tnSysIpAclIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIcmpCode.setStatus("current")


class _TnSysIpAclIpProtocol_Type(OctetString):
    """Custom type tnSysIpAclIpProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpAclIpProtocol_Type.__name__ = "OctetString"
_TnSysIpAclIpProtocol_Object = MibTableColumn
tnSysIpAclIpProtocol = _TnSysIpAclIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 10),
    _TnSysIpAclIpProtocol_Type()
)
tnSysIpAclIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpProtocol.setStatus("current")
_TnSysIpAclSrcAddr_Type = IpAddress
_TnSysIpAclSrcAddr_Object = MibTableColumn
tnSysIpAclSrcAddr = _TnSysIpAclSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 11),
    _TnSysIpAclSrcAddr_Type()
)
tnSysIpAclSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclSrcAddr.setStatus("current")


class _TnSysIpAclSrcPrefix_Type(Integer32):
    """Custom type tnSysIpAclSrcPrefix based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TnSysIpAclSrcPrefix_Type.__name__ = "Integer32"
_TnSysIpAclSrcPrefix_Object = MibTableColumn
tnSysIpAclSrcPrefix = _TnSysIpAclSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 12),
    _TnSysIpAclSrcPrefix_Type()
)
tnSysIpAclSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclSrcPrefix.setStatus("current")
_TnSysIpAclDestAddr_Type = IpAddress
_TnSysIpAclDestAddr_Object = MibTableColumn
tnSysIpAclDestAddr = _TnSysIpAclDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 13),
    _TnSysIpAclDestAddr_Type()
)
tnSysIpAclDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclDestAddr.setStatus("current")


class _TnSysIpAclDestPrefix_Type(Integer32):
    """Custom type tnSysIpAclDestPrefix based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TnSysIpAclDestPrefix_Type.__name__ = "Integer32"
_TnSysIpAclDestPrefix_Object = MibTableColumn
tnSysIpAclDestPrefix = _TnSysIpAclDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 14),
    _TnSysIpAclDestPrefix_Type()
)
tnSysIpAclDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclDestPrefix.setStatus("current")


class _TnSysIpAclIpFragment_Type(TruthValue):
    """Custom type tnSysIpAclIpFragment based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpFragment_Type.__name__ = "TruthValue"
_TnSysIpAclIpFragment_Object = MibTableColumn
tnSysIpAclIpFragment = _TnSysIpAclIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 15),
    _TnSysIpAclIpFragment_Type()
)
tnSysIpAclIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpFragment.setStatus("current")


class _TnSysIpAclTcpEstablish_Type(Integer32):
    """Custom type tnSysIpAclTcpEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("local", 3))
    )


_TnSysIpAclTcpEstablish_Type.__name__ = "Integer32"
_TnSysIpAclTcpEstablish_Object = MibTableColumn
tnSysIpAclTcpEstablish = _TnSysIpAclTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 16),
    _TnSysIpAclTcpEstablish_Type()
)
tnSysIpAclTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclTcpEstablish.setStatus("current")
_TnSysIpAclStatCount_Type = Counter32
_TnSysIpAclStatCount_Object = MibTableColumn
tnSysIpAclStatCount = _TnSysIpAclStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 17),
    _TnSysIpAclStatCount_Type()
)
tnSysIpAclStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclStatCount.setStatus("current")


class _TnSysIpAclAdminState_Type(Integer32):
    """Custom type tnSysIpAclAdminState based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("startToAdd", 3),
          ("startToModify", 4))
    )


_TnSysIpAclAdminState_Type.__name__ = "Integer32"
_TnSysIpAclAdminState_Object = MibTableColumn
tnSysIpAclAdminState = _TnSysIpAclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 23, 1, 18),
    _TnSysIpAclAdminState_Type()
)
tnSysIpAclAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclAdminState.setStatus("current")
_TnSysIpv6AclAttributeTotal_Type = Integer32
_TnSysIpv6AclAttributeTotal_Object = MibScalar
tnSysIpv6AclAttributeTotal = _TnSysIpv6AclAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 24),
    _TnSysIpv6AclAttributeTotal_Type()
)
tnSysIpv6AclAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclAttributeTotal.setStatus("current")
_TnSysIpv6AclTable_Object = MibTable
tnSysIpv6AclTable = _TnSysIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25)
)
if mibBuilder.loadTexts:
    tnSysIpv6AclTable.setStatus("current")
_TnSysIpv6AclEntry_Object = MibTableRow
tnSysIpv6AclEntry = _TnSysIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1)
)
tnSysIpv6AclEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpv6AclIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpv6AclEntry.setStatus("current")
_TnSysIpv6AclIndex_Type = Integer32
_TnSysIpv6AclIndex_Object = MibTableColumn
tnSysIpv6AclIndex = _TnSysIpv6AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 1),
    _TnSysIpv6AclIndex_Type()
)
tnSysIpv6AclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpv6AclIndex.setStatus("current")


class _TnSysIpv6AclDesc_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclDesc based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysIpv6AclDesc_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclDesc_Object = MibTableColumn
tnSysIpv6AclDesc = _TnSysIpv6AclDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 2),
    _TnSysIpv6AclDesc_Type()
)
tnSysIpv6AclDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclDesc.setStatus("current")


class _TnSysIpv6AclAccessID_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclAccessID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpv6AclAccessID_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclAccessID_Object = MibTableColumn
tnSysIpv6AclAccessID = _TnSysIpv6AclAccessID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 3),
    _TnSysIpv6AclAccessID_Type()
)
tnSysIpv6AclAccessID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclAccessID.setStatus("current")


class _TnSysIpv6AclInterface_Type(Unsigned32):
    """Custom type tnSysIpv6AclInterface based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TnSysIpv6AclInterface_Type.__name__ = "Unsigned32"
_TnSysIpv6AclInterface_Object = MibTableColumn
tnSysIpv6AclInterface = _TnSysIpv6AclInterface_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 4),
    _TnSysIpv6AclInterface_Type()
)
tnSysIpv6AclInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclInterface.setStatus("current")


class _TnSysIpv6AclAction_Type(Integer32):
    """Custom type tnSysIpv6AclAction based on Integer32"""
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
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3),
          ("log", 4))
    )


_TnSysIpv6AclAction_Type.__name__ = "Integer32"
_TnSysIpv6AclAction_Object = MibTableColumn
tnSysIpv6AclAction = _TnSysIpv6AclAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 5),
    _TnSysIpv6AclAction_Type()
)
tnSysIpv6AclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclAction.setStatus("current")


class _TnSysIpv6AclSrcPort_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclSrcPort based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpv6AclSrcPort_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclSrcPort_Object = MibTableColumn
tnSysIpv6AclSrcPort = _TnSysIpv6AclSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 6),
    _TnSysIpv6AclSrcPort_Type()
)
tnSysIpv6AclSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclSrcPort.setStatus("current")


class _TnSysIpv6AclDestPort_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclDestPort based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpv6AclDestPort_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclDestPort_Object = MibTableColumn
tnSysIpv6AclDestPort = _TnSysIpv6AclDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 7),
    _TnSysIpv6AclDestPort_Type()
)
tnSysIpv6AclDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclDestPort.setStatus("current")


class _TnSysIpv6AclIcmpType_Type(Integer32):
    """Custom type tnSysIpv6AclIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpv6AclIcmpType_Type.__name__ = "Integer32"
_TnSysIpv6AclIcmpType_Object = MibTableColumn
tnSysIpv6AclIcmpType = _TnSysIpv6AclIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 8),
    _TnSysIpv6AclIcmpType_Type()
)
tnSysIpv6AclIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclIcmpType.setStatus("current")


class _TnSysIpv6AclIcmpCode_Type(Integer32):
    """Custom type tnSysIpv6AclIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpv6AclIcmpCode_Type.__name__ = "Integer32"
_TnSysIpv6AclIcmpCode_Object = MibTableColumn
tnSysIpv6AclIcmpCode = _TnSysIpv6AclIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 9),
    _TnSysIpv6AclIcmpCode_Type()
)
tnSysIpv6AclIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclIcmpCode.setStatus("current")


class _TnSysIpv6AclIpProtocol_Type(OctetString):
    """Custom type tnSysIpv6AclIpProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TnSysIpv6AclIpProtocol_Type.__name__ = "OctetString"
_TnSysIpv6AclIpProtocol_Object = MibTableColumn
tnSysIpv6AclIpProtocol = _TnSysIpv6AclIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 10),
    _TnSysIpv6AclIpProtocol_Type()
)
tnSysIpv6AclIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclIpProtocol.setStatus("current")
_TnSysIpv6AclSrcAddr_Type = InetAddressIPv6
_TnSysIpv6AclSrcAddr_Object = MibTableColumn
tnSysIpv6AclSrcAddr = _TnSysIpv6AclSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 11),
    _TnSysIpv6AclSrcAddr_Type()
)
tnSysIpv6AclSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclSrcAddr.setStatus("current")
_TnSysIpv6AclSrcPrefixLen_Type = InetAddressPrefixLength
_TnSysIpv6AclSrcPrefixLen_Object = MibTableColumn
tnSysIpv6AclSrcPrefixLen = _TnSysIpv6AclSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 12),
    _TnSysIpv6AclSrcPrefixLen_Type()
)
tnSysIpv6AclSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclSrcPrefixLen.setStatus("current")
_TnSysIpv6AclDestAddr_Type = InetAddressIPv6
_TnSysIpv6AclDestAddr_Object = MibTableColumn
tnSysIpv6AclDestAddr = _TnSysIpv6AclDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 13),
    _TnSysIpv6AclDestAddr_Type()
)
tnSysIpv6AclDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclDestAddr.setStatus("current")
_TnSysIpv6AclDestPrefixLen_Type = InetAddressPrefixLength
_TnSysIpv6AclDestPrefixLen_Object = MibTableColumn
tnSysIpv6AclDestPrefixLen = _TnSysIpv6AclDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 14),
    _TnSysIpv6AclDestPrefixLen_Type()
)
tnSysIpv6AclDestPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclDestPrefixLen.setStatus("current")


class _TnSysIpv6AclTcpEstablish_Type(Integer32):
    """Custom type tnSysIpv6AclTcpEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("local", 3))
    )


_TnSysIpv6AclTcpEstablish_Type.__name__ = "Integer32"
_TnSysIpv6AclTcpEstablish_Object = MibTableColumn
tnSysIpv6AclTcpEstablish = _TnSysIpv6AclTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 15),
    _TnSysIpv6AclTcpEstablish_Type()
)
tnSysIpv6AclTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclTcpEstablish.setStatus("current")
_TnSysIpv6AclStatCount_Type = Counter32
_TnSysIpv6AclStatCount_Object = MibTableColumn
tnSysIpv6AclStatCount = _TnSysIpv6AclStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 16),
    _TnSysIpv6AclStatCount_Type()
)
tnSysIpv6AclStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclStatCount.setStatus("current")


class _TnSysIpv6AclAdminState_Type(Integer32):
    """Custom type tnSysIpv6AclAdminState based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("startToAdd", 3),
          ("startToModify", 4))
    )


_TnSysIpv6AclAdminState_Type.__name__ = "Integer32"
_TnSysIpv6AclAdminState_Object = MibTableColumn
tnSysIpv6AclAdminState = _TnSysIpv6AclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 25, 1, 17),
    _TnSysIpv6AclAdminState_Type()
)
tnSysIpv6AclAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclAdminState.setStatus("current")
_TnSysNtpServerIdStats_ObjectIdentity = ObjectIdentity
tnSysNtpServerIdStats = _TnSysNtpServerIdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18)
)
_TnSysNtpServerIdStatsTable_Object = MibTable
tnSysNtpServerIdStatsTable = _TnSysNtpServerIdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsTable.setStatus("current")
_TnSysNtpServerIdStatsEntry_Object = MibTableRow
tnSysNtpServerIdStatsEntry = _TnSysNtpServerIdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1)
)
tnSysNtpServerIdStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsEntry.setStatus("current")


class _TnSysNtpServerIdStatsIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerIdStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnSysNtpServerIdStatsIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerIdStatsIndex_Object = MibTableColumn
tnSysNtpServerIdStatsIndex = _TnSysNtpServerIdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 1),
    _TnSysNtpServerIdStatsIndex_Type()
)
tnSysNtpServerIdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsIndex.setStatus("current")


class _TnSysNtpServerIdStatsSelect_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsSelect based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnSysNtpServerIdStatsSelect_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsSelect_Object = MibTableColumn
tnSysNtpServerIdStatsSelect = _TnSysNtpServerIdStatsSelect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 2),
    _TnSysNtpServerIdStatsSelect_Type()
)
tnSysNtpServerIdStatsSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsSelect.setStatus("current")


class _TnSysNtpServerIdStatsIp_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsIp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TnSysNtpServerIdStatsIp_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsIp_Object = MibTableColumn
tnSysNtpServerIdStatsIp = _TnSysNtpServerIdStatsIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 3),
    _TnSysNtpServerIdStatsIp_Type()
)
tnSysNtpServerIdStatsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsIp.setStatus("current")


class _TnSysNtpServerIdStatsRefId_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsRefId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TnSysNtpServerIdStatsRefId_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsRefId_Object = MibTableColumn
tnSysNtpServerIdStatsRefId = _TnSysNtpServerIdStatsRefId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 4),
    _TnSysNtpServerIdStatsRefId_Type()
)
tnSysNtpServerIdStatsRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsRefId.setStatus("current")


class _TnSysNtpServerIdStatsStrtm_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsStrtm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TnSysNtpServerIdStatsStrtm_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsStrtm_Object = MibTableColumn
tnSysNtpServerIdStatsStrtm = _TnSysNtpServerIdStatsStrtm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 5),
    _TnSysNtpServerIdStatsStrtm_Type()
)
tnSysNtpServerIdStatsStrtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsStrtm.setStatus("current")


class _TnSysNtpServerIdStatsClockType_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsClockType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnSysNtpServerIdStatsClockType_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsClockType_Object = MibTableColumn
tnSysNtpServerIdStatsClockType = _TnSysNtpServerIdStatsClockType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 6),
    _TnSysNtpServerIdStatsClockType_Type()
)
tnSysNtpServerIdStatsClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsClockType.setStatus("current")


class _TnSysNtpServerIdStatsPoll_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsPoll based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TnSysNtpServerIdStatsPoll_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsPoll_Object = MibTableColumn
tnSysNtpServerIdStatsPoll = _TnSysNtpServerIdStatsPoll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 7),
    _TnSysNtpServerIdStatsPoll_Type()
)
tnSysNtpServerIdStatsPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsPoll.setStatus("current")


class _TnSysNtpServerIdStatsReach_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsReach based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_TnSysNtpServerIdStatsReach_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsReach_Object = MibTableColumn
tnSysNtpServerIdStatsReach = _TnSysNtpServerIdStatsReach_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 8),
    _TnSysNtpServerIdStatsReach_Type()
)
tnSysNtpServerIdStatsReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsReach.setStatus("current")


class _TnSysNtpServerIdStatsDelay_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsDelay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsDelay_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsDelay_Object = MibTableColumn
tnSysNtpServerIdStatsDelay = _TnSysNtpServerIdStatsDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 9),
    _TnSysNtpServerIdStatsDelay_Type()
)
tnSysNtpServerIdStatsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsDelay.setStatus("current")


class _TnSysNtpServerIdStatsOffset_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsOffset based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsOffset_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsOffset_Object = MibTableColumn
tnSysNtpServerIdStatsOffset = _TnSysNtpServerIdStatsOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 10),
    _TnSysNtpServerIdStatsOffset_Type()
)
tnSysNtpServerIdStatsOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsOffset.setStatus("current")


class _TnSysNtpServerIdStatsJitter_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsJitter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsJitter_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsJitter_Object = MibTableColumn
tnSysNtpServerIdStatsJitter = _TnSysNtpServerIdStatsJitter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 11),
    _TnSysNtpServerIdStatsJitter_Type()
)
tnSysNtpServerIdStatsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsJitter.setStatus("current")
_TnSysNtpServerIdStatsKeyIndex_Type = Unsigned32
_TnSysNtpServerIdStatsKeyIndex_Object = MibTableColumn
tnSysNtpServerIdStatsKeyIndex = _TnSysNtpServerIdStatsKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 12),
    _TnSysNtpServerIdStatsKeyIndex_Type()
)
tnSysNtpServerIdStatsKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsKeyIndex.setStatus("current")
_TnSysFtpServer_ObjectIdentity = ObjectIdentity
tnSysFtpServer = _TnSysFtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19)
)


class _TnSysFtpServerEnabled_Type(TruthValue):
    """Custom type tnSysFtpServerEnabled based on TruthValue"""
    defaultValue = 2


_TnSysFtpServerEnabled_Type.__name__ = "TruthValue"
_TnSysFtpServerEnabled_Object = MibScalar
tnSysFtpServerEnabled = _TnSysFtpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 1),
    _TnSysFtpServerEnabled_Type()
)
tnSysFtpServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFtpServerEnabled.setStatus("current")


class _TnSysFtpServerUserId_Type(SnmpAdminString):
    """Custom type tnSysFtpServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("UserSWNE")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysFtpServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysFtpServerUserId_Object = MibScalar
tnSysFtpServerUserId = _TnSysFtpServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 2),
    _TnSysFtpServerUserId_Type()
)
tnSysFtpServerUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysFtpServerUserId.setStatus("current")


class _TnSysFtpServerPassword_Type(SnmpAdminString):
    """Custom type tnSysFtpServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("********")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysFtpServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysFtpServerPassword_Object = MibScalar
tnSysFtpServerPassword = _TnSysFtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 3),
    _TnSysFtpServerPassword_Type()
)
tnSysFtpServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFtpServerPassword.setStatus("current")
_TnSysNtpServerAuthentication_ObjectIdentity = ObjectIdentity
tnSysNtpServerAuthentication = _TnSysNtpServerAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20)
)
_TnSysNtpServerAuthenticationAttributeTotal_Type = Integer32
_TnSysNtpServerAuthenticationAttributeTotal_Object = MibScalar
tnSysNtpServerAuthenticationAttributeTotal = _TnSysNtpServerAuthenticationAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 1),
    _TnSysNtpServerAuthenticationAttributeTotal_Type()
)
tnSysNtpServerAuthenticationAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationAttributeTotal.setStatus("current")
_TnSysNtpServerAuthenticationTable_Object = MibTable
tnSysNtpServerAuthenticationTable = _TnSysNtpServerAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationTable.setStatus("current")
_TnSysNtpServerAuthenticationEntry_Object = MibTableRow
tnSysNtpServerAuthenticationEntry = _TnSysNtpServerAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1)
)
tnSysNtpServerAuthenticationEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKeyIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationEntry.setStatus("current")


class _TnSysNtpServerAuthenticationKeyIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerAuthenticationKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysNtpServerAuthenticationKeyIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerAuthenticationKeyIndex_Object = MibTableColumn
tnSysNtpServerAuthenticationKeyIndex = _TnSysNtpServerAuthenticationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 1),
    _TnSysNtpServerAuthenticationKeyIndex_Type()
)
tnSysNtpServerAuthenticationKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKeyIndex.setStatus("current")
_TnSysNtpServerAuthenticationRowStatus_Type = RowStatus
_TnSysNtpServerAuthenticationRowStatus_Object = MibTableColumn
tnSysNtpServerAuthenticationRowStatus = _TnSysNtpServerAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 2),
    _TnSysNtpServerAuthenticationRowStatus_Type()
)
tnSysNtpServerAuthenticationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationRowStatus.setStatus("current")


class _TnSysNtpServerAuthenticationKeyType_Type(Integer32):
    """Custom type tnSysNtpServerAuthenticationKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("md5", 2))
    )


_TnSysNtpServerAuthenticationKeyType_Type.__name__ = "Integer32"
_TnSysNtpServerAuthenticationKeyType_Object = MibTableColumn
tnSysNtpServerAuthenticationKeyType = _TnSysNtpServerAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 3),
    _TnSysNtpServerAuthenticationKeyType_Type()
)
tnSysNtpServerAuthenticationKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKeyType.setStatus("current")


class _TnSysNtpServerAuthenticationKey_Type(OctetString):
    """Custom type tnSysNtpServerAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_TnSysNtpServerAuthenticationKey_Type.__name__ = "OctetString"
_TnSysNtpServerAuthenticationKey_Object = MibTableColumn
tnSysNtpServerAuthenticationKey = _TnSysNtpServerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 4),
    _TnSysNtpServerAuthenticationKey_Type()
)
tnSysNtpServerAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKey.setStatus("current")
_TnNeDiscovery_ObjectIdentity = ObjectIdentity
tnNeDiscovery = _TnNeDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21)
)
_TnNeDiscoveryAttributeTotal_Type = Integer32
_TnNeDiscoveryAttributeTotal_Object = MibScalar
tnNeDiscoveryAttributeTotal = _TnNeDiscoveryAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 1),
    _TnNeDiscoveryAttributeTotal_Type()
)
tnNeDiscoveryAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryAttributeTotal.setStatus("current")
_TnNeDiscoveryTable_Object = MibTable
tnNeDiscoveryTable = _TnNeDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    tnNeDiscoveryTable.setStatus("current")
_TnNeDiscoveryEntry_Object = MibTableRow
tnNeDiscoveryEntry = _TnNeDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1)
)
tnNeDiscoveryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnNeDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    tnNeDiscoveryEntry.setStatus("current")


class _TnNeDiscoveryIndex_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_TnNeDiscoveryIndex_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryIndex_Object = MibTableColumn
tnNeDiscoveryIndex = _TnNeDiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 1),
    _TnNeDiscoveryIndex_Type()
)
tnNeDiscoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNeDiscoveryIndex.setStatus("current")


class _TnNeDiscoveryFilename_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnNeDiscoveryFilename_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryFilename_Object = MibTableColumn
tnNeDiscoveryFilename = _TnNeDiscoveryFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 2),
    _TnNeDiscoveryFilename_Type()
)
tnNeDiscoveryFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryFilename.setStatus("current")


class _TnNeDiscoveryControl_Type(Integer32):
    """Custom type tnNeDiscoveryControl based on Integer32"""
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
        *(("noCmd", 1),
          ("start", 2),
          ("abort", 3))
    )


_TnNeDiscoveryControl_Type.__name__ = "Integer32"
_TnNeDiscoveryControl_Object = MibTableColumn
tnNeDiscoveryControl = _TnNeDiscoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 3),
    _TnNeDiscoveryControl_Type()
)
tnNeDiscoveryControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryControl.setStatus("current")


class _TnNeDiscoveryStatus_Type(Integer32):
    """Custom type tnNeDiscoveryStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnNeDiscoveryStatus_Type.__name__ = "Integer32"
_TnNeDiscoveryStatus_Object = MibTableColumn
tnNeDiscoveryStatus = _TnNeDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 4),
    _TnNeDiscoveryStatus_Type()
)
tnNeDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryStatus.setStatus("current")


class _TnNeDiscoveryErrorCode_Type(Integer32):
    """Custom type tnNeDiscoveryErrorCode based on Integer32"""
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
        *(("noError", 1),
          ("unknown", 2),
          ("timeout", 3),
          ("serverError", 4),
          ("networkError", 5),
          ("fileSystemError", 6),
          ("systemNotReady", 7))
    )


_TnNeDiscoveryErrorCode_Type.__name__ = "Integer32"
_TnNeDiscoveryErrorCode_Object = MibTableColumn
tnNeDiscoveryErrorCode = _TnNeDiscoveryErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 5),
    _TnNeDiscoveryErrorCode_Type()
)
tnNeDiscoveryErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryErrorCode.setStatus("current")


class _TnNeDiscoveryServerIp_Type(IpAddress):
    """Custom type tnNeDiscoveryServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnNeDiscoveryServerIp_Type.__name__ = "IpAddress"
_TnNeDiscoveryServerIp_Object = MibTableColumn
tnNeDiscoveryServerIp = _TnNeDiscoveryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 6),
    _TnNeDiscoveryServerIp_Type()
)
tnNeDiscoveryServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerIp.setStatus("current")
_TnNeDiscoveryServerProtocol_Type = AluWdmNewTransferProtocol
_TnNeDiscoveryServerProtocol_Object = MibTableColumn
tnNeDiscoveryServerProtocol = _TnNeDiscoveryServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 7),
    _TnNeDiscoveryServerProtocol_Type()
)
tnNeDiscoveryServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerProtocol.setStatus("current")


class _TnNeDiscoveryServerUserId_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TnNeDiscoveryServerUserId_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryServerUserId_Object = MibTableColumn
tnNeDiscoveryServerUserId = _TnNeDiscoveryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 8),
    _TnNeDiscoveryServerUserId_Type()
)
tnNeDiscoveryServerUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerUserId.setStatus("current")


class _TnNeDiscoveryServerPassword_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TnNeDiscoveryServerPassword_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryServerPassword_Object = MibTableColumn
tnNeDiscoveryServerPassword = _TnNeDiscoveryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 9),
    _TnNeDiscoveryServerPassword_Type()
)
tnNeDiscoveryServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerPassword.setStatus("current")
_TnNeDiscoveryServerTimeOut_Type = Integer32
_TnNeDiscoveryServerTimeOut_Object = MibTableColumn
tnNeDiscoveryServerTimeOut = _TnNeDiscoveryServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 10),
    _TnNeDiscoveryServerTimeOut_Type()
)
tnNeDiscoveryServerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerTimeOut.setStatus("current")
_TnNeDiscoveryRowStatus_Type = RowStatus
_TnNeDiscoveryRowStatus_Object = MibTableColumn
tnNeDiscoveryRowStatus = _TnNeDiscoveryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 11),
    _TnNeDiscoveryRowStatus_Type()
)
tnNeDiscoveryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryRowStatus.setStatus("current")


class _TnNeDiscoveryServerInetAddressType_Type(InetAddressType):
    """Custom type tnNeDiscoveryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnNeDiscoveryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnNeDiscoveryServerInetAddressType_Object = MibTableColumn
tnNeDiscoveryServerInetAddressType = _TnNeDiscoveryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 12),
    _TnNeDiscoveryServerInetAddressType_Type()
)
tnNeDiscoveryServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerInetAddressType.setStatus("current")


class _TnNeDiscoveryServerInetAddress_Type(InetAddress):
    """Custom type tnNeDiscoveryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnNeDiscoveryServerInetAddress_Type.__name__ = "InetAddress"
_TnNeDiscoveryServerInetAddress_Object = MibTableColumn
tnNeDiscoveryServerInetAddress = _TnNeDiscoveryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 13),
    _TnNeDiscoveryServerInetAddress_Type()
)
tnNeDiscoveryServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerInetAddress.setStatus("current")


class _TnNeDiscoveryDeltaFilename_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryDeltaFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnNeDiscoveryDeltaFilename_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryDeltaFilename_Object = MibTableColumn
tnNeDiscoveryDeltaFilename = _TnNeDiscoveryDeltaFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 14),
    _TnNeDiscoveryDeltaFilename_Type()
)
tnNeDiscoveryDeltaFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryDeltaFilename.setStatus("deprecated")


class _TnNeDiscoveryDeltaFileFlag_Type(Integer32):
    """Custom type tnNeDiscoveryDeltaFileFlag based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("eqptSyncEnable", 1),
          ("eqptSyncDisable", 2),
          ("tpSyncEnable", 3),
          ("tpSyncDisable", 4),
          ("sncSyncEnable", 5),
          ("sncSyncDisable", 6),
          ("tlSyncEnable", 7),
          ("tlSyncDisable", 8),
          ("pgSyncEnable", 9),
          ("pgSyncDisable", 10),
          ("syncTransfer", 11),
          ("syncClear", 12),
          ("syncDisable", 13),
          ("eqptSyncTransfer", 14),
          ("tpSyncTransfer", 15),
          ("sncSyncTransfer", 16),
          ("tlSyncTransfer", 17),
          ("pgSyncTransfer", 18),
          ("syncTrapEnable", 19),
          ("syncTrapDisable", 20),
          ("syncTrapTransfer", 21))
    )


_TnNeDiscoveryDeltaFileFlag_Type.__name__ = "Integer32"
_TnNeDiscoveryDeltaFileFlag_Object = MibTableColumn
tnNeDiscoveryDeltaFileFlag = _TnNeDiscoveryDeltaFileFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 15),
    _TnNeDiscoveryDeltaFileFlag_Type()
)
tnNeDiscoveryDeltaFileFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryDeltaFileFlag.setStatus("current")


class _TnNeDiscoveryDeltaSyncStatus_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryDeltaSyncStatus based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnNeDiscoveryDeltaSyncStatus_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryDeltaSyncStatus_Object = MibTableColumn
tnNeDiscoveryDeltaSyncStatus = _TnNeDiscoveryDeltaSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 16),
    _TnNeDiscoveryDeltaSyncStatus_Type()
)
tnNeDiscoveryDeltaSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryDeltaSyncStatus.setStatus("current")


class _TnNeDiscoveryPort_Type(Unsigned32):
    """Custom type tnNeDiscoveryPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnNeDiscoveryPort_Type.__name__ = "Unsigned32"
_TnNeDiscoveryPort_Object = MibTableColumn
tnNeDiscoveryPort = _TnNeDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 17),
    _TnNeDiscoveryPort_Type()
)
tnNeDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryPort.setStatus("current")
_TnSysOtdrScan_ObjectIdentity = ObjectIdentity
tnSysOtdrScan = _TnSysOtdrScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22)
)
_TnSysOtdrScanSystemProfile_ObjectIdentity = ObjectIdentity
tnSysOtdrScanSystemProfile = _TnSysOtdrScanSystemProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1)
)
_TnSysOtdrScanSystemProfileAttributeTotal_Type = Integer32
_TnSysOtdrScanSystemProfileAttributeTotal_Object = MibScalar
tnSysOtdrScanSystemProfileAttributeTotal = _TnSysOtdrScanSystemProfileAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 1),
    _TnSysOtdrScanSystemProfileAttributeTotal_Type()
)
tnSysOtdrScanSystemProfileAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAttributeTotal.setStatus("current")
_TnSysOtdrScanSystemProfileTable_Object = MibTable
tnSysOtdrScanSystemProfileTable = _TnSysOtdrScanSystemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2)
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileTable.setStatus("current")
_TnSysOtdrScanSystemProfileEntry_Object = MibTableRow
tnSysOtdrScanSystemProfileEntry = _TnSysOtdrScanSystemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1)
)
tnSysOtdrScanSystemProfileEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileId"),
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileEntry.setStatus("current")


class _TnSysOtdrScanSystemProfileId_Type(Integer32):
    """Custom type tnSysOtdrScanSystemProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TnSysOtdrScanSystemProfileId_Type.__name__ = "Integer32"
_TnSysOtdrScanSystemProfileId_Object = MibTableColumn
tnSysOtdrScanSystemProfileId = _TnSysOtdrScanSystemProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 1),
    _TnSysOtdrScanSystemProfileId_Type()
)
tnSysOtdrScanSystemProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileId.setStatus("current")


class _TnSysOtdrScanSystemProfileDescription_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanSystemProfileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnSysOtdrScanSystemProfileDescription_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanSystemProfileDescription_Object = MibTableColumn
tnSysOtdrScanSystemProfileDescription = _TnSysOtdrScanSystemProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 2),
    _TnSysOtdrScanSystemProfileDescription_Type()
)
tnSysOtdrScanSystemProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileDescription.setStatus("current")


class _TnSysOtdrScanSystemProfileWaveLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileWaveLength based on Unsigned32"""
    defaultValue = 1610


_TnSysOtdrScanSystemProfileWaveLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileWaveLength_Object = MibTableColumn
tnSysOtdrScanSystemProfileWaveLength = _TnSysOtdrScanSystemProfileWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 3),
    _TnSysOtdrScanSystemProfileWaveLength_Type()
)
tnSysOtdrScanSystemProfileWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileWaveLength.setUnits("nanometers")


class _TnSysOtdrScanSystemProfilePulseLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfilePulseLength based on Unsigned32"""
    defaultValue = 300


_TnSysOtdrScanSystemProfilePulseLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfilePulseLength_Object = MibTableColumn
tnSysOtdrScanSystemProfilePulseLength = _TnSysOtdrScanSystemProfilePulseLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 4),
    _TnSysOtdrScanSystemProfilePulseLength_Type()
)
tnSysOtdrScanSystemProfilePulseLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfilePulseLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfilePulseLength.setUnits("nanoseconds")


class _TnSysOtdrScanSystemProfileRange_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileRange based on Unsigned32"""
    defaultValue = 160000


_TnSysOtdrScanSystemProfileRange_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileRange_Object = MibTableColumn
tnSysOtdrScanSystemProfileRange = _TnSysOtdrScanSystemProfileRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 5),
    _TnSysOtdrScanSystemProfileRange_Type()
)
tnSysOtdrScanSystemProfileRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileRange.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileRange.setUnits("meters")


class _TnSysOtdrScanSystemProfileResolution_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileResolution based on Unsigned32"""
    defaultValue = 2500


_TnSysOtdrScanSystemProfileResolution_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileResolution_Object = MibTableColumn
tnSysOtdrScanSystemProfileResolution = _TnSysOtdrScanSystemProfileResolution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 6),
    _TnSysOtdrScanSystemProfileResolution_Type()
)
tnSysOtdrScanSystemProfileResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileResolution.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileResolution.setUnits("millimeters")


class _TnSysOtdrScanSystemProfileAvgTime_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileAvgTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_TnSysOtdrScanSystemProfileAvgTime_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileAvgTime_Object = MibTableColumn
tnSysOtdrScanSystemProfileAvgTime = _TnSysOtdrScanSystemProfileAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 7),
    _TnSysOtdrScanSystemProfileAvgTime_Type()
)
tnSysOtdrScanSystemProfileAvgTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAvgTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAvgTime.setUnits("seconds")


class _TnSysOtdrScanSystemProfileEventThreshold_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileEventThreshold based on Unsigned32"""
    defaultValue = 50


_TnSysOtdrScanSystemProfileEventThreshold_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileEventThreshold_Object = MibTableColumn
tnSysOtdrScanSystemProfileEventThreshold = _TnSysOtdrScanSystemProfileEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 8),
    _TnSysOtdrScanSystemProfileEventThreshold_Type()
)
tnSysOtdrScanSystemProfileEventThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileEventThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileEventThreshold.setUnits("mB")


class _TnSysOtdrScanSystemProfileIOR_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileIOR based on Unsigned32"""
    defaultValue = 1465


_TnSysOtdrScanSystemProfileIOR_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileIOR_Object = MibTableColumn
tnSysOtdrScanSystemProfileIOR = _TnSysOtdrScanSystemProfileIOR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 9),
    _TnSysOtdrScanSystemProfileIOR_Type()
)
tnSysOtdrScanSystemProfileIOR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileIOR.setStatus("current")
_TnSysOtdrScanTransfer_ObjectIdentity = ObjectIdentity
tnSysOtdrScanTransfer = _TnSysOtdrScanTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2)
)


class _TnSysOtdrScanTransferRemoteHostIp_Type(IpAddress):
    """Custom type tnSysOtdrScanTransferRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysOtdrScanTransferRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysOtdrScanTransferRemoteHostIp_Object = MibScalar
tnSysOtdrScanTransferRemoteHostIp = _TnSysOtdrScanTransferRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 1),
    _TnSysOtdrScanTransferRemoteHostIp_Type()
)
tnSysOtdrScanTransferRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferRemoteHostIp.setStatus("current")


class _TnSysOtdrScanTransferCommand_Type(Integer32):
    """Custom type tnSysOtdrScanTransferCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysOtdrScanTransferCommand_Type.__name__ = "Integer32"
_TnSysOtdrScanTransferCommand_Object = MibScalar
tnSysOtdrScanTransferCommand = _TnSysOtdrScanTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 2),
    _TnSysOtdrScanTransferCommand_Type()
)
tnSysOtdrScanTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferCommand.setStatus("current")


class _TnSysOtdrScanTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferRemotePath_Object = MibScalar
tnSysOtdrScanTransferRemotePath = _TnSysOtdrScanTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 3),
    _TnSysOtdrScanTransferRemotePath_Type()
)
tnSysOtdrScanTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferRemotePath.setStatus("current")


class _TnSysOtdrScanTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysOtdrScanTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysOtdrScanTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysOtdrScanTransferStatus_Object = MibScalar
tnSysOtdrScanTransferStatus = _TnSysOtdrScanTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 4),
    _TnSysOtdrScanTransferStatus_Type()
)
tnSysOtdrScanTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferStatus.setStatus("current")


class _TnSysOtdrScanTransferFilename_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanTransferFilename_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferFilename_Object = MibScalar
tnSysOtdrScanTransferFilename = _TnSysOtdrScanTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 5),
    _TnSysOtdrScanTransferFilename_Type()
)
tnSysOtdrScanTransferFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferFilename.setStatus("current")


class _TnSysOtdrScanTransferProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysOtdrScanTransferProtocol based on AluWdmTransferProtocol"""
    defaultValue = 1


_TnSysOtdrScanTransferProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysOtdrScanTransferProtocol_Object = MibScalar
tnSysOtdrScanTransferProtocol = _TnSysOtdrScanTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 6),
    _TnSysOtdrScanTransferProtocol_Type()
)
tnSysOtdrScanTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferProtocol.setStatus("current")


class _TnSysOtdrScanTransferUserId_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanTransferUserId_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferUserId_Object = MibScalar
tnSysOtdrScanTransferUserId = _TnSysOtdrScanTransferUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 7),
    _TnSysOtdrScanTransferUserId_Type()
)
tnSysOtdrScanTransferUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferUserId.setStatus("current")


class _TnSysOtdrScanTransferPassword_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanTransferPassword_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferPassword_Object = MibScalar
tnSysOtdrScanTransferPassword = _TnSysOtdrScanTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 8),
    _TnSysOtdrScanTransferPassword_Type()
)
tnSysOtdrScanTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferPassword.setStatus("current")


class _TnSysOtdrScanTransferInetAddressType_Type(InetAddressType):
    """Custom type tnSysOtdrScanTransferInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysOtdrScanTransferInetAddressType_Type.__name__ = "InetAddressType"
_TnSysOtdrScanTransferInetAddressType_Object = MibScalar
tnSysOtdrScanTransferInetAddressType = _TnSysOtdrScanTransferInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 9),
    _TnSysOtdrScanTransferInetAddressType_Type()
)
tnSysOtdrScanTransferInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferInetAddressType.setStatus("current")


class _TnSysOtdrScanTransferInetAddress_Type(InetAddress):
    """Custom type tnSysOtdrScanTransferInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysOtdrScanTransferInetAddress_Type.__name__ = "InetAddress"
_TnSysOtdrScanTransferInetAddress_Object = MibScalar
tnSysOtdrScanTransferInetAddress = _TnSysOtdrScanTransferInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 10),
    _TnSysOtdrScanTransferInetAddress_Type()
)
tnSysOtdrScanTransferInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferInetAddress.setStatus("current")


class _TnSysOtdrScanTransferPort_Type(Unsigned32):
    """Custom type tnSysOtdrScanTransferPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysOtdrScanTransferPort_Type.__name__ = "Unsigned32"
_TnSysOtdrScanTransferPort_Object = MibScalar
tnSysOtdrScanTransferPort = _TnSysOtdrScanTransferPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 11),
    _TnSysOtdrScanTransferPort_Type()
)
tnSysOtdrScanTransferPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferPort.setStatus("current")
_TnSysOtdrScanSystemProfileM_ObjectIdentity = ObjectIdentity
tnSysOtdrScanSystemProfileM = _TnSysOtdrScanSystemProfileM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3)
)
_TnSysOtdrScanSystemProfileMAttributeTotal_Type = Integer32
_TnSysOtdrScanSystemProfileMAttributeTotal_Object = MibScalar
tnSysOtdrScanSystemProfileMAttributeTotal = _TnSysOtdrScanSystemProfileMAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 1),
    _TnSysOtdrScanSystemProfileMAttributeTotal_Type()
)
tnSysOtdrScanSystemProfileMAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMAttributeTotal.setStatus("current")
_TnSysOtdrScanSystemProfileMTable_Object = MibTable
tnSysOtdrScanSystemProfileMTable = _TnSysOtdrScanSystemProfileMTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2)
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMTable.setStatus("current")
_TnSysOtdrScanSystemProfileMEntry_Object = MibTableRow
tnSysOtdrScanSystemProfileMEntry = _TnSysOtdrScanSystemProfileMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1)
)
tnSysOtdrScanSystemProfileMEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMId"),
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMEntry.setStatus("current")


class _TnSysOtdrScanSystemProfileMId_Type(Integer32):
    """Custom type tnSysOtdrScanSystemProfileMId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TnSysOtdrScanSystemProfileMId_Type.__name__ = "Integer32"
_TnSysOtdrScanSystemProfileMId_Object = MibTableColumn
tnSysOtdrScanSystemProfileMId = _TnSysOtdrScanSystemProfileMId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 1),
    _TnSysOtdrScanSystemProfileMId_Type()
)
tnSysOtdrScanSystemProfileMId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMId.setStatus("current")


class _TnSysOtdrScanSystemProfileMDescription_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanSystemProfileMDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnSysOtdrScanSystemProfileMDescription_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanSystemProfileMDescription_Object = MibTableColumn
tnSysOtdrScanSystemProfileMDescription = _TnSysOtdrScanSystemProfileMDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 2),
    _TnSysOtdrScanSystemProfileMDescription_Type()
)
tnSysOtdrScanSystemProfileMDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMDescription.setStatus("current")


class _TnSysOtdrScanSystemProfileMWaveLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMWaveLength based on Unsigned32"""
    defaultValue = 1610


_TnSysOtdrScanSystemProfileMWaveLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMWaveLength_Object = MibTableColumn
tnSysOtdrScanSystemProfileMWaveLength = _TnSysOtdrScanSystemProfileMWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 3),
    _TnSysOtdrScanSystemProfileMWaveLength_Type()
)
tnSysOtdrScanSystemProfileMWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMWaveLength.setUnits("nanometers")


class _TnSysOtdrScanSystemProfileMPulseLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMPulseLength based on Unsigned32"""
    defaultValue = 300


_TnSysOtdrScanSystemProfileMPulseLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMPulseLength_Object = MibTableColumn
tnSysOtdrScanSystemProfileMPulseLength = _TnSysOtdrScanSystemProfileMPulseLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 4),
    _TnSysOtdrScanSystemProfileMPulseLength_Type()
)
tnSysOtdrScanSystemProfileMPulseLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMPulseLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMPulseLength.setUnits("nanoseconds")


class _TnSysOtdrScanSystemProfileMRange_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMRange based on Unsigned32"""
    defaultValue = 160000


_TnSysOtdrScanSystemProfileMRange_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMRange_Object = MibTableColumn
tnSysOtdrScanSystemProfileMRange = _TnSysOtdrScanSystemProfileMRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 5),
    _TnSysOtdrScanSystemProfileMRange_Type()
)
tnSysOtdrScanSystemProfileMRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMRange.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMRange.setUnits("meters")


class _TnSysOtdrScanSystemProfileMResolution_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMResolution based on Unsigned32"""
    defaultValue = 2500


_TnSysOtdrScanSystemProfileMResolution_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMResolution_Object = MibTableColumn
tnSysOtdrScanSystemProfileMResolution = _TnSysOtdrScanSystemProfileMResolution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 6),
    _TnSysOtdrScanSystemProfileMResolution_Type()
)
tnSysOtdrScanSystemProfileMResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMResolution.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMResolution.setUnits("millimeters")


class _TnSysOtdrScanSystemProfileMAvgTime_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMAvgTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_TnSysOtdrScanSystemProfileMAvgTime_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMAvgTime_Object = MibTableColumn
tnSysOtdrScanSystemProfileMAvgTime = _TnSysOtdrScanSystemProfileMAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 7),
    _TnSysOtdrScanSystemProfileMAvgTime_Type()
)
tnSysOtdrScanSystemProfileMAvgTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMAvgTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMAvgTime.setUnits("seconds")


class _TnSysOtdrScanSystemProfileMEventThreshold_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMEventThreshold based on Unsigned32"""
    defaultValue = 50


_TnSysOtdrScanSystemProfileMEventThreshold_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMEventThreshold_Object = MibTableColumn
tnSysOtdrScanSystemProfileMEventThreshold = _TnSysOtdrScanSystemProfileMEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 8),
    _TnSysOtdrScanSystemProfileMEventThreshold_Type()
)
tnSysOtdrScanSystemProfileMEventThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMEventThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMEventThreshold.setUnits("mB")


class _TnSysOtdrScanSystemProfileMIOR_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileMIOR based on Unsigned32"""
    defaultValue = 1465


_TnSysOtdrScanSystemProfileMIOR_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileMIOR_Object = MibTableColumn
tnSysOtdrScanSystemProfileMIOR = _TnSysOtdrScanSystemProfileMIOR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 3, 2, 1, 9),
    _TnSysOtdrScanSystemProfileMIOR_Type()
)
tnSysOtdrScanSystemProfileMIOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMIOR.setStatus("current")
_TnSysOtdrScanResultsTransfer_ObjectIdentity = ObjectIdentity
tnSysOtdrScanResultsTransfer = _TnSysOtdrScanResultsTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4)
)


class _TnSysOtdrScanResultsTransferRemoteHostIp_Type(IpAddress):
    """Custom type tnSysOtdrScanResultsTransferRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysOtdrScanResultsTransferRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysOtdrScanResultsTransferRemoteHostIp_Object = MibScalar
tnSysOtdrScanResultsTransferRemoteHostIp = _TnSysOtdrScanResultsTransferRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 1),
    _TnSysOtdrScanResultsTransferRemoteHostIp_Type()
)
tnSysOtdrScanResultsTransferRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRemoteHostIp.setStatus("current")


class _TnSysOtdrScanResultsTransferProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysOtdrScanResultsTransferProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysOtdrScanResultsTransferProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysOtdrScanResultsTransferProtocol_Object = MibScalar
tnSysOtdrScanResultsTransferProtocol = _TnSysOtdrScanResultsTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 2),
    _TnSysOtdrScanResultsTransferProtocol_Type()
)
tnSysOtdrScanResultsTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferProtocol.setStatus("current")


class _TnSysOtdrScanResultsTransferUserId_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanResultsTransferUserId_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferUserId_Object = MibScalar
tnSysOtdrScanResultsTransferUserId = _TnSysOtdrScanResultsTransferUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 3),
    _TnSysOtdrScanResultsTransferUserId_Type()
)
tnSysOtdrScanResultsTransferUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferUserId.setStatus("current")


class _TnSysOtdrScanResultsTransferPassword_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanResultsTransferPassword_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferPassword_Object = MibScalar
tnSysOtdrScanResultsTransferPassword = _TnSysOtdrScanResultsTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 4),
    _TnSysOtdrScanResultsTransferPassword_Type()
)
tnSysOtdrScanResultsTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferPassword.setStatus("current")


class _TnSysOtdrScanResultsTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanResultsTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferRemotePath_Object = MibScalar
tnSysOtdrScanResultsTransferRemotePath = _TnSysOtdrScanResultsTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 5),
    _TnSysOtdrScanResultsTransferRemotePath_Type()
)
tnSysOtdrScanResultsTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRemotePath.setStatus("current")


class _TnSysOtdrScanResultsTransferCommand_Type(Integer32):
    """Custom type tnSysOtdrScanResultsTransferCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysOtdrScanResultsTransferCommand_Type.__name__ = "Integer32"
_TnSysOtdrScanResultsTransferCommand_Object = MibScalar
tnSysOtdrScanResultsTransferCommand = _TnSysOtdrScanResultsTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 6),
    _TnSysOtdrScanResultsTransferCommand_Type()
)
tnSysOtdrScanResultsTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferCommand.setStatus("current")


class _TnSysOtdrScanResultsTransferFilename_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanResultsTransferFilename_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferFilename_Object = MibScalar
tnSysOtdrScanResultsTransferFilename = _TnSysOtdrScanResultsTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 7),
    _TnSysOtdrScanResultsTransferFilename_Type()
)
tnSysOtdrScanResultsTransferFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferFilename.setStatus("current")


class _TnSysOtdrScanResultsTransferRecentSuccessFile_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferRecentSuccessFile based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysOtdrScanResultsTransferRecentSuccessFile_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferRecentSuccessFile_Object = MibScalar
tnSysOtdrScanResultsTransferRecentSuccessFile = _TnSysOtdrScanResultsTransferRecentSuccessFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 8),
    _TnSysOtdrScanResultsTransferRecentSuccessFile_Type()
)
tnSysOtdrScanResultsTransferRecentSuccessFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRecentSuccessFile.setStatus("current")


class _TnSysOtdrScanResultsTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysOtdrScanResultsTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysOtdrScanResultsTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysOtdrScanResultsTransferStatus_Object = MibScalar
tnSysOtdrScanResultsTransferStatus = _TnSysOtdrScanResultsTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 9),
    _TnSysOtdrScanResultsTransferStatus_Type()
)
tnSysOtdrScanResultsTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferStatus.setStatus("current")


class _TnSysOtdrScanResultsLastTransferTimestamp_Type(Unsigned32):
    """Custom type tnSysOtdrScanResultsLastTransferTimestamp based on Unsigned32"""
    defaultValue = 0


_TnSysOtdrScanResultsLastTransferTimestamp_Type.__name__ = "Unsigned32"
_TnSysOtdrScanResultsLastTransferTimestamp_Object = MibScalar
tnSysOtdrScanResultsLastTransferTimestamp = _TnSysOtdrScanResultsLastTransferTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 10),
    _TnSysOtdrScanResultsLastTransferTimestamp_Type()
)
tnSysOtdrScanResultsLastTransferTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsLastTransferTimestamp.setStatus("current")


class _TnSysOtdrScanResultsTransferRemoteInetAddressType_Type(InetAddressType):
    """Custom type tnSysOtdrScanResultsTransferRemoteInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysOtdrScanResultsTransferRemoteInetAddressType_Type.__name__ = "InetAddressType"
_TnSysOtdrScanResultsTransferRemoteInetAddressType_Object = MibScalar
tnSysOtdrScanResultsTransferRemoteInetAddressType = _TnSysOtdrScanResultsTransferRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 11),
    _TnSysOtdrScanResultsTransferRemoteInetAddressType_Type()
)
tnSysOtdrScanResultsTransferRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRemoteInetAddressType.setStatus("current")


class _TnSysOtdrScanResultsTransferRemoteInetAddress_Type(InetAddress):
    """Custom type tnSysOtdrScanResultsTransferRemoteInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysOtdrScanResultsTransferRemoteInetAddress_Type.__name__ = "InetAddress"
_TnSysOtdrScanResultsTransferRemoteInetAddress_Object = MibScalar
tnSysOtdrScanResultsTransferRemoteInetAddress = _TnSysOtdrScanResultsTransferRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 12),
    _TnSysOtdrScanResultsTransferRemoteInetAddress_Type()
)
tnSysOtdrScanResultsTransferRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRemoteInetAddress.setStatus("current")


class _TnSysOtdrScanResultsTransferPort_Type(Unsigned32):
    """Custom type tnSysOtdrScanResultsTransferPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysOtdrScanResultsTransferPort_Type.__name__ = "Unsigned32"
_TnSysOtdrScanResultsTransferPort_Object = MibScalar
tnSysOtdrScanResultsTransferPort = _TnSysOtdrScanResultsTransferPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 13),
    _TnSysOtdrScanResultsTransferPort_Type()
)
tnSysOtdrScanResultsTransferPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferPort.setStatus("current")


class _TnSysOtdrScanResultsTransferRemoveFileFromNE_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanResultsTransferRemoveFileFromNE based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysOtdrScanResultsTransferRemoveFileFromNE_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanResultsTransferRemoveFileFromNE_Object = MibScalar
tnSysOtdrScanResultsTransferRemoveFileFromNE = _TnSysOtdrScanResultsTransferRemoveFileFromNE_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 4, 14),
    _TnSysOtdrScanResultsTransferRemoveFileFromNE_Type()
)
tnSysOtdrScanResultsTransferRemoveFileFromNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferRemoveFileFromNE.setStatus("current")
_TnClusterObjs_ObjectIdentity = ObjectIdentity
tnClusterObjs = _TnClusterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23)
)
_TnClusterTable_Object = MibTable
tnClusterTable = _TnClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1)
)
if mibBuilder.loadTexts:
    tnClusterTable.setStatus("current")
_TnClusterEntry_Object = MibTableRow
tnClusterEntry = _TnClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1)
)
tnClusterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnClusterFarEndNode"),
)
if mibBuilder.loadTexts:
    tnClusterEntry.setStatus("current")
_TnClusterRowStatus_Type = RowStatus
_TnClusterRowStatus_Object = MibTableColumn
tnClusterRowStatus = _TnClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 1),
    _TnClusterRowStatus_Type()
)
tnClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterRowStatus.setStatus("current")
_TnClusterFarEndNode_Type = OctetString
_TnClusterFarEndNode_Object = MibTableColumn
tnClusterFarEndNode = _TnClusterFarEndNode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 2),
    _TnClusterFarEndNode_Type()
)
tnClusterFarEndNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnClusterFarEndNode.setStatus("current")


class _TnClusterIpAddress_Type(IpAddress):
    """Custom type tnClusterIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnClusterIpAddress_Type.__name__ = "IpAddress"
_TnClusterIpAddress_Object = MibTableColumn
tnClusterIpAddress = _TnClusterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 3),
    _TnClusterIpAddress_Type()
)
tnClusterIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterIpAddress.setStatus("current")


class _TnClusterlinkStatus_Type(Integer32):
    """Custom type tnClusterlinkStatus based on Integer32"""
    defaultValue = 3

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
          ("unknown", 3))
    )


_TnClusterlinkStatus_Type.__name__ = "Integer32"
_TnClusterlinkStatus_Object = MibTableColumn
tnClusterlinkStatus = _TnClusterlinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 4),
    _TnClusterlinkStatus_Type()
)
tnClusterlinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterlinkStatus.setStatus("current")


class _TnClusterInetAddressType_Type(InetAddressType):
    """Custom type tnClusterInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnClusterInetAddressType_Type.__name__ = "InetAddressType"
_TnClusterInetAddressType_Object = MibTableColumn
tnClusterInetAddressType = _TnClusterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 5),
    _TnClusterInetAddressType_Type()
)
tnClusterInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterInetAddressType.setStatus("current")


class _TnClusterInetAddress_Type(InetAddress):
    """Custom type tnClusterInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnClusterInetAddress_Type.__name__ = "InetAddress"
_TnClusterInetAddress_Object = MibTableColumn
tnClusterInetAddress = _TnClusterInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 6),
    _TnClusterInetAddress_Type()
)
tnClusterInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterInetAddress.setStatus("current")
_TnSysPmFetchBulk_ObjectIdentity = ObjectIdentity
tnSysPmFetchBulk = _TnSysPmFetchBulk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24)
)


class _TnSysPmFetchBulkStart_Type(TnCommand):
    """Custom type tnSysPmFetchBulkStart based on TnCommand"""
    defaultValue = 1


_TnSysPmFetchBulkStart_Type.__name__ = "TnCommand"
_TnSysPmFetchBulkStart_Object = MibScalar
tnSysPmFetchBulkStart = _TnSysPmFetchBulkStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 1),
    _TnSysPmFetchBulkStart_Type()
)
tnSysPmFetchBulkStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStart.setStatus("current")


class _TnSysPmFetchBulkStatus_Type(Integer32):
    """Custom type tnSysPmFetchBulkStatus based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnSysPmFetchBulkStatus_Type.__name__ = "Integer32"
_TnSysPmFetchBulkStatus_Object = MibScalar
tnSysPmFetchBulkStatus = _TnSysPmFetchBulkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 2),
    _TnSysPmFetchBulkStatus_Type()
)
tnSysPmFetchBulkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStatus.setStatus("current")


class _TnSysPmFetchBulkRemoteHostIp_Type(IpAddress):
    """Custom type tnSysPmFetchBulkRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysPmFetchBulkRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysPmFetchBulkRemoteHostIp_Object = MibScalar
tnSysPmFetchBulkRemoteHostIp = _TnSysPmFetchBulkRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 3),
    _TnSysPmFetchBulkRemoteHostIp_Type()
)
tnSysPmFetchBulkRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkRemoteHostIp.setStatus("current")


class _TnSysPmFetchBulkUserId_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysPmFetchBulkUserId_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkUserId_Object = MibScalar
tnSysPmFetchBulkUserId = _TnSysPmFetchBulkUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 4),
    _TnSysPmFetchBulkUserId_Type()
)
tnSysPmFetchBulkUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkUserId.setStatus("current")


class _TnSysPmFetchBulkPassword_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysPmFetchBulkPassword_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkPassword_Object = MibScalar
tnSysPmFetchBulkPassword = _TnSysPmFetchBulkPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 5),
    _TnSysPmFetchBulkPassword_Type()
)
tnSysPmFetchBulkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkPassword.setStatus("current")


class _TnSysPmFetchBulkRemotePath_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysPmFetchBulkRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkRemotePath_Object = MibScalar
tnSysPmFetchBulkRemotePath = _TnSysPmFetchBulkRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 6),
    _TnSysPmFetchBulkRemotePath_Type()
)
tnSysPmFetchBulkRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkRemotePath.setStatus("current")


class _TnSysPmFetchBulkStatsInterval_Type(Unsigned32):
    """Custom type tnSysPmFetchBulkStatsInterval based on Unsigned32"""
    defaultValue = 0


_TnSysPmFetchBulkStatsInterval_Type.__name__ = "Unsigned32"
_TnSysPmFetchBulkStatsInterval_Object = MibScalar
tnSysPmFetchBulkStatsInterval = _TnSysPmFetchBulkStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 7),
    _TnSysPmFetchBulkStatsInterval_Type()
)
tnSysPmFetchBulkStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStatsInterval.setStatus("current")


class _TnSysPmFetchBulkBinnedStatsBin_Type(Unsigned32):
    """Custom type tnSysPmFetchBulkBinnedStatsBin based on Unsigned32"""
    defaultValue = 0


_TnSysPmFetchBulkBinnedStatsBin_Type.__name__ = "Unsigned32"
_TnSysPmFetchBulkBinnedStatsBin_Object = MibScalar
tnSysPmFetchBulkBinnedStatsBin = _TnSysPmFetchBulkBinnedStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 8),
    _TnSysPmFetchBulkBinnedStatsBin_Type()
)
tnSysPmFetchBulkBinnedStatsBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkBinnedStatsBin.setStatus("current")


class _TnSysPmFetchBulkShelfNum_Type(Integer32):
    """Custom type tnSysPmFetchBulkShelfNum based on Integer32"""
    defaultValue = 1


_TnSysPmFetchBulkShelfNum_Type.__name__ = "Integer32"
_TnSysPmFetchBulkShelfNum_Object = MibScalar
tnSysPmFetchBulkShelfNum = _TnSysPmFetchBulkShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 9),
    _TnSysPmFetchBulkShelfNum_Type()
)
tnSysPmFetchBulkShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkShelfNum.setStatus("current")
_TnSysDebugTransfer_ObjectIdentity = ObjectIdentity
tnSysDebugTransfer = _TnSysDebugTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25)
)


class _TnSysDebugTransferRemoteHostIp_Type(IpAddress):
    """Custom type tnSysDebugTransferRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysDebugTransferRemoteHostIp_Type.__name__ = "IpAddress"
_TnSysDebugTransferRemoteHostIp_Object = MibScalar
tnSysDebugTransferRemoteHostIp = _TnSysDebugTransferRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 1),
    _TnSysDebugTransferRemoteHostIp_Type()
)
tnSysDebugTransferRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteHostIp.setStatus("current")


class _TnSysDebugTransferCommand_Type(Integer32):
    """Custom type tnSysDebugTransferCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysDebugTransferCommand_Type.__name__ = "Integer32"
_TnSysDebugTransferCommand_Object = MibScalar
tnSysDebugTransferCommand = _TnSysDebugTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 2),
    _TnSysDebugTransferCommand_Type()
)
tnSysDebugTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferCommand.setStatus("current")


class _TnSysDebugTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDebugTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferRemotePath_Object = MibScalar
tnSysDebugTransferRemotePath = _TnSysDebugTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 3),
    _TnSysDebugTransferRemotePath_Type()
)
tnSysDebugTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemotePath.setStatus("current")


class _TnSysDebugTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysDebugTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysDebugTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysDebugTransferStatus_Object = MibScalar
tnSysDebugTransferStatus = _TnSysDebugTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 4),
    _TnSysDebugTransferStatus_Type()
)
tnSysDebugTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferStatus.setStatus("current")


class _TnSysDebugTransferProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysDebugTransferProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysDebugTransferProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysDebugTransferProtocol_Object = MibScalar
tnSysDebugTransferProtocol = _TnSysDebugTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 5),
    _TnSysDebugTransferProtocol_Type()
)
tnSysDebugTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferProtocol.setStatus("current")


class _TnSysDebugTransferUserId_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysDebugTransferUserId_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferUserId_Object = MibScalar
tnSysDebugTransferUserId = _TnSysDebugTransferUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 6),
    _TnSysDebugTransferUserId_Type()
)
tnSysDebugTransferUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferUserId.setStatus("current")


class _TnSysDebugTransferPassword_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysDebugTransferPassword_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferPassword_Object = MibScalar
tnSysDebugTransferPassword = _TnSysDebugTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 7),
    _TnSysDebugTransferPassword_Type()
)
tnSysDebugTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferPassword.setStatus("current")


class _TnSysDebugTransferFilename_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysDebugTransferFilename_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferFilename_Object = MibScalar
tnSysDebugTransferFilename = _TnSysDebugTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 8),
    _TnSysDebugTransferFilename_Type()
)
tnSysDebugTransferFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferFilename.setStatus("current")


class _TnSysDebugTransferRecentSuccessFile_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferRecentSuccessFile based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysDebugTransferRecentSuccessFile_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferRecentSuccessFile_Object = MibScalar
tnSysDebugTransferRecentSuccessFile = _TnSysDebugTransferRecentSuccessFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 9),
    _TnSysDebugTransferRecentSuccessFile_Type()
)
tnSysDebugTransferRecentSuccessFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferRecentSuccessFile.setStatus("current")


class _TnSysDebugTransferTimestamp_Type(Unsigned32):
    """Custom type tnSysDebugTransferTimestamp based on Unsigned32"""
    defaultValue = 0


_TnSysDebugTransferTimestamp_Type.__name__ = "Unsigned32"
_TnSysDebugTransferTimestamp_Object = MibScalar
tnSysDebugTransferTimestamp = _TnSysDebugTransferTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 10),
    _TnSysDebugTransferTimestamp_Type()
)
tnSysDebugTransferTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferTimestamp.setStatus("current")


class _TnSysDebugTransferShelfNum_Type(Integer32):
    """Custom type tnSysDebugTransferShelfNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TnSysDebugTransferShelfNum_Type.__name__ = "Integer32"
_TnSysDebugTransferShelfNum_Object = MibScalar
tnSysDebugTransferShelfNum = _TnSysDebugTransferShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 11),
    _TnSysDebugTransferShelfNum_Type()
)
tnSysDebugTransferShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferShelfNum.setStatus("current")


class _TnSysDebugTransferPercentCompleted_Type(Unsigned32):
    """Custom type tnSysDebugTransferPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysDebugTransferPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysDebugTransferPercentCompleted_Object = MibScalar
tnSysDebugTransferPercentCompleted = _TnSysDebugTransferPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 12),
    _TnSysDebugTransferPercentCompleted_Type()
)
tnSysDebugTransferPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferPercentCompleted.setStatus("current")


class _TnSysDebugTransferRemoteInetAddress_Type(InetAddress):
    """Custom type tnSysDebugTransferRemoteInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysDebugTransferRemoteInetAddress_Type.__name__ = "InetAddress"
_TnSysDebugTransferRemoteInetAddress_Object = MibScalar
tnSysDebugTransferRemoteInetAddress = _TnSysDebugTransferRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 14),
    _TnSysDebugTransferRemoteInetAddress_Type()
)
tnSysDebugTransferRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteInetAddress.setStatus("current")


class _TnSysDebugTransferRemoteInetAddressType_Type(InetAddressType):
    """Custom type tnSysDebugTransferRemoteInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysDebugTransferRemoteInetAddressType_Type.__name__ = "InetAddressType"
_TnSysDebugTransferRemoteInetAddressType_Object = MibScalar
tnSysDebugTransferRemoteInetAddressType = _TnSysDebugTransferRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 15),
    _TnSysDebugTransferRemoteInetAddressType_Type()
)
tnSysDebugTransferRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteInetAddressType.setStatus("current")


class _TnSysDebugTransferScratchDir_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferScratchDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnSysDebugTransferScratchDir_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferScratchDir_Object = MibScalar
tnSysDebugTransferScratchDir = _TnSysDebugTransferScratchDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 16),
    _TnSysDebugTransferScratchDir_Type()
)
tnSysDebugTransferScratchDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferScratchDir.setStatus("current")


class _TnSysDebugTransferIncludeInDumps_Type(Integer32):
    """Custom type tnSysDebugTransferIncludeInDumps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expert", 1),
          ("basic", 2),
          ("occ", 3))
    )


_TnSysDebugTransferIncludeInDumps_Type.__name__ = "Integer32"
_TnSysDebugTransferIncludeInDumps_Object = MibScalar
tnSysDebugTransferIncludeInDumps = _TnSysDebugTransferIncludeInDumps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 17),
    _TnSysDebugTransferIncludeInDumps_Type()
)
tnSysDebugTransferIncludeInDumps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferIncludeInDumps.setStatus("current")


class _TnSysDebugTransferPort_Type(Unsigned32):
    """Custom type tnSysDebugTransferPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysDebugTransferPort_Type.__name__ = "Unsigned32"
_TnSysDebugTransferPort_Object = MibScalar
tnSysDebugTransferPort = _TnSysDebugTransferPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 18),
    _TnSysDebugTransferPort_Type()
)
tnSysDebugTransferPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferPort.setStatus("current")
_TnSysLicenseInv_ObjectIdentity = ObjectIdentity
tnSysLicenseInv = _TnSysLicenseInv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26)
)


class _TnSysLicenseInvPathIp_Type(IpAddress):
    """Custom type tnSysLicenseInvPathIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysLicenseInvPathIp_Type.__name__ = "IpAddress"
_TnSysLicenseInvPathIp_Object = MibScalar
tnSysLicenseInvPathIp = _TnSysLicenseInvPathIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 1),
    _TnSysLicenseInvPathIp_Type()
)
tnSysLicenseInvPathIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathIp.setStatus("current")


class _TnSysLicenseInvFile_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvFile based on SnmpAdminString"""
    defaultValue = OctetString("./LicenseInv-file")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysLicenseInvFile_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvFile_Object = MibScalar
tnSysLicenseInvFile = _TnSysLicenseInvFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 2),
    _TnSysLicenseInvFile_Type()
)
tnSysLicenseInvFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvFile.setStatus("current")


class _TnSysLicenseInvProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysLicenseInvProtocol based on AluWdmTransferProtocol"""
    defaultValue = 1


_TnSysLicenseInvProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysLicenseInvProtocol_Object = MibScalar
tnSysLicenseInvProtocol = _TnSysLicenseInvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 3),
    _TnSysLicenseInvProtocol_Type()
)
tnSysLicenseInvProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvProtocol.setStatus("current")


class _TnSysLicenseInvUserId_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvUserId based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvUserId_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvUserId_Object = MibScalar
tnSysLicenseInvUserId = _TnSysLicenseInvUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 4),
    _TnSysLicenseInvUserId_Type()
)
tnSysLicenseInvUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvUserId.setStatus("current")


class _TnSysLicenseInvPassword_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvPassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvPassword_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvPassword_Object = MibScalar
tnSysLicenseInvPassword = _TnSysLicenseInvPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 5),
    _TnSysLicenseInvPassword_Type()
)
tnSysLicenseInvPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPassword.setStatus("current")


class _TnSysLicenseInvFileUploadOper_Type(TruthValue):
    """Custom type tnSysLicenseInvFileUploadOper based on TruthValue"""
    defaultValue = 2


_TnSysLicenseInvFileUploadOper_Type.__name__ = "TruthValue"
_TnSysLicenseInvFileUploadOper_Object = MibScalar
tnSysLicenseInvFileUploadOper = _TnSysLicenseInvFileUploadOper_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 6),
    _TnSysLicenseInvFileUploadOper_Type()
)
tnSysLicenseInvFileUploadOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileUploadOper.setStatus("current")


class _TnSysLicenseInvPathInetAddressType_Type(InetAddressType):
    """Custom type tnSysLicenseInvPathInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysLicenseInvPathInetAddressType_Type.__name__ = "InetAddressType"
_TnSysLicenseInvPathInetAddressType_Object = MibScalar
tnSysLicenseInvPathInetAddressType = _TnSysLicenseInvPathInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 7),
    _TnSysLicenseInvPathInetAddressType_Type()
)
tnSysLicenseInvPathInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathInetAddressType.setStatus("current")


class _TnSysLicenseInvPathInetAddress_Type(InetAddress):
    """Custom type tnSysLicenseInvPathInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysLicenseInvPathInetAddress_Type.__name__ = "InetAddress"
_TnSysLicenseInvPathInetAddress_Object = MibScalar
tnSysLicenseInvPathInetAddress = _TnSysLicenseInvPathInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 8),
    _TnSysLicenseInvPathInetAddress_Type()
)
tnSysLicenseInvPathInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathInetAddress.setStatus("current")


class _TnSysLicenseInvLastOperPercentCompleted_Type(Unsigned32):
    """Custom type tnSysLicenseInvLastOperPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysLicenseInvLastOperPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysLicenseInvLastOperPercentCompleted_Object = MibScalar
tnSysLicenseInvLastOperPercentCompleted = _TnSysLicenseInvLastOperPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 9),
    _TnSysLicenseInvLastOperPercentCompleted_Type()
)
tnSysLicenseInvLastOperPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvLastOperPercentCompleted.setStatus("current")


class _TnSysLicenseInvLastUploadFileName_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvLastUploadFileName based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvLastUploadFileName_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvLastUploadFileName_Object = MibScalar
tnSysLicenseInvLastUploadFileName = _TnSysLicenseInvLastUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 10),
    _TnSysLicenseInvLastUploadFileName_Type()
)
tnSysLicenseInvLastUploadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvLastUploadFileName.setStatus("current")


class _TnSysLicenseInvFileLastUploadStatus_Type(Integer32):
    """Custom type tnSysLicenseInvFileLastUploadStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2),
          ("none", 3))
    )


_TnSysLicenseInvFileLastUploadStatus_Type.__name__ = "Integer32"
_TnSysLicenseInvFileLastUploadStatus_Object = MibScalar
tnSysLicenseInvFileLastUploadStatus = _TnSysLicenseInvFileLastUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 11),
    _TnSysLicenseInvFileLastUploadStatus_Type()
)
tnSysLicenseInvFileLastUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileLastUploadStatus.setStatus("current")


class _TnSysLicenseInvFileLastUploadTimeStamp_Type(Unsigned32):
    """Custom type tnSysLicenseInvFileLastUploadTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysLicenseInvFileLastUploadTimeStamp_Type.__name__ = "Unsigned32"
_TnSysLicenseInvFileLastUploadTimeStamp_Object = MibScalar
tnSysLicenseInvFileLastUploadTimeStamp = _TnSysLicenseInvFileLastUploadTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 12),
    _TnSysLicenseInvFileLastUploadTimeStamp_Type()
)
tnSysLicenseInvFileLastUploadTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileLastUploadTimeStamp.setStatus("current")
_TnSysLinux_ObjectIdentity = ObjectIdentity
tnSysLinux = _TnSysLinux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28)
)


class _TnSysLinuxRootUserId_Type(SnmpAdminString):
    """Custom type tnSysLinuxRootUserId based on SnmpAdminString"""
    defaultValue = OctetString("root")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnSysLinuxRootUserId_Type.__name__ = "SnmpAdminString"
_TnSysLinuxRootUserId_Object = MibScalar
tnSysLinuxRootUserId = _TnSysLinuxRootUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 1),
    _TnSysLinuxRootUserId_Type()
)
tnSysLinuxRootUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserId.setStatus("current")


class _TnSysLinuxRootUserPassword_Type(SnmpAdminString):
    """Custom type tnSysLinuxRootUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysLinuxRootUserPassword_Type.__name__ = "SnmpAdminString"
_TnSysLinuxRootUserPassword_Object = MibScalar
tnSysLinuxRootUserPassword = _TnSysLinuxRootUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 2),
    _TnSysLinuxRootUserPassword_Type()
)
tnSysLinuxRootUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserPassword.setStatus("current")


class _TnSysLinuxApplUserId_Type(SnmpAdminString):
    """Custom type tnSysLinuxApplUserId based on SnmpAdminString"""
    defaultValue = OctetString("appl")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnSysLinuxApplUserId_Type.__name__ = "SnmpAdminString"
_TnSysLinuxApplUserId_Object = MibScalar
tnSysLinuxApplUserId = _TnSysLinuxApplUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 3),
    _TnSysLinuxApplUserId_Type()
)
tnSysLinuxApplUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxApplUserId.setStatus("current")


class _TnSysLinuxApplUserPassword_Type(SnmpAdminString):
    """Custom type tnSysLinuxApplUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysLinuxApplUserPassword_Type.__name__ = "SnmpAdminString"
_TnSysLinuxApplUserPassword_Object = MibScalar
tnSysLinuxApplUserPassword = _TnSysLinuxApplUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 4),
    _TnSysLinuxApplUserPassword_Type()
)
tnSysLinuxApplUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxApplUserPassword.setStatus("current")


class _TnSysLinuxRootPasswordStatus_Type(TruthValue):
    """Custom type tnSysLinuxRootPasswordStatus based on TruthValue"""
    defaultValue = 2


_TnSysLinuxRootPasswordStatus_Type.__name__ = "TruthValue"
_TnSysLinuxRootPasswordStatus_Object = MibScalar
tnSysLinuxRootPasswordStatus = _TnSysLinuxRootPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 5),
    _TnSysLinuxRootPasswordStatus_Type()
)
tnSysLinuxRootPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxRootPasswordStatus.setStatus("current")


class _TnSysLinuxApplPasswordStatus_Type(TruthValue):
    """Custom type tnSysLinuxApplPasswordStatus based on TruthValue"""
    defaultValue = 2


_TnSysLinuxApplPasswordStatus_Type.__name__ = "TruthValue"
_TnSysLinuxApplPasswordStatus_Object = MibScalar
tnSysLinuxApplPasswordStatus = _TnSysLinuxApplPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 6),
    _TnSysLinuxApplPasswordStatus_Type()
)
tnSysLinuxApplPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxApplPasswordStatus.setStatus("current")


class _TnSysLinuxRootUserStatus_Type(TruthValue):
    """Custom type tnSysLinuxRootUserStatus based on TruthValue"""
    defaultValue = 1


_TnSysLinuxRootUserStatus_Type.__name__ = "TruthValue"
_TnSysLinuxRootUserStatus_Object = MibScalar
tnSysLinuxRootUserStatus = _TnSysLinuxRootUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 7),
    _TnSysLinuxRootUserStatus_Type()
)
tnSysLinuxRootUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserStatus.setStatus("current")


class _TnSysLinuxApplUserStatus_Type(TruthValue):
    """Custom type tnSysLinuxApplUserStatus based on TruthValue"""
    defaultValue = 1


_TnSysLinuxApplUserStatus_Type.__name__ = "TruthValue"
_TnSysLinuxApplUserStatus_Object = MibScalar
tnSysLinuxApplUserStatus = _TnSysLinuxApplUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 8),
    _TnSysLinuxApplUserStatus_Type()
)
tnSysLinuxApplUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxApplUserStatus.setStatus("current")


class _TnSysLinuxLoginInactivityTimeOut_Type(Unsigned32):
    """Custom type tnSysLinuxLoginInactivityTimeOut based on Unsigned32"""
    defaultValue = 15


_TnSysLinuxLoginInactivityTimeOut_Type.__name__ = "Unsigned32"
_TnSysLinuxLoginInactivityTimeOut_Object = MibScalar
tnSysLinuxLoginInactivityTimeOut = _TnSysLinuxLoginInactivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 9),
    _TnSysLinuxLoginInactivityTimeOut_Type()
)
tnSysLinuxLoginInactivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxLoginInactivityTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tnSysLinuxLoginInactivityTimeOut.setUnits("minutes")


class _TnSysLinuxSmsUserId_Type(SnmpAdminString):
    """Custom type tnSysLinuxSmsUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnSysLinuxSmsUserId_Type.__name__ = "SnmpAdminString"
_TnSysLinuxSmsUserId_Object = MibScalar
tnSysLinuxSmsUserId = _TnSysLinuxSmsUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 10),
    _TnSysLinuxSmsUserId_Type()
)
tnSysLinuxSmsUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxSmsUserId.setStatus("current")


class _TnSysLinuxSmsUserPassword_Type(SnmpAdminString):
    """Custom type tnSysLinuxSmsUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysLinuxSmsUserPassword_Type.__name__ = "SnmpAdminString"
_TnSysLinuxSmsUserPassword_Object = MibScalar
tnSysLinuxSmsUserPassword = _TnSysLinuxSmsUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 11),
    _TnSysLinuxSmsUserPassword_Type()
)
tnSysLinuxSmsUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxSmsUserPassword.setStatus("current")


class _TnSysLinuxSmsPasswordStatus_Type(TruthValue):
    """Custom type tnSysLinuxSmsPasswordStatus based on TruthValue"""
    defaultValue = 2


_TnSysLinuxSmsPasswordStatus_Type.__name__ = "TruthValue"
_TnSysLinuxSmsPasswordStatus_Object = MibScalar
tnSysLinuxSmsPasswordStatus = _TnSysLinuxSmsPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 12),
    _TnSysLinuxSmsPasswordStatus_Type()
)
tnSysLinuxSmsPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxSmsPasswordStatus.setStatus("current")


class _TnSysLinuxSmsUserStatus_Type(TruthValue):
    """Custom type tnSysLinuxSmsUserStatus based on TruthValue"""
    defaultValue = 1


_TnSysLinuxSmsUserStatus_Type.__name__ = "TruthValue"
_TnSysLinuxSmsUserStatus_Object = MibScalar
tnSysLinuxSmsUserStatus = _TnSysLinuxSmsUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 13),
    _TnSysLinuxSmsUserStatus_Type()
)
tnSysLinuxSmsUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxSmsUserStatus.setStatus("current")


class _TnSysLinuxRootUserLocalStatus_Type(TruthValue):
    """Custom type tnSysLinuxRootUserLocalStatus based on TruthValue"""
    defaultValue = 1


_TnSysLinuxRootUserLocalStatus_Type.__name__ = "TruthValue"
_TnSysLinuxRootUserLocalStatus_Object = MibScalar
tnSysLinuxRootUserLocalStatus = _TnSysLinuxRootUserLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 14),
    _TnSysLinuxRootUserLocalStatus_Type()
)
tnSysLinuxRootUserLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserLocalStatus.setStatus("current")


class _TnSysLinuxSecurityCommit_Type(TruthValue):
    """Custom type tnSysLinuxSecurityCommit based on TruthValue"""
    defaultValue = 1


_TnSysLinuxSecurityCommit_Type.__name__ = "TruthValue"
_TnSysLinuxSecurityCommit_Object = MibScalar
tnSysLinuxSecurityCommit = _TnSysLinuxSecurityCommit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 15),
    _TnSysLinuxSecurityCommit_Type()
)
tnSysLinuxSecurityCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxSecurityCommit.setStatus("current")


class _TnSysLinuxRootUserPort_Type(Integer32):
    """Custom type tnSysLinuxRootUserPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port5122", 1),
          ("port22", 2))
    )


_TnSysLinuxRootUserPort_Type.__name__ = "Integer32"
_TnSysLinuxRootUserPort_Object = MibScalar
tnSysLinuxRootUserPort = _TnSysLinuxRootUserPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 16),
    _TnSysLinuxRootUserPort_Type()
)
tnSysLinuxRootUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserPort.setStatus("current")
_TnSysIpAclIpv6SysDefault_ObjectIdentity = ObjectIdentity
tnSysIpAclIpv6SysDefault = _TnSysIpAclIpv6SysDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29)
)


class _TnSysIpAclIpv6RxAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6RxAction based on Integer32"""
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
        *(("pass", 1),
          ("block", 2),
          ("dropAndlog", 3))
    )


_TnSysIpAclIpv6RxAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6RxAction_Object = MibScalar
tnSysIpAclIpv6RxAction = _TnSysIpAclIpv6RxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 1),
    _TnSysIpAclIpv6RxAction_Type()
)
tnSysIpAclIpv6RxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6RxAction.setStatus("current")


class _TnSysIpAclIpv6TxAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6TxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclIpv6TxAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6TxAction_Object = MibScalar
tnSysIpAclIpv6TxAction = _TnSysIpAclIpv6TxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 2),
    _TnSysIpAclIpv6TxAction_Type()
)
tnSysIpAclIpv6TxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6TxAction.setStatus("current")


class _TnSysIpAclIpv6SnmpCfgEnable_Type(TruthValue):
    """Custom type tnSysIpAclIpv6SnmpCfgEnable based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6SnmpCfgEnable_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6SnmpCfgEnable_Object = MibScalar
tnSysIpAclIpv6SnmpCfgEnable = _TnSysIpAclIpv6SnmpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 3),
    _TnSysIpAclIpv6SnmpCfgEnable_Type()
)
tnSysIpAclIpv6SnmpCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6SnmpCfgEnable.setStatus("current")


class _TnSysIpAclIpv6CfgRestoreToDefault_Type(TruthValue):
    """Custom type tnSysIpAclIpv6CfgRestoreToDefault based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6CfgRestoreToDefault_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6CfgRestoreToDefault_Object = MibScalar
tnSysIpAclIpv6CfgRestoreToDefault = _TnSysIpAclIpv6CfgRestoreToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 4),
    _TnSysIpAclIpv6CfgRestoreToDefault_Type()
)
tnSysIpAclIpv6CfgRestoreToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6CfgRestoreToDefault.setStatus("current")


class _TnSysIpAclIPv6ClearCounter_Type(TruthValue):
    """Custom type tnSysIpAclIPv6ClearCounter based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIPv6ClearCounter_Type.__name__ = "TruthValue"
_TnSysIpAclIPv6ClearCounter_Object = MibScalar
tnSysIpAclIPv6ClearCounter = _TnSysIpAclIPv6ClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 5),
    _TnSysIpAclIPv6ClearCounter_Type()
)
tnSysIpAclIPv6ClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIPv6ClearCounter.setStatus("current")
_TnSysFileInitialization_ObjectIdentity = ObjectIdentity
tnSysFileInitialization = _TnSysFileInitialization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30)
)


class _TnSysFileInitializationRoot_Type(SnmpAdminString):
    """Custom type tnSysFileInitializationRoot based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysFileInitializationRoot_Type.__name__ = "SnmpAdminString"
_TnSysFileInitializationRoot_Object = MibScalar
tnSysFileInitializationRoot = _TnSysFileInitializationRoot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 1),
    _TnSysFileInitializationRoot_Type()
)
tnSysFileInitializationRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationRoot.setStatus("current")


class _TnSysFileInitializationUserId_Type(SnmpAdminString):
    """Custom type tnSysFileInitializationUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysFileInitializationUserId_Type.__name__ = "SnmpAdminString"
_TnSysFileInitializationUserId_Object = MibScalar
tnSysFileInitializationUserId = _TnSysFileInitializationUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 2),
    _TnSysFileInitializationUserId_Type()
)
tnSysFileInitializationUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationUserId.setStatus("current")


class _TnSysFileInitializationPassword_Type(SnmpAdminString):
    """Custom type tnSysFileInitializationPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysFileInitializationPassword_Type.__name__ = "SnmpAdminString"
_TnSysFileInitializationPassword_Object = MibScalar
tnSysFileInitializationPassword = _TnSysFileInitializationPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 3),
    _TnSysFileInitializationPassword_Type()
)
tnSysFileInitializationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationPassword.setStatus("current")


class _TnSysFileInitializationFilename_Type(SnmpAdminString):
    """Custom type tnSysFileInitializationFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysFileInitializationFilename_Type.__name__ = "SnmpAdminString"
_TnSysFileInitializationFilename_Object = MibScalar
tnSysFileInitializationFilename = _TnSysFileInitializationFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 4),
    _TnSysFileInitializationFilename_Type()
)
tnSysFileInitializationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationFilename.setStatus("current")


class _TnSysFileInitializationInetAddressType_Type(InetAddressType):
    """Custom type tnSysFileInitializationInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysFileInitializationInetAddressType_Type.__name__ = "InetAddressType"
_TnSysFileInitializationInetAddressType_Object = MibScalar
tnSysFileInitializationInetAddressType = _TnSysFileInitializationInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 5),
    _TnSysFileInitializationInetAddressType_Type()
)
tnSysFileInitializationInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationInetAddressType.setStatus("current")


class _TnSysFileInitializationInetAddress_Type(InetAddress):
    """Custom type tnSysFileInitializationInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysFileInitializationInetAddress_Type.__name__ = "InetAddress"
_TnSysFileInitializationInetAddress_Object = MibScalar
tnSysFileInitializationInetAddress = _TnSysFileInitializationInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 30, 6),
    _TnSysFileInitializationInetAddress_Type()
)
tnSysFileInitializationInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFileInitializationInetAddress.setStatus("current")
_TnSysBtInterface_ObjectIdentity = ObjectIdentity
tnSysBtInterface = _TnSysBtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31)
)


class _TnSysBtInterfaceDescription_Type(SnmpAdminString):
    """Custom type tnSysBtInterfaceDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysBtInterfaceDescription_Type.__name__ = "SnmpAdminString"
_TnSysBtInterfaceDescription_Object = MibScalar
tnSysBtInterfaceDescription = _TnSysBtInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 1),
    _TnSysBtInterfaceDescription_Type()
)
tnSysBtInterfaceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceDescription.setStatus("current")


class _TnSysBtInterfaceIpAddr_Type(IpAddress):
    """Custom type tnSysBtInterfaceIpAddr based on IpAddress"""
    defaultHexValue = "AC100201"


_TnSysBtInterfaceIpAddr_Type.__name__ = "IpAddress"
_TnSysBtInterfaceIpAddr_Object = MibScalar
tnSysBtInterfaceIpAddr = _TnSysBtInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 2),
    _TnSysBtInterfaceIpAddr_Type()
)
tnSysBtInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceIpAddr.setStatus("current")


class _TnSysBtInterfaceIpSubMask_Type(IpAddress):
    """Custom type tnSysBtInterfaceIpSubMask based on IpAddress"""
    defaultHexValue = "FFFFFF00"


_TnSysBtInterfaceIpSubMask_Type.__name__ = "IpAddress"
_TnSysBtInterfaceIpSubMask_Object = MibScalar
tnSysBtInterfaceIpSubMask = _TnSysBtInterfaceIpSubMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 3),
    _TnSysBtInterfaceIpSubMask_Type()
)
tnSysBtInterfaceIpSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceIpSubMask.setStatus("current")


class _TnSysBtInterfaceAdminState_Type(TropicAdminStateType):
    """Custom type tnSysBtInterfaceAdminState based on TropicAdminStateType"""
    defaultValue = 1


_TnSysBtInterfaceAdminState_Type.__name__ = "TropicAdminStateType"
_TnSysBtInterfaceAdminState_Object = MibScalar
tnSysBtInterfaceAdminState = _TnSysBtInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 4),
    _TnSysBtInterfaceAdminState_Type()
)
tnSysBtInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceAdminState.setStatus("current")


class _TnSysBtInterfaceLinkIntegrityStatus_Type(TropicOperationalStateType):
    """Custom type tnSysBtInterfaceLinkIntegrityStatus based on TropicOperationalStateType"""
    defaultValue = 2


_TnSysBtInterfaceLinkIntegrityStatus_Type.__name__ = "TropicOperationalStateType"
_TnSysBtInterfaceLinkIntegrityStatus_Object = MibScalar
tnSysBtInterfaceLinkIntegrityStatus = _TnSysBtInterfaceLinkIntegrityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 5),
    _TnSysBtInterfaceLinkIntegrityStatus_Type()
)
tnSysBtInterfaceLinkIntegrityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBtInterfaceLinkIntegrityStatus.setStatus("current")


class _TnSysBtInterfaceDHCPServer_Type(Integer32):
    """Custom type tnSysBtInterfaceDHCPServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnSysBtInterfaceDHCPServer_Type.__name__ = "Integer32"
_TnSysBtInterfaceDHCPServer_Object = MibScalar
tnSysBtInterfaceDHCPServer = _TnSysBtInterfaceDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 6),
    _TnSysBtInterfaceDHCPServer_Type()
)
tnSysBtInterfaceDHCPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceDHCPServer.setStatus("current")


class _TnSysBtInterfaceDHCPRange_Type(Unsigned32):
    """Custom type tnSysBtInterfaceDHCPRange based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnSysBtInterfaceDHCPRange_Type.__name__ = "Unsigned32"
_TnSysBtInterfaceDHCPRange_Object = MibScalar
tnSysBtInterfaceDHCPRange = _TnSysBtInterfaceDHCPRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 7),
    _TnSysBtInterfaceDHCPRange_Type()
)
tnSysBtInterfaceDHCPRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBtInterfaceDHCPRange.setStatus("current")


class _TnSysBtInterfaceNodeSerialNum_Type(SnmpAdminString):
    """Custom type tnSysBtInterfaceNodeSerialNum based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnSysBtInterfaceNodeSerialNum_Type.__name__ = "SnmpAdminString"
_TnSysBtInterfaceNodeSerialNum_Object = MibScalar
tnSysBtInterfaceNodeSerialNum = _TnSysBtInterfaceNodeSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 8),
    _TnSysBtInterfaceNodeSerialNum_Type()
)
tnSysBtInterfaceNodeSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBtInterfaceNodeSerialNum.setStatus("current")
_TnSysBtInterfaceMacAddress_Type = MacAddress
_TnSysBtInterfaceMacAddress_Object = MibScalar
tnSysBtInterfaceMacAddress = _TnSysBtInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 31, 9),
    _TnSysBtInterfaceMacAddress_Type()
)
tnSysBtInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBtInterfaceMacAddress.setStatus("current")
_TnSysLicenseMgr_ObjectIdentity = ObjectIdentity
tnSysLicenseMgr = _TnSysLicenseMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32)
)


class _TnSysLicenseMgrKeepAliveTimer_Type(Unsigned32):
    """Custom type tnSysLicenseMgrKeepAliveTimer based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 86400),
    )


_TnSysLicenseMgrKeepAliveTimer_Type.__name__ = "Unsigned32"
_TnSysLicenseMgrKeepAliveTimer_Object = MibScalar
tnSysLicenseMgrKeepAliveTimer = _TnSysLicenseMgrKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 1),
    _TnSysLicenseMgrKeepAliveTimer_Type()
)
tnSysLicenseMgrKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrKeepAliveTimer.setStatus("current")


class _TnSysLicenseMgrPrimaryServerIp_Type(IpAddress):
    """Custom type tnSysLicenseMgrPrimaryServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysLicenseMgrPrimaryServerIp_Type.__name__ = "IpAddress"
_TnSysLicenseMgrPrimaryServerIp_Object = MibScalar
tnSysLicenseMgrPrimaryServerIp = _TnSysLicenseMgrPrimaryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 2),
    _TnSysLicenseMgrPrimaryServerIp_Type()
)
tnSysLicenseMgrPrimaryServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrPrimaryServerIp.setStatus("current")


class _TnSysLicenseMgrPrimaryServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysLicenseMgrPrimaryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysLicenseMgrPrimaryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysLicenseMgrPrimaryServerInetAddressType_Object = MibScalar
tnSysLicenseMgrPrimaryServerInetAddressType = _TnSysLicenseMgrPrimaryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 3),
    _TnSysLicenseMgrPrimaryServerInetAddressType_Type()
)
tnSysLicenseMgrPrimaryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrPrimaryServerInetAddressType.setStatus("current")


class _TnSysLicenseMgrPrimaryServerInetAddress_Type(InetAddress):
    """Custom type tnSysLicenseMgrPrimaryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysLicenseMgrPrimaryServerInetAddress_Type.__name__ = "InetAddress"
_TnSysLicenseMgrPrimaryServerInetAddress_Object = MibScalar
tnSysLicenseMgrPrimaryServerInetAddress = _TnSysLicenseMgrPrimaryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 4),
    _TnSysLicenseMgrPrimaryServerInetAddress_Type()
)
tnSysLicenseMgrPrimaryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrPrimaryServerInetAddress.setStatus("current")


class _TnSysLicenseMgrSecondaryServerIp_Type(IpAddress):
    """Custom type tnSysLicenseMgrSecondaryServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysLicenseMgrSecondaryServerIp_Type.__name__ = "IpAddress"
_TnSysLicenseMgrSecondaryServerIp_Object = MibScalar
tnSysLicenseMgrSecondaryServerIp = _TnSysLicenseMgrSecondaryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 5),
    _TnSysLicenseMgrSecondaryServerIp_Type()
)
tnSysLicenseMgrSecondaryServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrSecondaryServerIp.setStatus("current")


class _TnSysLicenseMgrSecondaryServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysLicenseMgrSecondaryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysLicenseMgrSecondaryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysLicenseMgrSecondaryServerInetAddressType_Object = MibScalar
tnSysLicenseMgrSecondaryServerInetAddressType = _TnSysLicenseMgrSecondaryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 6),
    _TnSysLicenseMgrSecondaryServerInetAddressType_Type()
)
tnSysLicenseMgrSecondaryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrSecondaryServerInetAddressType.setStatus("current")


class _TnSysLicenseMgrSecondaryServerInetAddress_Type(InetAddress):
    """Custom type tnSysLicenseMgrSecondaryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysLicenseMgrSecondaryServerInetAddress_Type.__name__ = "InetAddress"
_TnSysLicenseMgrSecondaryServerInetAddress_Object = MibScalar
tnSysLicenseMgrSecondaryServerInetAddress = _TnSysLicenseMgrSecondaryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 7),
    _TnSysLicenseMgrSecondaryServerInetAddress_Type()
)
tnSysLicenseMgrSecondaryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrSecondaryServerInetAddress.setStatus("current")


class _TnSysLicenseMgrPrimaryServerStatus_Type(Integer32):
    """Custom type tnSysLicenseMgrPrimaryServerStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notConnected", 4))
    )


_TnSysLicenseMgrPrimaryServerStatus_Type.__name__ = "Integer32"
_TnSysLicenseMgrPrimaryServerStatus_Object = MibScalar
tnSysLicenseMgrPrimaryServerStatus = _TnSysLicenseMgrPrimaryServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 8),
    _TnSysLicenseMgrPrimaryServerStatus_Type()
)
tnSysLicenseMgrPrimaryServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrPrimaryServerStatus.setStatus("current")


class _TnSysLicenseMgrSecondaryServerStatus_Type(Integer32):
    """Custom type tnSysLicenseMgrSecondaryServerStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notConnected", 4))
    )


_TnSysLicenseMgrSecondaryServerStatus_Type.__name__ = "Integer32"
_TnSysLicenseMgrSecondaryServerStatus_Object = MibScalar
tnSysLicenseMgrSecondaryServerStatus = _TnSysLicenseMgrSecondaryServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 9),
    _TnSysLicenseMgrSecondaryServerStatus_Type()
)
tnSysLicenseMgrSecondaryServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrSecondaryServerStatus.setStatus("current")


class _TnSysLicenseMgrExpiration_Type(SnmpAdminString):
    """Custom type tnSysLicenseMgrExpiration based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysLicenseMgrExpiration_Type.__name__ = "SnmpAdminString"
_TnSysLicenseMgrExpiration_Object = MibScalar
tnSysLicenseMgrExpiration = _TnSysLicenseMgrExpiration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 10),
    _TnSysLicenseMgrExpiration_Type()
)
tnSysLicenseMgrExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseMgrExpiration.setStatus("current")


class _TnSysLicenseMgrTimeOut_Type(Unsigned32):
    """Custom type tnSysLicenseMgrTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnSysLicenseMgrTimeOut_Type.__name__ = "Unsigned32"
_TnSysLicenseMgrTimeOut_Object = MibScalar
tnSysLicenseMgrTimeOut = _TnSysLicenseMgrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 11),
    _TnSysLicenseMgrTimeOut_Type()
)
tnSysLicenseMgrTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrTimeOut.setStatus("current")


class _TnSysLicenseMgrRetries_Type(Unsigned32):
    """Custom type tnSysLicenseMgrRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnSysLicenseMgrRetries_Type.__name__ = "Unsigned32"
_TnSysLicenseMgrRetries_Object = MibScalar
tnSysLicenseMgrRetries = _TnSysLicenseMgrRetries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 12),
    _TnSysLicenseMgrRetries_Type()
)
tnSysLicenseMgrRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseMgrRetries.setStatus("current")


class _TnSysLicenseMgrLastRefresh_Type(SnmpAdminString):
    """Custom type tnSysLicenseMgrLastRefresh based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseMgrLastRefresh_Type.__name__ = "SnmpAdminString"
_TnSysLicenseMgrLastRefresh_Object = MibScalar
tnSysLicenseMgrLastRefresh = _TnSysLicenseMgrLastRefresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 13),
    _TnSysLicenseMgrLastRefresh_Type()
)
tnSysLicenseMgrLastRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseMgrLastRefresh.setStatus("current")


class _TnSysLicenseMgrCertStatus_Type(Integer32):
    """Custom type tnSysLicenseMgrCertStatus based on Integer32"""
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
        *(("unknown", 1),
          ("success", 2),
          ("failure", 3))
    )


_TnSysLicenseMgrCertStatus_Type.__name__ = "Integer32"
_TnSysLicenseMgrCertStatus_Object = MibScalar
tnSysLicenseMgrCertStatus = _TnSysLicenseMgrCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 14),
    _TnSysLicenseMgrCertStatus_Type()
)
tnSysLicenseMgrCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseMgrCertStatus.setStatus("current")
_TnSysLicenseMgrNextRefreshTime_Type = Integer32
_TnSysLicenseMgrNextRefreshTime_Object = MibScalar
tnSysLicenseMgrNextRefreshTime = _TnSysLicenseMgrNextRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 32, 15),
    _TnSysLicenseMgrNextRefreshTime_Type()
)
tnSysLicenseMgrNextRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseMgrNextRefreshTime.setStatus("current")
_TnLicenseObjs_ObjectIdentity = ObjectIdentity
tnLicenseObjs = _TnLicenseObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33)
)
_TnLicenseEntityTable_Object = MibTable
tnLicenseEntityTable = _TnLicenseEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1)
)
if mibBuilder.loadTexts:
    tnLicenseEntityTable.setStatus("current")
_TnLicenseEntityEntry_Object = MibTableRow
tnLicenseEntityEntry = _TnLicenseEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1)
)
tnLicenseEntityEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnLicenseEntity"),
)
if mibBuilder.loadTexts:
    tnLicenseEntityEntry.setStatus("current")
_TnLicenseEntity_Type = Unsigned32
_TnLicenseEntity_Object = MibTableColumn
tnLicenseEntity = _TnLicenseEntity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1, 1),
    _TnLicenseEntity_Type()
)
tnLicenseEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLicenseEntity.setStatus("current")


class _TnLicenseEntityRefreshSet_Type(TnCommand):
    """Custom type tnLicenseEntityRefreshSet based on TnCommand"""
    defaultValue = 1


_TnLicenseEntityRefreshSet_Type.__name__ = "TnCommand"
_TnLicenseEntityRefreshSet_Object = MibTableColumn
tnLicenseEntityRefreshSet = _TnLicenseEntityRefreshSet_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1, 2),
    _TnLicenseEntityRefreshSet_Type()
)
tnLicenseEntityRefreshSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnLicenseEntityRefreshSet.setStatus("current")
_TnLicenseEntityNumberInUse_Type = Unsigned32
_TnLicenseEntityNumberInUse_Object = MibTableColumn
tnLicenseEntityNumberInUse = _TnLicenseEntityNumberInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1, 3),
    _TnLicenseEntityNumberInUse_Type()
)
tnLicenseEntityNumberInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLicenseEntityNumberInUse.setStatus("current")
_TnLicenseEntityNumberExceedAvail_Type = Unsigned32
_TnLicenseEntityNumberExceedAvail_Object = MibTableColumn
tnLicenseEntityNumberExceedAvail = _TnLicenseEntityNumberExceedAvail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1, 4),
    _TnLicenseEntityNumberExceedAvail_Type()
)
tnLicenseEntityNumberExceedAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLicenseEntityNumberExceedAvail.setStatus("current")
_TnLicenseEntityEntitlementNeeded_Type = Unsigned32
_TnLicenseEntityEntitlementNeeded_Object = MibTableColumn
tnLicenseEntityEntitlementNeeded = _TnLicenseEntityEntitlementNeeded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 1, 1, 5),
    _TnLicenseEntityEntitlementNeeded_Type()
)
tnLicenseEntityEntitlementNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLicenseEntityEntitlementNeeded.setStatus("current")
_TnLicenseEntitlementTable_Object = MibTable
tnLicenseEntitlementTable = _TnLicenseEntitlementTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 2)
)
if mibBuilder.loadTexts:
    tnLicenseEntitlementTable.setStatus("current")
_TnLicenseEntitlementEntry_Object = MibTableRow
tnLicenseEntitlementEntry = _TnLicenseEntitlementEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 2, 1)
)
tnLicenseEntitlementEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnLicenseEntitlementCategoryID"),
    (0, "TROPIC-SYSTEM-MIB", "tnLicenseEntitlementEntries"),
)
if mibBuilder.loadTexts:
    tnLicenseEntitlementEntry.setStatus("current")
_TnLicenseEntitlementCategoryID_Type = Unsigned32
_TnLicenseEntitlementCategoryID_Object = MibTableColumn
tnLicenseEntitlementCategoryID = _TnLicenseEntitlementCategoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 2, 1, 1),
    _TnLicenseEntitlementCategoryID_Type()
)
tnLicenseEntitlementCategoryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLicenseEntitlementCategoryID.setStatus("current")
_TnLicenseEntitlementEntries_Type = Unsigned32
_TnLicenseEntitlementEntries_Object = MibTableColumn
tnLicenseEntitlementEntries = _TnLicenseEntitlementEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 2, 1, 2),
    _TnLicenseEntitlementEntries_Type()
)
tnLicenseEntitlementEntries.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLicenseEntitlementEntries.setStatus("current")


class _TnLicenseEntitlementDetails_Type(SnmpAdminString):
    """Custom type tnLicenseEntitlementDetails based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_TnLicenseEntitlementDetails_Type.__name__ = "SnmpAdminString"
_TnLicenseEntitlementDetails_Object = MibTableColumn
tnLicenseEntitlementDetails = _TnLicenseEntitlementDetails_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 33, 2, 1, 3),
    _TnLicenseEntitlementDetails_Type()
)
tnLicenseEntitlementDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLicenseEntitlementDetails.setStatus("current")
_TnSysKeyStore_ObjectIdentity = ObjectIdentity
tnSysKeyStore = _TnSysKeyStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34)
)
_TnSysKeyStoreServiceTable_Object = MibTable
tnSysKeyStoreServiceTable = _TnSysKeyStoreServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1)
)
if mibBuilder.loadTexts:
    tnSysKeyStoreServiceTable.setStatus("current")
_TnSysKeyStoreServiceEntry_Object = MibTableRow
tnSysKeyStoreServiceEntry = _TnSysKeyStoreServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1)
)
tnSysKeyStoreServiceEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysKeyStoreNameIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysKeyStoreTypeIndex"),
)
if mibBuilder.loadTexts:
    tnSysKeyStoreServiceEntry.setStatus("current")


class _TnSysKeyStoreNameIndex_Type(Integer32):
    """Custom type tnSysKeyStoreNameIndex based on Integer32"""
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
        *(("invalid", 1),
          ("ztp", 2),
          ("internecomm", 3),
          ("system", 4))
    )


_TnSysKeyStoreNameIndex_Type.__name__ = "Integer32"
_TnSysKeyStoreNameIndex_Object = MibTableColumn
tnSysKeyStoreNameIndex = _TnSysKeyStoreNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 1),
    _TnSysKeyStoreNameIndex_Type()
)
tnSysKeyStoreNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysKeyStoreNameIndex.setStatus("current")


class _TnSysKeyStoreTypeIndex_Type(Integer32):
    """Custom type tnSysKeyStoreTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("trustAnchor", 2),
          ("privateKey", 3))
    )


_TnSysKeyStoreTypeIndex_Type.__name__ = "Integer32"
_TnSysKeyStoreTypeIndex_Object = MibTableColumn
tnSysKeyStoreTypeIndex = _TnSysKeyStoreTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 2),
    _TnSysKeyStoreTypeIndex_Type()
)
tnSysKeyStoreTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysKeyStoreTypeIndex.setStatus("current")


class _TnSysKeyStoreTransServerCommand_Type(Integer32):
    """Custom type tnSysKeyStoreTransServerCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("upload", 2),
          ("download", 3),
          ("install", 4),
          ("restoreToDefault", 5),
          ("downloadThenInstall", 6),
          ("clear", 7))
    )


_TnSysKeyStoreTransServerCommand_Type.__name__ = "Integer32"
_TnSysKeyStoreTransServerCommand_Object = MibTableColumn
tnSysKeyStoreTransServerCommand = _TnSysKeyStoreTransServerCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 3),
    _TnSysKeyStoreTransServerCommand_Type()
)
tnSysKeyStoreTransServerCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerCommand.setStatus("current")


class _TnSysKeyStoreTransServerProtocol_Type(Integer32):
    """Custom type tnSysKeyStoreTransServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("https", 2),
          ("sftp", 3))
    )


_TnSysKeyStoreTransServerProtocol_Type.__name__ = "Integer32"
_TnSysKeyStoreTransServerProtocol_Object = MibTableColumn
tnSysKeyStoreTransServerProtocol = _TnSysKeyStoreTransServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 4),
    _TnSysKeyStoreTransServerProtocol_Type()
)
tnSysKeyStoreTransServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerProtocol.setStatus("current")


class _TnSysKeyStoreTransServerHost_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreTransServerHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysKeyStoreTransServerHost_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreTransServerHost_Object = MibTableColumn
tnSysKeyStoreTransServerHost = _TnSysKeyStoreTransServerHost_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 5),
    _TnSysKeyStoreTransServerHost_Type()
)
tnSysKeyStoreTransServerHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerHost.setStatus("current")
_TnSysKeyStoreTransServerPort_Type = Unsigned32
_TnSysKeyStoreTransServerPort_Object = MibTableColumn
tnSysKeyStoreTransServerPort = _TnSysKeyStoreTransServerPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 6),
    _TnSysKeyStoreTransServerPort_Type()
)
tnSysKeyStoreTransServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerPort.setStatus("current")


class _TnSysKeyStoreTransServerLocation_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreTransServerLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysKeyStoreTransServerLocation_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreTransServerLocation_Object = MibTableColumn
tnSysKeyStoreTransServerLocation = _TnSysKeyStoreTransServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 7),
    _TnSysKeyStoreTransServerLocation_Type()
)
tnSysKeyStoreTransServerLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerLocation.setStatus("current")


class _TnSysKeyStoreTransServerUserId_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreTransServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysKeyStoreTransServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreTransServerUserId_Object = MibTableColumn
tnSysKeyStoreTransServerUserId = _TnSysKeyStoreTransServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 8),
    _TnSysKeyStoreTransServerUserId_Type()
)
tnSysKeyStoreTransServerUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerUserId.setStatus("current")


class _TnSysKeyStoreTransServerPassword_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreTransServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TnSysKeyStoreTransServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreTransServerPassword_Object = MibTableColumn
tnSysKeyStoreTransServerPassword = _TnSysKeyStoreTransServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 9),
    _TnSysKeyStoreTransServerPassword_Type()
)
tnSysKeyStoreTransServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerPassword.setStatus("current")
_TnSysKeyStoreTransServerInetAddressType_Type = InetAddressType
_TnSysKeyStoreTransServerInetAddressType_Object = MibTableColumn
tnSysKeyStoreTransServerInetAddressType = _TnSysKeyStoreTransServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 10),
    _TnSysKeyStoreTransServerInetAddressType_Type()
)
tnSysKeyStoreTransServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerInetAddressType.setStatus("current")
_TnSysKeyStoreTransServerInetAddress_Type = InetAddress
_TnSysKeyStoreTransServerInetAddress_Object = MibTableColumn
tnSysKeyStoreTransServerInetAddress = _TnSysKeyStoreTransServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 11),
    _TnSysKeyStoreTransServerInetAddress_Type()
)
tnSysKeyStoreTransServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerInetAddress.setStatus("current")


class _TnSysKeyStoreServiceStatus_Type(Integer32):
    """Custom type tnSysKeyStoreServiceStatus based on Integer32"""
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
        *(("none", 1),
          ("installed", 2),
          ("downloaded", 3),
          ("in-progress", 4),
          ("transferfail", 5),
          ("formaterror", 6))
    )


_TnSysKeyStoreServiceStatus_Type.__name__ = "Integer32"
_TnSysKeyStoreServiceStatus_Object = MibTableColumn
tnSysKeyStoreServiceStatus = _TnSysKeyStoreServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 12),
    _TnSysKeyStoreServiceStatus_Type()
)
tnSysKeyStoreServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreServiceStatus.setStatus("current")


class _TnSysKeyStoreServerLastTransferTime_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreServerLastTransferTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysKeyStoreServerLastTransferTime_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreServerLastTransferTime_Object = MibTableColumn
tnSysKeyStoreServerLastTransferTime = _TnSysKeyStoreServerLastTransferTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 13),
    _TnSysKeyStoreServerLastTransferTime_Type()
)
tnSysKeyStoreServerLastTransferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreServerLastTransferTime.setStatus("current")


class _TnSysKeyStoreTransServerURI_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreTransServerURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_TnSysKeyStoreTransServerURI_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreTransServerURI_Object = MibTableColumn
tnSysKeyStoreTransServerURI = _TnSysKeyStoreTransServerURI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 1, 1, 14),
    _TnSysKeyStoreTransServerURI_Type()
)
tnSysKeyStoreTransServerURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysKeyStoreTransServerURI.setStatus("current")
_TnSysKeyStoreCertInfoTable_Object = MibTable
tnSysKeyStoreCertInfoTable = _TnSysKeyStoreCertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2)
)
if mibBuilder.loadTexts:
    tnSysKeyStoreCertInfoTable.setStatus("current")
_TnSysKeyStoreCertInfoEntry_Object = MibTableRow
tnSysKeyStoreCertInfoEntry = _TnSysKeyStoreCertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1)
)
tnSysKeyStoreCertInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertRepositoryIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertIndex"),
)
if mibBuilder.loadTexts:
    tnSysKeyStoreCertInfoEntry.setStatus("current")


class _TnSysKeyStoreCertRepositoryIndex_Type(Integer32):
    """Custom type tnSysKeyStoreCertRepositoryIndex based on Integer32"""
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
        *(("invalid", 1),
          ("trustAnchorInstalledOfZtp", 2),
          ("trustAnchorDownLoadedOfZtp", 3),
          ("trustAnchorInstalledOfSystem", 4),
          ("trustAnchorDownLoadedOfSystem", 5))
    )


_TnSysKeyStoreCertRepositoryIndex_Type.__name__ = "Integer32"
_TnSysKeyStoreCertRepositoryIndex_Object = MibTableColumn
tnSysKeyStoreCertRepositoryIndex = _TnSysKeyStoreCertRepositoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 1),
    _TnSysKeyStoreCertRepositoryIndex_Type()
)
tnSysKeyStoreCertRepositoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertRepositoryIndex.setStatus("current")
_TnSysKeyStoreCertIndex_Type = Unsigned32
_TnSysKeyStoreCertIndex_Object = MibTableColumn
tnSysKeyStoreCertIndex = _TnSysKeyStoreCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 2),
    _TnSysKeyStoreCertIndex_Type()
)
tnSysKeyStoreCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertIndex.setStatus("current")


class _TnSysKeyStoreCertVersion_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnSysKeyStoreCertVersion_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertVersion_Object = MibTableColumn
tnSysKeyStoreCertVersion = _TnSysKeyStoreCertVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 3),
    _TnSysKeyStoreCertVersion_Type()
)
tnSysKeyStoreCertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertVersion.setStatus("current")


class _TnSysKeyStoreCertSerialNumber_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnSysKeyStoreCertSerialNumber_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSerialNumber_Object = MibTableColumn
tnSysKeyStoreCertSerialNumber = _TnSysKeyStoreCertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 4),
    _TnSysKeyStoreCertSerialNumber_Type()
)
tnSysKeyStoreCertSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSerialNumber.setStatus("current")


class _TnSysKeyStoreCertSignatureAlgorithm_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSignatureAlgorithm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnSysKeyStoreCertSignatureAlgorithm_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSignatureAlgorithm_Object = MibTableColumn
tnSysKeyStoreCertSignatureAlgorithm = _TnSysKeyStoreCertSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 5),
    _TnSysKeyStoreCertSignatureAlgorithm_Type()
)
tnSysKeyStoreCertSignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSignatureAlgorithm.setStatus("current")


class _TnSysKeyStoreCertIssuer_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertIssuer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_TnSysKeyStoreCertIssuer_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertIssuer_Object = MibTableColumn
tnSysKeyStoreCertIssuer = _TnSysKeyStoreCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 6),
    _TnSysKeyStoreCertIssuer_Type()
)
tnSysKeyStoreCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertIssuer.setStatus("current")


class _TnSysKeyStoreCertValidity_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertValidity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysKeyStoreCertValidity_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertValidity_Object = MibTableColumn
tnSysKeyStoreCertValidity = _TnSysKeyStoreCertValidity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 7),
    _TnSysKeyStoreCertValidity_Type()
)
tnSysKeyStoreCertValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertValidity.setStatus("current")


class _TnSysKeyStoreCertSubject_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSubject based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_TnSysKeyStoreCertSubject_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSubject_Object = MibTableColumn
tnSysKeyStoreCertSubject = _TnSysKeyStoreCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 8),
    _TnSysKeyStoreCertSubject_Type()
)
tnSysKeyStoreCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSubject.setStatus("current")


class _TnSysKeyStoreCertSubjectPublicKeyInfo_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSubjectPublicKeyInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TnSysKeyStoreCertSubjectPublicKeyInfo_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSubjectPublicKeyInfo_Object = MibTableColumn
tnSysKeyStoreCertSubjectPublicKeyInfo = _TnSysKeyStoreCertSubjectPublicKeyInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 9),
    _TnSysKeyStoreCertSubjectPublicKeyInfo_Type()
)
tnSysKeyStoreCertSubjectPublicKeyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSubjectPublicKeyInfo.setStatus("current")


class _TnSysKeyStoreCertKeyUsage_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertKeyUsage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnSysKeyStoreCertKeyUsage_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertKeyUsage_Object = MibTableColumn
tnSysKeyStoreCertKeyUsage = _TnSysKeyStoreCertKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 10),
    _TnSysKeyStoreCertKeyUsage_Type()
)
tnSysKeyStoreCertKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertKeyUsage.setStatus("current")


class _TnSysKeyStoreCertSubjectAlternativeName_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSubjectAlternativeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnSysKeyStoreCertSubjectAlternativeName_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSubjectAlternativeName_Object = MibTableColumn
tnSysKeyStoreCertSubjectAlternativeName = _TnSysKeyStoreCertSubjectAlternativeName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 11),
    _TnSysKeyStoreCertSubjectAlternativeName_Type()
)
tnSysKeyStoreCertSubjectAlternativeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSubjectAlternativeName.setStatus("current")


class _TnSysKeyStoreCertExtendedKeyUsage_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertExtendedKeyUsage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnSysKeyStoreCertExtendedKeyUsage_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertExtendedKeyUsage_Object = MibTableColumn
tnSysKeyStoreCertExtendedKeyUsage = _TnSysKeyStoreCertExtendedKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 12),
    _TnSysKeyStoreCertExtendedKeyUsage_Type()
)
tnSysKeyStoreCertExtendedKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertExtendedKeyUsage.setStatus("current")


class _TnSysKeyStoreCertBasicConstraints_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertBasicConstraints based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnSysKeyStoreCertBasicConstraints_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertBasicConstraints_Object = MibTableColumn
tnSysKeyStoreCertBasicConstraints = _TnSysKeyStoreCertBasicConstraints_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 13),
    _TnSysKeyStoreCertBasicConstraints_Type()
)
tnSysKeyStoreCertBasicConstraints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertBasicConstraints.setStatus("current")


class _TnSysKeyStoreCertSHA256Fingerprint_Type(SnmpAdminString):
    """Custom type tnSysKeyStoreCertSHA256Fingerprint based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TnSysKeyStoreCertSHA256Fingerprint_Type.__name__ = "SnmpAdminString"
_TnSysKeyStoreCertSHA256Fingerprint_Object = MibTableColumn
tnSysKeyStoreCertSHA256Fingerprint = _TnSysKeyStoreCertSHA256Fingerprint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 34, 2, 1, 14),
    _TnSysKeyStoreCertSHA256Fingerprint_Type()
)
tnSysKeyStoreCertSHA256Fingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysKeyStoreCertSHA256Fingerprint.setStatus("current")
_TnSysBgp_ObjectIdentity = ObjectIdentity
tnSysBgp = _TnSysBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35)
)
_TnSysBgpPeerTable_Object = MibTable
tnSysBgpPeerTable = _TnSysBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1)
)
if mibBuilder.loadTexts:
    tnSysBgpPeerTable.setStatus("current")
_TnSysBgpPeerEntry_Object = MibTableRow
tnSysBgpPeerEntry = _TnSysBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1)
)
tnSysBgpPeerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysBgpPeerIndex"),
)
if mibBuilder.loadTexts:
    tnSysBgpPeerEntry.setStatus("current")
_TnSysBgpPeerIndex_Type = Unsigned32
_TnSysBgpPeerIndex_Object = MibTableColumn
tnSysBgpPeerIndex = _TnSysBgpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 1),
    _TnSysBgpPeerIndex_Type()
)
tnSysBgpPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysBgpPeerIndex.setStatus("current")
_TnSysBgpPeerRowStatus_Type = RowStatus
_TnSysBgpPeerRowStatus_Object = MibTableColumn
tnSysBgpPeerRowStatus = _TnSysBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 2),
    _TnSysBgpPeerRowStatus_Type()
)
tnSysBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerRowStatus.setStatus("current")


class _TnSysBgpPeerInetAddressType_Type(InetAddressType):
    """Custom type tnSysBgpPeerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysBgpPeerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysBgpPeerInetAddressType_Object = MibTableColumn
tnSysBgpPeerInetAddressType = _TnSysBgpPeerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 3),
    _TnSysBgpPeerInetAddressType_Type()
)
tnSysBgpPeerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerInetAddressType.setStatus("current")


class _TnSysBgpPeerIp_Type(IpAddress):
    """Custom type tnSysBgpPeerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysBgpPeerIp_Type.__name__ = "IpAddress"
_TnSysBgpPeerIp_Object = MibTableColumn
tnSysBgpPeerIp = _TnSysBgpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 4),
    _TnSysBgpPeerIp_Type()
)
tnSysBgpPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerIp.setStatus("current")


class _TnSysBgpPeerInetAddress_Type(InetAddress):
    """Custom type tnSysBgpPeerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysBgpPeerInetAddress_Type.__name__ = "InetAddress"
_TnSysBgpPeerInetAddress_Object = MibTableColumn
tnSysBgpPeerInetAddress = _TnSysBgpPeerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 5),
    _TnSysBgpPeerInetAddress_Type()
)
tnSysBgpPeerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerInetAddress.setStatus("current")
_TnSysBgpPeerRemoteASN_Type = Unsigned32
_TnSysBgpPeerRemoteASN_Object = MibTableColumn
tnSysBgpPeerRemoteASN = _TnSysBgpPeerRemoteASN_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 6),
    _TnSysBgpPeerRemoteASN_Type()
)
tnSysBgpPeerRemoteASN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerRemoteASN.setStatus("current")


class _TnSysBgpPeerSecurityKey_Type(SnmpAdminString):
    """Custom type tnSysBgpPeerSecurityKey based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnSysBgpPeerSecurityKey_Type.__name__ = "SnmpAdminString"
_TnSysBgpPeerSecurityKey_Object = MibTableColumn
tnSysBgpPeerSecurityKey = _TnSysBgpPeerSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 7),
    _TnSysBgpPeerSecurityKey_Type()
)
tnSysBgpPeerSecurityKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerSecurityKey.setStatus("current")


class _TnSysBgpPeerRouterId_Type(IpAddress):
    """Custom type tnSysBgpPeerRouterId based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysBgpPeerRouterId_Type.__name__ = "IpAddress"
_TnSysBgpPeerRouterId_Object = MibTableColumn
tnSysBgpPeerRouterId = _TnSysBgpPeerRouterId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 8),
    _TnSysBgpPeerRouterId_Type()
)
tnSysBgpPeerRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpPeerRouterId.setStatus("current")


class _TnSysBgpPeerStatus_Type(Integer32):
    """Custom type tnSysBgpPeerStatus based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("openSent", 4),
          ("openConfirm", 5),
          ("established", 6))
    )


_TnSysBgpPeerStatus_Type.__name__ = "Integer32"
_TnSysBgpPeerStatus_Object = MibTableColumn
tnSysBgpPeerStatus = _TnSysBgpPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 9),
    _TnSysBgpPeerStatus_Type()
)
tnSysBgpPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpPeerStatus.setStatus("current")
_TnSysBgpMaxPrefixIpv4Limit_Type = Unsigned32
_TnSysBgpMaxPrefixIpv4Limit_Object = MibTableColumn
tnSysBgpMaxPrefixIpv4Limit = _TnSysBgpMaxPrefixIpv4Limit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 10),
    _TnSysBgpMaxPrefixIpv4Limit_Type()
)
tnSysBgpMaxPrefixIpv4Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv4Limit.setStatus("current")
_TnSysBgpMaxPrefixIpv4Threshold_Type = Unsigned32
_TnSysBgpMaxPrefixIpv4Threshold_Object = MibTableColumn
tnSysBgpMaxPrefixIpv4Threshold = _TnSysBgpMaxPrefixIpv4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 11),
    _TnSysBgpMaxPrefixIpv4Threshold_Type()
)
tnSysBgpMaxPrefixIpv4Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv4Threshold.setStatus("current")
_TnSysBgpMaxPrefixIpv4Action_Type = NokiaSysBgpMaxPrefixAction
_TnSysBgpMaxPrefixIpv4Action_Object = MibTableColumn
tnSysBgpMaxPrefixIpv4Action = _TnSysBgpMaxPrefixIpv4Action_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 12),
    _TnSysBgpMaxPrefixIpv4Action_Type()
)
tnSysBgpMaxPrefixIpv4Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv4Action.setStatus("current")
_TnSysBgpMaxPrefixIpv6Limit_Type = Unsigned32
_TnSysBgpMaxPrefixIpv6Limit_Object = MibTableColumn
tnSysBgpMaxPrefixIpv6Limit = _TnSysBgpMaxPrefixIpv6Limit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 13),
    _TnSysBgpMaxPrefixIpv6Limit_Type()
)
tnSysBgpMaxPrefixIpv6Limit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv6Limit.setStatus("current")
_TnSysBgpMaxPrefixIpv6Threshold_Type = Unsigned32
_TnSysBgpMaxPrefixIpv6Threshold_Object = MibTableColumn
tnSysBgpMaxPrefixIpv6Threshold = _TnSysBgpMaxPrefixIpv6Threshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 14),
    _TnSysBgpMaxPrefixIpv6Threshold_Type()
)
tnSysBgpMaxPrefixIpv6Threshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv6Threshold.setStatus("current")
_TnSysBgpMaxPrefixIpv6Action_Type = NokiaSysBgpMaxPrefixAction
_TnSysBgpMaxPrefixIpv6Action_Object = MibTableColumn
tnSysBgpMaxPrefixIpv6Action = _TnSysBgpMaxPrefixIpv6Action_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 15),
    _TnSysBgpMaxPrefixIpv6Action_Type()
)
tnSysBgpMaxPrefixIpv6Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpMaxPrefixIpv6Action.setStatus("current")
_TnSysBgpStatsIpv4PrefixInCount_Type = Unsigned32
_TnSysBgpStatsIpv4PrefixInCount_Object = MibTableColumn
tnSysBgpStatsIpv4PrefixInCount = _TnSysBgpStatsIpv4PrefixInCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 16),
    _TnSysBgpStatsIpv4PrefixInCount_Type()
)
tnSysBgpStatsIpv4PrefixInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpStatsIpv4PrefixInCount.setStatus("current")
_TnSysBgpStatsIpv6PrefixInCount_Type = Unsigned32
_TnSysBgpStatsIpv6PrefixInCount_Object = MibTableColumn
tnSysBgpStatsIpv6PrefixInCount = _TnSysBgpStatsIpv6PrefixInCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 17),
    _TnSysBgpStatsIpv6PrefixInCount_Type()
)
tnSysBgpStatsIpv6PrefixInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpStatsIpv6PrefixInCount.setStatus("current")
_TnSysBgpStatsIpv4PrefixOutCount_Type = Unsigned32
_TnSysBgpStatsIpv4PrefixOutCount_Object = MibTableColumn
tnSysBgpStatsIpv4PrefixOutCount = _TnSysBgpStatsIpv4PrefixOutCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 18),
    _TnSysBgpStatsIpv4PrefixOutCount_Type()
)
tnSysBgpStatsIpv4PrefixOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpStatsIpv4PrefixOutCount.setStatus("current")
_TnSysBgpStatsIpv6PrefixOutCount_Type = Unsigned32
_TnSysBgpStatsIpv6PrefixOutCount_Object = MibTableColumn
tnSysBgpStatsIpv6PrefixOutCount = _TnSysBgpStatsIpv6PrefixOutCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 19),
    _TnSysBgpStatsIpv6PrefixOutCount_Type()
)
tnSysBgpStatsIpv6PrefixOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBgpStatsIpv6PrefixOutCount.setStatus("current")


class _TnSysBgpPeerStatsInetAddressType_Type(InetAddressType):
    """Custom type tnSysBgpPeerStatsInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysBgpPeerStatsInetAddressType_Type.__name__ = "InetAddressType"
_TnSysBgpPeerStatsInetAddressType_Object = MibTableColumn
tnSysBgpPeerStatsInetAddressType = _TnSysBgpPeerStatsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 20),
    _TnSysBgpPeerStatsInetAddressType_Type()
)
tnSysBgpPeerStatsInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerStatsInetAddressType.setStatus("current")


class _TnSysBgpPeerStatsIp_Type(IpAddress):
    """Custom type tnSysBgpPeerStatsIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysBgpPeerStatsIp_Type.__name__ = "IpAddress"
_TnSysBgpPeerStatsIp_Object = MibTableColumn
tnSysBgpPeerStatsIp = _TnSysBgpPeerStatsIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 21),
    _TnSysBgpPeerStatsIp_Type()
)
tnSysBgpPeerStatsIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerStatsIp.setStatus("current")


class _TnSysBgpPeerStatsInetAddress_Type(InetAddress):
    """Custom type tnSysBgpPeerStatsInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysBgpPeerStatsInetAddress_Type.__name__ = "InetAddress"
_TnSysBgpPeerStatsInetAddress_Object = MibTableColumn
tnSysBgpPeerStatsInetAddress = _TnSysBgpPeerStatsInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 35, 1, 1, 22),
    _TnSysBgpPeerStatsInetAddress_Type()
)
tnSysBgpPeerStatsInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysBgpPeerStatsInetAddress.setStatus("current")
_TnSysDiscoverMe_ObjectIdentity = ObjectIdentity
tnSysDiscoverMe = _TnSysDiscoverMe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 36)
)


class _TnSysDiscoverMeTraps_Type(TmnxEnabledDisabled):
    """Custom type tnSysDiscoverMeTraps based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnSysDiscoverMeTraps_Type.__name__ = "TmnxEnabledDisabled"
_TnSysDiscoverMeTraps_Object = MibScalar
tnSysDiscoverMeTraps = _TnSysDiscoverMeTraps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 36, 1),
    _TnSysDiscoverMeTraps_Type()
)
tnSysDiscoverMeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoverMeTraps.setStatus("current")
_TnSyslogServer_ObjectIdentity = ObjectIdentity
tnSyslogServer = _TnSyslogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37)
)
_TnSyslogServerTable_Object = MibTable
tnSyslogServerTable = _TnSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1)
)
if mibBuilder.loadTexts:
    tnSyslogServerTable.setStatus("current")
_TnSyslogServerEntry_Object = MibTableRow
tnSyslogServerEntry = _TnSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1)
)
tnSyslogServerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    tnSyslogServerEntry.setStatus("current")
_TnSyslogServerIndex_Type = Unsigned32
_TnSyslogServerIndex_Object = MibTableColumn
tnSyslogServerIndex = _TnSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 1),
    _TnSyslogServerIndex_Type()
)
tnSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSyslogServerIndex.setStatus("current")


class _TnSyslogServerIpAddress_Type(IpAddress):
    """Custom type tnSyslogServerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSyslogServerIpAddress_Type.__name__ = "IpAddress"
_TnSyslogServerIpAddress_Object = MibTableColumn
tnSyslogServerIpAddress = _TnSyslogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 2),
    _TnSyslogServerIpAddress_Type()
)
tnSyslogServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerIpAddress.setStatus("current")


class _TnSyslogServerPort_Type(Unsigned32):
    """Custom type tnSyslogServerPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSyslogServerPort_Type.__name__ = "Unsigned32"
_TnSyslogServerPort_Object = MibTableColumn
tnSyslogServerPort = _TnSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 3),
    _TnSyslogServerPort_Type()
)
tnSyslogServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerPort.setStatus("current")


class _TnSyslogServerFacility_Type(Integer32):
    """Custom type tnSyslogServerFacility based on Integer32"""
    defaultValue = 13

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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kern", 1),
          ("user", 2),
          ("mail", 3),
          ("daemon", 4),
          ("auth", 5),
          ("syslog", 6),
          ("lpr", 7),
          ("news", 8),
          ("uucp", 9),
          ("cron", 10),
          ("authPriv", 11),
          ("ftp", 12),
          ("local0", 13),
          ("local1", 14),
          ("local2", 15),
          ("local3", 16),
          ("local4", 17),
          ("local5", 18),
          ("local6", 19),
          ("local7", 20),
          ("all", 21),
          ("logAudit", 22),
          ("logAlert", 23))
    )


_TnSyslogServerFacility_Type.__name__ = "Integer32"
_TnSyslogServerFacility_Object = MibTableColumn
tnSyslogServerFacility = _TnSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 4),
    _TnSyslogServerFacility_Type()
)
tnSyslogServerFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerFacility.setStatus("current")


class _TnSyslogServerPriority_Type(Integer32):
    """Custom type tnSyslogServerPriority based on Integer32"""
    defaultValue = 8

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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_TnSyslogServerPriority_Type.__name__ = "Integer32"
_TnSyslogServerPriority_Object = MibTableColumn
tnSyslogServerPriority = _TnSyslogServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 5),
    _TnSyslogServerPriority_Type()
)
tnSyslogServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerPriority.setStatus("current")


class _TnSyslogServerEnabled_Type(TruthValue):
    """Custom type tnSyslogServerEnabled based on TruthValue"""
    defaultValue = 2


_TnSyslogServerEnabled_Type.__name__ = "TruthValue"
_TnSyslogServerEnabled_Object = MibTableColumn
tnSyslogServerEnabled = _TnSyslogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 6),
    _TnSyslogServerEnabled_Type()
)
tnSyslogServerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerEnabled.setStatus("current")


class _TnSyslogServerInetAddress_Type(InetAddress):
    """Custom type tnSyslogServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSyslogServerInetAddress_Type.__name__ = "InetAddress"
_TnSyslogServerInetAddress_Object = MibTableColumn
tnSyslogServerInetAddress = _TnSyslogServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 7),
    _TnSyslogServerInetAddress_Type()
)
tnSyslogServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerInetAddress.setStatus("current")


class _TnSyslogServerInetAddressType_Type(InetAddressType):
    """Custom type tnSyslogServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSyslogServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSyslogServerInetAddressType_Object = MibTableColumn
tnSyslogServerInetAddressType = _TnSyslogServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 8),
    _TnSyslogServerInetAddressType_Type()
)
tnSyslogServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerInetAddressType.setStatus("current")


class _TnSyslogServerProtocol_Type(Integer32):
    """Custom type tnSyslogServerProtocol based on Integer32"""
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
        *(("udp", 1),
          ("tcp", 2),
          ("tls", 3))
    )


_TnSyslogServerProtocol_Type.__name__ = "Integer32"
_TnSyslogServerProtocol_Object = MibTableColumn
tnSyslogServerProtocol = _TnSyslogServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 9),
    _TnSyslogServerProtocol_Type()
)
tnSyslogServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerProtocol.setStatus("current")


class _TnSyslogServerType_Type(Integer32):
    """Custom type tnSyslogServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("domain", 2))
    )


_TnSyslogServerType_Type.__name__ = "Integer32"
_TnSyslogServerType_Object = MibTableColumn
tnSyslogServerType = _TnSyslogServerType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 10),
    _TnSyslogServerType_Type()
)
tnSyslogServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerType.setStatus("current")
_TnSyslogServerDomain_Type = SnmpAdminString
_TnSyslogServerDomain_Object = MibTableColumn
tnSyslogServerDomain = _TnSyslogServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 37, 1, 1, 11),
    _TnSyslogServerDomain_Type()
)
tnSyslogServerDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyslogServerDomain.setStatus("current")
_TnPctObjs_ObjectIdentity = ObjectIdentity
tnPctObjs = _TnPctObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 38)
)


class _TnPctVerificationPeriod_Type(Unsigned32):
    """Custom type tnPctVerificationPeriod based on Unsigned32"""
    defaultValue = 6


_TnPctVerificationPeriod_Type.__name__ = "Unsigned32"
_TnPctVerificationPeriod_Object = MibScalar
tnPctVerificationPeriod = _TnPctVerificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 38, 1),
    _TnPctVerificationPeriod_Type()
)
tnPctVerificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPctVerificationPeriod.setStatus("current")
_TnPctVerificationLossThreshold_Type = Integer32
_TnPctVerificationLossThreshold_Object = MibScalar
tnPctVerificationLossThreshold = _TnPctVerificationLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 38, 2),
    _TnPctVerificationLossThreshold_Type()
)
tnPctVerificationLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPctVerificationLossThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnPctVerificationLossThreshold.setUnits("mB")


class _TnPctVerificationOffset_Type(Unsigned32):
    """Custom type tnPctVerificationOffset based on Unsigned32"""
    defaultValue = 0


_TnPctVerificationOffset_Type.__name__ = "Unsigned32"
_TnPctVerificationOffset_Object = MibScalar
tnPctVerificationOffset = _TnPctVerificationOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 38, 3),
    _TnPctVerificationOffset_Type()
)
tnPctVerificationOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPctVerificationOffset.setStatus("current")


class _TnPctVerificationStatus_Type(Integer32):
    """Custom type tnPctVerificationStatus based on Integer32"""
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
        *(("running", 1),
          ("notRunning", 2),
          ("disabled", 3),
          ("singlePath", 4))
    )


_TnPctVerificationStatus_Type.__name__ = "Integer32"
_TnPctVerificationStatus_Object = MibScalar
tnPctVerificationStatus = _TnPctVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 38, 4),
    _TnPctVerificationStatus_Type()
)
tnPctVerificationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPctVerificationStatus.setStatus("current")
_TnKeyObjs_ObjectIdentity = ObjectIdentity
tnKeyObjs = _TnKeyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39)
)
_TnHostKeyTable_Object = MibTable
tnHostKeyTable = _TnHostKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1)
)
if mibBuilder.loadTexts:
    tnHostKeyTable.setStatus("current")
_TnHostKeyEntry_Object = MibTableRow
tnHostKeyEntry = _TnHostKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1, 1)
)
tnHostKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnHostKeyModuleID"),
    (0, "TROPIC-SYSTEM-MIB", "tnHostKeyIndex"),
)
if mibBuilder.loadTexts:
    tnHostKeyEntry.setStatus("current")
_TnHostKeyModuleID_Type = Integer32
_TnHostKeyModuleID_Object = MibTableColumn
tnHostKeyModuleID = _TnHostKeyModuleID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1, 1, 1),
    _TnHostKeyModuleID_Type()
)
tnHostKeyModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHostKeyModuleID.setStatus("current")
_TnHostKeyIndex_Type = Integer32
_TnHostKeyIndex_Object = MibTableColumn
tnHostKeyIndex = _TnHostKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1, 1, 2),
    _TnHostKeyIndex_Type()
)
tnHostKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHostKeyIndex.setStatus("current")


class _TnHostKeyString1_Type(SnmpAdminString):
    """Custom type tnHostKeyString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnHostKeyString1_Type.__name__ = "SnmpAdminString"
_TnHostKeyString1_Object = MibTableColumn
tnHostKeyString1 = _TnHostKeyString1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1, 1, 3),
    _TnHostKeyString1_Type()
)
tnHostKeyString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHostKeyString1.setStatus("current")


class _TnHostKeyString2_Type(SnmpAdminString):
    """Custom type tnHostKeyString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnHostKeyString2_Type.__name__ = "SnmpAdminString"
_TnHostKeyString2_Object = MibTableColumn
tnHostKeyString2 = _TnHostKeyString2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 1, 1, 4),
    _TnHostKeyString2_Type()
)
tnHostKeyString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnHostKeyString2.setStatus("current")
_TnSshPrivKeyTable_Object = MibTable
tnSshPrivKeyTable = _TnSshPrivKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2)
)
if mibBuilder.loadTexts:
    tnSshPrivKeyTable.setStatus("current")
_TnSshPrivKeyEntry_Object = MibTableRow
tnSshPrivKeyEntry = _TnSshPrivKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2, 1)
)
tnSshPrivKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshPrivKeyModuleID"),
)
if mibBuilder.loadTexts:
    tnSshPrivKeyEntry.setStatus("current")
_TnSshPrivKeyModuleID_Type = Integer32
_TnSshPrivKeyModuleID_Object = MibTableColumn
tnSshPrivKeyModuleID = _TnSshPrivKeyModuleID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2, 1, 1),
    _TnSshPrivKeyModuleID_Type()
)
tnSshPrivKeyModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshPrivKeyModuleID.setStatus("current")


class _TnSshPrivKeyString1_Type(SnmpAdminString):
    """Custom type tnSshPrivKeyString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshPrivKeyString1_Type.__name__ = "SnmpAdminString"
_TnSshPrivKeyString1_Object = MibTableColumn
tnSshPrivKeyString1 = _TnSshPrivKeyString1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2, 1, 2),
    _TnSshPrivKeyString1_Type()
)
tnSshPrivKeyString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshPrivKeyString1.setStatus("current")


class _TnSshPrivKeyString2_Type(SnmpAdminString):
    """Custom type tnSshPrivKeyString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSshPrivKeyString2_Type.__name__ = "SnmpAdminString"
_TnSshPrivKeyString2_Object = MibTableColumn
tnSshPrivKeyString2 = _TnSshPrivKeyString2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2, 1, 3),
    _TnSshPrivKeyString2_Type()
)
tnSshPrivKeyString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshPrivKeyString2.setStatus("current")


class _TnSshPrivKeyPassword_Type(SnmpAdminString):
    """Custom type tnSshPrivKeyPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSshPrivKeyPassword_Type.__name__ = "SnmpAdminString"
_TnSshPrivKeyPassword_Object = MibTableColumn
tnSshPrivKeyPassword = _TnSshPrivKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 2, 1, 4),
    _TnSshPrivKeyPassword_Type()
)
tnSshPrivKeyPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshPrivKeyPassword.setStatus("current")
_TnSysNESshKeyTable_Object = MibTable
tnSysNESshKeyTable = _TnSysNESshKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3)
)
if mibBuilder.loadTexts:
    tnSysNESshKeyTable.setStatus("current")
_TnSysNESshKeyEntry_Object = MibTableRow
tnSysNESshKeyEntry = _TnSysNESshKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1)
)
tnSysNESshKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNESshKeyUserName"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysNESshKeyIndex"),
)
if mibBuilder.loadTexts:
    tnSysNESshKeyEntry.setStatus("current")


class _TnSysNESshKeyUserName_Type(SnmpAdminString):
    """Custom type tnSysNESshKeyUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnSysNESshKeyUserName_Type.__name__ = "SnmpAdminString"
_TnSysNESshKeyUserName_Object = MibTableColumn
tnSysNESshKeyUserName = _TnSysNESshKeyUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1, 1),
    _TnSysNESshKeyUserName_Type()
)
tnSysNESshKeyUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNESshKeyUserName.setStatus("current")
_TnSysNESshKeyIndex_Type = Integer32
_TnSysNESshKeyIndex_Object = MibTableColumn
tnSysNESshKeyIndex = _TnSysNESshKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1, 2),
    _TnSysNESshKeyIndex_Type()
)
tnSysNESshKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNESshKeyIndex.setStatus("current")
_TnSysNESshKeyRowStatus_Type = RowStatus
_TnSysNESshKeyRowStatus_Object = MibTableColumn
tnSysNESshKeyRowStatus = _TnSysNESshKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1, 3),
    _TnSysNESshKeyRowStatus_Type()
)
tnSysNESshKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNESshKeyRowStatus.setStatus("current")


class _TnSysNESshKeyString1_Type(SnmpAdminString):
    """Custom type tnSysNESshKeyString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSysNESshKeyString1_Type.__name__ = "SnmpAdminString"
_TnSysNESshKeyString1_Object = MibTableColumn
tnSysNESshKeyString1 = _TnSysNESshKeyString1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1, 4),
    _TnSysNESshKeyString1_Type()
)
tnSysNESshKeyString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNESshKeyString1.setStatus("current")


class _TnSysNESshKeyString2_Type(SnmpAdminString):
    """Custom type tnSysNESshKeyString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSysNESshKeyString2_Type.__name__ = "SnmpAdminString"
_TnSysNESshKeyString2_Object = MibTableColumn
tnSysNESshKeyString2 = _TnSysNESshKeyString2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 3, 1, 5),
    _TnSysNESshKeyString2_Type()
)
tnSysNESshKeyString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNESshKeyString2.setStatus("current")
_TnNESshKeyTable_Object = MibTable
tnNESshKeyTable = _TnNESshKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4)
)
if mibBuilder.loadTexts:
    tnNESshKeyTable.setStatus("current")
_TnNESshKeyEntry_Object = MibTableRow
tnNESshKeyEntry = _TnNESshKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1)
)
tnNESshKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnNESshKeyUserName"),
    (0, "TROPIC-SYSTEM-MIB", "tnNESshKeyIndex"),
)
if mibBuilder.loadTexts:
    tnNESshKeyEntry.setStatus("current")


class _TnNESshKeyUserName_Type(SnmpAdminString):
    """Custom type tnNESshKeyUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TnNESshKeyUserName_Type.__name__ = "SnmpAdminString"
_TnNESshKeyUserName_Object = MibTableColumn
tnNESshKeyUserName = _TnNESshKeyUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1, 1),
    _TnNESshKeyUserName_Type()
)
tnNESshKeyUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNESshKeyUserName.setStatus("current")
_TnNESshKeyIndex_Type = Integer32
_TnNESshKeyIndex_Object = MibTableColumn
tnNESshKeyIndex = _TnNESshKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1, 2),
    _TnNESshKeyIndex_Type()
)
tnNESshKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNESshKeyIndex.setStatus("current")
_TnNESshKeyRowStatus_Type = RowStatus
_TnNESshKeyRowStatus_Object = MibTableColumn
tnNESshKeyRowStatus = _TnNESshKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1, 3),
    _TnNESshKeyRowStatus_Type()
)
tnNESshKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNESshKeyRowStatus.setStatus("current")


class _TnNESshKeyString1_Type(SnmpAdminString):
    """Custom type tnNESshKeyString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnNESshKeyString1_Type.__name__ = "SnmpAdminString"
_TnNESshKeyString1_Object = MibTableColumn
tnNESshKeyString1 = _TnNESshKeyString1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1, 4),
    _TnNESshKeyString1_Type()
)
tnNESshKeyString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNESshKeyString1.setStatus("current")


class _TnNESshKeyString2_Type(SnmpAdminString):
    """Custom type tnNESshKeyString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnNESshKeyString2_Type.__name__ = "SnmpAdminString"
_TnNESshKeyString2_Object = MibTableColumn
tnNESshKeyString2 = _TnNESshKeyString2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 4, 1, 5),
    _TnNESshKeyString2_Type()
)
tnNESshKeyString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNESshKeyString2.setStatus("current")
_TnSshCiphersTable_Object = MibTable
tnSshCiphersTable = _TnSshCiphersTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 5)
)
if mibBuilder.loadTexts:
    tnSshCiphersTable.setStatus("current")
_TnSshCiphersEntry_Object = MibTableRow
tnSshCiphersEntry = _TnSshCiphersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 5, 1)
)
tnSshCiphersEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshCiphersAlgType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSshCiphersProfileName"),
)
if mibBuilder.loadTexts:
    tnSshCiphersEntry.setStatus("current")
_TnSshCiphersAlgType_Type = Unsigned32
_TnSshCiphersAlgType_Object = MibTableColumn
tnSshCiphersAlgType = _TnSshCiphersAlgType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 5, 1, 1),
    _TnSshCiphersAlgType_Type()
)
tnSshCiphersAlgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshCiphersAlgType.setStatus("current")
_TnSshCiphersProfileName_Type = OctetString
_TnSshCiphersProfileName_Object = MibTableColumn
tnSshCiphersProfileName = _TnSshCiphersProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 5, 1, 2),
    _TnSshCiphersProfileName_Type()
)
tnSshCiphersProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshCiphersProfileName.setStatus("current")
_TnSshCiphersEnabled_Type = TruthValue
_TnSshCiphersEnabled_Object = MibTableColumn
tnSshCiphersEnabled = _TnSshCiphersEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 5, 1, 3),
    _TnSshCiphersEnabled_Type()
)
tnSshCiphersEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshCiphersEnabled.setStatus("current")
_TnSshHostKeyTable_Object = MibTable
tnSshHostKeyTable = _TnSshHostKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 6)
)
if mibBuilder.loadTexts:
    tnSshHostKeyTable.setStatus("current")
_TnSshHostKeyEntry_Object = MibTableRow
tnSshHostKeyEntry = _TnSshHostKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 6, 1)
)
tnSshHostKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshHostKeyAlgType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSshHostKeyProfileName"),
)
if mibBuilder.loadTexts:
    tnSshHostKeyEntry.setStatus("current")
_TnSshHostKeyAlgType_Type = Unsigned32
_TnSshHostKeyAlgType_Object = MibTableColumn
tnSshHostKeyAlgType = _TnSshHostKeyAlgType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 6, 1, 1),
    _TnSshHostKeyAlgType_Type()
)
tnSshHostKeyAlgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshHostKeyAlgType.setStatus("current")
_TnSshHostKeyProfileName_Type = OctetString
_TnSshHostKeyProfileName_Object = MibTableColumn
tnSshHostKeyProfileName = _TnSshHostKeyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 6, 1, 2),
    _TnSshHostKeyProfileName_Type()
)
tnSshHostKeyProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshHostKeyProfileName.setStatus("current")
_TnSshHostKeyEnabled_Type = TruthValue
_TnSshHostKeyEnabled_Object = MibTableColumn
tnSshHostKeyEnabled = _TnSshHostKeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 6, 1, 3),
    _TnSshHostKeyEnabled_Type()
)
tnSshHostKeyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshHostKeyEnabled.setStatus("current")
_TnSshMacsTable_Object = MibTable
tnSshMacsTable = _TnSshMacsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 7)
)
if mibBuilder.loadTexts:
    tnSshMacsTable.setStatus("current")
_TnSshMacsEntry_Object = MibTableRow
tnSshMacsEntry = _TnSshMacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 7, 1)
)
tnSshMacsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshMacsAlgType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSshMacsProfileName"),
)
if mibBuilder.loadTexts:
    tnSshMacsEntry.setStatus("current")
_TnSshMacsAlgType_Type = Unsigned32
_TnSshMacsAlgType_Object = MibTableColumn
tnSshMacsAlgType = _TnSshMacsAlgType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 7, 1, 1),
    _TnSshMacsAlgType_Type()
)
tnSshMacsAlgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshMacsAlgType.setStatus("current")
_TnSshMacsProfileName_Type = OctetString
_TnSshMacsProfileName_Object = MibTableColumn
tnSshMacsProfileName = _TnSshMacsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 7, 1, 2),
    _TnSshMacsProfileName_Type()
)
tnSshMacsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshMacsProfileName.setStatus("current")
_TnSshMacsEnabled_Type = TruthValue
_TnSshMacsEnabled_Object = MibTableColumn
tnSshMacsEnabled = _TnSshMacsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 7, 1, 3),
    _TnSshMacsEnabled_Type()
)
tnSshMacsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshMacsEnabled.setStatus("current")
_TnSshKexTable_Object = MibTable
tnSshKexTable = _TnSshKexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 8)
)
if mibBuilder.loadTexts:
    tnSshKexTable.setStatus("current")
_TnSshKexEntry_Object = MibTableRow
tnSshKexEntry = _TnSshKexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 8, 1)
)
tnSshKexEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshKexAlgType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSshKexProfileName"),
)
if mibBuilder.loadTexts:
    tnSshKexEntry.setStatus("current")
_TnSshKexAlgType_Type = Unsigned32
_TnSshKexAlgType_Object = MibTableColumn
tnSshKexAlgType = _TnSshKexAlgType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 8, 1, 1),
    _TnSshKexAlgType_Type()
)
tnSshKexAlgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshKexAlgType.setStatus("current")
_TnSshKexProfileName_Type = OctetString
_TnSshKexProfileName_Object = MibTableColumn
tnSshKexProfileName = _TnSshKexProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 8, 1, 2),
    _TnSshKexProfileName_Type()
)
tnSshKexProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshKexProfileName.setStatus("current")
_TnSshKexEnabled_Type = TruthValue
_TnSshKexEnabled_Object = MibTableColumn
tnSshKexEnabled = _TnSshKexEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 8, 1, 3),
    _TnSshKexEnabled_Type()
)
tnSshKexEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshKexEnabled.setStatus("current")
_TnSshPubKeyTable_Object = MibTable
tnSshPubKeyTable = _TnSshPubKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 9)
)
if mibBuilder.loadTexts:
    tnSshPubKeyTable.setStatus("current")
_TnSshPubKeyEntry_Object = MibTableRow
tnSshPubKeyEntry = _TnSshPubKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 9, 1)
)
tnSshPubKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshPubKeyAlgType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSshPubKeyProfileName"),
)
if mibBuilder.loadTexts:
    tnSshPubKeyEntry.setStatus("current")
_TnSshPubKeyAlgType_Type = Unsigned32
_TnSshPubKeyAlgType_Object = MibTableColumn
tnSshPubKeyAlgType = _TnSshPubKeyAlgType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 9, 1, 1),
    _TnSshPubKeyAlgType_Type()
)
tnSshPubKeyAlgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshPubKeyAlgType.setStatus("current")
_TnSshPubKeyProfileName_Type = OctetString
_TnSshPubKeyProfileName_Object = MibTableColumn
tnSshPubKeyProfileName = _TnSshPubKeyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 9, 1, 2),
    _TnSshPubKeyProfileName_Type()
)
tnSshPubKeyProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshPubKeyProfileName.setStatus("current")
_TnSshPubKeyEnabled_Type = TruthValue
_TnSshPubKeyEnabled_Object = MibTableColumn
tnSshPubKeyEnabled = _TnSshPubKeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 9, 1, 3),
    _TnSshPubKeyEnabled_Type()
)
tnSshPubKeyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshPubKeyEnabled.setStatus("current")
_TnTlsProfileTable_Object = MibTable
tnTlsProfileTable = _TnTlsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10)
)
if mibBuilder.loadTexts:
    tnTlsProfileTable.setStatus("current")
_TnTlsProfileEntry_Object = MibTableRow
tnTlsProfileEntry = _TnTlsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1)
)
tnTlsProfileEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnTlsProfileName"),
)
if mibBuilder.loadTexts:
    tnTlsProfileEntry.setStatus("current")
_TnTlsProfileName_Type = OctetString
_TnTlsProfileName_Object = MibTableColumn
tnTlsProfileName = _TnTlsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1, 1),
    _TnTlsProfileName_Type()
)
tnTlsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsProfileName.setStatus("current")
_TnTlsProfileMinVersion_Type = Integer32
_TnTlsProfileMinVersion_Object = MibTableColumn
tnTlsProfileMinVersion = _TnTlsProfileMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1, 2),
    _TnTlsProfileMinVersion_Type()
)
tnTlsProfileMinVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsProfileMinVersion.setStatus("current")
_TnTlsProfileMaxVersion_Type = Integer32
_TnTlsProfileMaxVersion_Object = MibTableColumn
tnTlsProfileMaxVersion = _TnTlsProfileMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1, 3),
    _TnTlsProfileMaxVersion_Type()
)
tnTlsProfileMaxVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsProfileMaxVersion.setStatus("current")
_TnTlsProfileMutualAuth_Type = AluWdmEnabledDisabled
_TnTlsProfileMutualAuth_Object = MibTableColumn
tnTlsProfileMutualAuth = _TnTlsProfileMutualAuth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1, 4),
    _TnTlsProfileMutualAuth_Type()
)
tnTlsProfileMutualAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsProfileMutualAuth.setStatus("current")


class _TnTlsProfileDescription_Type(SnmpAdminString):
    """Custom type tnTlsProfileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnTlsProfileDescription_Type.__name__ = "SnmpAdminString"
_TnTlsProfileDescription_Object = MibTableColumn
tnTlsProfileDescription = _TnTlsProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 10, 1, 5),
    _TnTlsProfileDescription_Type()
)
tnTlsProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTlsProfileDescription.setStatus("current")
_TnSanListTable_Object = MibTable
tnSanListTable = _TnSanListTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11)
)
if mibBuilder.loadTexts:
    tnSanListTable.setStatus("current")
_TnSanListEntry_Object = MibTableRow
tnSanListEntry = _TnSanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11, 1)
)
tnSanListEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSanListName"),
    (0, "TROPIC-SYSTEM-MIB", "tnSanListType"),
    (0, "TROPIC-SYSTEM-MIB", "tnSanListIndex"),
)
if mibBuilder.loadTexts:
    tnSanListEntry.setStatus("current")
_TnSanListName_Type = OctetString
_TnSanListName_Object = MibTableColumn
tnSanListName = _TnSanListName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11, 1, 1),
    _TnSanListName_Type()
)
tnSanListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSanListName.setStatus("current")


class _TnSanListType_Type(Integer32):
    """Custom type tnSanListType based on Integer32"""
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
          ("domain", 3))
    )


_TnSanListType_Type.__name__ = "Integer32"
_TnSanListType_Object = MibTableColumn
tnSanListType = _TnSanListType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11, 1, 2),
    _TnSanListType_Type()
)
tnSanListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSanListType.setStatus("current")
_TnSanListIndex_Type = OctetString
_TnSanListIndex_Object = MibTableColumn
tnSanListIndex = _TnSanListIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11, 1, 3),
    _TnSanListIndex_Type()
)
tnSanListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSanListIndex.setStatus("current")
_TnSanListRowStatus_Type = RowStatus
_TnSanListRowStatus_Object = MibTableColumn
tnSanListRowStatus = _TnSanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 11, 1, 4),
    _TnSanListRowStatus_Type()
)
tnSanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSanListRowStatus.setStatus("current")
_TnCsrSanListTable_Object = MibTable
tnCsrSanListTable = _TnCsrSanListTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 12)
)
if mibBuilder.loadTexts:
    tnCsrSanListTable.setStatus("current")
_TnCsrSanListEntry_Object = MibTableRow
tnCsrSanListEntry = _TnCsrSanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 12, 1)
)
tnCsrSanListEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnCsrSanListType"),
    (0, "TROPIC-SYSTEM-MIB", "tnCsrSanListIndex"),
)
if mibBuilder.loadTexts:
    tnCsrSanListEntry.setStatus("current")


class _TnCsrSanListType_Type(Integer32):
    """Custom type tnCsrSanListType based on Integer32"""
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
          ("domain", 3))
    )


_TnCsrSanListType_Type.__name__ = "Integer32"
_TnCsrSanListType_Object = MibTableColumn
tnCsrSanListType = _TnCsrSanListType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 12, 1, 1),
    _TnCsrSanListType_Type()
)
tnCsrSanListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCsrSanListType.setStatus("current")
_TnCsrSanListIndex_Type = OctetString
_TnCsrSanListIndex_Object = MibTableColumn
tnCsrSanListIndex = _TnCsrSanListIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 12, 1, 2),
    _TnCsrSanListIndex_Type()
)
tnCsrSanListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCsrSanListIndex.setStatus("current")
_TnCsrSanListRowStatus_Type = RowStatus
_TnCsrSanListRowStatus_Object = MibTableColumn
tnCsrSanListRowStatus = _TnCsrSanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 12, 1, 3),
    _TnCsrSanListRowStatus_Type()
)
tnCsrSanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCsrSanListRowStatus.setStatus("current")
_TnSanListAuthTable_Object = MibTable
tnSanListAuthTable = _TnSanListAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 13)
)
if mibBuilder.loadTexts:
    tnSanListAuthTable.setStatus("current")
_TnSanListAuthEntry_Object = MibTableRow
tnSanListAuthEntry = _TnSanListAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 13, 1)
)
tnSanListAuthEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSanListName"),
)
if mibBuilder.loadTexts:
    tnSanListAuthEntry.setStatus("current")
_TnSanListAuthentication_Type = AluWdmEnabledDisabled
_TnSanListAuthentication_Object = MibTableColumn
tnSanListAuthentication = _TnSanListAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 13, 1, 1),
    _TnSanListAuthentication_Type()
)
tnSanListAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSanListAuthentication.setStatus("current")


class _TnSanListProfileDescription_Type(SnmpAdminString):
    """Custom type tnSanListProfileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSanListProfileDescription_Type.__name__ = "SnmpAdminString"
_TnSanListProfileDescription_Object = MibTableColumn
tnSanListProfileDescription = _TnSanListProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 13, 1, 2),
    _TnSanListProfileDescription_Type()
)
tnSanListProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSanListProfileDescription.setStatus("current")
_TnOcspProfileTable_Object = MibTable
tnOcspProfileTable = _TnOcspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14)
)
if mibBuilder.loadTexts:
    tnOcspProfileTable.setStatus("current")
_TnOcspProfileEntry_Object = MibTableRow
tnOcspProfileEntry = _TnOcspProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1)
)
tnOcspProfileEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnOcspProfileName"),
)
if mibBuilder.loadTexts:
    tnOcspProfileEntry.setStatus("current")
_TnOcspProfileName_Type = OctetString
_TnOcspProfileName_Object = MibTableColumn
tnOcspProfileName = _TnOcspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 1),
    _TnOcspProfileName_Type()
)
tnOcspProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOcspProfileName.setStatus("current")
_TnOcspProfileRowStatus_Type = RowStatus
_TnOcspProfileRowStatus_Object = MibTableColumn
tnOcspProfileRowStatus = _TnOcspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 2),
    _TnOcspProfileRowStatus_Type()
)
tnOcspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOcspProfileRowStatus.setStatus("current")


class _TnOcspProfileRetry_Type(Unsigned32):
    """Custom type tnOcspProfileRetry based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnOcspProfileRetry_Type.__name__ = "Unsigned32"
_TnOcspProfileRetry_Object = MibTableColumn
tnOcspProfileRetry = _TnOcspProfileRetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 3),
    _TnOcspProfileRetry_Type()
)
tnOcspProfileRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOcspProfileRetry.setStatus("current")


class _TnOcspProfileServerUrl_Type(SnmpAdminString):
    """Custom type tnOcspProfileServerUrl based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnOcspProfileServerUrl_Type.__name__ = "SnmpAdminString"
_TnOcspProfileServerUrl_Object = MibTableColumn
tnOcspProfileServerUrl = _TnOcspProfileServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 4),
    _TnOcspProfileServerUrl_Type()
)
tnOcspProfileServerUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOcspProfileServerUrl.setStatus("current")
_TnOcspProfileStatus_Type = AluWdmEnabledDisabled
_TnOcspProfileStatus_Object = MibTableColumn
tnOcspProfileStatus = _TnOcspProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 5),
    _TnOcspProfileStatus_Type()
)
tnOcspProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOcspProfileStatus.setStatus("current")


class _TnOcspProfileTimeout_Type(Unsigned32):
    """Custom type tnOcspProfileTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnOcspProfileTimeout_Type.__name__ = "Unsigned32"
_TnOcspProfileTimeout_Object = MibTableColumn
tnOcspProfileTimeout = _TnOcspProfileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 14, 1, 6),
    _TnOcspProfileTimeout_Type()
)
tnOcspProfileTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOcspProfileTimeout.setStatus("current")
_TnSshProfileTable_Object = MibTable
tnSshProfileTable = _TnSshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 15)
)
if mibBuilder.loadTexts:
    tnSshProfileTable.setStatus("current")
_TnSshProfileEntry_Object = MibTableRow
tnSshProfileEntry = _TnSshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 15, 1)
)
tnSshProfileEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshProfileName"),
)
if mibBuilder.loadTexts:
    tnSshProfileEntry.setStatus("current")
_TnSshProfileName_Type = OctetString
_TnSshProfileName_Object = MibTableColumn
tnSshProfileName = _TnSshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 15, 1, 1),
    _TnSshProfileName_Type()
)
tnSshProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshProfileName.setStatus("current")


class _TnSshProfileDescription_Type(SnmpAdminString):
    """Custom type tnSshProfileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSshProfileDescription_Type.__name__ = "SnmpAdminString"
_TnSshProfileDescription_Object = MibTableColumn
tnSshProfileDescription = _TnSshProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 39, 15, 1, 2),
    _TnSshProfileDescription_Type()
)
tnSshProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSshProfileDescription.setStatus("current")
_TnTransferSysLog_ObjectIdentity = ObjectIdentity
tnTransferSysLog = _TnTransferSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40)
)


class _TnTransferSysLogCommand_Type(Integer32):
    """Custom type tnTransferSysLogCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnTransferSysLogCommand_Type.__name__ = "Integer32"
_TnTransferSysLogCommand_Object = MibScalar
tnTransferSysLogCommand = _TnTransferSysLogCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 1),
    _TnTransferSysLogCommand_Type()
)
tnTransferSysLogCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogCommand.setStatus("current")


class _TnTransferSysLogRemoteHostIp_Type(IpAddress):
    """Custom type tnTransferSysLogRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnTransferSysLogRemoteHostIp_Type.__name__ = "IpAddress"
_TnTransferSysLogRemoteHostIp_Object = MibScalar
tnTransferSysLogRemoteHostIp = _TnTransferSysLogRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 2),
    _TnTransferSysLogRemoteHostIp_Type()
)
tnTransferSysLogRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogRemoteHostIp.setStatus("current")


class _TnTransferSysLogRemoteHostInetAddressType_Type(InetAddressType):
    """Custom type tnTransferSysLogRemoteHostInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnTransferSysLogRemoteHostInetAddressType_Type.__name__ = "InetAddressType"
_TnTransferSysLogRemoteHostInetAddressType_Object = MibScalar
tnTransferSysLogRemoteHostInetAddressType = _TnTransferSysLogRemoteHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 3),
    _TnTransferSysLogRemoteHostInetAddressType_Type()
)
tnTransferSysLogRemoteHostInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogRemoteHostInetAddressType.setStatus("current")


class _TnTransferSysLogRemoteHostInetAddress_Type(InetAddress):
    """Custom type tnTransferSysLogRemoteHostInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnTransferSysLogRemoteHostInetAddress_Type.__name__ = "InetAddress"
_TnTransferSysLogRemoteHostInetAddress_Object = MibScalar
tnTransferSysLogRemoteHostInetAddress = _TnTransferSysLogRemoteHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 4),
    _TnTransferSysLogRemoteHostInetAddress_Type()
)
tnTransferSysLogRemoteHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogRemoteHostInetAddress.setStatus("current")


class _TnTransferSysLogPort_Type(Unsigned32):
    """Custom type tnTransferSysLogPort based on Unsigned32"""
    defaultValue = 22

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnTransferSysLogPort_Type.__name__ = "Unsigned32"
_TnTransferSysLogPort_Object = MibScalar
tnTransferSysLogPort = _TnTransferSysLogPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 5),
    _TnTransferSysLogPort_Type()
)
tnTransferSysLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogPort.setStatus("current")


class _TnTransferSysLogProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnTransferSysLogProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 2


_TnTransferSysLogProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnTransferSysLogProtocol_Object = MibScalar
tnTransferSysLogProtocol = _TnTransferSysLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 6),
    _TnTransferSysLogProtocol_Type()
)
tnTransferSysLogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogProtocol.setStatus("current")


class _TnTransferSysLogUserId_Type(SnmpAdminString):
    """Custom type tnTransferSysLogUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnTransferSysLogUserId_Type.__name__ = "SnmpAdminString"
_TnTransferSysLogUserId_Object = MibScalar
tnTransferSysLogUserId = _TnTransferSysLogUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 7),
    _TnTransferSysLogUserId_Type()
)
tnTransferSysLogUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogUserId.setStatus("current")


class _TnTransferSysLogPassword_Type(SnmpAdminString):
    """Custom type tnTransferSysLogPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTransferSysLogPassword_Type.__name__ = "SnmpAdminString"
_TnTransferSysLogPassword_Object = MibScalar
tnTransferSysLogPassword = _TnTransferSysLogPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 8),
    _TnTransferSysLogPassword_Type()
)
tnTransferSysLogPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogPassword.setStatus("current")


class _TnTransferSysLogRemotePath_Type(SnmpAdminString):
    """Custom type tnTransferSysLogRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTransferSysLogRemotePath_Type.__name__ = "SnmpAdminString"
_TnTransferSysLogRemotePath_Object = MibScalar
tnTransferSysLogRemotePath = _TnTransferSysLogRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 9),
    _TnTransferSysLogRemotePath_Type()
)
tnTransferSysLogRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogRemotePath.setStatus("current")
_TnTransferSysLogPeriod_Type = Unsigned32
_TnTransferSysLogPeriod_Object = MibScalar
tnTransferSysLogPeriod = _TnTransferSysLogPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 10),
    _TnTransferSysLogPeriod_Type()
)
tnTransferSysLogPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogPeriod.setStatus("current")


class _TnTransferSysLogLastFileTransfer_Type(Integer32):
    """Custom type tnTransferSysLogLastFileTransfer based on Integer32"""
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
          ("completed", 2),
          ("inProgress", 3),
          ("failed", 4),
          ("failTimeOut", 5))
    )


_TnTransferSysLogLastFileTransfer_Type.__name__ = "Integer32"
_TnTransferSysLogLastFileTransfer_Object = MibScalar
tnTransferSysLogLastFileTransfer = _TnTransferSysLogLastFileTransfer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 11),
    _TnTransferSysLogLastFileTransfer_Type()
)
tnTransferSysLogLastFileTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferSysLogLastFileTransfer.setStatus("current")


class _TnTransferSysLogEnable_Type(TruthValue):
    """Custom type tnTransferSysLogEnable based on TruthValue"""
    defaultValue = 2


_TnTransferSysLogEnable_Type.__name__ = "TruthValue"
_TnTransferSysLogEnable_Object = MibScalar
tnTransferSysLogEnable = _TnTransferSysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 40, 12),
    _TnTransferSysLogEnable_Type()
)
tnTransferSysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTransferSysLogEnable.setStatus("current")
_TnSysHealthCare_ObjectIdentity = ObjectIdentity
tnSysHealthCare = _TnSysHealthCare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41)
)


class _TnSysHealthCareCheckCommand_Type(Integer32):
    """Custom type tnSysHealthCareCheckCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("check", 2),
          ("abort", 3))
    )


_TnSysHealthCareCheckCommand_Type.__name__ = "Integer32"
_TnSysHealthCareCheckCommand_Object = MibScalar
tnSysHealthCareCheckCommand = _TnSysHealthCareCheckCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 1),
    _TnSysHealthCareCheckCommand_Type()
)
tnSysHealthCareCheckCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckCommand.setStatus("current")


class _TnSysHealthCareCheckShelfNum_Type(Integer32):
    """Custom type tnSysHealthCareCheckShelfNum based on Integer32"""
    defaultValue = 0


_TnSysHealthCareCheckShelfNum_Type.__name__ = "Integer32"
_TnSysHealthCareCheckShelfNum_Object = MibScalar
tnSysHealthCareCheckShelfNum = _TnSysHealthCareCheckShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 2),
    _TnSysHealthCareCheckShelfNum_Type()
)
tnSysHealthCareCheckShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckShelfNum.setStatus("current")


class _TnSysHealthCareCheckSlotNum_Type(Integer32):
    """Custom type tnSysHealthCareCheckSlotNum based on Integer32"""
    defaultValue = 0


_TnSysHealthCareCheckSlotNum_Type.__name__ = "Integer32"
_TnSysHealthCareCheckSlotNum_Object = MibScalar
tnSysHealthCareCheckSlotNum = _TnSysHealthCareCheckSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 3),
    _TnSysHealthCareCheckSlotNum_Type()
)
tnSysHealthCareCheckSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckSlotNum.setStatus("current")


class _TnSysHealthCareCheckPercentCompleted_Type(Unsigned32):
    """Custom type tnSysHealthCareCheckPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysHealthCareCheckPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysHealthCareCheckPercentCompleted_Object = MibScalar
tnSysHealthCareCheckPercentCompleted = _TnSysHealthCareCheckPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 4),
    _TnSysHealthCareCheckPercentCompleted_Type()
)
tnSysHealthCareCheckPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckPercentCompleted.setStatus("current")


class _TnSysHealthCareCheckStatus_Type(Integer32):
    """Custom type tnSysHealthCareCheckStatus based on Integer32"""
    defaultValue = 4

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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("none", 4))
    )


_TnSysHealthCareCheckStatus_Type.__name__ = "Integer32"
_TnSysHealthCareCheckStatus_Object = MibScalar
tnSysHealthCareCheckStatus = _TnSysHealthCareCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 5),
    _TnSysHealthCareCheckStatus_Type()
)
tnSysHealthCareCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckStatus.setStatus("current")


class _TnSysHealthCareCheckResult_Type(Integer32):
    """Custom type tnSysHealthCareCheckResult based on Integer32"""
    defaultValue = 4

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
        *(("ok", 1),
          ("warning", 2),
          ("critical", 3),
          ("none", 4))
    )


_TnSysHealthCareCheckResult_Type.__name__ = "Integer32"
_TnSysHealthCareCheckResult_Object = MibScalar
tnSysHealthCareCheckResult = _TnSysHealthCareCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 6),
    _TnSysHealthCareCheckResult_Type()
)
tnSysHealthCareCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckResult.setStatus("current")


class _TnSysHealthCareCheckScratchDir_Type(SnmpAdminString):
    """Custom type tnSysHealthCareCheckScratchDir based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnSysHealthCareCheckScratchDir_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareCheckScratchDir_Object = MibScalar
tnSysHealthCareCheckScratchDir = _TnSysHealthCareCheckScratchDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 7),
    _TnSysHealthCareCheckScratchDir_Type()
)
tnSysHealthCareCheckScratchDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareCheckScratchDir.setStatus("current")


class _TnSysHealthCareServerIp_Type(IpAddress):
    """Custom type tnSysHealthCareServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysHealthCareServerIp_Type.__name__ = "IpAddress"
_TnSysHealthCareServerIp_Object = MibScalar
tnSysHealthCareServerIp = _TnSysHealthCareServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 8),
    _TnSysHealthCareServerIp_Type()
)
tnSysHealthCareServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerIp.setStatus("current")


class _TnSysHealthCareServerProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnSysHealthCareServerProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnSysHealthCareServerProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnSysHealthCareServerProtocol_Object = MibScalar
tnSysHealthCareServerProtocol = _TnSysHealthCareServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 9),
    _TnSysHealthCareServerProtocol_Type()
)
tnSysHealthCareServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerProtocol.setStatus("current")


class _TnSysHealthCareServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysHealthCareServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysHealthCareServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysHealthCareServerInetAddressType_Object = MibScalar
tnSysHealthCareServerInetAddressType = _TnSysHealthCareServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 10),
    _TnSysHealthCareServerInetAddressType_Type()
)
tnSysHealthCareServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerInetAddressType.setStatus("current")


class _TnSysHealthCareServerInetAddress_Type(InetAddress):
    """Custom type tnSysHealthCareServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysHealthCareServerInetAddress_Type.__name__ = "InetAddress"
_TnSysHealthCareServerInetAddress_Object = MibScalar
tnSysHealthCareServerInetAddress = _TnSysHealthCareServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 11),
    _TnSysHealthCareServerInetAddress_Type()
)
tnSysHealthCareServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerInetAddress.setStatus("current")


class _TnSysHealthCareServerPort_Type(Unsigned32):
    """Custom type tnSysHealthCareServerPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysHealthCareServerPort_Type.__name__ = "Unsigned32"
_TnSysHealthCareServerPort_Object = MibScalar
tnSysHealthCareServerPort = _TnSysHealthCareServerPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 12),
    _TnSysHealthCareServerPort_Type()
)
tnSysHealthCareServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerPort.setStatus("current")


class _TnSysHealthCareServerUserId_Type(SnmpAdminString):
    """Custom type tnSysHealthCareServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysHealthCareServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareServerUserId_Object = MibScalar
tnSysHealthCareServerUserId = _TnSysHealthCareServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 13),
    _TnSysHealthCareServerUserId_Type()
)
tnSysHealthCareServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerUserId.setStatus("current")


class _TnSysHealthCareServerPassword_Type(SnmpAdminString):
    """Custom type tnSysHealthCareServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysHealthCareServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareServerPassword_Object = MibScalar
tnSysHealthCareServerPassword = _TnSysHealthCareServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 14),
    _TnSysHealthCareServerPassword_Type()
)
tnSysHealthCareServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerPassword.setStatus("current")


class _TnSysHealthCareServerLocation_Type(SnmpAdminString):
    """Custom type tnSysHealthCareServerLocation based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysHealthCareServerLocation_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareServerLocation_Object = MibScalar
tnSysHealthCareServerLocation = _TnSysHealthCareServerLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 15),
    _TnSysHealthCareServerLocation_Type()
)
tnSysHealthCareServerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareServerLocation.setStatus("current")


class _TnSysHealthCareTransferCommand_Type(Integer32):
    """Custom type tnSysHealthCareTransferCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("transfer", 2),
          ("abort", 3))
    )


_TnSysHealthCareTransferCommand_Type.__name__ = "Integer32"
_TnSysHealthCareTransferCommand_Object = MibScalar
tnSysHealthCareTransferCommand = _TnSysHealthCareTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 16),
    _TnSysHealthCareTransferCommand_Type()
)
tnSysHealthCareTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareTransferCommand.setStatus("current")


class _TnSysHealthCareTransferPercentCompleted_Type(Unsigned32):
    """Custom type tnSysHealthCareTransferPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysHealthCareTransferPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysHealthCareTransferPercentCompleted_Object = MibScalar
tnSysHealthCareTransferPercentCompleted = _TnSysHealthCareTransferPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 17),
    _TnSysHealthCareTransferPercentCompleted_Type()
)
tnSysHealthCareTransferPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareTransferPercentCompleted.setStatus("current")


class _TnSysHealthCareTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysHealthCareTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysHealthCareTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysHealthCareTransferStatus_Object = MibScalar
tnSysHealthCareTransferStatus = _TnSysHealthCareTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 18),
    _TnSysHealthCareTransferStatus_Type()
)
tnSysHealthCareTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareTransferStatus.setStatus("current")


class _TnSysHealthCareTransferLastFile_Type(SnmpAdminString):
    """Custom type tnSysHealthCareTransferLastFile based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysHealthCareTransferLastFile_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareTransferLastFile_Object = MibScalar
tnSysHealthCareTransferLastFile = _TnSysHealthCareTransferLastFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 19),
    _TnSysHealthCareTransferLastFile_Type()
)
tnSysHealthCareTransferLastFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareTransferLastFile.setStatus("current")


class _TnSysHealthCareLastOperation_Type(Integer32):
    """Custom type tnSysHealthCareLastOperation based on Integer32"""
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
        *(("none", 1),
          ("check", 2),
          ("transfer", 3))
    )


_TnSysHealthCareLastOperation_Type.__name__ = "Integer32"
_TnSysHealthCareLastOperation_Object = MibScalar
tnSysHealthCareLastOperation = _TnSysHealthCareLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 20),
    _TnSysHealthCareLastOperation_Type()
)
tnSysHealthCareLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHealthCareLastOperation.setStatus("current")


class _TnSysHealthCareSetCriteriaTcId_Type(SnmpAdminString):
    """Custom type tnSysHealthCareSetCriteriaTcId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysHealthCareSetCriteriaTcId_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareSetCriteriaTcId_Object = MibScalar
tnSysHealthCareSetCriteriaTcId = _TnSysHealthCareSetCriteriaTcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 21),
    _TnSysHealthCareSetCriteriaTcId_Type()
)
tnSysHealthCareSetCriteriaTcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareSetCriteriaTcId.setStatus("current")


class _TnSysHealthCareSetCriteria_Type(SnmpAdminString):
    """Custom type tnSysHealthCareSetCriteria based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSysHealthCareSetCriteria_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareSetCriteria_Object = MibScalar
tnSysHealthCareSetCriteria = _TnSysHealthCareSetCriteria_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 22),
    _TnSysHealthCareSetCriteria_Type()
)
tnSysHealthCareSetCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareSetCriteria.setStatus("current")


class _TnSysHealthCareDeleteCriteriaTcId_Type(SnmpAdminString):
    """Custom type tnSysHealthCareDeleteCriteriaTcId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysHealthCareDeleteCriteriaTcId_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareDeleteCriteriaTcId_Object = MibScalar
tnSysHealthCareDeleteCriteriaTcId = _TnSysHealthCareDeleteCriteriaTcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 23),
    _TnSysHealthCareDeleteCriteriaTcId_Type()
)
tnSysHealthCareDeleteCriteriaTcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareDeleteCriteriaTcId.setStatus("current")


class _TnSysHealthCareDeleteCriteria_Type(SnmpAdminString):
    """Custom type tnSysHealthCareDeleteCriteria based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnSysHealthCareDeleteCriteria_Type.__name__ = "SnmpAdminString"
_TnSysHealthCareDeleteCriteria_Object = MibScalar
tnSysHealthCareDeleteCriteria = _TnSysHealthCareDeleteCriteria_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 24),
    _TnSysHealthCareDeleteCriteria_Type()
)
tnSysHealthCareDeleteCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareDeleteCriteria.setStatus("current")


class _TnSysHealthCareApplyCriteriaCommand_Type(Integer32):
    """Custom type tnSysHealthCareApplyCriteriaCommand based on Integer32"""
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
        *(("none", 1),
          ("apply", 2),
          ("resetToDefault", 3))
    )


_TnSysHealthCareApplyCriteriaCommand_Type.__name__ = "Integer32"
_TnSysHealthCareApplyCriteriaCommand_Object = MibScalar
tnSysHealthCareApplyCriteriaCommand = _TnSysHealthCareApplyCriteriaCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 41, 25),
    _TnSysHealthCareApplyCriteriaCommand_Type()
)
tnSysHealthCareApplyCriteriaCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysHealthCareApplyCriteriaCommand.setStatus("current")
_TnSysTrapThrottling_ObjectIdentity = ObjectIdentity
tnSysTrapThrottling = _TnSysTrapThrottling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42)
)


class _TnSysTrapThrottlingStatus_Type(AluWdmDisabledEnabled):
    """Custom type tnSysTrapThrottlingStatus based on AluWdmDisabledEnabled"""
    defaultValue = 1


_TnSysTrapThrottlingStatus_Type.__name__ = "AluWdmDisabledEnabled"
_TnSysTrapThrottlingStatus_Object = MibScalar
tnSysTrapThrottlingStatus = _TnSysTrapThrottlingStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 1),
    _TnSysTrapThrottlingStatus_Type()
)
tnSysTrapThrottlingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingStatus.setStatus("current")


class _TnSysTrapThrottlingThreshold1_Type(Unsigned32):
    """Custom type tnSysTrapThrottlingThreshold1 based on Unsigned32"""
    defaultValue = 20


_TnSysTrapThrottlingThreshold1_Type.__name__ = "Unsigned32"
_TnSysTrapThrottlingThreshold1_Object = MibScalar
tnSysTrapThrottlingThreshold1 = _TnSysTrapThrottlingThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 2),
    _TnSysTrapThrottlingThreshold1_Type()
)
tnSysTrapThrottlingThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingThreshold1.setStatus("current")


class _TnSysTrapThrottlingThreshold2_Type(Unsigned32):
    """Custom type tnSysTrapThrottlingThreshold2 based on Unsigned32"""
    defaultValue = 20


_TnSysTrapThrottlingThreshold2_Type.__name__ = "Unsigned32"
_TnSysTrapThrottlingThreshold2_Object = MibScalar
tnSysTrapThrottlingThreshold2 = _TnSysTrapThrottlingThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 3),
    _TnSysTrapThrottlingThreshold2_Type()
)
tnSysTrapThrottlingThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingThreshold2.setStatus("current")


class _TnSysTrapThrottlingThreshold3_Type(Unsigned32):
    """Custom type tnSysTrapThrottlingThreshold3 based on Unsigned32"""
    defaultValue = 20


_TnSysTrapThrottlingThreshold3_Type.__name__ = "Unsigned32"
_TnSysTrapThrottlingThreshold3_Object = MibScalar
tnSysTrapThrottlingThreshold3 = _TnSysTrapThrottlingThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 4),
    _TnSysTrapThrottlingThreshold3_Type()
)
tnSysTrapThrottlingThreshold3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingThreshold3.setStatus("current")


class _TnSysTrapThrottlingTimeOverThreshold_Type(Unsigned32):
    """Custom type tnSysTrapThrottlingTimeOverThreshold based on Unsigned32"""
    defaultValue = 5


_TnSysTrapThrottlingTimeOverThreshold_Type.__name__ = "Unsigned32"
_TnSysTrapThrottlingTimeOverThreshold_Object = MibScalar
tnSysTrapThrottlingTimeOverThreshold = _TnSysTrapThrottlingTimeOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 5),
    _TnSysTrapThrottlingTimeOverThreshold_Type()
)
tnSysTrapThrottlingTimeOverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingTimeOverThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingTimeOverThreshold.setUnits("seconds")


class _TnSysTrapThrottlingTimeUnderThreshold_Type(Unsigned32):
    """Custom type tnSysTrapThrottlingTimeUnderThreshold based on Unsigned32"""
    defaultValue = 20


_TnSysTrapThrottlingTimeUnderThreshold_Type.__name__ = "Unsigned32"
_TnSysTrapThrottlingTimeUnderThreshold_Object = MibScalar
tnSysTrapThrottlingTimeUnderThreshold = _TnSysTrapThrottlingTimeUnderThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 6),
    _TnSysTrapThrottlingTimeUnderThreshold_Type()
)
tnSysTrapThrottlingTimeUnderThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingTimeUnderThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingTimeUnderThreshold.setUnits("seconds")


class _TnSysTrapThrottlingState_Type(TruthValue):
    """Custom type tnSysTrapThrottlingState based on TruthValue"""
    defaultValue = 2


_TnSysTrapThrottlingState_Type.__name__ = "TruthValue"
_TnSysTrapThrottlingState_Object = MibScalar
tnSysTrapThrottlingState = _TnSysTrapThrottlingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 42, 7),
    _TnSysTrapThrottlingState_Type()
)
tnSysTrapThrottlingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTrapThrottlingState.setStatus("current")
_TnSysNmsObjs_ObjectIdentity = ObjectIdentity
tnSysNmsObjs = _TnSysNmsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43)
)
_TnSysNmsIpListTable_Object = MibTable
tnSysNmsIpListTable = _TnSysNmsIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1)
)
if mibBuilder.loadTexts:
    tnSysNmsIpListTable.setStatus("current")
_TnSysNmsIpListEntry_Object = MibTableRow
tnSysNmsIpListEntry = _TnSysNmsIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1)
)
tnSysNmsIpListEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNmsIpListIndex"),
)
if mibBuilder.loadTexts:
    tnSysNmsIpListEntry.setStatus("current")
_TnSysNmsIpListIndex_Type = OctetString
_TnSysNmsIpListIndex_Object = MibTableColumn
tnSysNmsIpListIndex = _TnSysNmsIpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1, 1),
    _TnSysNmsIpListIndex_Type()
)
tnSysNmsIpListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNmsIpListIndex.setStatus("current")
_TnSysNmsIpListRowStatus_Type = RowStatus
_TnSysNmsIpListRowStatus_Object = MibTableColumn
tnSysNmsIpListRowStatus = _TnSysNmsIpListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1, 2),
    _TnSysNmsIpListRowStatus_Type()
)
tnSysNmsIpListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNmsIpListRowStatus.setStatus("current")


class _TnSysNmsIpListIpAddress_Type(IpAddress):
    """Custom type tnSysNmsIpListIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysNmsIpListIpAddress_Type.__name__ = "IpAddress"
_TnSysNmsIpListIpAddress_Object = MibTableColumn
tnSysNmsIpListIpAddress = _TnSysNmsIpListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1, 3),
    _TnSysNmsIpListIpAddress_Type()
)
tnSysNmsIpListIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNmsIpListIpAddress.setStatus("current")


class _TnSysNmsIpListInetAddress_Type(InetAddress):
    """Custom type tnSysNmsIpListInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysNmsIpListInetAddress_Type.__name__ = "InetAddress"
_TnSysNmsIpListInetAddress_Object = MibTableColumn
tnSysNmsIpListInetAddress = _TnSysNmsIpListInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1, 4),
    _TnSysNmsIpListInetAddress_Type()
)
tnSysNmsIpListInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNmsIpListInetAddress.setStatus("current")


class _TnSysNmsIpListInetAddressType_Type(InetAddressType):
    """Custom type tnSysNmsIpListInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysNmsIpListInetAddressType_Type.__name__ = "InetAddressType"
_TnSysNmsIpListInetAddressType_Object = MibTableColumn
tnSysNmsIpListInetAddressType = _TnSysNmsIpListInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 43, 1, 1, 5),
    _TnSysNmsIpListInetAddressType_Type()
)
tnSysNmsIpListInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNmsIpListInetAddressType.setStatus("current")
_TnSysDnsServer_ObjectIdentity = ObjectIdentity
tnSysDnsServer = _TnSysDnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44)
)
_TnSysDnsServerTable_Object = MibTable
tnSysDnsServerTable = _TnSysDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1)
)
if mibBuilder.loadTexts:
    tnSysDnsServerTable.setStatus("current")
_TnSysDnsServerEntry_Object = MibTableRow
tnSysDnsServerEntry = _TnSysDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1, 1)
)
tnSysDnsServerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysDnsServerIndex"),
)
if mibBuilder.loadTexts:
    tnSysDnsServerEntry.setStatus("current")
_TnSysDnsServerIndex_Type = Unsigned32
_TnSysDnsServerIndex_Object = MibTableColumn
tnSysDnsServerIndex = _TnSysDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1, 1, 1),
    _TnSysDnsServerIndex_Type()
)
tnSysDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysDnsServerIndex.setStatus("current")


class _TnSysDnsServerIpAddress_Type(IpAddress):
    """Custom type tnSysDnsServerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysDnsServerIpAddress_Type.__name__ = "IpAddress"
_TnSysDnsServerIpAddress_Object = MibTableColumn
tnSysDnsServerIpAddress = _TnSysDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1, 1, 2),
    _TnSysDnsServerIpAddress_Type()
)
tnSysDnsServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysDnsServerIpAddress.setStatus("current")


class _TnSysDnsServerInetAddress_Type(InetAddress):
    """Custom type tnSysDnsServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysDnsServerInetAddress_Type.__name__ = "InetAddress"
_TnSysDnsServerInetAddress_Object = MibTableColumn
tnSysDnsServerInetAddress = _TnSysDnsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1, 1, 3),
    _TnSysDnsServerInetAddress_Type()
)
tnSysDnsServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysDnsServerInetAddress.setStatus("current")


class _TnSysDnsServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysDnsServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysDnsServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysDnsServerInetAddressType_Object = MibTableColumn
tnSysDnsServerInetAddressType = _TnSysDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 44, 1, 1, 4),
    _TnSysDnsServerInetAddressType_Type()
)
tnSysDnsServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysDnsServerInetAddressType.setStatus("current")
_TnTransferPMDiscovery_ObjectIdentity = ObjectIdentity
tnTransferPMDiscovery = _TnTransferPMDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45)
)
_TnTransferPMDiscoveryTable_Object = MibTable
tnTransferPMDiscoveryTable = _TnTransferPMDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1)
)
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryTable.setStatus("current")
_TnTransferPMDiscoveryEntry_Object = MibTableRow
tnTransferPMDiscoveryEntry = _TnTransferPMDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1)
)
tnTransferPMDiscoveryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryEntry.setStatus("current")
_TnTransferPMDiscoveryIndex_Type = SnmpAdminString
_TnTransferPMDiscoveryIndex_Object = MibTableColumn
tnTransferPMDiscoveryIndex = _TnTransferPMDiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 1),
    _TnTransferPMDiscoveryIndex_Type()
)
tnTransferPMDiscoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryIndex.setStatus("current")
_TnTransferPMDiscoveryRowStatus_Type = RowStatus
_TnTransferPMDiscoveryRowStatus_Object = MibTableColumn
tnTransferPMDiscoveryRowStatus = _TnTransferPMDiscoveryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 2),
    _TnTransferPMDiscoveryRowStatus_Type()
)
tnTransferPMDiscoveryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryRowStatus.setStatus("current")


class _TnTransferPMDiscoveryFilename_Type(SnmpAdminString):
    """Custom type tnTransferPMDiscoveryFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnTransferPMDiscoveryFilename_Type.__name__ = "SnmpAdminString"
_TnTransferPMDiscoveryFilename_Object = MibTableColumn
tnTransferPMDiscoveryFilename = _TnTransferPMDiscoveryFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 3),
    _TnTransferPMDiscoveryFilename_Type()
)
tnTransferPMDiscoveryFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryFilename.setStatus("current")


class _TnTransferPMDiscoveryControl_Type(Integer32):
    """Custom type tnTransferPMDiscoveryControl based on Integer32"""
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
        *(("noCmd", 1),
          ("start", 2),
          ("abort", 3))
    )


_TnTransferPMDiscoveryControl_Type.__name__ = "Integer32"
_TnTransferPMDiscoveryControl_Object = MibTableColumn
tnTransferPMDiscoveryControl = _TnTransferPMDiscoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 4),
    _TnTransferPMDiscoveryControl_Type()
)
tnTransferPMDiscoveryControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryControl.setStatus("current")


class _TnTransferPMDiscoveryStatus_Type(Integer32):
    """Custom type tnTransferPMDiscoveryStatus based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnTransferPMDiscoveryStatus_Type.__name__ = "Integer32"
_TnTransferPMDiscoveryStatus_Object = MibTableColumn
tnTransferPMDiscoveryStatus = _TnTransferPMDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 5),
    _TnTransferPMDiscoveryStatus_Type()
)
tnTransferPMDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryStatus.setStatus("current")


class _TnTransferPMDiscoveryErrorCode_Type(Integer32):
    """Custom type tnTransferPMDiscoveryErrorCode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("unknown", 2),
          ("timeout", 3),
          ("serverError", 4),
          ("networkError", 5),
          ("fileSystemError", 6),
          ("statsBinsRolled", 7))
    )


_TnTransferPMDiscoveryErrorCode_Type.__name__ = "Integer32"
_TnTransferPMDiscoveryErrorCode_Object = MibTableColumn
tnTransferPMDiscoveryErrorCode = _TnTransferPMDiscoveryErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 6),
    _TnTransferPMDiscoveryErrorCode_Type()
)
tnTransferPMDiscoveryErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryErrorCode.setStatus("current")


class _TnTransferPMDiscoveryServerProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnTransferPMDiscoveryServerProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnTransferPMDiscoveryServerProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnTransferPMDiscoveryServerProtocol_Object = MibTableColumn
tnTransferPMDiscoveryServerProtocol = _TnTransferPMDiscoveryServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 7),
    _TnTransferPMDiscoveryServerProtocol_Type()
)
tnTransferPMDiscoveryServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerProtocol.setStatus("current")


class _TnTransferPMDiscoveryServerIp_Type(IpAddress):
    """Custom type tnTransferPMDiscoveryServerIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnTransferPMDiscoveryServerIp_Type.__name__ = "IpAddress"
_TnTransferPMDiscoveryServerIp_Object = MibTableColumn
tnTransferPMDiscoveryServerIp = _TnTransferPMDiscoveryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 8),
    _TnTransferPMDiscoveryServerIp_Type()
)
tnTransferPMDiscoveryServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerIp.setStatus("current")


class _TnTransferPMDiscoveryServerUserId_Type(SnmpAdminString):
    """Custom type tnTransferPMDiscoveryServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnTransferPMDiscoveryServerUserId_Type.__name__ = "SnmpAdminString"
_TnTransferPMDiscoveryServerUserId_Object = MibTableColumn
tnTransferPMDiscoveryServerUserId = _TnTransferPMDiscoveryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 9),
    _TnTransferPMDiscoveryServerUserId_Type()
)
tnTransferPMDiscoveryServerUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerUserId.setStatus("current")


class _TnTransferPMDiscoveryServerPassword_Type(SnmpAdminString):
    """Custom type tnTransferPMDiscoveryServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnTransferPMDiscoveryServerPassword_Type.__name__ = "SnmpAdminString"
_TnTransferPMDiscoveryServerPassword_Object = MibTableColumn
tnTransferPMDiscoveryServerPassword = _TnTransferPMDiscoveryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 10),
    _TnTransferPMDiscoveryServerPassword_Type()
)
tnTransferPMDiscoveryServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerPassword.setStatus("current")


class _TnTransferPMDiscoveryServerInetAddressType_Type(InetAddressType):
    """Custom type tnTransferPMDiscoveryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnTransferPMDiscoveryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnTransferPMDiscoveryServerInetAddressType_Object = MibTableColumn
tnTransferPMDiscoveryServerInetAddressType = _TnTransferPMDiscoveryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 11),
    _TnTransferPMDiscoveryServerInetAddressType_Type()
)
tnTransferPMDiscoveryServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerInetAddressType.setStatus("current")


class _TnTransferPMDiscoveryServerInetAddress_Type(InetAddress):
    """Custom type tnTransferPMDiscoveryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnTransferPMDiscoveryServerInetAddress_Type.__name__ = "InetAddress"
_TnTransferPMDiscoveryServerInetAddress_Object = MibTableColumn
tnTransferPMDiscoveryServerInetAddress = _TnTransferPMDiscoveryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 12),
    _TnTransferPMDiscoveryServerInetAddress_Type()
)
tnTransferPMDiscoveryServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryServerInetAddress.setStatus("current")


class _TnTransferPMDiscoveryPort_Type(Unsigned32):
    """Custom type tnTransferPMDiscoveryPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnTransferPMDiscoveryPort_Type.__name__ = "Unsigned32"
_TnTransferPMDiscoveryPort_Object = MibTableColumn
tnTransferPMDiscoveryPort = _TnTransferPMDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 13),
    _TnTransferPMDiscoveryPort_Type()
)
tnTransferPMDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryPort.setStatus("current")


class _TnTransferPMDiscoveryPrevious15minBinFilesTransfer_Type(Unsigned32):
    """Custom type tnTransferPMDiscoveryPrevious15minBinFilesTransfer based on Unsigned32"""
    defaultValue = 0


_TnTransferPMDiscoveryPrevious15minBinFilesTransfer_Type.__name__ = "Unsigned32"
_TnTransferPMDiscoveryPrevious15minBinFilesTransfer_Object = MibTableColumn
tnTransferPMDiscoveryPrevious15minBinFilesTransfer = _TnTransferPMDiscoveryPrevious15minBinFilesTransfer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 14),
    _TnTransferPMDiscoveryPrevious15minBinFilesTransfer_Type()
)
tnTransferPMDiscoveryPrevious15minBinFilesTransfer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryPrevious15minBinFilesTransfer.setStatus("current")


class _TnTransferPMDiscoveryPrevious1dayBinFilesTransfer_Type(Unsigned32):
    """Custom type tnTransferPMDiscoveryPrevious1dayBinFilesTransfer based on Unsigned32"""
    defaultValue = 0


_TnTransferPMDiscoveryPrevious1dayBinFilesTransfer_Type.__name__ = "Unsigned32"
_TnTransferPMDiscoveryPrevious1dayBinFilesTransfer_Object = MibTableColumn
tnTransferPMDiscoveryPrevious1dayBinFilesTransfer = _TnTransferPMDiscoveryPrevious1dayBinFilesTransfer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 15),
    _TnTransferPMDiscoveryPrevious1dayBinFilesTransfer_Type()
)
tnTransferPMDiscoveryPrevious1dayBinFilesTransfer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryPrevious1dayBinFilesTransfer.setStatus("current")


class _TnTransferPMDiscoveryTransferTimeOffset_Type(Unsigned32):
    """Custom type tnTransferPMDiscoveryTransferTimeOffset based on Unsigned32"""
    defaultValue = 0


_TnTransferPMDiscoveryTransferTimeOffset_Type.__name__ = "Unsigned32"
_TnTransferPMDiscoveryTransferTimeOffset_Object = MibTableColumn
tnTransferPMDiscoveryTransferTimeOffset = _TnTransferPMDiscoveryTransferTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 16),
    _TnTransferPMDiscoveryTransferTimeOffset_Type()
)
tnTransferPMDiscoveryTransferTimeOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryTransferTimeOffset.setStatus("current")


class _TnTransferPMDiscovery15minBinFileTransferCount_Type(Unsigned32):
    """Custom type tnTransferPMDiscovery15minBinFileTransferCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnTransferPMDiscovery15minBinFileTransferCount_Type.__name__ = "Unsigned32"
_TnTransferPMDiscovery15minBinFileTransferCount_Object = MibTableColumn
tnTransferPMDiscovery15minBinFileTransferCount = _TnTransferPMDiscovery15minBinFileTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 17),
    _TnTransferPMDiscovery15minBinFileTransferCount_Type()
)
tnTransferPMDiscovery15minBinFileTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscovery15minBinFileTransferCount.setStatus("current")


class _TnTransferPMDiscovery1dayBinFileTransferCount_Type(Unsigned32):
    """Custom type tnTransferPMDiscovery1dayBinFileTransferCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnTransferPMDiscovery1dayBinFileTransferCount_Type.__name__ = "Unsigned32"
_TnTransferPMDiscovery1dayBinFileTransferCount_Object = MibTableColumn
tnTransferPMDiscovery1dayBinFileTransferCount = _TnTransferPMDiscovery1dayBinFileTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 18),
    _TnTransferPMDiscovery1dayBinFileTransferCount_Type()
)
tnTransferPMDiscovery1dayBinFileTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscovery1dayBinFileTransferCount.setStatus("current")


class _TnTransferPMDiscovery15minBinFileTransferFailureCount_Type(Unsigned32):
    """Custom type tnTransferPMDiscovery15minBinFileTransferFailureCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnTransferPMDiscovery15minBinFileTransferFailureCount_Type.__name__ = "Unsigned32"
_TnTransferPMDiscovery15minBinFileTransferFailureCount_Object = MibTableColumn
tnTransferPMDiscovery15minBinFileTransferFailureCount = _TnTransferPMDiscovery15minBinFileTransferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 19),
    _TnTransferPMDiscovery15minBinFileTransferFailureCount_Type()
)
tnTransferPMDiscovery15minBinFileTransferFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscovery15minBinFileTransferFailureCount.setStatus("current")


class _TnTransferPMDiscovery1dayBinFileTransferFailureCount_Type(Unsigned32):
    """Custom type tnTransferPMDiscovery1dayBinFileTransferFailureCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnTransferPMDiscovery1dayBinFileTransferFailureCount_Type.__name__ = "Unsigned32"
_TnTransferPMDiscovery1dayBinFileTransferFailureCount_Object = MibTableColumn
tnTransferPMDiscovery1dayBinFileTransferFailureCount = _TnTransferPMDiscovery1dayBinFileTransferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 45, 1, 1, 20),
    _TnTransferPMDiscovery1dayBinFileTransferFailureCount_Type()
)
tnTransferPMDiscovery1dayBinFileTransferFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTransferPMDiscovery1dayBinFileTransferFailureCount.setStatus("current")
snmpTargetAddrEntry.registerAugmentions(
    ("TROPIC-SYSTEM-MIB",
     "tnSnmpTargetAddrEntry")
)
tnSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

tnSystemBasicsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 1)
)
tnSystemBasicsGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDescr"),
        ("TROPIC-SYSTEM-MIB", "tnSysTelnetPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysHttpPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysDateAndTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysReset"),
        ("TROPIC-SYSTEM-MIB", "tnSysMIBVersion"),
        ("TROPIC-SYSTEM-MIB", "tnSysRingID"),
        ("TROPIC-SYSTEM-MIB", "tnSysNetworkElementID"),
        ("TROPIC-SYSTEM-MIB", "tnSysAINSDebounceTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysSonetSdhMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysAlarmReportingControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysWavelengthTrackerWaveKeySpace"),
        ("TROPIC-SYSTEM-MIB", "tnSysSecureMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysExtendedTemperatureRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysTemperatureInCelsius"),
        ("TROPIC-SYSTEM-MIB", "tnSysName"),
        ("TROPIC-SYSTEM-MIB", "tnSysEquipmentControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysFirstLevelControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysMatrix0CompactCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysUniversalMatrixFirstLevelControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimeOffsetTimeZone"),
        ("TROPIC-SYSTEM-MIB", "tnSysFipsSquelchMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrListOfFileNames"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrFileCounts"),
        ("TROPIC-SYSTEM-MIB", "tnSysAltitude"),
        ("TROPIC-SYSTEM-MIB", "tnSysThermalShutdownAutotimer"),
        ("TROPIC-SYSTEM-MIB", "tnSysDisplayShelfLabel"),
        ("TROPIC-SYSTEM-MIB", "tnSysPMFineGranularityControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFmRead"),
        ("TROPIC-SYSTEM-MIB", "tnSysPMStreamingServerControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysSlotMigrationControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFlexGridClusterOcsAddDropEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysFilterCheckTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysCNLinkPhysicalIfIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSysUserlabel"),
        ("TROPIC-SYSTEM-MIB", "tnSysOpenAgentControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysUnkeyedDanglingOchAddDropEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysNetWorkTraceV3SecurityUser"),
        ("TROPIC-SYSTEM-MIB", "tnSysScotV3SecurityUser"),
        ("TROPIC-SYSTEM-MIB", "tnSysTL1Enable"),
        ("TROPIC-SYSTEM-MIB", "tnSysLMEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysAlienChannelLicensingEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebug"),
        ("TROPIC-SYSTEM-MIB", "tnSysClusterV3SecurityUser"),
        ("TROPIC-SYSTEM-MIB", "tnSysSyncMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysPMMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysShelfLatitude"),
        ("TROPIC-SYSTEM-MIB", "tnSysShelfLongitude"),
        ("TROPIC-SYSTEM-MIB", "tnSysAlmProfName"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpAsn"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpLocalRouterId"),
        ("TROPIC-SYSTEM-MIB", "tnSysNodeIdLabel"),
        ("TROPIC-SYSTEM-MIB", "tnSysNodeNumber"),
        ("TROPIC-SYSTEM-MIB", "tnSysNodeCLLI"),
        ("TROPIC-SYSTEM-MIB", "tnSysNodeTemplate"),
        ("TROPIC-SYSTEM-MIB", "tnSysCustomerApplicationMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysMDCli"),
        ("TROPIC-SYSTEM-MIB", "tnSysMultiShelfMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysMultiShelfConfigList"),
        ("TROPIC-SYSTEM-MIB", "tnSysMultiShelfUnknownList"),
        ("TROPIC-SYSTEM-MIB", "tnSysMultiShelfMissingList"),
        ("TROPIC-SYSTEM-MIB", "tnSysPrompt"),
        ("TROPIC-SYSTEM-MIB", "tnSysPromptType"),
        ("TROPIC-SYSTEM-MIB", "tnSysShelfAltitude"),
        ("TROPIC-SYSTEM-MIB", "tnSysTacacsSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysRadiusSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSftpSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysHttpSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysHttpsSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSnmpSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSyslogSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysAutoTurnUpActiveTemplate"),
        ("TROPIC-SYSTEM-MIB", "tnSysAuthenticationOrder"),
        ("TROPIC-SYSTEM-MIB", "tnSysAuthRejectOption"),
        ("TROPIC-SYSTEM-MIB", "tnSysAutoTurnUpActiveTemplateForce"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeatureAutoTurnUp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDelayResetNE"),
        ("TROPIC-SYSTEM-MIB", "tnSysDelayReboot"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsUserName"),
        ("TROPIC-SYSTEM-MIB", "tnSysVersionPatchId"),
        ("TROPIC-SYSTEM-MIB", "tnSysVersionPatchDescr"),
        ("TROPIC-SYSTEM-MIB", "tnSysCustomerLifeCycleState"),
        ("TROPIC-SYSTEM-MIB", "tnSysUSBInstall"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsIpVerifyState"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcspSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysDnsSourceIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtcWaitTimeAfterPowerChange"),
        ("TROPIC-SYSTEM-MIB", "tnSysDHCPClassName"),
        ("TROPIC-SYSTEM-MIB", "tnSysDHCPMatchString"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyLicense"),
        ("TROPIC-SYSTEM-MIB", "tnSysHwIfMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNextIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNextIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSysDHCPClass"),
        ("TROPIC-SYSTEM-MIB", "tnSysProtocolIpMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysMultiShelfAvailableList"),
        ("TROPIC-SYSTEM-MIB", "tnSysPerformanceMemoryTotal"),
        ("TROPIC-SYSTEM-MIB", "tnSysPerformanceMemoryUsed"),
        ("TROPIC-SYSTEM-MIB", "tnSysPerformanceMemoryUsedPercentage"),
        ("TROPIC-SYSTEM-MIB", "tnSysPerformanceTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysPerformanceCPUStatsPercentages"),
        ("TROPIC-SYSTEM-MIB", "tnSysPower"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertExpiration"),
        ("TROPIC-SYSTEM-MIB", "tnSysNumOspfV2AreaIndependentLsas"),
        ("TROPIC-SYSTEM-MIB", "tnSysNumOspfV3AreaIndependentLsas"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpAdminDistance"))
)
if mibBuilder.loadTexts:
    tnSystemBasicsGroup.setStatus("current")

tnSystemControlNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 2)
)
tnSystemControlNetworkGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysSubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSource"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcsIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcs2IpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcs3IpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs1LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs2LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs3LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSource"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredLoopbackIp1"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredLoopbackIp1SubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSource1"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSource1"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoopbackIpAddress1"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoopbackIp1SubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredPrefixLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp1Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp2Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp3Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSourceIPv6"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSourceIPv6"))
)
if mibBuilder.loadTexts:
    tnSystemControlNetworkGroup.setStatus("current")

tnSystemRedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 3)
)
tnSystemRedundancyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbSynchState"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbResynch"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbAudit"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbClear"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyActiveCCSlot"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbInvalid"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyMateCCReadyToProtect"))
)
if mibBuilder.loadTexts:
    tnSystemRedundancyGroup.setStatus("current")

tnSystemDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 4)
)
tnSystemDiscoveryGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDiscoveryFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryErrorCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryBinnedStatsInterval"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryBinnedStatsBin"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryPrevious15minBinFilesTransfer"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryPrevious1dayBinFilesTransfer"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryTransferTimeOffset"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryTransferTraps"))
)
if mibBuilder.loadTexts:
    tnSystemDiscoveryGroup.setStatus("current")

tnSystemLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 5)
)
tnSystemLoggingGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLoggingCLI"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoggingSNMP"))
)
if mibBuilder.loadTexts:
    tnSystemLoggingGroup.setStatus("current")

tnSystemBackupAndRestoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 6)
)
tnSystemBackupAndRestoreGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestorePercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFileTimeStamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestorePassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFileCrc"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLocalInfo"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLocalDelete"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestorePort"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreFallBackTimeStamp"))
)
if mibBuilder.loadTexts:
    tnSystemBackupAndRestoreGroup.setStatus("current")

tnSysNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 7)
)
tnSysNtpGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpSynched"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpDriftString"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpTimeOffsetString"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpClockMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysNtpGroup.setStatus("current")

tnSysNtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 8)
)
tnSysNtpServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerKeyIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerInetAddressType"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerGroup.setStatus("current")

tnSnmpTargetAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 9)
)
tnSnmpTargetAddressGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddrNmsStationGroupId"),
        ("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddrTrapGroupId"),
        ("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddrDisableTrap"))
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddressGroup.setStatus("current")

tnSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 10)
)
tnSyslogGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSyslogIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogPort"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogFacility"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogPriority"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogProtocol"))
)
if mibBuilder.loadTexts:
    tnSyslogGroup.setStatus("current")

tnSysTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 11)
)
tnSysTimingGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingLastSwitchTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceTimingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceTimingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingActiveReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingClockingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSwitchingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingFreeRunSuppressAlarms"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1FramingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1LineCoding"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1SsmProcessing"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsAClockQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsBClockQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingActiveLineTimingCable"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitSourceType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsAModuleType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsBModuleType"))
)
if mibBuilder.loadTexts:
    tnSysTimingGroup.setStatus("current")

tnSysFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 12)
)
tnSysFeaturesGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysFeatureAutoTopology"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeaturePauseFlowControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeatureIpUtilitiesRestricted"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeatureFastServiceSetup"))
)
if mibBuilder.loadTexts:
    tnSysFeaturesGroup.setStatus("current")

tnSysFaultCorrelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 13)
)
tnSysFaultCorrelationGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysFaultCorrelationTransientSuppression")
)
if mibBuilder.loadTexts:
    tnSysFaultCorrelationGroup.setStatus("current")

tnSysErrorHandlingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 14)
)
tnSysErrorHandlingGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysSetRequestErrorMessage")
)
if mibBuilder.loadTexts:
    tnSysErrorHandlingGroup.setStatus("current")

tnSysSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 15)
)
tnSysSecurityGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysSecurityMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyModulus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshEcdsaKeyModulus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyModulus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemoteIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemoteUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemotePassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCountry"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrState"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrLocality"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrOrganization"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrOrganizationUnit"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCommonName"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrEmailAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertSignatureAlgorithm"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertValidity"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrUploadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertDownloadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertInstallStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSshPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertVerification"),
        ("TROPIC-SYSTEM-MIB", "tnSshPublicKey1"),
        ("TROPIC-SYSTEM-MIB", "tnSshEcdsaPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSshEcdsaPublicKey1"),
        ("TROPIC-SYSTEM-MIB", "tnSshEd25519PublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSshEd25519PublicKey1"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertExpiration"))
)
if mibBuilder.loadTexts:
    tnSysSecurityGroup.setStatus("current")

tnSysTransferLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 16)
)
tnSysTransferLogGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysTransferLogCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastLogFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastFileTimeStamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogWindowStart"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogWindowStop"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogPort"))
)
if mibBuilder.loadTexts:
    tnSysTransferLogGroup.setStatus("current")

tnSysIpAclSysDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 17)
)
tnSysIpAclSysDefaultGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclRxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclTxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSnmpCfgEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclCfgRestoreToDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclClearCounter"))
)
if mibBuilder.loadTexts:
    tnSysIpAclSysDefaultGroup.setStatus("current")

tnSysIpAclPatternScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 18)
)
tnSysIpAclPatternScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternScalarsGroup.setStatus("current")

tnSysIpAclPatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 19)
)
tnSysIpAclPatternGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternICMPERROR"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIpProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIpFragment"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIcmpType"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIcmpCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternTcpEstablish"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSystemDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcPortRangeEnd"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestPortRangeEnd"))
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternGroup.setStatus("current")

tnSysIpAclFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 20)
)
tnSysIpAclFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterScalarsGroup.setStatus("current")

tnSysIpAclFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 21)
)
tnSysIpAclFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterPatternID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterStatCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterGroup.setStatus("current")

tnSysIpAclInterfaceScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 22)
)
tnSysIpAclInterfaceScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceScalarsGroup.setStatus("current")

tnSysIpAclInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 23)
)
tnSysIpAclInterfaceGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceSystemDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterLog"))
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceGroup.setStatus("current")

tnSysNtpServerIdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 24)
)
tnSysNtpServerIdStatsGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsSelect"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsRefId"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsStrtm"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsClockType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsPoll"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsReach"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsDelay"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsOffset"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsJitter"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsKeyIndex"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsGroup.setStatus("current")

tnSysFtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 25)
)
tnSysFtpServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysFtpServerEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerPassword"))
)
if mibBuilder.loadTexts:
    tnSysFtpServerGroup.setStatus("current")

tnSysNtpServerAuthenticationScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 26)
)
tnSysNtpServerAuthenticationScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationScalarsGroup.setStatus("current")

tnSysNtpServerAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 27)
)
tnSysNtpServerAuthenticationGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKey"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationGroup.setStatus("current")

tnSysIpAclNetIfFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 28)
)
tnSysIpAclNetIfFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterScalarsGroup.setStatus("current")

tnSysIpAclNetIfFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 29)
)
tnSysIpAclNetIfFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterGroup.setStatus("current")

tnNeDiscoveryScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 30)
)
tnNeDiscoveryScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryAttributeTotal")
)
if mibBuilder.loadTexts:
    tnNeDiscoveryScalarsGroup.setStatus("current")

tnNeDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 31)
)
tnNeDiscoveryGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnNeDiscoveryFilename"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryControl"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryErrorCode"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerTimeOut"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryDeltaFilename"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryDeltaFileFlag"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryDeltaSyncStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryPort"))
)
if mibBuilder.loadTexts:
    tnNeDiscoveryGroup.setStatus("current")

tnSysOtdrScanSystemProfileScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 32)
)
tnSysOtdrScanSystemProfileScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileScalarsGroup.setStatus("current")

tnSysOtdrScanSystemProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 33)
)
tnSysOtdrScanSystemProfileGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileDescription"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileWaveLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfilePulseLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileResolution"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileAvgTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileEventThreshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileIOR"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileGroup.setStatus("current")

tnSysOtdrScanTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 34)
)
tnSysOtdrScanTransferGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferPort"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferGroup.setStatus("current")

tnClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 35)
)
tnClusterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnClusterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnClusterIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnClusterlinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnClusterInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnClusterInetAddress"))
)
if mibBuilder.loadTexts:
    tnClusterGroup.setStatus("current")

tnSysPmFetchBulkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 36)
)
tnSysPmFetchBulkGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStart"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStatsInterval"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkBinnedStatsBin"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkShelfNum"))
)
if mibBuilder.loadTexts:
    tnSysPmFetchBulkGroup.setStatus("current")

tnSysDebugTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 37)
)
tnSysDebugTransferGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRecentSuccessFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferTimestamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferShelfNum"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferScratchDir"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferIncludeInDumps"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferPort"))
)
if mibBuilder.loadTexts:
    tnSysDebugTransferGroup.setStatus("current")

tnSysLicenseInvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 38)
)
tnSysLicenseInvGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileUploadOper"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvLastOperPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvLastUploadFileName"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileLastUploadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileLastUploadTimeStamp"))
)
if mibBuilder.loadTexts:
    tnSysLicenseInvGroup.setStatus("current")

tnSysLinuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 40)
)
tnSysLinuxGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplUserPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootPasswordStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplPasswordStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplUserStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxLoginInactivityTimeOut"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxSmsUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxSmsUserPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxSmsPasswordStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxSmsUserStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserLocalStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxSecurityCommit"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserPort"))
)
if mibBuilder.loadTexts:
    tnSysLinuxGroup.setStatus("current")

tnSysIpAclIpv6SysDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 41)
)
tnSysIpAclIpv6SysDefaultGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6RxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6TxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6SnmpCfgEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6CfgRestoreToDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIPv6ClearCounter"))
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6SysDefaultGroup.setStatus("current")

tnSysFileInitializationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 42)
)
tnSysFileInitializationGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysFileInitializationRoot"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysFileInitializationGroup.setStatus("current")

tnSysOtdrScanSystemProfileMScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 43)
)
tnSysOtdrScanSystemProfileMScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMScalarsGroup.setStatus("current")

tnSysOtdrScanSystemProfileMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 44)
)
tnSysOtdrScanSystemProfileMGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMDescription"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMWaveLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMPulseLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMResolution"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMAvgTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMEventThreshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMIOR"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileMGroup.setStatus("current")

tnSysSecurityScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 45)
)
tnSysSecurityScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshKeyAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysSecurityScalarsGroup.setStatus("current")

tnSysIpAclIpv6PatternScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 46)
)
tnSysIpAclIpv6PatternScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternScalarsGroup.setStatus("current")

tnSysIpAclIpv6PatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 47)
)
tnSysIpAclIpv6PatternGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternICMPV6ERROR"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternSrcAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternSrcPrefixLen"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternDestAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternDestPrefixLen"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternIpProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternIcmpType"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternIcmpCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternSrcPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternDestPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternIpFragment"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternTcpEstablish"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternSystemDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternSrcPortRangeEnd"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternDestPortRangeEnd"))
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternGroup.setStatus("current")

tnSysIpAclIpv6FilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 48)
)
tnSysIpAclIpv6FilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterScalarsGroup.setStatus("current")

tnSysIpAclIpv6FilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 49)
)
tnSysIpAclIpv6FilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterPatternID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterStatCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterGroup.setStatus("current")

tnSysIpAclIpv6InterfaceScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 50)
)
tnSysIpAclIpv6InterfaceScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceScalarsGroup.setStatus("current")

tnSysIpAclIpv6InterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 51)
)
tnSysIpAclIpv6InterfaceGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceSystemDefault"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterLog"))
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceGroup.setStatus("current")

tnSysIpv6AclNetIfFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 52)
)
tnSysIpv6AclNetIfFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterScalarsGroup.setStatus("current")

tnSysIpv6AclNetIfFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 53)
)
tnSysIpv6AclNetIfFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterGroup.setStatus("current")

tnSysIpAclEthIfFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 54)
)
tnSysIpAclEthIfFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterScalarsGroup.setStatus("current")

tnSysIpAclEthIfFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 55)
)
tnSysIpAclEthIfFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclEthIfFilterGroup.setStatus("current")

tnSysIpv6AclEthIfFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 56)
)
tnSysIpv6AclEthIfFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterScalarsGroup.setStatus("current")

tnSysIpv6AclEthIfFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 57)
)
tnSysIpv6AclEthIfFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpv6AclEthIfFilterGroup.setStatus("current")

tnSysBtInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 58)
)
tnSysBtInterfaceGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceDescription"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceIpAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceIpSubMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceAdminState"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceLinkIntegrityStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceDHCPServer"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceDHCPRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceNodeSerialNum"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceMacAddress"))
)
if mibBuilder.loadTexts:
    tnSysBtInterfaceGroup.setStatus("current")

tnSysOtdrScanResultsTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 59)
)
tnSysOtdrScanResultsTransferGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRecentSuccessFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsLastTransferTimestamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRemoteInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRemoteInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferRemoveFileFromNE"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanResultsTransferGroup.setStatus("current")

tnSysLicenseMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 60)
)
tnSysLicenseMgrGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrKeepAliveTimer"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrPrimaryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrPrimaryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrPrimaryServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrSecondaryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrSecondaryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrSecondaryServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrPrimaryServerStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrSecondaryServerStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrExpiration"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrTimeOut"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrRetries"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrLastRefresh"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrCertStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrNextRefreshTime"))
)
if mibBuilder.loadTexts:
    tnSysLicenseMgrGroup.setStatus("current")

tnLicenseEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 61)
)
tnLicenseEntityGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnLicenseEntityRefreshSet"),
        ("TROPIC-SYSTEM-MIB", "tnLicenseEntityNumberInUse"),
        ("TROPIC-SYSTEM-MIB", "tnLicenseEntityNumberExceedAvail"),
        ("TROPIC-SYSTEM-MIB", "tnLicenseEntityEntitlementNeeded"))
)
if mibBuilder.loadTexts:
    tnLicenseEntityGroup.setStatus("current")

tnSysKeyStoreServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 62)
)
tnSysKeyStoreServiceGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerHost"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerLocation"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreServiceStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreServerLastTransferTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreTransServerURI"))
)
if mibBuilder.loadTexts:
    tnSysKeyStoreServiceGroup.setStatus("current")

tnSysKeyStoreCertInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 63)
)
tnSysKeyStoreCertInfoGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertVersion"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSerialNumber"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSignatureAlgorithm"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertIssuer"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertValidity"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSubject"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSubjectPublicKeyInfo"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertKeyUsage"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSubjectAlternativeName"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertExtendedKeyUsage"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertBasicConstraints"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertSHA256Fingerprint"))
)
if mibBuilder.loadTexts:
    tnSysKeyStoreCertInfoGroup.setStatus("current")

tnSysBgpPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 64)
)
tnSysBgpPeerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysBgpPeerRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerRemoteASN"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerSecurityKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerRouterId"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv4Limit"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv4Threshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv4Action"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv6Limit"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv6Threshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpMaxPrefixIpv6Action"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpStatsIpv4PrefixInCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpStatsIpv6PrefixInCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpStatsIpv4PrefixOutCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpStatsIpv6PrefixOutCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerStatsInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerStatsIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerStatsInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysBgpPeerGroup.setStatus("current")

tnSysDiscoverMeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 65)
)
tnSysDiscoverMeGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysDiscoverMeTraps")
)
if mibBuilder.loadTexts:
    tnSysDiscoverMeGroup.setStatus("current")

tnSyslogServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 66)
)
tnSyslogServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSyslogServerIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerPort"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerFacility"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerPriority"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerType"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerDomain"))
)
if mibBuilder.loadTexts:
    tnSyslogServerGroup.setStatus("current")

tnLicenseEntitlementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 67)
)
tnLicenseEntitlementGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnLicenseEntitlementDetails")
)
if mibBuilder.loadTexts:
    tnLicenseEntitlementGroup.setStatus("current")

tnPctObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 68)
)
tnPctObjsGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnPctVerificationPeriod"),
        ("TROPIC-SYSTEM-MIB", "tnPctVerificationLossThreshold"),
        ("TROPIC-SYSTEM-MIB", "tnPctVerificationOffset"),
        ("TROPIC-SYSTEM-MIB", "tnPctVerificationStatus"))
)
if mibBuilder.loadTexts:
    tnPctObjsGroup.setStatus("current")

tnHostKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 69)
)
tnHostKeyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnHostKeyString1"),
        ("TROPIC-SYSTEM-MIB", "tnHostKeyString2"))
)
if mibBuilder.loadTexts:
    tnHostKeyGroup.setStatus("current")

tnSshPrivKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 70)
)
tnSshPrivKeyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSshPrivKeyString1"),
        ("TROPIC-SYSTEM-MIB", "tnSshPrivKeyString2"),
        ("TROPIC-SYSTEM-MIB", "tnSshPrivKeyPassword"))
)
if mibBuilder.loadTexts:
    tnSshPrivKeyGroup.setStatus("current")

tnSysNESshKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 71)
)
tnSysNESshKeyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNESshKeyRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNESshKeyString1"),
        ("TROPIC-SYSTEM-MIB", "tnSysNESshKeyString2"))
)
if mibBuilder.loadTexts:
    tnSysNESshKeyGroup.setStatus("current")

tnNESshKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 72)
)
tnNESshKeyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnNESshKeyRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNESshKeyString1"),
        ("TROPIC-SYSTEM-MIB", "tnNESshKeyString2"))
)
if mibBuilder.loadTexts:
    tnNESshKeyGroup.setStatus("current")

tnTransferSysLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 73)
)
tnTransferSysLogGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnTransferSysLogCommand"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogRemoteHostInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogRemoteHostInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogPort"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogUserId"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogPassword"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogPeriod"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogLastFileTransfer"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogEnable"))
)
if mibBuilder.loadTexts:
    tnTransferSysLogGroup.setStatus("current")

tnSysHealthCareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 74)
)
tnSysHealthCareGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckShelfNum"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckSlotNum"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckResult"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareCheckScratchDir"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareServerLocation"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareTransferPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareTransferLastFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareLastOperation"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareSetCriteriaTcId"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareSetCriteria"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareDeleteCriteriaTcId"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareDeleteCriteria"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareApplyCriteriaCommand"))
)
if mibBuilder.loadTexts:
    tnSysHealthCareGroup.setStatus("current")

tnSshCiphersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 75)
)
tnSshCiphersGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshCiphersEnabled")
)
if mibBuilder.loadTexts:
    tnSshCiphersGroup.setStatus("current")

tnSshHostKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 76)
)
tnSshHostKeyGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshHostKeyEnabled")
)
if mibBuilder.loadTexts:
    tnSshHostKeyGroup.setStatus("current")

tnSshMacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 77)
)
tnSshMacsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshMacsEnabled")
)
if mibBuilder.loadTexts:
    tnSshMacsGroup.setStatus("current")

tnSshKexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 78)
)
tnSshKexGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshKexEnabled")
)
if mibBuilder.loadTexts:
    tnSshKexGroup.setStatus("current")

tnSshPubKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 79)
)
tnSshPubKeyGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshPubKeyEnabled")
)
if mibBuilder.loadTexts:
    tnSshPubKeyGroup.setStatus("current")

tnTlsProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 80)
)
tnTlsProfileGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnTlsProfileMinVersion"),
        ("TROPIC-SYSTEM-MIB", "tnTlsProfileMaxVersion"),
        ("TROPIC-SYSTEM-MIB", "tnTlsProfileMutualAuth"),
        ("TROPIC-SYSTEM-MIB", "tnTlsProfileDescription"))
)
if mibBuilder.loadTexts:
    tnTlsProfileGroup.setStatus("current")

tnSysTrapThrottlingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 81)
)
tnSysTrapThrottlingGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingThreshold1"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingThreshold2"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingThreshold3"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingTimeOverThreshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingTimeUnderThreshold"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingState"))
)
if mibBuilder.loadTexts:
    tnSysTrapThrottlingGroup.setStatus("current")

tnSanListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 82)
)
tnSanListGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSanListRowStatus")
)
if mibBuilder.loadTexts:
    tnSanListGroup.setStatus("current")

tnCsrSanListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 83)
)
tnCsrSanListGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnCsrSanListRowStatus")
)
if mibBuilder.loadTexts:
    tnCsrSanListGroup.setStatus("current")

tnSanListAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 84)
)
tnSanListAuthGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSanListAuthentication"),
        ("TROPIC-SYSTEM-MIB", "tnSanListProfileDescription"))
)
if mibBuilder.loadTexts:
    tnSanListAuthGroup.setStatus("current")

tnSysNmsIpListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 85)
)
tnSysNmsIpListGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNmsIpListRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsIpListIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsIpListInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsIpListInetAddressType"))
)
if mibBuilder.loadTexts:
    tnSysNmsIpListGroup.setStatus("current")

tnOcspProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 86)
)
tnOcspProfileGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnOcspProfileRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnOcspProfileRetry"),
        ("TROPIC-SYSTEM-MIB", "tnOcspProfileServerUrl"),
        ("TROPIC-SYSTEM-MIB", "tnOcspProfileStatus"),
        ("TROPIC-SYSTEM-MIB", "tnOcspProfileTimeout"))
)
if mibBuilder.loadTexts:
    tnOcspProfileGroup.setStatus("current")

tnSysDnsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 87)
)
tnSysDnsServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDnsServerIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysDnsServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysDnsServerInetAddressType"))
)
if mibBuilder.loadTexts:
    tnSysDnsServerGroup.setStatus("current")

tnTransferPMDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 88)
)
tnTransferPMDiscoveryGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryFilename"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryControl"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryStatus"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryErrorCode"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryPort"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryPrevious15minBinFilesTransfer"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryPrevious1dayBinFilesTransfer"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryTransferTimeOffset"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscovery15minBinFileTransferCount"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscovery1dayBinFileTransferCount"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscovery15minBinFileTransferFailureCount"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscovery1dayBinFileTransferFailureCount"))
)
if mibBuilder.loadTexts:
    tnTransferPMDiscoveryGroup.setStatus("current")

tnSysIpAclScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 89)
)
tnSysIpAclScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclScalarsGroup.setStatus("current")

tnSysIpAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 90)
)
tnSysIpAclGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclDesc"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclAccessID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterface"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSrcPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclDestPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIcmpType"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIcmpCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSrcAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSrcPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclDestAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclDestPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpFragment"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclTcpEstablish"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclStatCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclAdminState"))
)
if mibBuilder.loadTexts:
    tnSysIpAclGroup.setStatus("current")

tnSysIpv6AclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 91)
)
tnSysIpv6AclGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpv6AclDesc"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclAccessID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclInterface"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclSrcPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclDestPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclIcmpType"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclIcmpCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclIpProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclSrcAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclSrcPrefixLen"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclDestAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclDestPrefixLen"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclTcpEstablish"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclStatCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclAdminState"))
)
if mibBuilder.loadTexts:
    tnSysIpv6AclGroup.setStatus("current")

tnSysIpv6AclScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 92)
)
tnSysIpv6AclScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpv6AclScalarsGroup.setStatus("current")

tnSshProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 93)
)
tnSshProfileGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSshProfileDescription")
)
if mibBuilder.loadTexts:
    tnSshProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 2, 1)
)
tnSystemCompliance.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSystemBasicsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemControlNetworkGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemRedundancyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemDiscoveryGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemLoggingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemBackupAndRestoreGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddressGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeaturesGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFaultCorrelationGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysErrorHandlingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysSecurityGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSysDefaultGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferGroup"),
        ("TROPIC-SYSTEM-MIB", "tnClusterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6SysDefaultGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFileInitializationGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileMGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysSecurityScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclEthIfFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclEthIfFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysBtInterfaceGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanResultsTransferGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseMgrGroup"),
        ("TROPIC-SYSTEM-MIB", "tnLicenseEntityGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreServiceGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysKeyStoreCertInfoGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysBgpPeerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoverMeGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnLicenseEntitlementGroup"),
        ("TROPIC-SYSTEM-MIB", "tnPctObjsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnHostKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshPrivKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNESshKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnNESshKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnTransferSysLogGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysHealthCareGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshCiphersGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshHostKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshMacsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshKexGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshPubKeyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnTlsProfileGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysTrapThrottlingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSanListGroup"),
        ("TROPIC-SYSTEM-MIB", "tnCsrSanListGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSanListAuthGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNmsIpListGroup"),
        ("TROPIC-SYSTEM-MIB", "tnOcspProfileGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysDnsServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnTransferPMDiscoveryGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpv6AclGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSshProfileGroup"))
)
if mibBuilder.loadTexts:
    tnSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SYSTEM-MIB",
    **{"TropicSysTimingReferenceQuality": TropicSysTimingReferenceQuality,
       "TropicSysTimingReferenceTimingMode": TropicSysTimingReferenceTimingMode,
       "AluWdmSslOperationStatus": AluWdmSslOperationStatus,
       "AluWdmTransferStatus": AluWdmTransferStatus,
       "AluWdmOcsLinkStatus": AluWdmOcsLinkStatus,
       "NokiaSysBgpMaxPrefixAction": NokiaSysBgpMaxPrefixAction,
       "tnSystemMibModule": tnSystemMibModule,
       "tnSystemConf": tnSystemConf,
       "tnSystemGroups": tnSystemGroups,
       "tnSystemBasicsGroup": tnSystemBasicsGroup,
       "tnSystemControlNetworkGroup": tnSystemControlNetworkGroup,
       "tnSystemRedundancyGroup": tnSystemRedundancyGroup,
       "tnSystemDiscoveryGroup": tnSystemDiscoveryGroup,
       "tnSystemLoggingGroup": tnSystemLoggingGroup,
       "tnSystemBackupAndRestoreGroup": tnSystemBackupAndRestoreGroup,
       "tnSysNtpGroup": tnSysNtpGroup,
       "tnSysNtpServerGroup": tnSysNtpServerGroup,
       "tnSnmpTargetAddressGroup": tnSnmpTargetAddressGroup,
       "tnSyslogGroup": tnSyslogGroup,
       "tnSysTimingGroup": tnSysTimingGroup,
       "tnSysFeaturesGroup": tnSysFeaturesGroup,
       "tnSysFaultCorrelationGroup": tnSysFaultCorrelationGroup,
       "tnSysErrorHandlingGroup": tnSysErrorHandlingGroup,
       "tnSysSecurityGroup": tnSysSecurityGroup,
       "tnSysTransferLogGroup": tnSysTransferLogGroup,
       "tnSysIpAclSysDefaultGroup": tnSysIpAclSysDefaultGroup,
       "tnSysIpAclPatternScalarsGroup": tnSysIpAclPatternScalarsGroup,
       "tnSysIpAclPatternGroup": tnSysIpAclPatternGroup,
       "tnSysIpAclFilterScalarsGroup": tnSysIpAclFilterScalarsGroup,
       "tnSysIpAclFilterGroup": tnSysIpAclFilterGroup,
       "tnSysIpAclInterfaceScalarsGroup": tnSysIpAclInterfaceScalarsGroup,
       "tnSysIpAclInterfaceGroup": tnSysIpAclInterfaceGroup,
       "tnSysNtpServerIdStatsGroup": tnSysNtpServerIdStatsGroup,
       "tnSysFtpServerGroup": tnSysFtpServerGroup,
       "tnSysNtpServerAuthenticationScalarsGroup": tnSysNtpServerAuthenticationScalarsGroup,
       "tnSysNtpServerAuthenticationGroup": tnSysNtpServerAuthenticationGroup,
       "tnSysIpAclNetIfFilterScalarsGroup": tnSysIpAclNetIfFilterScalarsGroup,
       "tnSysIpAclNetIfFilterGroup": tnSysIpAclNetIfFilterGroup,
       "tnNeDiscoveryScalarsGroup": tnNeDiscoveryScalarsGroup,
       "tnNeDiscoveryGroup": tnNeDiscoveryGroup,
       "tnSysOtdrScanSystemProfileScalarsGroup": tnSysOtdrScanSystemProfileScalarsGroup,
       "tnSysOtdrScanSystemProfileGroup": tnSysOtdrScanSystemProfileGroup,
       "tnSysOtdrScanTransferGroup": tnSysOtdrScanTransferGroup,
       "tnClusterGroup": tnClusterGroup,
       "tnSysPmFetchBulkGroup": tnSysPmFetchBulkGroup,
       "tnSysDebugTransferGroup": tnSysDebugTransferGroup,
       "tnSysLicenseInvGroup": tnSysLicenseInvGroup,
       "tnSysLinuxGroup": tnSysLinuxGroup,
       "tnSysIpAclIpv6SysDefaultGroup": tnSysIpAclIpv6SysDefaultGroup,
       "tnSysFileInitializationGroup": tnSysFileInitializationGroup,
       "tnSysOtdrScanSystemProfileMScalarsGroup": tnSysOtdrScanSystemProfileMScalarsGroup,
       "tnSysOtdrScanSystemProfileMGroup": tnSysOtdrScanSystemProfileMGroup,
       "tnSysSecurityScalarsGroup": tnSysSecurityScalarsGroup,
       "tnSysIpAclIpv6PatternScalarsGroup": tnSysIpAclIpv6PatternScalarsGroup,
       "tnSysIpAclIpv6PatternGroup": tnSysIpAclIpv6PatternGroup,
       "tnSysIpAclIpv6FilterScalarsGroup": tnSysIpAclIpv6FilterScalarsGroup,
       "tnSysIpAclIpv6FilterGroup": tnSysIpAclIpv6FilterGroup,
       "tnSysIpAclIpv6InterfaceScalarsGroup": tnSysIpAclIpv6InterfaceScalarsGroup,
       "tnSysIpAclIpv6InterfaceGroup": tnSysIpAclIpv6InterfaceGroup,
       "tnSysIpv6AclNetIfFilterScalarsGroup": tnSysIpv6AclNetIfFilterScalarsGroup,
       "tnSysIpv6AclNetIfFilterGroup": tnSysIpv6AclNetIfFilterGroup,
       "tnSysIpAclEthIfFilterScalarsGroup": tnSysIpAclEthIfFilterScalarsGroup,
       "tnSysIpAclEthIfFilterGroup": tnSysIpAclEthIfFilterGroup,
       "tnSysIpv6AclEthIfFilterScalarsGroup": tnSysIpv6AclEthIfFilterScalarsGroup,
       "tnSysIpv6AclEthIfFilterGroup": tnSysIpv6AclEthIfFilterGroup,
       "tnSysBtInterfaceGroup": tnSysBtInterfaceGroup,
       "tnSysOtdrScanResultsTransferGroup": tnSysOtdrScanResultsTransferGroup,
       "tnSysLicenseMgrGroup": tnSysLicenseMgrGroup,
       "tnLicenseEntityGroup": tnLicenseEntityGroup,
       "tnSysKeyStoreServiceGroup": tnSysKeyStoreServiceGroup,
       "tnSysKeyStoreCertInfoGroup": tnSysKeyStoreCertInfoGroup,
       "tnSysBgpPeerGroup": tnSysBgpPeerGroup,
       "tnSysDiscoverMeGroup": tnSysDiscoverMeGroup,
       "tnSyslogServerGroup": tnSyslogServerGroup,
       "tnLicenseEntitlementGroup": tnLicenseEntitlementGroup,
       "tnPctObjsGroup": tnPctObjsGroup,
       "tnHostKeyGroup": tnHostKeyGroup,
       "tnSshPrivKeyGroup": tnSshPrivKeyGroup,
       "tnSysNESshKeyGroup": tnSysNESshKeyGroup,
       "tnNESshKeyGroup": tnNESshKeyGroup,
       "tnTransferSysLogGroup": tnTransferSysLogGroup,
       "tnSysHealthCareGroup": tnSysHealthCareGroup,
       "tnSshCiphersGroup": tnSshCiphersGroup,
       "tnSshHostKeyGroup": tnSshHostKeyGroup,
       "tnSshMacsGroup": tnSshMacsGroup,
       "tnSshKexGroup": tnSshKexGroup,
       "tnSshPubKeyGroup": tnSshPubKeyGroup,
       "tnTlsProfileGroup": tnTlsProfileGroup,
       "tnSysTrapThrottlingGroup": tnSysTrapThrottlingGroup,
       "tnSanListGroup": tnSanListGroup,
       "tnCsrSanListGroup": tnCsrSanListGroup,
       "tnSanListAuthGroup": tnSanListAuthGroup,
       "tnSysNmsIpListGroup": tnSysNmsIpListGroup,
       "tnOcspProfileGroup": tnOcspProfileGroup,
       "tnSysDnsServerGroup": tnSysDnsServerGroup,
       "tnTransferPMDiscoveryGroup": tnTransferPMDiscoveryGroup,
       "tnSysIpAclScalarsGroup": tnSysIpAclScalarsGroup,
       "tnSysIpAclGroup": tnSysIpAclGroup,
       "tnSysIpv6AclGroup": tnSysIpv6AclGroup,
       "tnSysIpv6AclScalarsGroup": tnSysIpv6AclScalarsGroup,
       "tnSshProfileGroup": tnSshProfileGroup,
       "tnSystemCompliances": tnSystemCompliances,
       "tnSystemCompliance": tnSystemCompliance,
       "tnSystemObjs": tnSystemObjs,
       "tnSysBasics": tnSysBasics,
       "tnSysDescr": tnSysDescr,
       "tnSysTelnetPort": tnSysTelnetPort,
       "tnSysHttpPort": tnSysHttpPort,
       "tnSysDateAndTime": tnSysDateAndTime,
       "tnSysReset": tnSysReset,
       "tnSysMIBVersion": tnSysMIBVersion,
       "tnSysRingID": tnSysRingID,
       "tnSysNetworkElementID": tnSysNetworkElementID,
       "tnSysAINSDebounceTime": tnSysAINSDebounceTime,
       "tnSysSonetSdhMode": tnSysSonetSdhMode,
       "tnSysAlarmReportingControl": tnSysAlarmReportingControl,
       "tnSysWavelengthTrackerWaveKeySpace": tnSysWavelengthTrackerWaveKeySpace,
       "tnSysSecureMode": tnSysSecureMode,
       "tnSysExtendedTemperatureRange": tnSysExtendedTemperatureRange,
       "tnSysTemperatureInCelsius": tnSysTemperatureInCelsius,
       "tnSysName": tnSysName,
       "tnSysEquipmentControllerCapacity": tnSysEquipmentControllerCapacity,
       "tnSysFirstLevelControllerCapacity": tnSysFirstLevelControllerCapacity,
       "tnSysMatrix0CompactCapacity": tnSysMatrix0CompactCapacity,
       "tnSysUniversalMatrixFirstLevelControllerCapacity": tnSysUniversalMatrixFirstLevelControllerCapacity,
       "tnSysTimeOffsetTimeZone": tnSysTimeOffsetTimeZone,
       "tnSysSwitchId": tnSysSwitchId,
       "tnSysFipsSquelchMode": tnSysFipsSquelchMode,
       "tnSysOtdrListOfFileNames": tnSysOtdrListOfFileNames,
       "tnSysOtdrFileCounts": tnSysOtdrFileCounts,
       "tnSysAltitude": tnSysAltitude,
       "tnSysThermalShutdownAutotimer": tnSysThermalShutdownAutotimer,
       "tnSysDisplayShelfLabel": tnSysDisplayShelfLabel,
       "tnSysPMFineGranularityControl": tnSysPMFineGranularityControl,
       "tnSysFmRead": tnSysFmRead,
       "tnSysPMStreamingServerControl": tnSysPMStreamingServerControl,
       "tnSysSlotMigrationControl": tnSysSlotMigrationControl,
       "tnSysFlexGridClusterOcsAddDropEnabled": tnSysFlexGridClusterOcsAddDropEnabled,
       "tnSysFilterCheckTime": tnSysFilterCheckTime,
       "tnSysCNLinkPhysicalIfIndex": tnSysCNLinkPhysicalIfIndex,
       "tnSysUserlabel": tnSysUserlabel,
       "tnSysOpenAgentControl": tnSysOpenAgentControl,
       "tnSysUnkeyedDanglingOchAddDropEnabled": tnSysUnkeyedDanglingOchAddDropEnabled,
       "tnSysNetWorkTraceV3SecurityUser": tnSysNetWorkTraceV3SecurityUser,
       "tnSysScotV3SecurityUser": tnSysScotV3SecurityUser,
       "tnSysTL1Enable": tnSysTL1Enable,
       "tnSysLMEnabled": tnSysLMEnabled,
       "tnSysAlienChannelLicensingEnabled": tnSysAlienChannelLicensingEnabled,
       "tnSysDebug": tnSysDebug,
       "tnSysClusterV3SecurityUser": tnSysClusterV3SecurityUser,
       "tnSysSyncMode": tnSysSyncMode,
       "tnSysPMMode": tnSysPMMode,
       "tnSysShelfLatitude": tnSysShelfLatitude,
       "tnSysShelfLongitude": tnSysShelfLongitude,
       "tnSysAlmProfName": tnSysAlmProfName,
       "tnSysBgpAsn": tnSysBgpAsn,
       "tnSysBgpLocalRouterId": tnSysBgpLocalRouterId,
       "tnSysNodeIdLabel": tnSysNodeIdLabel,
       "tnSysNodeNumber": tnSysNodeNumber,
       "tnSysNodeCLLI": tnSysNodeCLLI,
       "tnSysNodeTemplate": tnSysNodeTemplate,
       "tnSysCustomerApplicationMode": tnSysCustomerApplicationMode,
       "tnSysMDCli": tnSysMDCli,
       "tnSysMultiShelfMode": tnSysMultiShelfMode,
       "tnSysMultiShelfConfigList": tnSysMultiShelfConfigList,
       "tnSysMultiShelfUnknownList": tnSysMultiShelfUnknownList,
       "tnSysMultiShelfMissingList": tnSysMultiShelfMissingList,
       "tnSysPrompt": tnSysPrompt,
       "tnSysPromptType": tnSysPromptType,
       "tnSysShelfAltitude": tnSysShelfAltitude,
       "tnSysTacacsSourceIpMode": tnSysTacacsSourceIpMode,
       "tnSysRadiusSourceIpMode": tnSysRadiusSourceIpMode,
       "tnSysFtpSourceIpMode": tnSysFtpSourceIpMode,
       "tnSysSftpSourceIpMode": tnSysSftpSourceIpMode,
       "tnSysHttpSourceIpMode": tnSysHttpSourceIpMode,
       "tnSysHttpsSourceIpMode": tnSysHttpsSourceIpMode,
       "tnSysSnmpSourceIpMode": tnSysSnmpSourceIpMode,
       "tnSysSyslogSourceIpMode": tnSysSyslogSourceIpMode,
       "tnSysSshSourceIpMode": tnSysSshSourceIpMode,
       "tnSysAutoTurnUpActiveTemplate": tnSysAutoTurnUpActiveTemplate,
       "tnSysAuthenticationOrder": tnSysAuthenticationOrder,
       "tnSysAuthRejectOption": tnSysAuthRejectOption,
       "tnSysAutoTurnUpActiveTemplateForce": tnSysAutoTurnUpActiveTemplateForce,
       "tnSysNtpSourceIpMode": tnSysNtpSourceIpMode,
       "tnSysFeatureAutoTurnUp": tnSysFeatureAutoTurnUp,
       "tnSysDelayResetNE": tnSysDelayResetNE,
       "tnSysDelayReboot": tnSysDelayReboot,
       "tnSysNmsUserName": tnSysNmsUserName,
       "tnSysVersionPatchId": tnSysVersionPatchId,
       "tnSysVersionPatchDescr": tnSysVersionPatchDescr,
       "tnSysCustomerLifeCycleState": tnSysCustomerLifeCycleState,
       "tnSysUSBInstall": tnSysUSBInstall,
       "tnSysNmsIpVerifyState": tnSysNmsIpVerifyState,
       "tnSysOcspSourceIpMode": tnSysOcspSourceIpMode,
       "tnSysDnsSourceIpMode": tnSysDnsSourceIpMode,
       "tnSysOtcWaitTimeAfterPowerChange": tnSysOtcWaitTimeAfterPowerChange,
       "tnSysDHCPClassName": tnSysDHCPClassName,
       "tnSysDHCPMatchString": tnSysDHCPMatchString,
       "tnSysKeyLicense": tnSysKeyLicense,
       "tnSysHwIfMode": tnSysHwIfMode,
       "tnSysIpAclNextIndex": tnSysIpAclNextIndex,
       "tnSysIpv6AclNextIndex": tnSysIpv6AclNextIndex,
       "tnSysDHCPClass": tnSysDHCPClass,
       "tnSysProtocolIpMode": tnSysProtocolIpMode,
       "tnSysMultiShelfAvailableList": tnSysMultiShelfAvailableList,
       "tnSysPerformanceMemoryTotal": tnSysPerformanceMemoryTotal,
       "tnSysPerformanceMemoryUsed": tnSysPerformanceMemoryUsed,
       "tnSysPerformanceMemoryUsedPercentage": tnSysPerformanceMemoryUsedPercentage,
       "tnSysPerformanceTime": tnSysPerformanceTime,
       "tnSysPerformanceCPUStatsPercentages": tnSysPerformanceCPUStatsPercentages,
       "tnSysPower": tnSysPower,
       "tnSysKeyStoreCertExpiration": tnSysKeyStoreCertExpiration,
       "tnSysNumOspfV2AreaIndependentLsas": tnSysNumOspfV2AreaIndependentLsas,
       "tnSysNumOspfV3AreaIndependentLsas": tnSysNumOspfV3AreaIndependentLsas,
       "tnSysBgpAdminDistance": tnSysBgpAdminDistance,
       "tnSysControlNetwork": tnSysControlNetwork,
       "tnSysIpAddress": tnSysIpAddress,
       "tnSysSubnetMask": tnSysSubnetMask,
       "tnSysConfiguredIpAddress": tnSysConfiguredIpAddress,
       "tnSysConfiguredSubnetMask": tnSysConfiguredSubnetMask,
       "tnSysConfiguredSnmpSource": tnSysConfiguredSnmpSource,
       "tnSysConfiguredOcsIpAddress": tnSysConfiguredOcsIpAddress,
       "tnSysConfiguredOcs2IpAddress": tnSysConfiguredOcs2IpAddress,
       "tnSysConfiguredOcs3IpAddress": tnSysConfiguredOcs3IpAddress,
       "tnSysOcs1LinkStatus": tnSysOcs1LinkStatus,
       "tnSysOcs2LinkStatus": tnSysOcs2LinkStatus,
       "tnSysOcs3LinkStatus": tnSysOcs3LinkStatus,
       "tnSysConfiguredRadiusSource": tnSysConfiguredRadiusSource,
       "tnSysConfiguredLoopbackIp1": tnSysConfiguredLoopbackIp1,
       "tnSysConfiguredLoopbackIp1SubnetMask": tnSysConfiguredLoopbackIp1SubnetMask,
       "tnSysConfiguredSnmpSource1": tnSysConfiguredSnmpSource1,
       "tnSysConfiguredRadiusSource1": tnSysConfiguredRadiusSource1,
       "tnSysLoopbackIpAddress1": tnSysLoopbackIpAddress1,
       "tnSysLoopbackIp1SubnetMask": tnSysLoopbackIp1SubnetMask,
       "tnSysConfiguredInetAddressType": tnSysConfiguredInetAddressType,
       "tnSysConfiguredInetAddress": tnSysConfiguredInetAddress,
       "tnSysConfiguredPrefixLength": tnSysConfiguredPrefixLength,
       "tnSysOcsIp1Password": tnSysOcsIp1Password,
       "tnSysOcsIp2Password": tnSysOcsIp2Password,
       "tnSysOcsIp3Password": tnSysOcsIp3Password,
       "tnSysConfiguredSnmpSourceIPv6": tnSysConfiguredSnmpSourceIPv6,
       "tnSysConfiguredRadiusSourceIPv6": tnSysConfiguredRadiusSourceIPv6,
       "tnSysRedundancy": tnSysRedundancy,
       "tnSysRedundancyDbSynchState": tnSysRedundancyDbSynchState,
       "tnSysRedundancyDbResynch": tnSysRedundancyDbResynch,
       "tnSysRedundancyDbAudit": tnSysRedundancyDbAudit,
       "tnSysRedundancyDbClear": tnSysRedundancyDbClear,
       "tnSysRedundancyActiveCCSlot": tnSysRedundancyActiveCCSlot,
       "tnSysRedundancyDbInvalid": tnSysRedundancyDbInvalid,
       "tnSysRedundancyMateCCReadyToProtect": tnSysRedundancyMateCCReadyToProtect,
       "tnSysDiscovery": tnSysDiscovery,
       "tnSysDiscoveryFilename": tnSysDiscoveryFilename,
       "tnSysDiscoveryMask": tnSysDiscoveryMask,
       "tnSysDiscoveryControl": tnSysDiscoveryControl,
       "tnSysDiscoveryStatus": tnSysDiscoveryStatus,
       "tnSysDiscoveryErrorCode": tnSysDiscoveryErrorCode,
       "tnSysDiscoveryBinnedStatsInterval": tnSysDiscoveryBinnedStatsInterval,
       "tnSysDiscoveryBinnedStatsBin": tnSysDiscoveryBinnedStatsBin,
       "tnSysDiscoveryServerProtocol": tnSysDiscoveryServerProtocol,
       "tnSysDiscoveryServerIp": tnSysDiscoveryServerIp,
       "tnSysDiscoveryServerUserId": tnSysDiscoveryServerUserId,
       "tnSysDiscoveryServerPassword": tnSysDiscoveryServerPassword,
       "tnSysDiscoveryServerInetAddressType": tnSysDiscoveryServerInetAddressType,
       "tnSysDiscoveryServerInetAddress": tnSysDiscoveryServerInetAddress,
       "tnSysDiscoveryPort": tnSysDiscoveryPort,
       "tnSysDiscoveryPrevious15minBinFilesTransfer": tnSysDiscoveryPrevious15minBinFilesTransfer,
       "tnSysDiscoveryPrevious1dayBinFilesTransfer": tnSysDiscoveryPrevious1dayBinFilesTransfer,
       "tnSysDiscoveryTransferTimeOffset": tnSysDiscoveryTransferTimeOffset,
       "tnSysDiscoveryTransferTraps": tnSysDiscoveryTransferTraps,
       "tnSysLogging": tnSysLogging,
       "tnSysLoggingCLI": tnSysLoggingCLI,
       "tnSysLoggingSNMP": tnSysLoggingSNMP,
       "tnSysBackupAndRestore": tnSysBackupAndRestore,
       "tnSysBackupAndRestoreCommand": tnSysBackupAndRestoreCommand,
       "tnSysBackupAndRestoreRemoteHostIp": tnSysBackupAndRestoreRemoteHostIp,
       "tnSysBackupAndRestoreRemotePath": tnSysBackupAndRestoreRemotePath,
       "tnSysBackupAndRestoreStatus": tnSysBackupAndRestoreStatus,
       "tnSysBackupAndRestoreLastBackupFilename": tnSysBackupAndRestoreLastBackupFilename,
       "tnSysBackupAndRestoreLastCommand": tnSysBackupAndRestoreLastCommand,
       "tnSysBackupAndRestorePercentCompleted": tnSysBackupAndRestorePercentCompleted,
       "tnSysBackupAndRestoreLastBackupFileTimeStamp": tnSysBackupAndRestoreLastBackupFileTimeStamp,
       "tnSysBackupAndRestoreProtocol": tnSysBackupAndRestoreProtocol,
       "tnSysBackupAndRestoreUserId": tnSysBackupAndRestoreUserId,
       "tnSysBackupAndRestorePassword": tnSysBackupAndRestorePassword,
       "tnSysBackupAndRestoreLastBackupFileCrc": tnSysBackupAndRestoreLastBackupFileCrc,
       "tnSysBackupAndRestoreRemoteHostInetAddressType": tnSysBackupAndRestoreRemoteHostInetAddressType,
       "tnSysBackupAndRestoreRemoteHostInetAddress": tnSysBackupAndRestoreRemoteHostInetAddress,
       "tnSysBackupAndRestoreLocalInfo": tnSysBackupAndRestoreLocalInfo,
       "tnSysBackupAndRestoreLocalDelete": tnSysBackupAndRestoreLocalDelete,
       "tnSysBackupAndRestorePort": tnSysBackupAndRestorePort,
       "tnSysBackupAndRestoreFallBackTimeStamp": tnSysBackupAndRestoreFallBackTimeStamp,
       "tnSysNtp": tnSysNtp,
       "tnSysNtpEnable": tnSysNtpEnable,
       "tnSysNtpSynched": tnSysNtpSynched,
       "tnSysNtpServerCurrentIpAddress": tnSysNtpServerCurrentIpAddress,
       "tnSysNtpDriftString": tnSysNtpDriftString,
       "tnSysNtpTimeOffsetString": tnSysNtpTimeOffsetString,
       "tnSysNtpClockMode": tnSysNtpClockMode,
       "tnSysNtpServerCurrentInetAddressType": tnSysNtpServerCurrentInetAddressType,
       "tnSysNtpServerCurrentInetAddress": tnSysNtpServerCurrentInetAddress,
       "tnSysNtpServers": tnSysNtpServers,
       "tnSysNtpServerTable": tnSysNtpServerTable,
       "tnSysNtpServerEntry": tnSysNtpServerEntry,
       "tnSysNtpServerIndex": tnSysNtpServerIndex,
       "tnSysNtpServerIpAddress": tnSysNtpServerIpAddress,
       "tnSysNtpServerRowStatus": tnSysNtpServerRowStatus,
       "tnSysNtpServerKeyIndex": tnSysNtpServerKeyIndex,
       "tnSysNtpServerInetAddress": tnSysNtpServerInetAddress,
       "tnSysNtpServerInetAddressType": tnSysNtpServerInetAddressType,
       "tnSnmpTargetAddresses": tnSnmpTargetAddresses,
       "tnSnmpTargetAddrTable": tnSnmpTargetAddrTable,
       "tnSnmpTargetAddrEntry": tnSnmpTargetAddrEntry,
       "tnSnmpTargetAddrNmsStationGroupId": tnSnmpTargetAddrNmsStationGroupId,
       "tnSnmpTargetAddrTrapGroupId": tnSnmpTargetAddrTrapGroupId,
       "tnSnmpTargetAddrDisableTrap": tnSnmpTargetAddrDisableTrap,
       "tnSyslog": tnSyslog,
       "tnSyslogIpAddress": tnSyslogIpAddress,
       "tnSyslogPort": tnSyslogPort,
       "tnSyslogFacility": tnSyslogFacility,
       "tnSyslogPriority": tnSyslogPriority,
       "tnSyslogEnabled": tnSyslogEnabled,
       "tnSyslogInetAddress": tnSyslogInetAddress,
       "tnSyslogInetAddressType": tnSyslogInetAddressType,
       "tnSyslogProtocol": tnSyslogProtocol,
       "tnSysTiming": tnSysTiming,
       "tnSysTimingPrimaryReference": tnSysTimingPrimaryReference,
       "tnSysTimingSecondaryReference": tnSysTimingSecondaryReference,
       "tnSysTimingLastSwitchTime": tnSysTimingLastSwitchTime,
       "tnSysTimingControl": tnSysTimingControl,
       "tnSysTimingPrimaryReferenceStatus": tnSysTimingPrimaryReferenceStatus,
       "tnSysTimingSecondaryReferenceStatus": tnSysTimingSecondaryReferenceStatus,
       "tnSysTimingPrimaryReferenceQuality": tnSysTimingPrimaryReferenceQuality,
       "tnSysTimingSecondaryReferenceQuality": tnSysTimingSecondaryReferenceQuality,
       "tnSysTimingPrimaryReferenceTimingMode": tnSysTimingPrimaryReferenceTimingMode,
       "tnSysTimingSecondaryReferenceTimingMode": tnSysTimingSecondaryReferenceTimingMode,
       "tnSysTimingActiveReference": tnSysTimingActiveReference,
       "tnSysTimingClockingMode": tnSysTimingClockingMode,
       "tnSysTimingSwitchingMode": tnSysTimingSwitchingMode,
       "tnSysTimingFreeRunSuppressAlarms": tnSysTimingFreeRunSuppressAlarms,
       "tnSysTimingDs1FramingMode": tnSysTimingDs1FramingMode,
       "tnSysTimingDs1LineCoding": tnSysTimingDs1LineCoding,
       "tnSysTimingDs1SsmProcessing": tnSysTimingDs1SsmProcessing,
       "tnSysTimingBitsAClockQuality": tnSysTimingBitsAClockQuality,
       "tnSysTimingBitsBClockQuality": tnSysTimingBitsBClockQuality,
       "tnSysTimingActiveLineTimingCable": tnSysTimingActiveLineTimingCable,
       "tnSysTimingBitSourceType": tnSysTimingBitSourceType,
       "tnSysTimingBitsAModuleType": tnSysTimingBitsAModuleType,
       "tnSysTimingBitsBModuleType": tnSysTimingBitsBModuleType,
       "tnSysFeatures": tnSysFeatures,
       "tnSysFeatureAutoTopology": tnSysFeatureAutoTopology,
       "tnSysFeaturePauseFlowControl": tnSysFeaturePauseFlowControl,
       "tnSysFeatureIpUtilitiesRestricted": tnSysFeatureIpUtilitiesRestricted,
       "tnSysFeatureFastServiceSetup": tnSysFeatureFastServiceSetup,
       "tnSysFaultCorrelation": tnSysFaultCorrelation,
       "tnSysFaultCorrelationTransientSuppression": tnSysFaultCorrelationTransientSuppression,
       "tnSysErrorHandling": tnSysErrorHandling,
       "tnSysSetRequestErrorMessage": tnSysSetRequestErrorMessage,
       "tnSysSecurity": tnSysSecurity,
       "tnSysSecurityMode": tnSysSecurityMode,
       "tnSysSsh": tnSysSsh,
       "tnSysSshKeyType": tnSysSshKeyType,
       "tnSysSshKeyModulus": tnSysSshKeyModulus,
       "tnSysSshPublicKey": tnSysSshPublicKey,
       "tnSysSshKeyCommand": tnSysSshKeyCommand,
       "tnSysSshKeyGenerationStatus": tnSysSshKeyGenerationStatus,
       "tnSysSshEcdsaKeyModulus": tnSysSshEcdsaKeyModulus,
       "tnSysSsl": tnSysSsl,
       "tnSysSslKeyType": tnSysSslKeyType,
       "tnSysSslKeyModulus": tnSysSslKeyModulus,
       "tnSysSslPublicKey": tnSysSslPublicKey,
       "tnSysSslKeyCommand": tnSysSslKeyCommand,
       "tnSysSslKeyGenerationStatus": tnSysSslKeyGenerationStatus,
       "tnSysSslCertTransferCommand": tnSysSslCertTransferCommand,
       "tnSysSslCertTransferProtocol": tnSysSslCertTransferProtocol,
       "tnSysSslCertTransferRemoteIp": tnSysSslCertTransferRemoteIp,
       "tnSysSslCertTransferRemotePath": tnSysSslCertTransferRemotePath,
       "tnSysSslCertTransferRemoteUserId": tnSysSslCertTransferRemoteUserId,
       "tnSysSslCertTransferRemotePassword": tnSysSslCertTransferRemotePassword,
       "tnSysSslCsrCommand": tnSysSslCsrCommand,
       "tnSysSslCsrCountry": tnSysSslCsrCountry,
       "tnSysSslCsrState": tnSysSslCsrState,
       "tnSysSslCsrLocality": tnSysSslCsrLocality,
       "tnSysSslCsrOrganization": tnSysSslCsrOrganization,
       "tnSysSslCsrOrganizationUnit": tnSysSslCsrOrganizationUnit,
       "tnSysSslCsrCommonName": tnSysSslCsrCommonName,
       "tnSysSslCsrEmailAddress": tnSysSslCsrEmailAddress,
       "tnSysSslCertCommand": tnSysSslCertCommand,
       "tnSysSslCertSignatureAlgorithm": tnSysSslCertSignatureAlgorithm,
       "tnSysSslCertValidity": tnSysSslCertValidity,
       "tnSysSslCsrUploadStatus": tnSysSslCsrUploadStatus,
       "tnSysSslCertDownloadStatus": tnSysSslCertDownloadStatus,
       "tnSysSslCertInstallStatus": tnSysSslCertInstallStatus,
       "tnSysSslCsrGenerationStatus": tnSysSslCsrGenerationStatus,
       "tnSysSslCertTransferInetAddressType": tnSysSslCertTransferInetAddressType,
       "tnSysSslCertTransferInetAddress": tnSysSslCertTransferInetAddress,
       "tnSysSslCertTransferPort": tnSysSslCertTransferPort,
       "tnSysSslCertVerification": tnSysSslCertVerification,
       "tnSysSslCertExpiration": tnSysSslCertExpiration,
       "tnSysKey": tnSysKey,
       "tnSshKeyAttributeTotal": tnSshKeyAttributeTotal,
       "tnSshKeyTable": tnSshKeyTable,
       "tnSshKeyEntry": tnSshKeyEntry,
       "tnSshKeyTypeIndex": tnSshKeyTypeIndex,
       "tnSshPublicKey": tnSshPublicKey,
       "tnSshPublicKey1": tnSshPublicKey1,
       "tnSshEcdsaPublicKey": tnSshEcdsaPublicKey,
       "tnSshEcdsaPublicKey1": tnSshEcdsaPublicKey1,
       "tnSshEd25519PublicKey": tnSshEd25519PublicKey,
       "tnSshEd25519PublicKey1": tnSshEd25519PublicKey1,
       "tnSysTransferLog": tnSysTransferLog,
       "tnSysTransferLogCommand": tnSysTransferLogCommand,
       "tnSysTransferLogRemoteHostIp": tnSysTransferLogRemoteHostIp,
       "tnSysTransferLogRemotePath": tnSysTransferLogRemotePath,
       "tnSysTransferLogType": tnSysTransferLogType,
       "tnSysTransferLogStatus": tnSysTransferLogStatus,
       "tnSysTransferLogLastLogFilename": tnSysTransferLogLastLogFilename,
       "tnSysTransferLogLastCommand": tnSysTransferLogLastCommand,
       "tnSysTransferLogLastFileTimeStamp": tnSysTransferLogLastFileTimeStamp,
       "tnSysTransferLogProtocol": tnSysTransferLogProtocol,
       "tnSysTransferLogUserId": tnSysTransferLogUserId,
       "tnSysTransferLogPassword": tnSysTransferLogPassword,
       "tnSysTransferLogWindowStart": tnSysTransferLogWindowStart,
       "tnSysTransferLogWindowStop": tnSysTransferLogWindowStop,
       "tnSysTransferLogRemoteHostInetAddressType": tnSysTransferLogRemoteHostInetAddressType,
       "tnSysTransferLogRemoteHostInetAddress": tnSysTransferLogRemoteHostInetAddress,
       "tnSysTransferLogPort": tnSysTransferLogPort,
       "tnSysAccessControlList": tnSysAccessControlList,
       "tnSysIpAclSysDefault": tnSysIpAclSysDefault,
       "tnSysIpAclRxAction": tnSysIpAclRxAction,
       "tnSysIpAclTxAction": tnSysIpAclTxAction,
       "tnSysIpAclSnmpCfgEnable": tnSysIpAclSnmpCfgEnable,
       "tnSysIpAclCfgRestoreToDefault": tnSysIpAclCfgRestoreToDefault,
       "tnSysIpAclClearCounter": tnSysIpAclClearCounter,
       "tnSysIpAclPatternAttributeTotal": tnSysIpAclPatternAttributeTotal,
       "tnSysIpAclPatternTable": tnSysIpAclPatternTable,
       "tnSysIpAclPatternEntry": tnSysIpAclPatternEntry,
       "tnSysIpAclPatternID": tnSysIpAclPatternID,
       "tnSysIpAclPatternAction": tnSysIpAclPatternAction,
       "tnSysIpAclPatternICMPERROR": tnSysIpAclPatternICMPERROR,
       "tnSysIpAclPatternSrcAddr": tnSysIpAclPatternSrcAddr,
       "tnSysIpAclPatternSrcPrefix": tnSysIpAclPatternSrcPrefix,
       "tnSysIpAclPatternDestAddr": tnSysIpAclPatternDestAddr,
       "tnSysIpAclPatternDestPrefix": tnSysIpAclPatternDestPrefix,
       "tnSysIpAclPatternDestPort": tnSysIpAclPatternDestPort,
       "tnSysIpAclPatternIpProtocol": tnSysIpAclPatternIpProtocol,
       "tnSysIpAclPatternIpFragment": tnSysIpAclPatternIpFragment,
       "tnSysIpAclPatternIcmpType": tnSysIpAclPatternIcmpType,
       "tnSysIpAclPatternIcmpCode": tnSysIpAclPatternIcmpCode,
       "tnSysIpAclPatternTcpEstablish": tnSysIpAclPatternTcpEstablish,
       "tnSysIpAclPatternRowStatus": tnSysIpAclPatternRowStatus,
       "tnSysIpAclPatternSrcPort": tnSysIpAclPatternSrcPort,
       "tnSysIpAclPatternSystemDefault": tnSysIpAclPatternSystemDefault,
       "tnSysIpAclPatternSrcPortRangeEnd": tnSysIpAclPatternSrcPortRangeEnd,
       "tnSysIpAclPatternDestPortRangeEnd": tnSysIpAclPatternDestPortRangeEnd,
       "tnSysIpAclFilterAttributeTotal": tnSysIpAclFilterAttributeTotal,
       "tnSysIpAclFilterTable": tnSysIpAclFilterTable,
       "tnSysIpAclFilterEntry": tnSysIpAclFilterEntry,
       "tnSysIpAclFilterID": tnSysIpAclFilterID,
       "tnSysIpAclFilterPatternIndex": tnSysIpAclFilterPatternIndex,
       "tnSysIpAclFilterPatternID": tnSysIpAclFilterPatternID,
       "tnSysIpAclFilterStatCount": tnSysIpAclFilterStatCount,
       "tnSysIpAclFilterRowStatus": tnSysIpAclFilterRowStatus,
       "tnSysIpAclFilterSystemDefault": tnSysIpAclFilterSystemDefault,
       "tnSysIpAclInterfaceAttributeTotal": tnSysIpAclInterfaceAttributeTotal,
       "tnSysIpAclInterfaceTable": tnSysIpAclInterfaceTable,
       "tnSysIpAclInterfaceEntry": tnSysIpAclInterfaceEntry,
       "tnSysIpAclInterfaceFilterDir": tnSysIpAclInterfaceFilterDir,
       "tnSysIpAclInterfaceFilterID": tnSysIpAclInterfaceFilterID,
       "tnSysIpAclInterfaceFilterEnable": tnSysIpAclInterfaceFilterEnable,
       "tnSysIpAclInterfaceFilterRowStatus": tnSysIpAclInterfaceFilterRowStatus,
       "tnSysIpAclInterfaceSystemDefault": tnSysIpAclInterfaceSystemDefault,
       "tnSysIpAclInterfaceFilterLog": tnSysIpAclInterfaceFilterLog,
       "tnSysIpAclNetIfFilterAttributeTotal": tnSysIpAclNetIfFilterAttributeTotal,
       "tnSysIpAclNetIfFilterTable": tnSysIpAclNetIfFilterTable,
       "tnSysIpAclNetIfFilterEntry": tnSysIpAclNetIfFilterEntry,
       "tnSysIpAclNetIfFilterDir": tnSysIpAclNetIfFilterDir,
       "tnSysIpAclNetIfFilterRowStatus": tnSysIpAclNetIfFilterRowStatus,
       "tnSysIpAclNetIfFilterID": tnSysIpAclNetIfFilterID,
       "tnSysIpAclNetIfFilterEnable": tnSysIpAclNetIfFilterEnable,
       "tnSysIpAclNetIfFilterSystemDefault": tnSysIpAclNetIfFilterSystemDefault,
       "tnSysIpAclIpv6PatternAttributeTotal": tnSysIpAclIpv6PatternAttributeTotal,
       "tnSysIpAclIpv6PatternTable": tnSysIpAclIpv6PatternTable,
       "tnSysIpAclIpv6PatternEntry": tnSysIpAclIpv6PatternEntry,
       "tnSysIpAclIpv6PatternID": tnSysIpAclIpv6PatternID,
       "tnSysIpAclIpv6PatternAction": tnSysIpAclIpv6PatternAction,
       "tnSysIpAclIpv6PatternICMPV6ERROR": tnSysIpAclIpv6PatternICMPV6ERROR,
       "tnSysIpAclIpv6PatternSrcAddr": tnSysIpAclIpv6PatternSrcAddr,
       "tnSysIpAclIpv6PatternSrcPrefixLen": tnSysIpAclIpv6PatternSrcPrefixLen,
       "tnSysIpAclIpv6PatternDestAddr": tnSysIpAclIpv6PatternDestAddr,
       "tnSysIpAclIpv6PatternDestPrefixLen": tnSysIpAclIpv6PatternDestPrefixLen,
       "tnSysIpAclIpv6PatternIpProtocol": tnSysIpAclIpv6PatternIpProtocol,
       "tnSysIpAclIpv6PatternIcmpType": tnSysIpAclIpv6PatternIcmpType,
       "tnSysIpAclIpv6PatternIcmpCode": tnSysIpAclIpv6PatternIcmpCode,
       "tnSysIpAclIpv6PatternSrcPort": tnSysIpAclIpv6PatternSrcPort,
       "tnSysIpAclIpv6PatternDestPort": tnSysIpAclIpv6PatternDestPort,
       "tnSysIpAclIpv6PatternIpFragment": tnSysIpAclIpv6PatternIpFragment,
       "tnSysIpAclIpv6PatternTcpEstablish": tnSysIpAclIpv6PatternTcpEstablish,
       "tnSysIpAclIpv6PatternSystemDefault": tnSysIpAclIpv6PatternSystemDefault,
       "tnSysIpAclIpv6PatternRowStatus": tnSysIpAclIpv6PatternRowStatus,
       "tnSysIpAclIpv6PatternSrcPortRangeEnd": tnSysIpAclIpv6PatternSrcPortRangeEnd,
       "tnSysIpAclIpv6PatternDestPortRangeEnd": tnSysIpAclIpv6PatternDestPortRangeEnd,
       "tnSysIpAclIpv6FilterAttributeTotal": tnSysIpAclIpv6FilterAttributeTotal,
       "tnSysIpAclIpv6FilterTable": tnSysIpAclIpv6FilterTable,
       "tnSysIpAclIpv6FilterEntry": tnSysIpAclIpv6FilterEntry,
       "tnSysIpAclIpv6FilterID": tnSysIpAclIpv6FilterID,
       "tnSysIpAclIpv6FilterPatternIndex": tnSysIpAclIpv6FilterPatternIndex,
       "tnSysIpAclIpv6FilterPatternID": tnSysIpAclIpv6FilterPatternID,
       "tnSysIpAclIpv6FilterStatCount": tnSysIpAclIpv6FilterStatCount,
       "tnSysIpAclIpv6FilterRowStatus": tnSysIpAclIpv6FilterRowStatus,
       "tnSysIpAclIpv6FilterSystemDefault": tnSysIpAclIpv6FilterSystemDefault,
       "tnSysIpAclIpv6InterfaceAttributeTotal": tnSysIpAclIpv6InterfaceAttributeTotal,
       "tnSysIpAclIpv6InterfaceTable": tnSysIpAclIpv6InterfaceTable,
       "tnSysIpAclIpv6InterfaceEntry": tnSysIpAclIpv6InterfaceEntry,
       "tnSysIpAclIpv6InterfaceFilterDir": tnSysIpAclIpv6InterfaceFilterDir,
       "tnSysIpAclIpv6InterfaceFilterID": tnSysIpAclIpv6InterfaceFilterID,
       "tnSysIpAclIpv6InterfaceFilterEnable": tnSysIpAclIpv6InterfaceFilterEnable,
       "tnSysIpAclIpv6InterfaceFilterRowStatus": tnSysIpAclIpv6InterfaceFilterRowStatus,
       "tnSysIpAclIpv6InterfaceSystemDefault": tnSysIpAclIpv6InterfaceSystemDefault,
       "tnSysIpAclIpv6InterfaceFilterLog": tnSysIpAclIpv6InterfaceFilterLog,
       "tnSysIpv6AclNetIfFilterAttributeTotal": tnSysIpv6AclNetIfFilterAttributeTotal,
       "tnSysIpv6AclNetIfFilterTable": tnSysIpv6AclNetIfFilterTable,
       "tnSysIpv6AclNetIfFilterEntry": tnSysIpv6AclNetIfFilterEntry,
       "tnSysIpv6AclNetIfFilterDir": tnSysIpv6AclNetIfFilterDir,
       "tnSysIpv6AclNetIfFilterRowStatus": tnSysIpv6AclNetIfFilterRowStatus,
       "tnSysIpv6AclNetIfFilterID": tnSysIpv6AclNetIfFilterID,
       "tnSysIpv6AclNetIfFilterEnable": tnSysIpv6AclNetIfFilterEnable,
       "tnSysIpv6AclNetIfFilterSystemDefault": tnSysIpv6AclNetIfFilterSystemDefault,
       "tnSysIpAclEthIfFilterAttributeTotal": tnSysIpAclEthIfFilterAttributeTotal,
       "tnSysIpAclEthIfFilterTable": tnSysIpAclEthIfFilterTable,
       "tnSysIpAclEthIfFilterEntry": tnSysIpAclEthIfFilterEntry,
       "tnSysIpAclEthIfFilterDir": tnSysIpAclEthIfFilterDir,
       "tnSysIpAclEthIfFilterRowStatus": tnSysIpAclEthIfFilterRowStatus,
       "tnSysIpAclEthIfFilterID": tnSysIpAclEthIfFilterID,
       "tnSysIpAclEthIfFilterEnable": tnSysIpAclEthIfFilterEnable,
       "tnSysIpAclEthIfFilterSystemDefault": tnSysIpAclEthIfFilterSystemDefault,
       "tnSysIpv6AclEthIfFilterAttributeTotal": tnSysIpv6AclEthIfFilterAttributeTotal,
       "tnSysIpv6AclEthIfFilterTable": tnSysIpv6AclEthIfFilterTable,
       "tnSysIpv6AclEthIfFilterEntry": tnSysIpv6AclEthIfFilterEntry,
       "tnSysIpv6AclEthIfFilterDir": tnSysIpv6AclEthIfFilterDir,
       "tnSysIpv6AclEthIfFilterRowStatus": tnSysIpv6AclEthIfFilterRowStatus,
       "tnSysIpv6AclEthIfFilterID": tnSysIpv6AclEthIfFilterID,
       "tnSysIpv6AclEthIfFilterEnable": tnSysIpv6AclEthIfFilterEnable,
       "tnSysIpv6AclEthIfFilterSystemDefault": tnSysIpv6AclEthIfFilterSystemDefault,
       "tnSysIpAclAttributeTotal": tnSysIpAclAttributeTotal,
       "tnSysIpAclTable": tnSysIpAclTable,
       "tnSysIpAclEntry": tnSysIpAclEntry,
       "tnSysIpAclIndex": tnSysIpAclIndex,
       "tnSysIpAclDesc": tnSysIpAclDesc,
       "tnSysIpAclAccessID": tnSysIpAclAccessID,
       "tnSysIpAclInterface": tnSysIpAclInterface,
       "tnSysIpAclAction": tnSysIpAclAction,
       "tnSysIpAclSrcPort": tnSysIpAclSrcPort,
       "tnSysIpAclDestPort": tnSysIpAclDestPort,
       "tnSysIpAclIcmpType": tnSysIpAclIcmpType,
       "tnSysIpAclIcmpCode": tnSysIpAclIcmpCode,
       "tnSysIpAclIpProtocol": tnSysIpAclIpProtocol,
       "tnSysIpAclSrcAddr": tnSysIpAclSrcAddr,
       "tnSysIpAclSrcPrefix": tnSysIpAclSrcPrefix,
       "tnSysIpAclDestAddr": tnSysIpAclDestAddr,
       "tnSysIpAclDestPrefix": tnSysIpAclDestPrefix,
       "tnSysIpAclIpFragment": tnSysIpAclIpFragment,
       "tnSysIpAclTcpEstablish": tnSysIpAclTcpEstablish,
       "tnSysIpAclStatCount": tnSysIpAclStatCount,
       "tnSysIpAclAdminState": tnSysIpAclAdminState,
       "tnSysIpv6AclAttributeTotal": tnSysIpv6AclAttributeTotal,
       "tnSysIpv6AclTable": tnSysIpv6AclTable,
       "tnSysIpv6AclEntry": tnSysIpv6AclEntry,
       "tnSysIpv6AclIndex": tnSysIpv6AclIndex,
       "tnSysIpv6AclDesc": tnSysIpv6AclDesc,
       "tnSysIpv6AclAccessID": tnSysIpv6AclAccessID,
       "tnSysIpv6AclInterface": tnSysIpv6AclInterface,
       "tnSysIpv6AclAction": tnSysIpv6AclAction,
       "tnSysIpv6AclSrcPort": tnSysIpv6AclSrcPort,
       "tnSysIpv6AclDestPort": tnSysIpv6AclDestPort,
       "tnSysIpv6AclIcmpType": tnSysIpv6AclIcmpType,
       "tnSysIpv6AclIcmpCode": tnSysIpv6AclIcmpCode,
       "tnSysIpv6AclIpProtocol": tnSysIpv6AclIpProtocol,
       "tnSysIpv6AclSrcAddr": tnSysIpv6AclSrcAddr,
       "tnSysIpv6AclSrcPrefixLen": tnSysIpv6AclSrcPrefixLen,
       "tnSysIpv6AclDestAddr": tnSysIpv6AclDestAddr,
       "tnSysIpv6AclDestPrefixLen": tnSysIpv6AclDestPrefixLen,
       "tnSysIpv6AclTcpEstablish": tnSysIpv6AclTcpEstablish,
       "tnSysIpv6AclStatCount": tnSysIpv6AclStatCount,
       "tnSysIpv6AclAdminState": tnSysIpv6AclAdminState,
       "tnSysNtpServerIdStats": tnSysNtpServerIdStats,
       "tnSysNtpServerIdStatsTable": tnSysNtpServerIdStatsTable,
       "tnSysNtpServerIdStatsEntry": tnSysNtpServerIdStatsEntry,
       "tnSysNtpServerIdStatsIndex": tnSysNtpServerIdStatsIndex,
       "tnSysNtpServerIdStatsSelect": tnSysNtpServerIdStatsSelect,
       "tnSysNtpServerIdStatsIp": tnSysNtpServerIdStatsIp,
       "tnSysNtpServerIdStatsRefId": tnSysNtpServerIdStatsRefId,
       "tnSysNtpServerIdStatsStrtm": tnSysNtpServerIdStatsStrtm,
       "tnSysNtpServerIdStatsClockType": tnSysNtpServerIdStatsClockType,
       "tnSysNtpServerIdStatsPoll": tnSysNtpServerIdStatsPoll,
       "tnSysNtpServerIdStatsReach": tnSysNtpServerIdStatsReach,
       "tnSysNtpServerIdStatsDelay": tnSysNtpServerIdStatsDelay,
       "tnSysNtpServerIdStatsOffset": tnSysNtpServerIdStatsOffset,
       "tnSysNtpServerIdStatsJitter": tnSysNtpServerIdStatsJitter,
       "tnSysNtpServerIdStatsKeyIndex": tnSysNtpServerIdStatsKeyIndex,
       "tnSysFtpServer": tnSysFtpServer,
       "tnSysFtpServerEnabled": tnSysFtpServerEnabled,
       "tnSysFtpServerUserId": tnSysFtpServerUserId,
       "tnSysFtpServerPassword": tnSysFtpServerPassword,
       "tnSysNtpServerAuthentication": tnSysNtpServerAuthentication,
       "tnSysNtpServerAuthenticationAttributeTotal": tnSysNtpServerAuthenticationAttributeTotal,
       "tnSysNtpServerAuthenticationTable": tnSysNtpServerAuthenticationTable,
       "tnSysNtpServerAuthenticationEntry": tnSysNtpServerAuthenticationEntry,
       "tnSysNtpServerAuthenticationKeyIndex": tnSysNtpServerAuthenticationKeyIndex,
       "tnSysNtpServerAuthenticationRowStatus": tnSysNtpServerAuthenticationRowStatus,
       "tnSysNtpServerAuthenticationKeyType": tnSysNtpServerAuthenticationKeyType,
       "tnSysNtpServerAuthenticationKey": tnSysNtpServerAuthenticationKey,
       "tnNeDiscovery": tnNeDiscovery,
       "tnNeDiscoveryAttributeTotal": tnNeDiscoveryAttributeTotal,
       "tnNeDiscoveryTable": tnNeDiscoveryTable,
       "tnNeDiscoveryEntry": tnNeDiscoveryEntry,
       "tnNeDiscoveryIndex": tnNeDiscoveryIndex,
       "tnNeDiscoveryFilename": tnNeDiscoveryFilename,
       "tnNeDiscoveryControl": tnNeDiscoveryControl,
       "tnNeDiscoveryStatus": tnNeDiscoveryStatus,
       "tnNeDiscoveryErrorCode": tnNeDiscoveryErrorCode,
       "tnNeDiscoveryServerIp": tnNeDiscoveryServerIp,
       "tnNeDiscoveryServerProtocol": tnNeDiscoveryServerProtocol,
       "tnNeDiscoveryServerUserId": tnNeDiscoveryServerUserId,
       "tnNeDiscoveryServerPassword": tnNeDiscoveryServerPassword,
       "tnNeDiscoveryServerTimeOut": tnNeDiscoveryServerTimeOut,
       "tnNeDiscoveryRowStatus": tnNeDiscoveryRowStatus,
       "tnNeDiscoveryServerInetAddressType": tnNeDiscoveryServerInetAddressType,
       "tnNeDiscoveryServerInetAddress": tnNeDiscoveryServerInetAddress,
       "tnNeDiscoveryDeltaFilename": tnNeDiscoveryDeltaFilename,
       "tnNeDiscoveryDeltaFileFlag": tnNeDiscoveryDeltaFileFlag,
       "tnNeDiscoveryDeltaSyncStatus": tnNeDiscoveryDeltaSyncStatus,
       "tnNeDiscoveryPort": tnNeDiscoveryPort,
       "tnSysOtdrScan": tnSysOtdrScan,
       "tnSysOtdrScanSystemProfile": tnSysOtdrScanSystemProfile,
       "tnSysOtdrScanSystemProfileAttributeTotal": tnSysOtdrScanSystemProfileAttributeTotal,
       "tnSysOtdrScanSystemProfileTable": tnSysOtdrScanSystemProfileTable,
       "tnSysOtdrScanSystemProfileEntry": tnSysOtdrScanSystemProfileEntry,
       "tnSysOtdrScanSystemProfileId": tnSysOtdrScanSystemProfileId,
       "tnSysOtdrScanSystemProfileDescription": tnSysOtdrScanSystemProfileDescription,
       "tnSysOtdrScanSystemProfileWaveLength": tnSysOtdrScanSystemProfileWaveLength,
       "tnSysOtdrScanSystemProfilePulseLength": tnSysOtdrScanSystemProfilePulseLength,
       "tnSysOtdrScanSystemProfileRange": tnSysOtdrScanSystemProfileRange,
       "tnSysOtdrScanSystemProfileResolution": tnSysOtdrScanSystemProfileResolution,
       "tnSysOtdrScanSystemProfileAvgTime": tnSysOtdrScanSystemProfileAvgTime,
       "tnSysOtdrScanSystemProfileEventThreshold": tnSysOtdrScanSystemProfileEventThreshold,
       "tnSysOtdrScanSystemProfileIOR": tnSysOtdrScanSystemProfileIOR,
       "tnSysOtdrScanTransfer": tnSysOtdrScanTransfer,
       "tnSysOtdrScanTransferRemoteHostIp": tnSysOtdrScanTransferRemoteHostIp,
       "tnSysOtdrScanTransferCommand": tnSysOtdrScanTransferCommand,
       "tnSysOtdrScanTransferRemotePath": tnSysOtdrScanTransferRemotePath,
       "tnSysOtdrScanTransferStatus": tnSysOtdrScanTransferStatus,
       "tnSysOtdrScanTransferFilename": tnSysOtdrScanTransferFilename,
       "tnSysOtdrScanTransferProtocol": tnSysOtdrScanTransferProtocol,
       "tnSysOtdrScanTransferUserId": tnSysOtdrScanTransferUserId,
       "tnSysOtdrScanTransferPassword": tnSysOtdrScanTransferPassword,
       "tnSysOtdrScanTransferInetAddressType": tnSysOtdrScanTransferInetAddressType,
       "tnSysOtdrScanTransferInetAddress": tnSysOtdrScanTransferInetAddress,
       "tnSysOtdrScanTransferPort": tnSysOtdrScanTransferPort,
       "tnSysOtdrScanSystemProfileM": tnSysOtdrScanSystemProfileM,
       "tnSysOtdrScanSystemProfileMAttributeTotal": tnSysOtdrScanSystemProfileMAttributeTotal,
       "tnSysOtdrScanSystemProfileMTable": tnSysOtdrScanSystemProfileMTable,
       "tnSysOtdrScanSystemProfileMEntry": tnSysOtdrScanSystemProfileMEntry,
       "tnSysOtdrScanSystemProfileMId": tnSysOtdrScanSystemProfileMId,
       "tnSysOtdrScanSystemProfileMDescription": tnSysOtdrScanSystemProfileMDescription,
       "tnSysOtdrScanSystemProfileMWaveLength": tnSysOtdrScanSystemProfileMWaveLength,
       "tnSysOtdrScanSystemProfileMPulseLength": tnSysOtdrScanSystemProfileMPulseLength,
       "tnSysOtdrScanSystemProfileMRange": tnSysOtdrScanSystemProfileMRange,
       "tnSysOtdrScanSystemProfileMResolution": tnSysOtdrScanSystemProfileMResolution,
       "tnSysOtdrScanSystemProfileMAvgTime": tnSysOtdrScanSystemProfileMAvgTime,
       "tnSysOtdrScanSystemProfileMEventThreshold": tnSysOtdrScanSystemProfileMEventThreshold,
       "tnSysOtdrScanSystemProfileMIOR": tnSysOtdrScanSystemProfileMIOR,
       "tnSysOtdrScanResultsTransfer": tnSysOtdrScanResultsTransfer,
       "tnSysOtdrScanResultsTransferRemoteHostIp": tnSysOtdrScanResultsTransferRemoteHostIp,
       "tnSysOtdrScanResultsTransferProtocol": tnSysOtdrScanResultsTransferProtocol,
       "tnSysOtdrScanResultsTransferUserId": tnSysOtdrScanResultsTransferUserId,
       "tnSysOtdrScanResultsTransferPassword": tnSysOtdrScanResultsTransferPassword,
       "tnSysOtdrScanResultsTransferRemotePath": tnSysOtdrScanResultsTransferRemotePath,
       "tnSysOtdrScanResultsTransferCommand": tnSysOtdrScanResultsTransferCommand,
       "tnSysOtdrScanResultsTransferFilename": tnSysOtdrScanResultsTransferFilename,
       "tnSysOtdrScanResultsTransferRecentSuccessFile": tnSysOtdrScanResultsTransferRecentSuccessFile,
       "tnSysOtdrScanResultsTransferStatus": tnSysOtdrScanResultsTransferStatus,
       "tnSysOtdrScanResultsLastTransferTimestamp": tnSysOtdrScanResultsLastTransferTimestamp,
       "tnSysOtdrScanResultsTransferRemoteInetAddressType": tnSysOtdrScanResultsTransferRemoteInetAddressType,
       "tnSysOtdrScanResultsTransferRemoteInetAddress": tnSysOtdrScanResultsTransferRemoteInetAddress,
       "tnSysOtdrScanResultsTransferPort": tnSysOtdrScanResultsTransferPort,
       "tnSysOtdrScanResultsTransferRemoveFileFromNE": tnSysOtdrScanResultsTransferRemoveFileFromNE,
       "tnClusterObjs": tnClusterObjs,
       "tnClusterTable": tnClusterTable,
       "tnClusterEntry": tnClusterEntry,
       "tnClusterRowStatus": tnClusterRowStatus,
       "tnClusterFarEndNode": tnClusterFarEndNode,
       "tnClusterIpAddress": tnClusterIpAddress,
       "tnClusterlinkStatus": tnClusterlinkStatus,
       "tnClusterInetAddressType": tnClusterInetAddressType,
       "tnClusterInetAddress": tnClusterInetAddress,
       "tnSysPmFetchBulk": tnSysPmFetchBulk,
       "tnSysPmFetchBulkStart": tnSysPmFetchBulkStart,
       "tnSysPmFetchBulkStatus": tnSysPmFetchBulkStatus,
       "tnSysPmFetchBulkRemoteHostIp": tnSysPmFetchBulkRemoteHostIp,
       "tnSysPmFetchBulkUserId": tnSysPmFetchBulkUserId,
       "tnSysPmFetchBulkPassword": tnSysPmFetchBulkPassword,
       "tnSysPmFetchBulkRemotePath": tnSysPmFetchBulkRemotePath,
       "tnSysPmFetchBulkStatsInterval": tnSysPmFetchBulkStatsInterval,
       "tnSysPmFetchBulkBinnedStatsBin": tnSysPmFetchBulkBinnedStatsBin,
       "tnSysPmFetchBulkShelfNum": tnSysPmFetchBulkShelfNum,
       "tnSysDebugTransfer": tnSysDebugTransfer,
       "tnSysDebugTransferRemoteHostIp": tnSysDebugTransferRemoteHostIp,
       "tnSysDebugTransferCommand": tnSysDebugTransferCommand,
       "tnSysDebugTransferRemotePath": tnSysDebugTransferRemotePath,
       "tnSysDebugTransferStatus": tnSysDebugTransferStatus,
       "tnSysDebugTransferProtocol": tnSysDebugTransferProtocol,
       "tnSysDebugTransferUserId": tnSysDebugTransferUserId,
       "tnSysDebugTransferPassword": tnSysDebugTransferPassword,
       "tnSysDebugTransferFilename": tnSysDebugTransferFilename,
       "tnSysDebugTransferRecentSuccessFile": tnSysDebugTransferRecentSuccessFile,
       "tnSysDebugTransferTimestamp": tnSysDebugTransferTimestamp,
       "tnSysDebugTransferShelfNum": tnSysDebugTransferShelfNum,
       "tnSysDebugTransferPercentCompleted": tnSysDebugTransferPercentCompleted,
       "tnSysDebugTransferRemoteInetAddress": tnSysDebugTransferRemoteInetAddress,
       "tnSysDebugTransferRemoteInetAddressType": tnSysDebugTransferRemoteInetAddressType,
       "tnSysDebugTransferScratchDir": tnSysDebugTransferScratchDir,
       "tnSysDebugTransferIncludeInDumps": tnSysDebugTransferIncludeInDumps,
       "tnSysDebugTransferPort": tnSysDebugTransferPort,
       "tnSysLicenseInv": tnSysLicenseInv,
       "tnSysLicenseInvPathIp": tnSysLicenseInvPathIp,
       "tnSysLicenseInvFile": tnSysLicenseInvFile,
       "tnSysLicenseInvProtocol": tnSysLicenseInvProtocol,
       "tnSysLicenseInvUserId": tnSysLicenseInvUserId,
       "tnSysLicenseInvPassword": tnSysLicenseInvPassword,
       "tnSysLicenseInvFileUploadOper": tnSysLicenseInvFileUploadOper,
       "tnSysLicenseInvPathInetAddressType": tnSysLicenseInvPathInetAddressType,
       "tnSysLicenseInvPathInetAddress": tnSysLicenseInvPathInetAddress,
       "tnSysLicenseInvLastOperPercentCompleted": tnSysLicenseInvLastOperPercentCompleted,
       "tnSysLicenseInvLastUploadFileName": tnSysLicenseInvLastUploadFileName,
       "tnSysLicenseInvFileLastUploadStatus": tnSysLicenseInvFileLastUploadStatus,
       "tnSysLicenseInvFileLastUploadTimeStamp": tnSysLicenseInvFileLastUploadTimeStamp,
       "tnSysLinux": tnSysLinux,
       "tnSysLinuxRootUserId": tnSysLinuxRootUserId,
       "tnSysLinuxRootUserPassword": tnSysLinuxRootUserPassword,
       "tnSysLinuxApplUserId": tnSysLinuxApplUserId,
       "tnSysLinuxApplUserPassword": tnSysLinuxApplUserPassword,
       "tnSysLinuxRootPasswordStatus": tnSysLinuxRootPasswordStatus,
       "tnSysLinuxApplPasswordStatus": tnSysLinuxApplPasswordStatus,
       "tnSysLinuxRootUserStatus": tnSysLinuxRootUserStatus,
       "tnSysLinuxApplUserStatus": tnSysLinuxApplUserStatus,
       "tnSysLinuxLoginInactivityTimeOut": tnSysLinuxLoginInactivityTimeOut,
       "tnSysLinuxSmsUserId": tnSysLinuxSmsUserId,
       "tnSysLinuxSmsUserPassword": tnSysLinuxSmsUserPassword,
       "tnSysLinuxSmsPasswordStatus": tnSysLinuxSmsPasswordStatus,
       "tnSysLinuxSmsUserStatus": tnSysLinuxSmsUserStatus,
       "tnSysLinuxRootUserLocalStatus": tnSysLinuxRootUserLocalStatus,
       "tnSysLinuxSecurityCommit": tnSysLinuxSecurityCommit,
       "tnSysLinuxRootUserPort": tnSysLinuxRootUserPort,
       "tnSysIpAclIpv6SysDefault": tnSysIpAclIpv6SysDefault,
       "tnSysIpAclIpv6RxAction": tnSysIpAclIpv6RxAction,
       "tnSysIpAclIpv6TxAction": tnSysIpAclIpv6TxAction,
       "tnSysIpAclIpv6SnmpCfgEnable": tnSysIpAclIpv6SnmpCfgEnable,
       "tnSysIpAclIpv6CfgRestoreToDefault": tnSysIpAclIpv6CfgRestoreToDefault,
       "tnSysIpAclIPv6ClearCounter": tnSysIpAclIPv6ClearCounter,
       "tnSysFileInitialization": tnSysFileInitialization,
       "tnSysFileInitializationRoot": tnSysFileInitializationRoot,
       "tnSysFileInitializationUserId": tnSysFileInitializationUserId,
       "tnSysFileInitializationPassword": tnSysFileInitializationPassword,
       "tnSysFileInitializationFilename": tnSysFileInitializationFilename,
       "tnSysFileInitializationInetAddressType": tnSysFileInitializationInetAddressType,
       "tnSysFileInitializationInetAddress": tnSysFileInitializationInetAddress,
       "tnSysBtInterface": tnSysBtInterface,
       "tnSysBtInterfaceDescription": tnSysBtInterfaceDescription,
       "tnSysBtInterfaceIpAddr": tnSysBtInterfaceIpAddr,
       "tnSysBtInterfaceIpSubMask": tnSysBtInterfaceIpSubMask,
       "tnSysBtInterfaceAdminState": tnSysBtInterfaceAdminState,
       "tnSysBtInterfaceLinkIntegrityStatus": tnSysBtInterfaceLinkIntegrityStatus,
       "tnSysBtInterfaceDHCPServer": tnSysBtInterfaceDHCPServer,
       "tnSysBtInterfaceDHCPRange": tnSysBtInterfaceDHCPRange,
       "tnSysBtInterfaceNodeSerialNum": tnSysBtInterfaceNodeSerialNum,
       "tnSysBtInterfaceMacAddress": tnSysBtInterfaceMacAddress,
       "tnSysLicenseMgr": tnSysLicenseMgr,
       "tnSysLicenseMgrKeepAliveTimer": tnSysLicenseMgrKeepAliveTimer,
       "tnSysLicenseMgrPrimaryServerIp": tnSysLicenseMgrPrimaryServerIp,
       "tnSysLicenseMgrPrimaryServerInetAddressType": tnSysLicenseMgrPrimaryServerInetAddressType,
       "tnSysLicenseMgrPrimaryServerInetAddress": tnSysLicenseMgrPrimaryServerInetAddress,
       "tnSysLicenseMgrSecondaryServerIp": tnSysLicenseMgrSecondaryServerIp,
       "tnSysLicenseMgrSecondaryServerInetAddressType": tnSysLicenseMgrSecondaryServerInetAddressType,
       "tnSysLicenseMgrSecondaryServerInetAddress": tnSysLicenseMgrSecondaryServerInetAddress,
       "tnSysLicenseMgrPrimaryServerStatus": tnSysLicenseMgrPrimaryServerStatus,
       "tnSysLicenseMgrSecondaryServerStatus": tnSysLicenseMgrSecondaryServerStatus,
       "tnSysLicenseMgrExpiration": tnSysLicenseMgrExpiration,
       "tnSysLicenseMgrTimeOut": tnSysLicenseMgrTimeOut,
       "tnSysLicenseMgrRetries": tnSysLicenseMgrRetries,
       "tnSysLicenseMgrLastRefresh": tnSysLicenseMgrLastRefresh,
       "tnSysLicenseMgrCertStatus": tnSysLicenseMgrCertStatus,
       "tnSysLicenseMgrNextRefreshTime": tnSysLicenseMgrNextRefreshTime,
       "tnLicenseObjs": tnLicenseObjs,
       "tnLicenseEntityTable": tnLicenseEntityTable,
       "tnLicenseEntityEntry": tnLicenseEntityEntry,
       "tnLicenseEntity": tnLicenseEntity,
       "tnLicenseEntityRefreshSet": tnLicenseEntityRefreshSet,
       "tnLicenseEntityNumberInUse": tnLicenseEntityNumberInUse,
       "tnLicenseEntityNumberExceedAvail": tnLicenseEntityNumberExceedAvail,
       "tnLicenseEntityEntitlementNeeded": tnLicenseEntityEntitlementNeeded,
       "tnLicenseEntitlementTable": tnLicenseEntitlementTable,
       "tnLicenseEntitlementEntry": tnLicenseEntitlementEntry,
       "tnLicenseEntitlementCategoryID": tnLicenseEntitlementCategoryID,
       "tnLicenseEntitlementEntries": tnLicenseEntitlementEntries,
       "tnLicenseEntitlementDetails": tnLicenseEntitlementDetails,
       "tnSysKeyStore": tnSysKeyStore,
       "tnSysKeyStoreServiceTable": tnSysKeyStoreServiceTable,
       "tnSysKeyStoreServiceEntry": tnSysKeyStoreServiceEntry,
       "tnSysKeyStoreNameIndex": tnSysKeyStoreNameIndex,
       "tnSysKeyStoreTypeIndex": tnSysKeyStoreTypeIndex,
       "tnSysKeyStoreTransServerCommand": tnSysKeyStoreTransServerCommand,
       "tnSysKeyStoreTransServerProtocol": tnSysKeyStoreTransServerProtocol,
       "tnSysKeyStoreTransServerHost": tnSysKeyStoreTransServerHost,
       "tnSysKeyStoreTransServerPort": tnSysKeyStoreTransServerPort,
       "tnSysKeyStoreTransServerLocation": tnSysKeyStoreTransServerLocation,
       "tnSysKeyStoreTransServerUserId": tnSysKeyStoreTransServerUserId,
       "tnSysKeyStoreTransServerPassword": tnSysKeyStoreTransServerPassword,
       "tnSysKeyStoreTransServerInetAddressType": tnSysKeyStoreTransServerInetAddressType,
       "tnSysKeyStoreTransServerInetAddress": tnSysKeyStoreTransServerInetAddress,
       "tnSysKeyStoreServiceStatus": tnSysKeyStoreServiceStatus,
       "tnSysKeyStoreServerLastTransferTime": tnSysKeyStoreServerLastTransferTime,
       "tnSysKeyStoreTransServerURI": tnSysKeyStoreTransServerURI,
       "tnSysKeyStoreCertInfoTable": tnSysKeyStoreCertInfoTable,
       "tnSysKeyStoreCertInfoEntry": tnSysKeyStoreCertInfoEntry,
       "tnSysKeyStoreCertRepositoryIndex": tnSysKeyStoreCertRepositoryIndex,
       "tnSysKeyStoreCertIndex": tnSysKeyStoreCertIndex,
       "tnSysKeyStoreCertVersion": tnSysKeyStoreCertVersion,
       "tnSysKeyStoreCertSerialNumber": tnSysKeyStoreCertSerialNumber,
       "tnSysKeyStoreCertSignatureAlgorithm": tnSysKeyStoreCertSignatureAlgorithm,
       "tnSysKeyStoreCertIssuer": tnSysKeyStoreCertIssuer,
       "tnSysKeyStoreCertValidity": tnSysKeyStoreCertValidity,
       "tnSysKeyStoreCertSubject": tnSysKeyStoreCertSubject,
       "tnSysKeyStoreCertSubjectPublicKeyInfo": tnSysKeyStoreCertSubjectPublicKeyInfo,
       "tnSysKeyStoreCertKeyUsage": tnSysKeyStoreCertKeyUsage,
       "tnSysKeyStoreCertSubjectAlternativeName": tnSysKeyStoreCertSubjectAlternativeName,
       "tnSysKeyStoreCertExtendedKeyUsage": tnSysKeyStoreCertExtendedKeyUsage,
       "tnSysKeyStoreCertBasicConstraints": tnSysKeyStoreCertBasicConstraints,
       "tnSysKeyStoreCertSHA256Fingerprint": tnSysKeyStoreCertSHA256Fingerprint,
       "tnSysBgp": tnSysBgp,
       "tnSysBgpPeerTable": tnSysBgpPeerTable,
       "tnSysBgpPeerEntry": tnSysBgpPeerEntry,
       "tnSysBgpPeerIndex": tnSysBgpPeerIndex,
       "tnSysBgpPeerRowStatus": tnSysBgpPeerRowStatus,
       "tnSysBgpPeerInetAddressType": tnSysBgpPeerInetAddressType,
       "tnSysBgpPeerIp": tnSysBgpPeerIp,
       "tnSysBgpPeerInetAddress": tnSysBgpPeerInetAddress,
       "tnSysBgpPeerRemoteASN": tnSysBgpPeerRemoteASN,
       "tnSysBgpPeerSecurityKey": tnSysBgpPeerSecurityKey,
       "tnSysBgpPeerRouterId": tnSysBgpPeerRouterId,
       "tnSysBgpPeerStatus": tnSysBgpPeerStatus,
       "tnSysBgpMaxPrefixIpv4Limit": tnSysBgpMaxPrefixIpv4Limit,
       "tnSysBgpMaxPrefixIpv4Threshold": tnSysBgpMaxPrefixIpv4Threshold,
       "tnSysBgpMaxPrefixIpv4Action": tnSysBgpMaxPrefixIpv4Action,
       "tnSysBgpMaxPrefixIpv6Limit": tnSysBgpMaxPrefixIpv6Limit,
       "tnSysBgpMaxPrefixIpv6Threshold": tnSysBgpMaxPrefixIpv6Threshold,
       "tnSysBgpMaxPrefixIpv6Action": tnSysBgpMaxPrefixIpv6Action,
       "tnSysBgpStatsIpv4PrefixInCount": tnSysBgpStatsIpv4PrefixInCount,
       "tnSysBgpStatsIpv6PrefixInCount": tnSysBgpStatsIpv6PrefixInCount,
       "tnSysBgpStatsIpv4PrefixOutCount": tnSysBgpStatsIpv4PrefixOutCount,
       "tnSysBgpStatsIpv6PrefixOutCount": tnSysBgpStatsIpv6PrefixOutCount,
       "tnSysBgpPeerStatsInetAddressType": tnSysBgpPeerStatsInetAddressType,
       "tnSysBgpPeerStatsIp": tnSysBgpPeerStatsIp,
       "tnSysBgpPeerStatsInetAddress": tnSysBgpPeerStatsInetAddress,
       "tnSysDiscoverMe": tnSysDiscoverMe,
       "tnSysDiscoverMeTraps": tnSysDiscoverMeTraps,
       "tnSyslogServer": tnSyslogServer,
       "tnSyslogServerTable": tnSyslogServerTable,
       "tnSyslogServerEntry": tnSyslogServerEntry,
       "tnSyslogServerIndex": tnSyslogServerIndex,
       "tnSyslogServerIpAddress": tnSyslogServerIpAddress,
       "tnSyslogServerPort": tnSyslogServerPort,
       "tnSyslogServerFacility": tnSyslogServerFacility,
       "tnSyslogServerPriority": tnSyslogServerPriority,
       "tnSyslogServerEnabled": tnSyslogServerEnabled,
       "tnSyslogServerInetAddress": tnSyslogServerInetAddress,
       "tnSyslogServerInetAddressType": tnSyslogServerInetAddressType,
       "tnSyslogServerProtocol": tnSyslogServerProtocol,
       "tnSyslogServerType": tnSyslogServerType,
       "tnSyslogServerDomain": tnSyslogServerDomain,
       "tnPctObjs": tnPctObjs,
       "tnPctVerificationPeriod": tnPctVerificationPeriod,
       "tnPctVerificationLossThreshold": tnPctVerificationLossThreshold,
       "tnPctVerificationOffset": tnPctVerificationOffset,
       "tnPctVerificationStatus": tnPctVerificationStatus,
       "tnKeyObjs": tnKeyObjs,
       "tnHostKeyTable": tnHostKeyTable,
       "tnHostKeyEntry": tnHostKeyEntry,
       "tnHostKeyModuleID": tnHostKeyModuleID,
       "tnHostKeyIndex": tnHostKeyIndex,
       "tnHostKeyString1": tnHostKeyString1,
       "tnHostKeyString2": tnHostKeyString2,
       "tnSshPrivKeyTable": tnSshPrivKeyTable,
       "tnSshPrivKeyEntry": tnSshPrivKeyEntry,
       "tnSshPrivKeyModuleID": tnSshPrivKeyModuleID,
       "tnSshPrivKeyString1": tnSshPrivKeyString1,
       "tnSshPrivKeyString2": tnSshPrivKeyString2,
       "tnSshPrivKeyPassword": tnSshPrivKeyPassword,
       "tnSysNESshKeyTable": tnSysNESshKeyTable,
       "tnSysNESshKeyEntry": tnSysNESshKeyEntry,
       "tnSysNESshKeyUserName": tnSysNESshKeyUserName,
       "tnSysNESshKeyIndex": tnSysNESshKeyIndex,
       "tnSysNESshKeyRowStatus": tnSysNESshKeyRowStatus,
       "tnSysNESshKeyString1": tnSysNESshKeyString1,
       "tnSysNESshKeyString2": tnSysNESshKeyString2,
       "tnNESshKeyTable": tnNESshKeyTable,
       "tnNESshKeyEntry": tnNESshKeyEntry,
       "tnNESshKeyUserName": tnNESshKeyUserName,
       "tnNESshKeyIndex": tnNESshKeyIndex,
       "tnNESshKeyRowStatus": tnNESshKeyRowStatus,
       "tnNESshKeyString1": tnNESshKeyString1,
       "tnNESshKeyString2": tnNESshKeyString2,
       "tnSshCiphersTable": tnSshCiphersTable,
       "tnSshCiphersEntry": tnSshCiphersEntry,
       "tnSshCiphersAlgType": tnSshCiphersAlgType,
       "tnSshCiphersProfileName": tnSshCiphersProfileName,
       "tnSshCiphersEnabled": tnSshCiphersEnabled,
       "tnSshHostKeyTable": tnSshHostKeyTable,
       "tnSshHostKeyEntry": tnSshHostKeyEntry,
       "tnSshHostKeyAlgType": tnSshHostKeyAlgType,
       "tnSshHostKeyProfileName": tnSshHostKeyProfileName,
       "tnSshHostKeyEnabled": tnSshHostKeyEnabled,
       "tnSshMacsTable": tnSshMacsTable,
       "tnSshMacsEntry": tnSshMacsEntry,
       "tnSshMacsAlgType": tnSshMacsAlgType,
       "tnSshMacsProfileName": tnSshMacsProfileName,
       "tnSshMacsEnabled": tnSshMacsEnabled,
       "tnSshKexTable": tnSshKexTable,
       "tnSshKexEntry": tnSshKexEntry,
       "tnSshKexAlgType": tnSshKexAlgType,
       "tnSshKexProfileName": tnSshKexProfileName,
       "tnSshKexEnabled": tnSshKexEnabled,
       "tnSshPubKeyTable": tnSshPubKeyTable,
       "tnSshPubKeyEntry": tnSshPubKeyEntry,
       "tnSshPubKeyAlgType": tnSshPubKeyAlgType,
       "tnSshPubKeyProfileName": tnSshPubKeyProfileName,
       "tnSshPubKeyEnabled": tnSshPubKeyEnabled,
       "tnTlsProfileTable": tnTlsProfileTable,
       "tnTlsProfileEntry": tnTlsProfileEntry,
       "tnTlsProfileName": tnTlsProfileName,
       "tnTlsProfileMinVersion": tnTlsProfileMinVersion,
       "tnTlsProfileMaxVersion": tnTlsProfileMaxVersion,
       "tnTlsProfileMutualAuth": tnTlsProfileMutualAuth,
       "tnTlsProfileDescription": tnTlsProfileDescription,
       "tnSanListTable": tnSanListTable,
       "tnSanListEntry": tnSanListEntry,
       "tnSanListName": tnSanListName,
       "tnSanListType": tnSanListType,
       "tnSanListIndex": tnSanListIndex,
       "tnSanListRowStatus": tnSanListRowStatus,
       "tnCsrSanListTable": tnCsrSanListTable,
       "tnCsrSanListEntry": tnCsrSanListEntry,
       "tnCsrSanListType": tnCsrSanListType,
       "tnCsrSanListIndex": tnCsrSanListIndex,
       "tnCsrSanListRowStatus": tnCsrSanListRowStatus,
       "tnSanListAuthTable": tnSanListAuthTable,
       "tnSanListAuthEntry": tnSanListAuthEntry,
       "tnSanListAuthentication": tnSanListAuthentication,
       "tnSanListProfileDescription": tnSanListProfileDescription,
       "tnOcspProfileTable": tnOcspProfileTable,
       "tnOcspProfileEntry": tnOcspProfileEntry,
       "tnOcspProfileName": tnOcspProfileName,
       "tnOcspProfileRowStatus": tnOcspProfileRowStatus,
       "tnOcspProfileRetry": tnOcspProfileRetry,
       "tnOcspProfileServerUrl": tnOcspProfileServerUrl,
       "tnOcspProfileStatus": tnOcspProfileStatus,
       "tnOcspProfileTimeout": tnOcspProfileTimeout,
       "tnSshProfileTable": tnSshProfileTable,
       "tnSshProfileEntry": tnSshProfileEntry,
       "tnSshProfileName": tnSshProfileName,
       "tnSshProfileDescription": tnSshProfileDescription,
       "tnTransferSysLog": tnTransferSysLog,
       "tnTransferSysLogCommand": tnTransferSysLogCommand,
       "tnTransferSysLogRemoteHostIp": tnTransferSysLogRemoteHostIp,
       "tnTransferSysLogRemoteHostInetAddressType": tnTransferSysLogRemoteHostInetAddressType,
       "tnTransferSysLogRemoteHostInetAddress": tnTransferSysLogRemoteHostInetAddress,
       "tnTransferSysLogPort": tnTransferSysLogPort,
       "tnTransferSysLogProtocol": tnTransferSysLogProtocol,
       "tnTransferSysLogUserId": tnTransferSysLogUserId,
       "tnTransferSysLogPassword": tnTransferSysLogPassword,
       "tnTransferSysLogRemotePath": tnTransferSysLogRemotePath,
       "tnTransferSysLogPeriod": tnTransferSysLogPeriod,
       "tnTransferSysLogLastFileTransfer": tnTransferSysLogLastFileTransfer,
       "tnTransferSysLogEnable": tnTransferSysLogEnable,
       "tnSysHealthCare": tnSysHealthCare,
       "tnSysHealthCareCheckCommand": tnSysHealthCareCheckCommand,
       "tnSysHealthCareCheckShelfNum": tnSysHealthCareCheckShelfNum,
       "tnSysHealthCareCheckSlotNum": tnSysHealthCareCheckSlotNum,
       "tnSysHealthCareCheckPercentCompleted": tnSysHealthCareCheckPercentCompleted,
       "tnSysHealthCareCheckStatus": tnSysHealthCareCheckStatus,
       "tnSysHealthCareCheckResult": tnSysHealthCareCheckResult,
       "tnSysHealthCareCheckScratchDir": tnSysHealthCareCheckScratchDir,
       "tnSysHealthCareServerIp": tnSysHealthCareServerIp,
       "tnSysHealthCareServerProtocol": tnSysHealthCareServerProtocol,
       "tnSysHealthCareServerInetAddressType": tnSysHealthCareServerInetAddressType,
       "tnSysHealthCareServerInetAddress": tnSysHealthCareServerInetAddress,
       "tnSysHealthCareServerPort": tnSysHealthCareServerPort,
       "tnSysHealthCareServerUserId": tnSysHealthCareServerUserId,
       "tnSysHealthCareServerPassword": tnSysHealthCareServerPassword,
       "tnSysHealthCareServerLocation": tnSysHealthCareServerLocation,
       "tnSysHealthCareTransferCommand": tnSysHealthCareTransferCommand,
       "tnSysHealthCareTransferPercentCompleted": tnSysHealthCareTransferPercentCompleted,
       "tnSysHealthCareTransferStatus": tnSysHealthCareTransferStatus,
       "tnSysHealthCareTransferLastFile": tnSysHealthCareTransferLastFile,
       "tnSysHealthCareLastOperation": tnSysHealthCareLastOperation,
       "tnSysHealthCareSetCriteriaTcId": tnSysHealthCareSetCriteriaTcId,
       "tnSysHealthCareSetCriteria": tnSysHealthCareSetCriteria,
       "tnSysHealthCareDeleteCriteriaTcId": tnSysHealthCareDeleteCriteriaTcId,
       "tnSysHealthCareDeleteCriteria": tnSysHealthCareDeleteCriteria,
       "tnSysHealthCareApplyCriteriaCommand": tnSysHealthCareApplyCriteriaCommand,
       "tnSysTrapThrottling": tnSysTrapThrottling,
       "tnSysTrapThrottlingStatus": tnSysTrapThrottlingStatus,
       "tnSysTrapThrottlingThreshold1": tnSysTrapThrottlingThreshold1,
       "tnSysTrapThrottlingThreshold2": tnSysTrapThrottlingThreshold2,
       "tnSysTrapThrottlingThreshold3": tnSysTrapThrottlingThreshold3,
       "tnSysTrapThrottlingTimeOverThreshold": tnSysTrapThrottlingTimeOverThreshold,
       "tnSysTrapThrottlingTimeUnderThreshold": tnSysTrapThrottlingTimeUnderThreshold,
       "tnSysTrapThrottlingState": tnSysTrapThrottlingState,
       "tnSysNmsObjs": tnSysNmsObjs,
       "tnSysNmsIpListTable": tnSysNmsIpListTable,
       "tnSysNmsIpListEntry": tnSysNmsIpListEntry,
       "tnSysNmsIpListIndex": tnSysNmsIpListIndex,
       "tnSysNmsIpListRowStatus": tnSysNmsIpListRowStatus,
       "tnSysNmsIpListIpAddress": tnSysNmsIpListIpAddress,
       "tnSysNmsIpListInetAddress": tnSysNmsIpListInetAddress,
       "tnSysNmsIpListInetAddressType": tnSysNmsIpListInetAddressType,
       "tnSysDnsServer": tnSysDnsServer,
       "tnSysDnsServerTable": tnSysDnsServerTable,
       "tnSysDnsServerEntry": tnSysDnsServerEntry,
       "tnSysDnsServerIndex": tnSysDnsServerIndex,
       "tnSysDnsServerIpAddress": tnSysDnsServerIpAddress,
       "tnSysDnsServerInetAddress": tnSysDnsServerInetAddress,
       "tnSysDnsServerInetAddressType": tnSysDnsServerInetAddressType,
       "tnTransferPMDiscovery": tnTransferPMDiscovery,
       "tnTransferPMDiscoveryTable": tnTransferPMDiscoveryTable,
       "tnTransferPMDiscoveryEntry": tnTransferPMDiscoveryEntry,
       "tnTransferPMDiscoveryIndex": tnTransferPMDiscoveryIndex,
       "tnTransferPMDiscoveryRowStatus": tnTransferPMDiscoveryRowStatus,
       "tnTransferPMDiscoveryFilename": tnTransferPMDiscoveryFilename,
       "tnTransferPMDiscoveryControl": tnTransferPMDiscoveryControl,
       "tnTransferPMDiscoveryStatus": tnTransferPMDiscoveryStatus,
       "tnTransferPMDiscoveryErrorCode": tnTransferPMDiscoveryErrorCode,
       "tnTransferPMDiscoveryServerProtocol": tnTransferPMDiscoveryServerProtocol,
       "tnTransferPMDiscoveryServerIp": tnTransferPMDiscoveryServerIp,
       "tnTransferPMDiscoveryServerUserId": tnTransferPMDiscoveryServerUserId,
       "tnTransferPMDiscoveryServerPassword": tnTransferPMDiscoveryServerPassword,
       "tnTransferPMDiscoveryServerInetAddressType": tnTransferPMDiscoveryServerInetAddressType,
       "tnTransferPMDiscoveryServerInetAddress": tnTransferPMDiscoveryServerInetAddress,
       "tnTransferPMDiscoveryPort": tnTransferPMDiscoveryPort,
       "tnTransferPMDiscoveryPrevious15minBinFilesTransfer": tnTransferPMDiscoveryPrevious15minBinFilesTransfer,
       "tnTransferPMDiscoveryPrevious1dayBinFilesTransfer": tnTransferPMDiscoveryPrevious1dayBinFilesTransfer,
       "tnTransferPMDiscoveryTransferTimeOffset": tnTransferPMDiscoveryTransferTimeOffset,
       "tnTransferPMDiscovery15minBinFileTransferCount": tnTransferPMDiscovery15minBinFileTransferCount,
       "tnTransferPMDiscovery1dayBinFileTransferCount": tnTransferPMDiscovery1dayBinFileTransferCount,
       "tnTransferPMDiscovery15minBinFileTransferFailureCount": tnTransferPMDiscovery15minBinFileTransferFailureCount,
       "tnTransferPMDiscovery1dayBinFileTransferFailureCount": tnTransferPMDiscovery1dayBinFileTransferFailureCount}
)
