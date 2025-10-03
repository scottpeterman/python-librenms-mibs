# SNMP MIB module (EKINOPS-MGNT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ekinops\EKINOPS-MGNT2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:12 2025
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

(EkiApiState,
 EkiLoadGWSW,
 EkiLoadPermutMethod,
 EkiLoadPermutMode,
 EkiLoadState,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiLoadGWSW",
    "EkiLoadPermutMethod",
    "EkiLoadPermutMode",
    "EkiLoadState",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mgnt2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7)
)
if mibBuilder.loadTexts:
    mgnt2.setRevisions(
        ("2005-11-24 00:00",
         "2006-01-24 00:00",
         "2006-03-10 00:00",
         "2006-05-10 00:00",
         "2006-05-23 00:00",
         "2006-09-28 00:00",
         "2006-12-13 00:00",
         "2007-02-09 00:00",
         "2007-04-24 00:00",
         "2007-06-19 00:00",
         "2007-08-27 00:00",
         "2007-11-27 00:00",
         "2008-05-20 00:00",
         "2008-06-18 00:00",
         "2008-08-18 00:00",
         "2008-10-07 00:00",
         "2008-11-19 00:00",
         "2009-01-05 00:00",
         "2009-12-15 00:00",
         "2010-01-04 00:00",
         "2010-02-16 00:00",
         "2010-07-16 00:00",
         "2010-10-27 00:00",
         "2011-03-17 00:00",
         "2011-04-07 00:00",
         "2011-04-13 00:00",
         "2011-05-27 00:00",
         "2011-06-08 00:00",
         "2011-06-30 00:00",
         "2011-09-12 00:00",
         "2012-02-08 00:00",
         "2012-03-19 00:00",
         "2012-07-16 00:00",
         "2013-05-28 00:00",
         "2013-05-30 00:00",
         "2013-08-29 00:00",
         "2013-09-04 00:00",
         "2013-09-11 00:00",
         "2013-11-06 00:00",
         "2014-07-30 00:00",
         "2014-09-01 00:00",
         "2015-02-11 00:00",
         "2015-04-01 00:00",
         "2015-04-14 00:00",
         "2015-04-14 00:00",
         "2015-10-09 00:00",
         "2015-11-05 00:00",
         "2016-05-27 00:00",
         "2016-06-15 00:00",
         "2016-10-12 00:00",
         "2017-01-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Mgnt2CliAccessValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCliByEthernet", 0),
          ("cliBySSH", 1),
          ("cliByTelnet", 2))
    )



class Mgnt2CraftAccessValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCraftAccess", 0),
          ("craftEnable", 1),
          ("craftEnableHttps", 2))
    )



class Mgnt2DccAccessValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mode1Slots2s4s6s8s10", 0),
          ("mode2Slots2s6s10s14s18", 1))
    )



class Mgnt2TrapModeValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syntheticTrap", 0),
          ("detailedTrap", 1),
          ("nmsTrap", 2))
    )



class Mgnt2AckMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 1),
          ("modeB", 2))
    )



class Mgnt2PerfResyncValues(TextualConvention, Integer32):
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
        *(("perfResyncIdle", 1),
          ("perfResyncSync", 2),
          ("perfResyncReady", 3),
          ("perfResyncDelete", 4))
    )



class Mgnt2NetMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("gateway", 2))
    )



class Mgnt2MasterEthMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )



class Mgnt2SubnetEthMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )



class Mgnt2AuthTypeValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authLocal", 0),
          ("authRADIUS", 1),
          ("authLDAP", 2))
    )



class Mgnt2LogFileMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("linear", 1),
          ("rotary", 2))
    )



class Mgnt2SlotStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("slotEmpty", 0),
          ("pmReady", 1),
          ("pmReset", 2),
          ("pmLoad", 3),
          ("pmPassive", 4),
          ("pmUnknown", 5),
          ("pmNotReady", 6))
    )



class EkiPlugInState(TextualConvention, Integer32):
    status = "current"
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
        *(("absent", 0),
          ("loaded", 1),
          ("versionError", 2),
          ("symbolError", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Mgnt2SNMPAgentData_ObjectIdentity = ObjectIdentity
mgnt2SNMPAgentData = _Mgnt2SNMPAgentData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1)
)
_Mgnt2IPmanagment_ObjectIdentity = ObjectIdentity
mgnt2IPmanagment = _Mgnt2IPmanagment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1)
)
_Mgnt2GigmManagerIpAddressTable_Object = MibTable
mgnt2GigmManagerIpAddressTable = _Mgnt2GigmManagerIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mgnt2GigmManagerIpAddressTable.setStatus("current")
_Mgnt2GigmManagerIpAddressEntry_Object = MibTableRow
mgnt2GigmManagerIpAddressEntry = _Mgnt2GigmManagerIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1)
)
mgnt2GigmManagerIpAddressEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2GigmManagerIpIndex"),
)
if mibBuilder.loadTexts:
    mgnt2GigmManagerIpAddressEntry.setStatus("current")


class _Mgnt2GigmManagerIpIndex_Type(Integer32):
    """Custom type mgnt2GigmManagerIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2GigmManagerIpIndex_Type.__name__ = "Integer32"
_Mgnt2GigmManagerIpIndex_Object = MibTableColumn
mgnt2GigmManagerIpIndex = _Mgnt2GigmManagerIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 1),
    _Mgnt2GigmManagerIpIndex_Type()
)
mgnt2GigmManagerIpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerIpIndex.setStatus("current")
_Mgnt2GigmManagerIpAddress_Type = IpAddress
_Mgnt2GigmManagerIpAddress_Object = MibTableColumn
mgnt2GigmManagerIpAddress = _Mgnt2GigmManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 2),
    _Mgnt2GigmManagerIpAddress_Type()
)
mgnt2GigmManagerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerIpAddress.setStatus("current")
_Mgnt2GigmManagerIpAddressTableRowStatus_Type = RowStatus
_Mgnt2GigmManagerIpAddressTableRowStatus_Object = MibTableColumn
mgnt2GigmManagerIpAddressTableRowStatus = _Mgnt2GigmManagerIpAddressTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 3),
    _Mgnt2GigmManagerIpAddressTableRowStatus_Type()
)
mgnt2GigmManagerIpAddressTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerIpAddressTableRowStatus.setStatus("current")
_Mgnt2GigmManagerTrapPort_Type = Integer32
_Mgnt2GigmManagerTrapPort_Object = MibTableColumn
mgnt2GigmManagerTrapPort = _Mgnt2GigmManagerTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 4),
    _Mgnt2GigmManagerTrapPort_Type()
)
mgnt2GigmManagerTrapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerTrapPort.setStatus("current")
_Mgnt2GigmManagerEnableCtrl_Type = EkiOnOff
_Mgnt2GigmManagerEnableCtrl_Object = MibTableColumn
mgnt2GigmManagerEnableCtrl = _Mgnt2GigmManagerEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 5),
    _Mgnt2GigmManagerEnableCtrl_Type()
)
mgnt2GigmManagerEnableCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableCtrl.setStatus("current")
_Mgnt2GigmManagerEnableConfig_Type = EkiOnOff
_Mgnt2GigmManagerEnableConfig_Object = MibTableColumn
mgnt2GigmManagerEnableConfig = _Mgnt2GigmManagerEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 6),
    _Mgnt2GigmManagerEnableConfig_Type()
)
mgnt2GigmManagerEnableConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableConfig.setStatus("current")
_Mgnt2GigmManagerEnableEvent_Type = EkiOnOff
_Mgnt2GigmManagerEnableEvent_Object = MibTableColumn
mgnt2GigmManagerEnableEvent = _Mgnt2GigmManagerEnableEvent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 7),
    _Mgnt2GigmManagerEnableEvent_Type()
)
mgnt2GigmManagerEnableEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableEvent.setStatus("current")
_Mgnt2GigmManagerEnableAlarmCrit_Type = EkiOnOff
_Mgnt2GigmManagerEnableAlarmCrit_Object = MibTableColumn
mgnt2GigmManagerEnableAlarmCrit = _Mgnt2GigmManagerEnableAlarmCrit_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 8),
    _Mgnt2GigmManagerEnableAlarmCrit_Type()
)
mgnt2GigmManagerEnableAlarmCrit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableAlarmCrit.setStatus("current")
_Mgnt2GigmManagerEnableAlarmMajor_Type = EkiOnOff
_Mgnt2GigmManagerEnableAlarmMajor_Object = MibTableColumn
mgnt2GigmManagerEnableAlarmMajor = _Mgnt2GigmManagerEnableAlarmMajor_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 9),
    _Mgnt2GigmManagerEnableAlarmMajor_Type()
)
mgnt2GigmManagerEnableAlarmMajor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableAlarmMajor.setStatus("current")
_Mgnt2GigmManagerEnableAlarmMinor_Type = EkiOnOff
_Mgnt2GigmManagerEnableAlarmMinor_Object = MibTableColumn
mgnt2GigmManagerEnableAlarmMinor = _Mgnt2GigmManagerEnableAlarmMinor_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 10),
    _Mgnt2GigmManagerEnableAlarmMinor_Type()
)
mgnt2GigmManagerEnableAlarmMinor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableAlarmMinor.setStatus("current")
_Mgnt2GigmManagerRegistrationTimeout_Type = Integer32
_Mgnt2GigmManagerRegistrationTimeout_Object = MibTableColumn
mgnt2GigmManagerRegistrationTimeout = _Mgnt2GigmManagerRegistrationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 11),
    _Mgnt2GigmManagerRegistrationTimeout_Type()
)
mgnt2GigmManagerRegistrationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerRegistrationTimeout.setStatus("current")
_Mgnt2GigmManagerEnableAlarmWarning_Type = EkiOnOff
_Mgnt2GigmManagerEnableAlarmWarning_Object = MibTableColumn
mgnt2GigmManagerEnableAlarmWarning = _Mgnt2GigmManagerEnableAlarmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 12),
    _Mgnt2GigmManagerEnableAlarmWarning_Type()
)
mgnt2GigmManagerEnableAlarmWarning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableAlarmWarning.setStatus("current")
_Mgnt2GigmManagerEnableAlarmIndeterminate_Type = EkiOnOff
_Mgnt2GigmManagerEnableAlarmIndeterminate_Object = MibTableColumn
mgnt2GigmManagerEnableAlarmIndeterminate = _Mgnt2GigmManagerEnableAlarmIndeterminate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 1, 1, 13),
    _Mgnt2GigmManagerEnableAlarmIndeterminate_Type()
)
mgnt2GigmManagerEnableAlarmIndeterminate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmManagerEnableAlarmIndeterminate.setStatus("current")
_Mgnt2GigmBoardIpAddress_Type = IpAddress
_Mgnt2GigmBoardIpAddress_Object = MibScalar
mgnt2GigmBoardIpAddress = _Mgnt2GigmBoardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 2),
    _Mgnt2GigmBoardIpAddress_Type()
)
mgnt2GigmBoardIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmBoardIpAddress.setStatus("current")
_Mgnt2GigmIPAddresByDHCP_Type = EkiState
_Mgnt2GigmIPAddresByDHCP_Object = MibScalar
mgnt2GigmIPAddresByDHCP = _Mgnt2GigmIPAddresByDHCP_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 3),
    _Mgnt2GigmIPAddresByDHCP_Type()
)
mgnt2GigmIPAddresByDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmIPAddresByDHCP.setStatus("current")
_Mgnt2GigmNetmask_Type = IpAddress
_Mgnt2GigmNetmask_Object = MibScalar
mgnt2GigmNetmask = _Mgnt2GigmNetmask_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 4),
    _Mgnt2GigmNetmask_Type()
)
mgnt2GigmNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmNetmask.setStatus("current")
_Mgnt2GigmGatewayAddressTable_Object = MibTable
mgnt2GigmGatewayAddressTable = _Mgnt2GigmGatewayAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mgnt2GigmGatewayAddressTable.setStatus("current")
_Mgnt2GigmGatewayAddressEntry_Object = MibTableRow
mgnt2GigmGatewayAddressEntry = _Mgnt2GigmGatewayAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 5, 1)
)
mgnt2GigmGatewayAddressEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2GigmGatewayIndex"),
)
if mibBuilder.loadTexts:
    mgnt2GigmGatewayAddressEntry.setStatus("current")


class _Mgnt2GigmGatewayIndex_Type(Integer32):
    """Custom type mgnt2GigmGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Mgnt2GigmGatewayIndex_Type.__name__ = "Integer32"
_Mgnt2GigmGatewayIndex_Object = MibTableColumn
mgnt2GigmGatewayIndex = _Mgnt2GigmGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 5, 1, 1),
    _Mgnt2GigmGatewayIndex_Type()
)
mgnt2GigmGatewayIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmGatewayIndex.setStatus("current")
_Mgnt2GigmGatewayAddress_Type = IpAddress
_Mgnt2GigmGatewayAddress_Object = MibTableColumn
mgnt2GigmGatewayAddress = _Mgnt2GigmGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 5, 1, 2),
    _Mgnt2GigmGatewayAddress_Type()
)
mgnt2GigmGatewayAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmGatewayAddress.setStatus("current")
_Mgnt2GigmGatewayOrder_Type = Integer32
_Mgnt2GigmGatewayOrder_Object = MibTableColumn
mgnt2GigmGatewayOrder = _Mgnt2GigmGatewayOrder_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 5, 1, 3),
    _Mgnt2GigmGatewayOrder_Type()
)
mgnt2GigmGatewayOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgnt2GigmGatewayOrder.setStatus("current")
_Mgnt2GigmSyslog_Type = IpAddress
_Mgnt2GigmSyslog_Object = MibScalar
mgnt2GigmSyslog = _Mgnt2GigmSyslog_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 6),
    _Mgnt2GigmSyslog_Type()
)
mgnt2GigmSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmSyslog.setStatus("current")
_Mgnt2GigmNtpServer_Type = IpAddress
_Mgnt2GigmNtpServer_Object = MibScalar
mgnt2GigmNtpServer = _Mgnt2GigmNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 7),
    _Mgnt2GigmNtpServer_Type()
)
mgnt2GigmNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmNtpServer.setStatus("current")
_Mgnt2GigmNodeIpAddress_Type = IpAddress
_Mgnt2GigmNodeIpAddress_Object = MibScalar
mgnt2GigmNodeIpAddress = _Mgnt2GigmNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 1, 8),
    _Mgnt2GigmNodeIpAddress_Type()
)
mgnt2GigmNodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmNodeIpAddress.setStatus("current")
_Mgnt2ModulesManagement_ObjectIdentity = ObjectIdentity
mgnt2ModulesManagement = _Mgnt2ModulesManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2)
)
_Mgnt2GigmBoardTable_Object = MibTable
mgnt2GigmBoardTable = _Mgnt2GigmBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mgnt2GigmBoardTable.setStatus("current")
_Mgnt2GigmBoardEntry_Object = MibTableRow
mgnt2GigmBoardEntry = _Mgnt2GigmBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1)
)
mgnt2GigmBoardEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexBoards"),
)
if mibBuilder.loadTexts:
    mgnt2GigmBoardEntry.setStatus("current")


class _Mgnt2IndexBoards_Type(Integer32):
    """Custom type mgnt2IndexBoards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2IndexBoards_Type.__name__ = "Integer32"
_Mgnt2IndexBoards_Object = MibTableColumn
mgnt2IndexBoards = _Mgnt2IndexBoards_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 1),
    _Mgnt2IndexBoards_Type()
)
mgnt2IndexBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexBoards.setStatus("current")


class _Mgnt2Position_Type(Integer32):
    """Custom type mgnt2Position based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2Position_Type.__name__ = "Integer32"
_Mgnt2Position_Object = MibTableColumn
mgnt2Position = _Mgnt2Position_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 2),
    _Mgnt2Position_Type()
)
mgnt2Position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2Position.setStatus("current")
_Mgnt2Name_Type = DisplayString
_Mgnt2Name_Object = MibTableColumn
mgnt2Name = _Mgnt2Name_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 3),
    _Mgnt2Name_Type()
)
mgnt2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2Name.setStatus("current")


class _Mgnt2PortNumber_Type(Integer32):
    """Custom type mgnt2PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2PortNumber_Type.__name__ = "Integer32"
_Mgnt2PortNumber_Object = MibTableColumn
mgnt2PortNumber = _Mgnt2PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 4),
    _Mgnt2PortNumber_Type()
)
mgnt2PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PortNumber.setStatus("current")


class _Mgnt2LineNumber_Type(Integer32):
    """Custom type mgnt2LineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2LineNumber_Type.__name__ = "Integer32"
_Mgnt2LineNumber_Object = MibTableColumn
mgnt2LineNumber = _Mgnt2LineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 5),
    _Mgnt2LineNumber_Type()
)
mgnt2LineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LineNumber.setStatus("current")


class _Mgnt2GroupNumber_Type(Integer32):
    """Custom type mgnt2GroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2GroupNumber_Type.__name__ = "Integer32"
_Mgnt2GroupNumber_Object = MibTableColumn
mgnt2GroupNumber = _Mgnt2GroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 6),
    _Mgnt2GroupNumber_Type()
)
mgnt2GroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2GroupNumber.setStatus("current")
_Mgnt2RootOIDInventory_Type = ObjectIdentifier
_Mgnt2RootOIDInventory_Object = MibTableColumn
mgnt2RootOIDInventory = _Mgnt2RootOIDInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 7),
    _Mgnt2RootOIDInventory_Type()
)
mgnt2RootOIDInventory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2RootOIDInventory.setStatus("current")
_Mgnt2SlotOcc_Type = DisplayString
_Mgnt2SlotOcc_Object = MibTableColumn
mgnt2SlotOcc = _Mgnt2SlotOcc_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 8),
    _Mgnt2SlotOcc_Type()
)
mgnt2SlotOcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SlotOcc.setStatus("current")
_Mgnt2SubFunctionLabel_Type = DisplayString
_Mgnt2SubFunctionLabel_Object = MibTableColumn
mgnt2SubFunctionLabel = _Mgnt2SubFunctionLabel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 9),
    _Mgnt2SubFunctionLabel_Type()
)
mgnt2SubFunctionLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SubFunctionLabel.setStatus("current")
_Mgnt2SlotStatus_Type = Mgnt2SlotStatus
_Mgnt2SlotStatus_Object = MibTableColumn
mgnt2SlotStatus = _Mgnt2SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 1, 1, 10),
    _Mgnt2SlotStatus_Type()
)
mgnt2SlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SlotStatus.setStatus("current")


class _Mgnt2GigmSelectedBoard_Type(Integer32):
    """Custom type mgnt2GigmSelectedBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Mgnt2GigmSelectedBoard_Type.__name__ = "Integer32"
_Mgnt2GigmSelectedBoard_Object = MibScalar
mgnt2GigmSelectedBoard = _Mgnt2GigmSelectedBoard_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 2, 7),
    _Mgnt2GigmSelectedBoard_Type()
)
mgnt2GigmSelectedBoard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmSelectedBoard.setStatus("current")
_Mgnt2GigmMibsTable_Object = MibTable
mgnt2GigmMibsTable = _Mgnt2GigmMibsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 4)
)
if mibBuilder.loadTexts:
    mgnt2GigmMibsTable.setStatus("obsolete")
_Mgnt2GigmMibsEntry_Object = MibTableRow
mgnt2GigmMibsEntry = _Mgnt2GigmMibsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 4, 1)
)
mgnt2GigmMibsEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexMibs"),
)
if mibBuilder.loadTexts:
    mgnt2GigmMibsEntry.setStatus("obsolete")


class _Mgnt2IndexMibs_Type(Integer32):
    """Custom type mgnt2IndexMibs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Mgnt2IndexMibs_Type.__name__ = "Integer32"
_Mgnt2IndexMibs_Object = MibTableColumn
mgnt2IndexMibs = _Mgnt2IndexMibs_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 4, 1, 1),
    _Mgnt2IndexMibs_Type()
)
mgnt2IndexMibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexMibs.setStatus("obsolete")
_Mgnt2MibName_Type = DisplayString
_Mgnt2MibName_Object = MibTableColumn
mgnt2MibName = _Mgnt2MibName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 4, 1, 2),
    _Mgnt2MibName_Type()
)
mgnt2MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2MibName.setStatus("obsolete")
_Mgnt2MibPartNumber_Type = DisplayString
_Mgnt2MibPartNumber_Object = MibTableColumn
mgnt2MibPartNumber = _Mgnt2MibPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 4, 1, 3),
    _Mgnt2MibPartNumber_Type()
)
mgnt2MibPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2MibPartNumber.setStatus("obsolete")
_Mgnt2GigmLogicalName_Type = DisplayString
_Mgnt2GigmLogicalName_Object = MibScalar
mgnt2GigmLogicalName = _Mgnt2GigmLogicalName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 5),
    _Mgnt2GigmLogicalName_Type()
)
mgnt2GigmLogicalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLogicalName.setStatus("current")


class _Mgnt2GigmEqptType_Type(Integer32):
    """Custom type mgnt2GigmEqptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Mgnt2GigmEqptType_Type.__name__ = "Integer32"
_Mgnt2GigmEqptType_Object = MibScalar
mgnt2GigmEqptType = _Mgnt2GigmEqptType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 6),
    _Mgnt2GigmEqptType_Type()
)
mgnt2GigmEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2GigmEqptType.setStatus("current")
_Mgnt2GigmTrapCount_ObjectIdentity = ObjectIdentity
mgnt2GigmTrapCount = _Mgnt2GigmTrapCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 7)
)


class _Mgnt2GigmTrapCounter_Type(Integer32):
    """Custom type mgnt2GigmTrapCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mgnt2GigmTrapCounter_Type.__name__ = "Integer32"
_Mgnt2GigmTrapCounter_Object = MibScalar
mgnt2GigmTrapCounter = _Mgnt2GigmTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 7, 1),
    _Mgnt2GigmTrapCounter_Type()
)
mgnt2GigmTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2GigmTrapCounter.setStatus("current")
_Mgnt2GigmResetTrapCounter_Type = EkiOnOff
_Mgnt2GigmResetTrapCounter_Object = MibScalar
mgnt2GigmResetTrapCounter = _Mgnt2GigmResetTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 7, 2),
    _Mgnt2GigmResetTrapCounter_Type()
)
mgnt2GigmResetTrapCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmResetTrapCounter.setStatus("current")
_Mgnt2GigmSecurity_ObjectIdentity = ObjectIdentity
mgnt2GigmSecurity = _Mgnt2GigmSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 8)
)
_Mgnt2GigmRoCommunity_Type = DisplayString
_Mgnt2GigmRoCommunity_Object = MibScalar
mgnt2GigmRoCommunity = _Mgnt2GigmRoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 8, 1),
    _Mgnt2GigmRoCommunity_Type()
)
mgnt2GigmRoCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmRoCommunity.setStatus("current")
_Mgnt2GigmRwCommunity_Type = DisplayString
_Mgnt2GigmRwCommunity_Object = MibScalar
mgnt2GigmRwCommunity = _Mgnt2GigmRwCommunity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 8, 2),
    _Mgnt2GigmRwCommunity_Type()
)
mgnt2GigmRwCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmRwCommunity.setStatus("current")
_Mgnt2GigmTrapCommunity_Type = DisplayString
_Mgnt2GigmTrapCommunity_Object = MibScalar
mgnt2GigmTrapCommunity = _Mgnt2GigmTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 8, 3),
    _Mgnt2GigmTrapCommunity_Type()
)
mgnt2GigmTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmTrapCommunity.setStatus("current")
_Mgnt2GigmTime_ObjectIdentity = ObjectIdentity
mgnt2GigmTime = _Mgnt2GigmTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9)
)


class _Mgnt2GigmCurrentHour_Type(Integer32):
    """Custom type mgnt2GigmCurrentHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Mgnt2GigmCurrentHour_Type.__name__ = "Integer32"
_Mgnt2GigmCurrentHour_Object = MibScalar
mgnt2GigmCurrentHour = _Mgnt2GigmCurrentHour_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9, 1),
    _Mgnt2GigmCurrentHour_Type()
)
mgnt2GigmCurrentHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmCurrentHour.setStatus("current")


class _Mgnt2GigmCurrentMinute_Type(Integer32):
    """Custom type mgnt2GigmCurrentMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Mgnt2GigmCurrentMinute_Type.__name__ = "Integer32"
_Mgnt2GigmCurrentMinute_Object = MibScalar
mgnt2GigmCurrentMinute = _Mgnt2GigmCurrentMinute_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9, 2),
    _Mgnt2GigmCurrentMinute_Type()
)
mgnt2GigmCurrentMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmCurrentMinute.setStatus("current")


class _Mgnt2GigmCurrentYear_Type(Integer32):
    """Custom type mgnt2GigmCurrentYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1970, 3000),
    )


_Mgnt2GigmCurrentYear_Type.__name__ = "Integer32"
_Mgnt2GigmCurrentYear_Object = MibScalar
mgnt2GigmCurrentYear = _Mgnt2GigmCurrentYear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9, 3),
    _Mgnt2GigmCurrentYear_Type()
)
mgnt2GigmCurrentYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmCurrentYear.setStatus("current")


class _Mgnt2GigmCurrentMonth_Type(Integer32):
    """Custom type mgnt2GigmCurrentMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Mgnt2GigmCurrentMonth_Type.__name__ = "Integer32"
_Mgnt2GigmCurrentMonth_Object = MibScalar
mgnt2GigmCurrentMonth = _Mgnt2GigmCurrentMonth_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9, 4),
    _Mgnt2GigmCurrentMonth_Type()
)
mgnt2GigmCurrentMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmCurrentMonth.setStatus("current")


class _Mgnt2GigmCurrentDay_Type(Integer32):
    """Custom type mgnt2GigmCurrentDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Mgnt2GigmCurrentDay_Type.__name__ = "Integer32"
_Mgnt2GigmCurrentDay_Object = MibScalar
mgnt2GigmCurrentDay = _Mgnt2GigmCurrentDay_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 9, 5),
    _Mgnt2GigmCurrentDay_Type()
)
mgnt2GigmCurrentDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmCurrentDay.setStatus("current")
_Mgnt2Authentication_ObjectIdentity = ObjectIdentity
mgnt2Authentication = _Mgnt2Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10)
)
_Mgnt2GigmRadiusServer_Type = IpAddress
_Mgnt2GigmRadiusServer_Object = MibScalar
mgnt2GigmRadiusServer = _Mgnt2GigmRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 1),
    _Mgnt2GigmRadiusServer_Type()
)
mgnt2GigmRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmRadiusServer.setStatus("current")
_Mgnt2GigmRadiusPort_Type = Integer32
_Mgnt2GigmRadiusPort_Object = MibScalar
mgnt2GigmRadiusPort = _Mgnt2GigmRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 2),
    _Mgnt2GigmRadiusPort_Type()
)
mgnt2GigmRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmRadiusPort.setStatus("current")
_Mgnt2GigmRadiusSecret_Type = DisplayString
_Mgnt2GigmRadiusSecret_Object = MibScalar
mgnt2GigmRadiusSecret = _Mgnt2GigmRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 3),
    _Mgnt2GigmRadiusSecret_Type()
)
mgnt2GigmRadiusSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmRadiusSecret.setStatus("current")
_Mgnt2GigmLdapHost_Type = IpAddress
_Mgnt2GigmLdapHost_Object = MibScalar
mgnt2GigmLdapHost = _Mgnt2GigmLdapHost_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 4),
    _Mgnt2GigmLdapHost_Type()
)
mgnt2GigmLdapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapHost.setStatus("deprecated")
_Mgnt2GigmLdapPort_Type = Integer32
_Mgnt2GigmLdapPort_Object = MibScalar
mgnt2GigmLdapPort = _Mgnt2GigmLdapPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 5),
    _Mgnt2GigmLdapPort_Type()
)
mgnt2GigmLdapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapPort.setStatus("deprecated")
_Mgnt2GigmLdapBase_Type = DisplayString
_Mgnt2GigmLdapBase_Object = MibScalar
mgnt2GigmLdapBase = _Mgnt2GigmLdapBase_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 6),
    _Mgnt2GigmLdapBase_Type()
)
mgnt2GigmLdapBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapBase.setStatus("deprecated")
_Mgnt2GigmLdapVersion_Type = Integer32
_Mgnt2GigmLdapVersion_Object = MibScalar
mgnt2GigmLdapVersion = _Mgnt2GigmLdapVersion_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 7),
    _Mgnt2GigmLdapVersion_Type()
)
mgnt2GigmLdapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapVersion.setStatus("deprecated")
_Mgnt2GigmLdapBindDn_Type = DisplayString
_Mgnt2GigmLdapBindDn_Object = MibScalar
mgnt2GigmLdapBindDn = _Mgnt2GigmLdapBindDn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 8),
    _Mgnt2GigmLdapBindDn_Type()
)
mgnt2GigmLdapBindDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapBindDn.setStatus("deprecated")
_Mgnt2GigmLdapBindPw_Type = DisplayString
_Mgnt2GigmLdapBindPw_Object = MibScalar
mgnt2GigmLdapBindPw = _Mgnt2GigmLdapBindPw_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 9),
    _Mgnt2GigmLdapBindPw_Type()
)
mgnt2GigmLdapBindPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapBindPw.setStatus("deprecated")
_Mgnt2GigmLdapScope_Type = DisplayString
_Mgnt2GigmLdapScope_Object = MibScalar
mgnt2GigmLdapScope = _Mgnt2GigmLdapScope_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 10),
    _Mgnt2GigmLdapScope_Type()
)
mgnt2GigmLdapScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapScope.setStatus("deprecated")
_Mgnt2GigmLdapPamPasswd_Type = DisplayString
_Mgnt2GigmLdapPamPasswd_Object = MibScalar
mgnt2GigmLdapPamPasswd = _Mgnt2GigmLdapPamPasswd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 11),
    _Mgnt2GigmLdapPamPasswd_Type()
)
mgnt2GigmLdapPamPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmLdapPamPasswd.setStatus("deprecated")
_Mgnt2GigmAuthenticationType_Type = Mgnt2AuthTypeValues
_Mgnt2GigmAuthenticationType_Object = MibScalar
mgnt2GigmAuthenticationType = _Mgnt2GigmAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 1, 10, 12),
    _Mgnt2GigmAuthenticationType_Type()
)
mgnt2GigmAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmAuthenticationType.setStatus("current")
_Mgnt2Hardware_ObjectIdentity = ObjectIdentity
mgnt2Hardware = _Mgnt2Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2)
)
_Mgnt2alarms_ObjectIdentity = ObjectIdentity
mgnt2alarms = _Mgnt2alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1)
)
_Mgnt2AlmsynthAlm0_ObjectIdentity = ObjectIdentity
mgnt2AlmsynthAlm0 = _Mgnt2AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0)
)
_Mgnt2AlmAbsFailure_Type = EkiOnOff
_Mgnt2AlmAbsFailure_Object = MibScalar
mgnt2AlmAbsFailure = _Mgnt2AlmAbsFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 9),
    _Mgnt2AlmAbsFailure_Type()
)
mgnt2AlmAbsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmAbsFailure.setStatus("current")
_Mgnt2AlmFansFailure_Type = EkiOnOff
_Mgnt2AlmFansFailure_Object = MibScalar
mgnt2AlmFansFailure = _Mgnt2AlmFansFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 10),
    _Mgnt2AlmFansFailure_Type()
)
mgnt2AlmFansFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFansFailure.setStatus("current")
_Mgnt2AlmDef48a_Type = EkiOnOff
_Mgnt2AlmDef48a_Object = MibScalar
mgnt2AlmDef48a = _Mgnt2AlmDef48a_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 11),
    _Mgnt2AlmDef48a_Type()
)
mgnt2AlmDef48a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmDef48a.setStatus("current")
_Mgnt2AlmDef48b_Type = EkiOnOff
_Mgnt2AlmDef48b_Object = MibScalar
mgnt2AlmDef48b = _Mgnt2AlmDef48b_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 12),
    _Mgnt2AlmDef48b_Type()
)
mgnt2AlmDef48b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmDef48b.setStatus("current")
_Mgnt2AlmMgntDefFuseA_Type = EkiOnOff
_Mgnt2AlmMgntDefFuseA_Object = MibScalar
mgnt2AlmMgntDefFuseA = _Mgnt2AlmMgntDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 15),
    _Mgnt2AlmMgntDefFuseA_Type()
)
mgnt2AlmMgntDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmMgntDefFuseA.setStatus("current")
_Mgnt2AlmMgntDefFuseB_Type = EkiOnOff
_Mgnt2AlmMgntDefFuseB_Object = MibScalar
mgnt2AlmMgntDefFuseB = _Mgnt2AlmMgntDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 0, 16),
    _Mgnt2AlmMgntDefFuseB_Type()
)
mgnt2AlmMgntDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmMgntDefFuseB.setStatus("current")
_Mgnt2AlmsynthAlm1_ObjectIdentity = ObjectIdentity
mgnt2AlmsynthAlm1 = _Mgnt2AlmsynthAlm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 1)
)
_Mgnt2AlmNurgVisual_Type = EkiOnOff
_Mgnt2AlmNurgVisual_Object = MibScalar
mgnt2AlmNurgVisual = _Mgnt2AlmNurgVisual_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 1, 1),
    _Mgnt2AlmNurgVisual_Type()
)
mgnt2AlmNurgVisual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmNurgVisual.setStatus("current")
_Mgnt2AlmUrgVisual_Type = EkiOnOff
_Mgnt2AlmUrgVisual_Object = MibScalar
mgnt2AlmUrgVisual = _Mgnt2AlmUrgVisual_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 1, 2),
    _Mgnt2AlmUrgVisual_Type()
)
mgnt2AlmUrgVisual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmUrgVisual.setStatus("current")
_Mgnt2AlmCritVisual_Type = EkiOnOff
_Mgnt2AlmCritVisual_Object = MibScalar
mgnt2AlmCritVisual = _Mgnt2AlmCritVisual_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 1, 3),
    _Mgnt2AlmCritVisual_Type()
)
mgnt2AlmCritVisual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmCritVisual.setStatus("current")
_Mgnt2AlmAcknowledge_Type = EkiOnOff
_Mgnt2AlmAcknowledge_Object = MibScalar
mgnt2AlmAcknowledge = _Mgnt2AlmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 1, 16),
    _Mgnt2AlmAcknowledge_Type()
)
mgnt2AlmAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmAcknowledge.setStatus("current")
_Mgnt2AlmboardMgmntSet1_ObjectIdentity = ObjectIdentity
mgnt2AlmboardMgmntSet1 = _Mgnt2AlmboardMgmntSet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16)
)
_Mgnt2AlmPmSlot1Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot1Absent_Object = MibScalar
mgnt2AlmPmSlot1Absent = _Mgnt2AlmPmSlot1Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 2),
    _Mgnt2AlmPmSlot1Absent_Type()
)
mgnt2AlmPmSlot1Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot1Absent.setStatus("current")
_Mgnt2AlmPmSlot2Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot2Absent_Object = MibScalar
mgnt2AlmPmSlot2Absent = _Mgnt2AlmPmSlot2Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 3),
    _Mgnt2AlmPmSlot2Absent_Type()
)
mgnt2AlmPmSlot2Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot2Absent.setStatus("current")
_Mgnt2AlmPmSlot3Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot3Absent_Object = MibScalar
mgnt2AlmPmSlot3Absent = _Mgnt2AlmPmSlot3Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 4),
    _Mgnt2AlmPmSlot3Absent_Type()
)
mgnt2AlmPmSlot3Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot3Absent.setStatus("current")
_Mgnt2AlmPmSlot4Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot4Absent_Object = MibScalar
mgnt2AlmPmSlot4Absent = _Mgnt2AlmPmSlot4Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 5),
    _Mgnt2AlmPmSlot4Absent_Type()
)
mgnt2AlmPmSlot4Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot4Absent.setStatus("current")
_Mgnt2AlmPmSlot5Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot5Absent_Object = MibScalar
mgnt2AlmPmSlot5Absent = _Mgnt2AlmPmSlot5Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 6),
    _Mgnt2AlmPmSlot5Absent_Type()
)
mgnt2AlmPmSlot5Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot5Absent.setStatus("current")
_Mgnt2AlmPmSlot6Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot6Absent_Object = MibScalar
mgnt2AlmPmSlot6Absent = _Mgnt2AlmPmSlot6Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 7),
    _Mgnt2AlmPmSlot6Absent_Type()
)
mgnt2AlmPmSlot6Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot6Absent.setStatus("current")
_Mgnt2AlmPmSlot7Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot7Absent_Object = MibScalar
mgnt2AlmPmSlot7Absent = _Mgnt2AlmPmSlot7Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 8),
    _Mgnt2AlmPmSlot7Absent_Type()
)
mgnt2AlmPmSlot7Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot7Absent.setStatus("current")
_Mgnt2AlmPmSlot8Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot8Absent_Object = MibScalar
mgnt2AlmPmSlot8Absent = _Mgnt2AlmPmSlot8Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 9),
    _Mgnt2AlmPmSlot8Absent_Type()
)
mgnt2AlmPmSlot8Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot8Absent.setStatus("current")
_Mgnt2AlmPmSlot9Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot9Absent_Object = MibScalar
mgnt2AlmPmSlot9Absent = _Mgnt2AlmPmSlot9Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 10),
    _Mgnt2AlmPmSlot9Absent_Type()
)
mgnt2AlmPmSlot9Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot9Absent.setStatus("current")
_Mgnt2AlmPmSlot10Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot10Absent_Object = MibScalar
mgnt2AlmPmSlot10Absent = _Mgnt2AlmPmSlot10Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 11),
    _Mgnt2AlmPmSlot10Absent_Type()
)
mgnt2AlmPmSlot10Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot10Absent.setStatus("current")
_Mgnt2AlmPmSlot11Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot11Absent_Object = MibScalar
mgnt2AlmPmSlot11Absent = _Mgnt2AlmPmSlot11Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 12),
    _Mgnt2AlmPmSlot11Absent_Type()
)
mgnt2AlmPmSlot11Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot11Absent.setStatus("current")
_Mgnt2AlmPmFanAbsent_Type = EkiOnOff
_Mgnt2AlmPmFanAbsent_Object = MibScalar
mgnt2AlmPmFanAbsent = _Mgnt2AlmPmFanAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 16, 14),
    _Mgnt2AlmPmFanAbsent_Type()
)
mgnt2AlmPmFanAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmFanAbsent.setStatus("current")
_Mgnt2AlmboardMgmntSet2_ObjectIdentity = ObjectIdentity
mgnt2AlmboardMgmntSet2 = _Mgnt2AlmboardMgmntSet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17)
)
_Mgnt2AlmPmSlot12Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot12Absent_Object = MibScalar
mgnt2AlmPmSlot12Absent = _Mgnt2AlmPmSlot12Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 1),
    _Mgnt2AlmPmSlot12Absent_Type()
)
mgnt2AlmPmSlot12Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot12Absent.setStatus("current")
_Mgnt2AlmPmSlot13Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot13Absent_Object = MibScalar
mgnt2AlmPmSlot13Absent = _Mgnt2AlmPmSlot13Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 2),
    _Mgnt2AlmPmSlot13Absent_Type()
)
mgnt2AlmPmSlot13Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot13Absent.setStatus("current")
_Mgnt2AlmPmSlot14Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot14Absent_Object = MibScalar
mgnt2AlmPmSlot14Absent = _Mgnt2AlmPmSlot14Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 3),
    _Mgnt2AlmPmSlot14Absent_Type()
)
mgnt2AlmPmSlot14Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot14Absent.setStatus("current")
_Mgnt2AlmPmSlot15Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot15Absent_Object = MibScalar
mgnt2AlmPmSlot15Absent = _Mgnt2AlmPmSlot15Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 4),
    _Mgnt2AlmPmSlot15Absent_Type()
)
mgnt2AlmPmSlot15Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot15Absent.setStatus("current")
_Mgnt2AlmPmSlot16Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot16Absent_Object = MibScalar
mgnt2AlmPmSlot16Absent = _Mgnt2AlmPmSlot16Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 5),
    _Mgnt2AlmPmSlot16Absent_Type()
)
mgnt2AlmPmSlot16Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot16Absent.setStatus("current")
_Mgnt2AlmPmSlot17Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot17Absent_Object = MibScalar
mgnt2AlmPmSlot17Absent = _Mgnt2AlmPmSlot17Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 6),
    _Mgnt2AlmPmSlot17Absent_Type()
)
mgnt2AlmPmSlot17Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot17Absent.setStatus("current")
_Mgnt2AlmPmSlot18Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot18Absent_Object = MibScalar
mgnt2AlmPmSlot18Absent = _Mgnt2AlmPmSlot18Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 7),
    _Mgnt2AlmPmSlot18Absent_Type()
)
mgnt2AlmPmSlot18Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot18Absent.setStatus("current")
_Mgnt2AlmPmSlot19Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot19Absent_Object = MibScalar
mgnt2AlmPmSlot19Absent = _Mgnt2AlmPmSlot19Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 8),
    _Mgnt2AlmPmSlot19Absent_Type()
)
mgnt2AlmPmSlot19Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot19Absent.setStatus("current")
_Mgnt2AlmPmSlot20Absent_Type = EkiOnOff
_Mgnt2AlmPmSlot20Absent_Object = MibScalar
mgnt2AlmPmSlot20Absent = _Mgnt2AlmPmSlot20Absent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 17, 9),
    _Mgnt2AlmPmSlot20Absent_Type()
)
mgnt2AlmPmSlot20Absent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPmSlot20Absent.setStatus("current")
_Mgnt2AlmfanMgmnt_ObjectIdentity = ObjectIdentity
mgnt2AlmfanMgmnt = _Mgnt2AlmfanMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20)
)
_Mgnt2AlmPbFan1Fail_Type = EkiOnOff
_Mgnt2AlmPbFan1Fail_Object = MibScalar
mgnt2AlmPbFan1Fail = _Mgnt2AlmPbFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 2),
    _Mgnt2AlmPbFan1Fail_Type()
)
mgnt2AlmPbFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan1Fail.setStatus("current")
_Mgnt2AlmPbFan2Fail_Type = EkiOnOff
_Mgnt2AlmPbFan2Fail_Object = MibScalar
mgnt2AlmPbFan2Fail = _Mgnt2AlmPbFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 3),
    _Mgnt2AlmPbFan2Fail_Type()
)
mgnt2AlmPbFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan2Fail.setStatus("current")
_Mgnt2AlmPbFan3Fail_Type = EkiOnOff
_Mgnt2AlmPbFan3Fail_Object = MibScalar
mgnt2AlmPbFan3Fail = _Mgnt2AlmPbFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 4),
    _Mgnt2AlmPbFan3Fail_Type()
)
mgnt2AlmPbFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan3Fail.setStatus("current")
_Mgnt2AlmPbFan4Fail_Type = EkiOnOff
_Mgnt2AlmPbFan4Fail_Object = MibScalar
mgnt2AlmPbFan4Fail = _Mgnt2AlmPbFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 5),
    _Mgnt2AlmPbFan4Fail_Type()
)
mgnt2AlmPbFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan4Fail.setStatus("current")
_Mgnt2AlmPbFan5Fail_Type = EkiOnOff
_Mgnt2AlmPbFan5Fail_Object = MibScalar
mgnt2AlmPbFan5Fail = _Mgnt2AlmPbFan5Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 6),
    _Mgnt2AlmPbFan5Fail_Type()
)
mgnt2AlmPbFan5Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan5Fail.setStatus("current")
_Mgnt2AlmPbFan6Fail_Type = EkiOnOff
_Mgnt2AlmPbFan6Fail_Object = MibScalar
mgnt2AlmPbFan6Fail = _Mgnt2AlmPbFan6Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 7),
    _Mgnt2AlmPbFan6Fail_Type()
)
mgnt2AlmPbFan6Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPbFan6Fail.setStatus("current")
_Mgnt2AlmFanFilterAbsent_Type = EkiOnOff
_Mgnt2AlmFanFilterAbsent_Object = MibScalar
mgnt2AlmFanFilterAbsent = _Mgnt2AlmFanFilterAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 20, 16),
    _Mgnt2AlmFanFilterAbsent_Type()
)
mgnt2AlmFanFilterAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFanFilterAbsent.setStatus("current")
_Mgnt2AlmfanPwrMgmnt_ObjectIdentity = ObjectIdentity
mgnt2AlmfanPwrMgmnt = _Mgnt2AlmfanPwrMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 24)
)
_Mgnt2AlmFanPwrProtOn_Type = EkiOnOff
_Mgnt2AlmFanPwrProtOn_Object = MibScalar
mgnt2AlmFanPwrProtOn = _Mgnt2AlmFanPwrProtOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 24, 12),
    _Mgnt2AlmFanPwrProtOn_Type()
)
mgnt2AlmFanPwrProtOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFanPwrProtOn.setStatus("current")
_Mgnt2AlmFanPwrFail1_Type = EkiOnOff
_Mgnt2AlmFanPwrFail1_Object = MibScalar
mgnt2AlmFanPwrFail1 = _Mgnt2AlmFanPwrFail1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 24, 13),
    _Mgnt2AlmFanPwrFail1_Type()
)
mgnt2AlmFanPwrFail1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFanPwrFail1.setStatus("current")
_Mgnt2AlmFanDefFuseA_Type = EkiOnOff
_Mgnt2AlmFanDefFuseA_Object = MibScalar
mgnt2AlmFanDefFuseA = _Mgnt2AlmFanDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 24, 15),
    _Mgnt2AlmFanDefFuseA_Type()
)
mgnt2AlmFanDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFanDefFuseA.setStatus("current")
_Mgnt2AlmFanDefFuseB_Type = EkiOnOff
_Mgnt2AlmFanDefFuseB_Object = MibScalar
mgnt2AlmFanDefFuseB = _Mgnt2AlmFanDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 24, 16),
    _Mgnt2AlmFanDefFuseB_Type()
)
mgnt2AlmFanDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFanDefFuseB.setStatus("current")
_Mgnt2AlmremoveablefanModuleFail_ObjectIdentity = ObjectIdentity
mgnt2AlmremoveablefanModuleFail = _Mgnt2AlmremoveablefanModuleFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 25)
)
_Mgnt2AlmFan1ModuleAbsent_Type = EkiOnOff
_Mgnt2AlmFan1ModuleAbsent_Object = MibScalar
mgnt2AlmFan1ModuleAbsent = _Mgnt2AlmFan1ModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 25, 1),
    _Mgnt2AlmFan1ModuleAbsent_Type()
)
mgnt2AlmFan1ModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan1ModuleAbsent.setStatus("current")
_Mgnt2AlmFan2ModuleAbsent_Type = EkiOnOff
_Mgnt2AlmFan2ModuleAbsent_Object = MibScalar
mgnt2AlmFan2ModuleAbsent = _Mgnt2AlmFan2ModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 25, 2),
    _Mgnt2AlmFan2ModuleAbsent_Type()
)
mgnt2AlmFan2ModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan2ModuleAbsent.setStatus("current")
_Mgnt2AlmFan3ModuleAbsent_Type = EkiOnOff
_Mgnt2AlmFan3ModuleAbsent_Object = MibScalar
mgnt2AlmFan3ModuleAbsent = _Mgnt2AlmFan3ModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 25, 3),
    _Mgnt2AlmFan3ModuleAbsent_Type()
)
mgnt2AlmFan3ModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan3ModuleAbsent.setStatus("current")
_Mgnt2AlmFan4ModuleAbsent_Type = EkiOnOff
_Mgnt2AlmFan4ModuleAbsent_Object = MibScalar
mgnt2AlmFan4ModuleAbsent = _Mgnt2AlmFan4ModuleAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 25, 4),
    _Mgnt2AlmFan4ModuleAbsent_Type()
)
mgnt2AlmFan4ModuleAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan4ModuleAbsent.setStatus("current")
_Mgnt2AlmremoveableFanModuleMgmnt_ObjectIdentity = ObjectIdentity
mgnt2AlmremoveableFanModuleMgmnt = _Mgnt2AlmremoveableFanModuleMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 26)
)
_Mgnt2AlmFan1ModuleFail_Type = EkiOnOff
_Mgnt2AlmFan1ModuleFail_Object = MibScalar
mgnt2AlmFan1ModuleFail = _Mgnt2AlmFan1ModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 26, 1),
    _Mgnt2AlmFan1ModuleFail_Type()
)
mgnt2AlmFan1ModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan1ModuleFail.setStatus("current")
_Mgnt2AlmFan2ModuleFail_Type = EkiOnOff
_Mgnt2AlmFan2ModuleFail_Object = MibScalar
mgnt2AlmFan2ModuleFail = _Mgnt2AlmFan2ModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 26, 2),
    _Mgnt2AlmFan2ModuleFail_Type()
)
mgnt2AlmFan2ModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan2ModuleFail.setStatus("current")
_Mgnt2AlmFan3ModuleFail_Type = EkiOnOff
_Mgnt2AlmFan3ModuleFail_Object = MibScalar
mgnt2AlmFan3ModuleFail = _Mgnt2AlmFan3ModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 26, 3),
    _Mgnt2AlmFan3ModuleFail_Type()
)
mgnt2AlmFan3ModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan3ModuleFail.setStatus("current")
_Mgnt2AlmFan4ModuleFail_Type = EkiOnOff
_Mgnt2AlmFan4ModuleFail_Object = MibScalar
mgnt2AlmFan4ModuleFail = _Mgnt2AlmFan4ModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 26, 4),
    _Mgnt2AlmFan4ModuleFail_Type()
)
mgnt2AlmFan4ModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFan4ModuleFail.setStatus("current")
_Mgnt2AlmswAlarm1_ObjectIdentity = ObjectIdentity
mgnt2AlmswAlarm1 = _Mgnt2AlmswAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 32)
)
_Mgnt2AlmApiError_Type = EkiOnOff
_Mgnt2AlmApiError_Object = MibScalar
mgnt2AlmApiError = _Mgnt2AlmApiError_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 32, 1),
    _Mgnt2AlmApiError_Type()
)
mgnt2AlmApiError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmApiError.setStatus("current")
_Mgnt2AlmFifoCmdError_Type = EkiOnOff
_Mgnt2AlmFifoCmdError_Object = MibScalar
mgnt2AlmFifoCmdError = _Mgnt2AlmFifoCmdError_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 32, 2),
    _Mgnt2AlmFifoCmdError_Type()
)
mgnt2AlmFifoCmdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmFifoCmdError.setStatus("current")
_Mgnt2AlmPollingManagerError_Type = EkiOnOff
_Mgnt2AlmPollingManagerError_Object = MibScalar
mgnt2AlmPollingManagerError = _Mgnt2AlmPollingManagerError_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 32, 3),
    _Mgnt2AlmPollingManagerError_Type()
)
mgnt2AlmPollingManagerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmPollingManagerError.setStatus("current")


class _Mgnt2AlmapiErrorCode_Type(Integer32):
    """Custom type mgnt2AlmapiErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgnt2AlmapiErrorCode_Type.__name__ = "Integer32"
_Mgnt2AlmapiErrorCode_Object = MibScalar
mgnt2AlmapiErrorCode = _Mgnt2AlmapiErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 33),
    _Mgnt2AlmapiErrorCode_Type()
)
mgnt2AlmapiErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmapiErrorCode.setStatus("current")
_Mgnt2AlmlogMgmnt_ObjectIdentity = ObjectIdentity
mgnt2AlmlogMgmnt = _Mgnt2AlmlogMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 34)
)
_Mgnt2AlmLogFileFull_Type = EkiOnOff
_Mgnt2AlmLogFileFull_Object = MibScalar
mgnt2AlmLogFileFull = _Mgnt2AlmLogFileFull_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 34, 1),
    _Mgnt2AlmLogFileFull_Type()
)
mgnt2AlmLogFileFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLogFileFull.setStatus("current")
_Mgnt2AlmLog80Full_Type = EkiOnOff
_Mgnt2AlmLog80Full_Object = MibScalar
mgnt2AlmLog80Full = _Mgnt2AlmLog80Full_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 34, 2),
    _Mgnt2AlmLog80Full_Type()
)
mgnt2AlmLog80Full.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmLog80Full.setStatus("current")
_Mgnt2AlmntpSyncLoss_ObjectIdentity = ObjectIdentity
mgnt2AlmntpSyncLoss = _Mgnt2AlmntpSyncLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 35)
)
_Mgnt2AlmNtpSyncLoss_Type = EkiOnOff
_Mgnt2AlmNtpSyncLoss_Object = MibScalar
mgnt2AlmNtpSyncLoss = _Mgnt2AlmNtpSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 35, 1),
    _Mgnt2AlmNtpSyncLoss_Type()
)
mgnt2AlmNtpSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmNtpSyncLoss.setStatus("current")
_Mgnt2AlmCpuTempOverRange_Type = EkiOnOff
_Mgnt2AlmCpuTempOverRange_Object = MibScalar
mgnt2AlmCpuTempOverRange = _Mgnt2AlmCpuTempOverRange_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 1, 35, 2),
    _Mgnt2AlmCpuTempOverRange_Type()
)
mgnt2AlmCpuTempOverRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2AlmCpuTempOverRange.setStatus("current")
_Mgnt2controls_ObjectIdentity = ObjectIdentity
mgnt2controls = _Mgnt2controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2)
)
_Mgnt2Ctrlsynth5_ObjectIdentity = ObjectIdentity
mgnt2Ctrlsynth5 = _Mgnt2Ctrlsynth5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 5)
)
_Mgnt2CtrlChassisShutdown_Type = EkiOnOff
_Mgnt2CtrlChassisShutdown_Object = MibScalar
mgnt2CtrlChassisShutdown = _Mgnt2CtrlChassisShutdown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 5, 2),
    _Mgnt2CtrlChassisShutdown_Type()
)
mgnt2CtrlChassisShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlChassisShutdown.setStatus("current")
_Mgnt2CtrlChassisWarmReset_Type = EkiOnOff
_Mgnt2CtrlChassisWarmReset_Object = MibScalar
mgnt2CtrlChassisWarmReset = _Mgnt2CtrlChassisWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 5, 3),
    _Mgnt2CtrlChassisWarmReset_Type()
)
mgnt2CtrlChassisWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlChassisWarmReset.setStatus("current")
_Mgnt2CtrlChassisColdReset_Type = EkiOnOff
_Mgnt2CtrlChassisColdReset_Object = MibScalar
mgnt2CtrlChassisColdReset = _Mgnt2CtrlChassisColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 5, 4),
    _Mgnt2CtrlChassisColdReset_Type()
)
mgnt2CtrlChassisColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlChassisColdReset.setStatus("current")
_Mgnt2CtrltestLed_ObjectIdentity = ObjectIdentity
mgnt2CtrltestLed = _Mgnt2CtrltestLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 18)
)
_Mgnt2CtrlGreenLed_Type = EkiOnOff
_Mgnt2CtrlGreenLed_Object = MibScalar
mgnt2CtrlGreenLed = _Mgnt2CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 18, 1),
    _Mgnt2CtrlGreenLed_Type()
)
mgnt2CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlGreenLed.setStatus("current")
_Mgnt2CtrlRedLed_Type = EkiOnOff
_Mgnt2CtrlRedLed_Object = MibScalar
mgnt2CtrlRedLed = _Mgnt2CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 18, 2),
    _Mgnt2CtrlRedLed_Type()
)
mgnt2CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlRedLed.setStatus("current")
_Mgnt2CtrlLedOff_Type = EkiOnOff
_Mgnt2CtrlLedOff_Object = MibScalar
mgnt2CtrlLedOff = _Mgnt2CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 18, 3),
    _Mgnt2CtrlLedOff_Type()
)
mgnt2CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlLedOff.setStatus("current")
_Mgnt2CtrllogFile_ObjectIdentity = ObjectIdentity
mgnt2CtrllogFile = _Mgnt2CtrllogFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 19)
)
_Mgnt2CtrlLogFileReset_Type = EkiOnOff
_Mgnt2CtrlLogFileReset_Object = MibScalar
mgnt2CtrlLogFileReset = _Mgnt2CtrlLogFileReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 19, 1),
    _Mgnt2CtrlLogFileReset_Type()
)
mgnt2CtrlLogFileReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlLogFileReset.setStatus("current")
_Mgnt2CtrlmgntSaveConfig_ObjectIdentity = ObjectIdentity
mgnt2CtrlmgntSaveConfig = _Mgnt2CtrlmgntSaveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 23)
)
_Mgnt2CtrlSaveConfig_Type = EkiOnOff
_Mgnt2CtrlSaveConfig_Object = MibScalar
mgnt2CtrlSaveConfig = _Mgnt2CtrlSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 23, 1),
    _Mgnt2CtrlSaveConfig_Type()
)
mgnt2CtrlSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlSaveConfig.setStatus("current")
_Mgnt2CtrlmgntGetGlobalConfig_ObjectIdentity = ObjectIdentity
mgnt2CtrlmgntGetGlobalConfig = _Mgnt2CtrlmgntGetGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 24)
)
_Mgnt2CtrlGetGlobalConfig_Type = EkiOnOff
_Mgnt2CtrlGetGlobalConfig_Object = MibScalar
mgnt2CtrlGetGlobalConfig = _Mgnt2CtrlGetGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 24, 1),
    _Mgnt2CtrlGetGlobalConfig_Type()
)
mgnt2CtrlGetGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlGetGlobalConfig.setStatus("current")
_Mgnt2CtrlmgntPutGlobalConfig_ObjectIdentity = ObjectIdentity
mgnt2CtrlmgntPutGlobalConfig = _Mgnt2CtrlmgntPutGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 25)
)
_Mgnt2CtrlPutGlobalConfig_Type = EkiOnOff
_Mgnt2CtrlPutGlobalConfig_Object = MibScalar
mgnt2CtrlPutGlobalConfig = _Mgnt2CtrlPutGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 25, 1),
    _Mgnt2CtrlPutGlobalConfig_Type()
)
mgnt2CtrlPutGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlPutGlobalConfig.setStatus("current")
_Mgnt2CtrlmgntAcknowledge_ObjectIdentity = ObjectIdentity
mgnt2CtrlmgntAcknowledge = _Mgnt2CtrlmgntAcknowledge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 26)
)
_Mgnt2CtrlAcknowledge_Type = EkiOnOff
_Mgnt2CtrlAcknowledge_Object = MibScalar
mgnt2CtrlAcknowledge = _Mgnt2CtrlAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 2, 26, 1),
    _Mgnt2CtrlAcknowledge_Type()
)
mgnt2CtrlAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CtrlAcknowledge.setStatus("current")
_Mgnt2config_ObjectIdentity = ObjectIdentity
mgnt2config = _Mgnt2config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3)
)
_Mgnt2CfgethPort2_ObjectIdentity = ObjectIdentity
mgnt2CfgethPort2 = _Mgnt2CfgethPort2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 17)
)
_Mgnt2CfgEthPort2Disable_Type = EkiOnOff
_Mgnt2CfgEthPort2Disable_Object = MibScalar
mgnt2CfgEthPort2Disable = _Mgnt2CfgEthPort2Disable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 17, 1),
    _Mgnt2CfgEthPort2Disable_Type()
)
mgnt2CfgEthPort2Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgEthPort2Disable.setStatus("current")
_Mgnt2CfgChassisEthernetSplit_Type = EkiOnOff
_Mgnt2CfgChassisEthernetSplit_Object = MibScalar
mgnt2CfgChassisEthernetSplit = _Mgnt2CfgChassisEthernetSplit_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 17, 2),
    _Mgnt2CfgChassisEthernetSplit_Type()
)
mgnt2CfgChassisEthernetSplit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgChassisEthernetSplit.setStatus("current")
_Mgnt2CfgmgntDccEnable_Type = Mgnt2DccAccessValues
_Mgnt2CfgmgntDccEnable_Object = MibScalar
mgnt2CfgmgntDccEnable = _Mgnt2CfgmgntDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 18),
    _Mgnt2CfgmgntDccEnable_Type()
)
mgnt2CfgmgntDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgmgntDccEnable.setStatus("current")
_Mgnt2CfgpmTrapEnable_ObjectIdentity = ObjectIdentity
mgnt2CfgpmTrapEnable = _Mgnt2CfgpmTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20)
)
_Mgnt2CfgPmCriticalTrapEn_Type = EkiOnOff
_Mgnt2CfgPmCriticalTrapEn_Object = MibScalar
mgnt2CfgPmCriticalTrapEn = _Mgnt2CfgPmCriticalTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20, 1),
    _Mgnt2CfgPmCriticalTrapEn_Type()
)
mgnt2CfgPmCriticalTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmCriticalTrapEn.setStatus("current")
_Mgnt2CfgPmMajorTrapEn_Type = EkiOnOff
_Mgnt2CfgPmMajorTrapEn_Object = MibScalar
mgnt2CfgPmMajorTrapEn = _Mgnt2CfgPmMajorTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20, 2),
    _Mgnt2CfgPmMajorTrapEn_Type()
)
mgnt2CfgPmMajorTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmMajorTrapEn.setStatus("current")
_Mgnt2CfgPmMinorTrapEn_Type = EkiOnOff
_Mgnt2CfgPmMinorTrapEn_Object = MibScalar
mgnt2CfgPmMinorTrapEn = _Mgnt2CfgPmMinorTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20, 3),
    _Mgnt2CfgPmMinorTrapEn_Type()
)
mgnt2CfgPmMinorTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmMinorTrapEn.setStatus("current")
_Mgnt2CfgPmControlTrapEn_Type = EkiOnOff
_Mgnt2CfgPmControlTrapEn_Object = MibScalar
mgnt2CfgPmControlTrapEn = _Mgnt2CfgPmControlTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20, 5),
    _Mgnt2CfgPmControlTrapEn_Type()
)
mgnt2CfgPmControlTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmControlTrapEn.setStatus("current")
_Mgnt2CfgPmConfigTrapEn_Type = EkiOnOff
_Mgnt2CfgPmConfigTrapEn_Object = MibScalar
mgnt2CfgPmConfigTrapEn = _Mgnt2CfgPmConfigTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 20, 6),
    _Mgnt2CfgPmConfigTrapEn_Type()
)
mgnt2CfgPmConfigTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmConfigTrapEn.setStatus("current")
_Mgnt2CfgmgntTrapEnable_ObjectIdentity = ObjectIdentity
mgnt2CfgmgntTrapEnable = _Mgnt2CfgmgntTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21)
)
_Mgnt2CfgMgntCriticalTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntCriticalTrapEn_Object = MibScalar
mgnt2CfgMgntCriticalTrapEn = _Mgnt2CfgMgntCriticalTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 1),
    _Mgnt2CfgMgntCriticalTrapEn_Type()
)
mgnt2CfgMgntCriticalTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntCriticalTrapEn.setStatus("current")
_Mgnt2CfgMgntMajorTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntMajorTrapEn_Object = MibScalar
mgnt2CfgMgntMajorTrapEn = _Mgnt2CfgMgntMajorTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 2),
    _Mgnt2CfgMgntMajorTrapEn_Type()
)
mgnt2CfgMgntMajorTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntMajorTrapEn.setStatus("current")
_Mgnt2CfgMgntMinorTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntMinorTrapEn_Object = MibScalar
mgnt2CfgMgntMinorTrapEn = _Mgnt2CfgMgntMinorTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 3),
    _Mgnt2CfgMgntMinorTrapEn_Type()
)
mgnt2CfgMgntMinorTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntMinorTrapEn.setStatus("current")
_Mgnt2CfgMgntControlTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntControlTrapEn_Object = MibScalar
mgnt2CfgMgntControlTrapEn = _Mgnt2CfgMgntControlTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 5),
    _Mgnt2CfgMgntControlTrapEn_Type()
)
mgnt2CfgMgntControlTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntControlTrapEn.setStatus("current")
_Mgnt2CfgMgntConfigTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntConfigTrapEn_Object = MibScalar
mgnt2CfgMgntConfigTrapEn = _Mgnt2CfgMgntConfigTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 6),
    _Mgnt2CfgMgntConfigTrapEn_Type()
)
mgnt2CfgMgntConfigTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntConfigTrapEn.setStatus("current")
_Mgnt2CfgMgntEventTrapEn_Type = EkiOnOff
_Mgnt2CfgMgntEventTrapEn_Object = MibScalar
mgnt2CfgMgntEventTrapEn = _Mgnt2CfgMgntEventTrapEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 21, 7),
    _Mgnt2CfgMgntEventTrapEn_Type()
)
mgnt2CfgMgntEventTrapEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgMgntEventTrapEn.setStatus("current")
_Mgnt2CfgmgntTrapMode_Type = Mgnt2TrapModeValues
_Mgnt2CfgmgntTrapMode_Object = MibScalar
mgnt2CfgmgntTrapMode = _Mgnt2CfgmgntTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 22),
    _Mgnt2CfgmgntTrapMode_Type()
)
mgnt2CfgmgntTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgmgntTrapMode.setStatus("current")
_Mgnt2CfgsyslogEnable_ObjectIdentity = ObjectIdentity
mgnt2CfgsyslogEnable = _Mgnt2CfgsyslogEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 23)
)
_Mgnt2CfgSyslogEventEn_Type = EkiOnOff
_Mgnt2CfgSyslogEventEn_Object = MibScalar
mgnt2CfgSyslogEventEn = _Mgnt2CfgSyslogEventEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 23, 1),
    _Mgnt2CfgSyslogEventEn_Type()
)
mgnt2CfgSyslogEventEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgSyslogEventEn.setStatus("current")
_Mgnt2CfgSyslogConfigEn_Type = EkiOnOff
_Mgnt2CfgSyslogConfigEn_Object = MibScalar
mgnt2CfgSyslogConfigEn = _Mgnt2CfgSyslogConfigEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 23, 2),
    _Mgnt2CfgSyslogConfigEn_Type()
)
mgnt2CfgSyslogConfigEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgSyslogConfigEn.setStatus("current")
_Mgnt2CfgSyslogCtrlEn_Type = EkiOnOff
_Mgnt2CfgSyslogCtrlEn_Object = MibScalar
mgnt2CfgSyslogCtrlEn = _Mgnt2CfgSyslogCtrlEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 23, 3),
    _Mgnt2CfgSyslogCtrlEn_Type()
)
mgnt2CfgSyslogCtrlEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgSyslogCtrlEn.setStatus("current")
_Mgnt2CfgSyslogAlarmEn_Type = EkiOnOff
_Mgnt2CfgSyslogAlarmEn_Object = MibScalar
mgnt2CfgSyslogAlarmEn = _Mgnt2CfgSyslogAlarmEn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 23, 4),
    _Mgnt2CfgSyslogAlarmEn_Type()
)
mgnt2CfgSyslogAlarmEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgSyslogAlarmEn.setStatus("current")


class _Mgnt2CfgntpTimeZone_Type(Integer32):
    """Custom type mgnt2CfgntpTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_Mgnt2CfgntpTimeZone_Type.__name__ = "Integer32"
_Mgnt2CfgntpTimeZone_Object = MibScalar
mgnt2CfgntpTimeZone = _Mgnt2CfgntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 24),
    _Mgnt2CfgntpTimeZone_Type()
)
mgnt2CfgntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgntpTimeZone.setStatus("current")
_Mgnt2CfgpmConfEnable_ObjectIdentity = ObjectIdentity
mgnt2CfgpmConfEnable = _Mgnt2CfgpmConfEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 25)
)
_Mgnt2CfgPmBackupEnable_Type = EkiOnOff
_Mgnt2CfgPmBackupEnable_Object = MibScalar
mgnt2CfgPmBackupEnable = _Mgnt2CfgPmBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 25, 1),
    _Mgnt2CfgPmBackupEnable_Type()
)
mgnt2CfgPmBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmBackupEnable.setStatus("current")
_Mgnt2CfgPmRestoreEnable_Type = EkiOnOff
_Mgnt2CfgPmRestoreEnable_Object = MibScalar
mgnt2CfgPmRestoreEnable = _Mgnt2CfgPmRestoreEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 25, 2),
    _Mgnt2CfgPmRestoreEnable_Type()
)
mgnt2CfgPmRestoreEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgPmRestoreEnable.setStatus("current")


class _Mgnt2CfginactivityTimeout_Type(Integer32):
    """Custom type mgnt2CfginactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Mgnt2CfginactivityTimeout_Type.__name__ = "Integer32"
_Mgnt2CfginactivityTimeout_Object = MibScalar
mgnt2CfginactivityTimeout = _Mgnt2CfginactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 26),
    _Mgnt2CfginactivityTimeout_Type()
)
mgnt2CfginactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfginactivityTimeout.setStatus("current")
_Mgnt2CfgcliAccess_Type = Mgnt2CliAccessValues
_Mgnt2CfgcliAccess_Object = MibScalar
mgnt2CfgcliAccess = _Mgnt2CfgcliAccess_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 27),
    _Mgnt2CfgcliAccess_Type()
)
mgnt2CfgcliAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgcliAccess.setStatus("current")
_Mgnt2CfgcraftAccess_Type = Mgnt2CraftAccessValues
_Mgnt2CfgcraftAccess_Object = MibScalar
mgnt2CfgcraftAccess = _Mgnt2CfgcraftAccess_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 28),
    _Mgnt2CfgcraftAccess_Type()
)
mgnt2CfgcraftAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgcraftAccess.setStatus("current")
_Mgnt2CfgperfModes1_Type = EkiSynchroMode
_Mgnt2CfgperfModes1_Object = MibScalar
mgnt2CfgperfModes1 = _Mgnt2CfgperfModes1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 29),
    _Mgnt2CfgperfModes1_Type()
)
mgnt2CfgperfModes1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgperfModes1.setStatus("current")
_Mgnt2CfgalarmModelActiv_Type = Mgnt2AckMode
_Mgnt2CfgalarmModelActiv_Object = MibScalar
mgnt2CfgalarmModelActiv = _Mgnt2CfgalarmModelActiv_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 30),
    _Mgnt2CfgalarmModelActiv_Type()
)
mgnt2CfgalarmModelActiv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgalarmModelActiv.setStatus("current")
_Mgnt2CfgnetworkInput_Type = Mgnt2NetMode
_Mgnt2CfgnetworkInput_Object = MibScalar
mgnt2CfgnetworkInput = _Mgnt2CfgnetworkInput_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 31),
    _Mgnt2CfgnetworkInput_Type()
)
mgnt2CfgnetworkInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgnetworkInput.setStatus("current")
_Mgnt2CfgmasterEthMode_Type = Mgnt2MasterEthMode
_Mgnt2CfgmasterEthMode_Object = MibScalar
mgnt2CfgmasterEthMode = _Mgnt2CfgmasterEthMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 32),
    _Mgnt2CfgmasterEthMode_Type()
)
mgnt2CfgmasterEthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgmasterEthMode.setStatus("current")
_Mgnt2CfgsubnetMode_Type = Mgnt2SubnetEthMode
_Mgnt2CfgsubnetMode_Object = MibScalar
mgnt2CfgsubnetMode = _Mgnt2CfgsubnetMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 33),
    _Mgnt2CfgsubnetMode_Type()
)
mgnt2CfgsubnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgsubnetMode.setStatus("current")
_Mgnt2CfgrstpMode_ObjectIdentity = ObjectIdentity
mgnt2CfgrstpMode = _Mgnt2CfgrstpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 34)
)
_Mgnt2CfgRstpEnable_Type = EkiOnOff
_Mgnt2CfgRstpEnable_Object = MibScalar
mgnt2CfgRstpEnable = _Mgnt2CfgRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 34, 1),
    _Mgnt2CfgRstpEnable_Type()
)
mgnt2CfgRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgRstpEnable.setStatus("current")
_Mgnt2CfglldpMode_ObjectIdentity = ObjectIdentity
mgnt2CfglldpMode = _Mgnt2CfglldpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 35)
)
_Mgnt2CfgLldpEnable_Type = EkiOnOff
_Mgnt2CfgLldpEnable_Object = MibScalar
mgnt2CfgLldpEnable = _Mgnt2CfgLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 35, 1),
    _Mgnt2CfgLldpEnable_Type()
)
mgnt2CfgLldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgLldpEnable.setStatus("current")
_Mgnt2CfglogMode_Type = Mgnt2LogFileMode
_Mgnt2CfglogMode_Object = MibScalar
mgnt2CfglogMode = _Mgnt2CfglogMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 36),
    _Mgnt2CfglogMode_Type()
)
mgnt2CfglogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfglogMode.setStatus("current")
_Mgnt2CfgnodeMode_ObjectIdentity = ObjectIdentity
mgnt2CfgnodeMode = _Mgnt2CfgnodeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 37)
)
_Mgnt2CfgNodeControllerEnable_Type = EkiOnOff
_Mgnt2CfgNodeControllerEnable_Object = MibScalar
mgnt2CfgNodeControllerEnable = _Mgnt2CfgNodeControllerEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 37, 1),
    _Mgnt2CfgNodeControllerEnable_Type()
)
mgnt2CfgNodeControllerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgNodeControllerEnable.setStatus("current")
_Mgnt2CfgunprivilegedUsersMode_ObjectIdentity = ObjectIdentity
mgnt2CfgunprivilegedUsersMode = _Mgnt2CfgunprivilegedUsersMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 38)
)
_Mgnt2CfgRestrictUnprivilegeUsers_Type = EkiOnOff
_Mgnt2CfgRestrictUnprivilegeUsers_Object = MibScalar
mgnt2CfgRestrictUnprivilegeUsers = _Mgnt2CfgRestrictUnprivilegeUsers_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 38, 1),
    _Mgnt2CfgRestrictUnprivilegeUsers_Type()
)
mgnt2CfgRestrictUnprivilegeUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgRestrictUnprivilegeUsers.setStatus("current")


class _Mgnt2CfgoscDccLinkUpThreshold_Type(Integer32):
    """Custom type mgnt2CfgoscDccLinkUpThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgnt2CfgoscDccLinkUpThreshold_Type.__name__ = "Integer32"
_Mgnt2CfgoscDccLinkUpThreshold_Object = MibScalar
mgnt2CfgoscDccLinkUpThreshold = _Mgnt2CfgoscDccLinkUpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 39),
    _Mgnt2CfgoscDccLinkUpThreshold_Type()
)
mgnt2CfgoscDccLinkUpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgoscDccLinkUpThreshold.setStatus("current")


class _Mgnt2CfgoscDccLinkDownThreshold_Type(Integer32):
    """Custom type mgnt2CfgoscDccLinkDownThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mgnt2CfgoscDccLinkDownThreshold_Type.__name__ = "Integer32"
_Mgnt2CfgoscDccLinkDownThreshold_Object = MibScalar
mgnt2CfgoscDccLinkDownThreshold = _Mgnt2CfgoscDccLinkDownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 40),
    _Mgnt2CfgoscDccLinkDownThreshold_Type()
)
mgnt2CfgoscDccLinkDownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgoscDccLinkDownThreshold.setStatus("current")


class _Mgnt2CfgaccountAutoLock_Type(Integer32):
    """Custom type mgnt2CfgaccountAutoLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Mgnt2CfgaccountAutoLock_Type.__name__ = "Integer32"
_Mgnt2CfgaccountAutoLock_Object = MibScalar
mgnt2CfgaccountAutoLock = _Mgnt2CfgaccountAutoLock_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 41),
    _Mgnt2CfgaccountAutoLock_Type()
)
mgnt2CfgaccountAutoLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgaccountAutoLock.setStatus("current")


class _Mgnt2CfgfailCountReset_Type(Integer32):
    """Custom type mgnt2CfgfailCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Mgnt2CfgfailCountReset_Type.__name__ = "Integer32"
_Mgnt2CfgfailCountReset_Object = MibScalar
mgnt2CfgfailCountReset = _Mgnt2CfgfailCountReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 42),
    _Mgnt2CfgfailCountReset_Type()
)
mgnt2CfgfailCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgfailCountReset.setStatus("current")
_Mgnt2CfgftpMode_ObjectIdentity = ObjectIdentity
mgnt2CfgftpMode = _Mgnt2CfgftpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 44)
)
_Mgnt2CfgFtpEnable_Type = EkiOnOff
_Mgnt2CfgFtpEnable_Object = MibScalar
mgnt2CfgFtpEnable = _Mgnt2CfgFtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 44, 1),
    _Mgnt2CfgFtpEnable_Type()
)
mgnt2CfgFtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgFtpEnable.setStatus("current")
_Mgnt2CfgtftpMode_ObjectIdentity = ObjectIdentity
mgnt2CfgtftpMode = _Mgnt2CfgtftpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 45)
)
_Mgnt2CfgTftpEnable_Type = EkiOnOff
_Mgnt2CfgTftpEnable_Object = MibScalar
mgnt2CfgTftpEnable = _Mgnt2CfgTftpEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 2, 3, 45, 1),
    _Mgnt2CfgTftpEnable_Type()
)
mgnt2CfgTftpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CfgTftpEnable.setStatus("current")
_Mgnt2Traps_ObjectIdentity = ObjectIdentity
mgnt2Traps = _Mgnt2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3)
)


class _Mgnt2TrapBoardNumber_Type(Integer32):
    """Custom type mgnt2TrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mgnt2TrapBoardNumber_Type.__name__ = "Integer32"
_Mgnt2TrapBoardNumber_Object = MibScalar
mgnt2TrapBoardNumber = _Mgnt2TrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 50),
    _Mgnt2TrapBoardNumber_Type()
)
mgnt2TrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapBoardNumber.setStatus("current")
_Mgnt2TrapSeverity_Type = DisplayString
_Mgnt2TrapSeverity_Object = MibScalar
mgnt2TrapSeverity = _Mgnt2TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 51),
    _Mgnt2TrapSeverity_Type()
)
mgnt2TrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSeverity.setStatus("current")
_Mgnt2TrapSourcePm_Type = DisplayString
_Mgnt2TrapSourcePm_Object = MibScalar
mgnt2TrapSourcePm = _Mgnt2TrapSourcePm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 52),
    _Mgnt2TrapSourcePm_Type()
)
mgnt2TrapSourcePm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSourcePm.setStatus("current")
_Mgnt2TrapSourcePortType_Type = DisplayString
_Mgnt2TrapSourcePortType_Object = MibScalar
mgnt2TrapSourcePortType = _Mgnt2TrapSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 53),
    _Mgnt2TrapSourcePortType_Type()
)
mgnt2TrapSourcePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSourcePortType.setStatus("current")


class _Mgnt2TrapSourcePortNumber_Type(Integer32):
    """Custom type mgnt2TrapSourcePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mgnt2TrapSourcePortNumber_Type.__name__ = "Integer32"
_Mgnt2TrapSourcePortNumber_Object = MibScalar
mgnt2TrapSourcePortNumber = _Mgnt2TrapSourcePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 54),
    _Mgnt2TrapSourcePortNumber_Type()
)
mgnt2TrapSourcePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSourcePortNumber.setStatus("current")
_Mgnt2TrapSourceLabel_Type = DisplayString
_Mgnt2TrapSourceLabel_Object = MibScalar
mgnt2TrapSourceLabel = _Mgnt2TrapSourceLabel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 55),
    _Mgnt2TrapSourceLabel_Type()
)
mgnt2TrapSourceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSourceLabel.setStatus("current")
_Mgnt2TrapSourceValue_Type = EkiOnOff
_Mgnt2TrapSourceValue_Object = MibScalar
mgnt2TrapSourceValue = _Mgnt2TrapSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 56),
    _Mgnt2TrapSourceValue_Type()
)
mgnt2TrapSourceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapSourceValue.setStatus("current")
_Mgnt2TrapEventLabel_Type = DisplayString
_Mgnt2TrapEventLabel_Object = MibScalar
mgnt2TrapEventLabel = _Mgnt2TrapEventLabel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 57),
    _Mgnt2TrapEventLabel_Type()
)
mgnt2TrapEventLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapEventLabel.setStatus("current")
_Mgnt2TrapNodeControllerIpAddress_Type = IpAddress
_Mgnt2TrapNodeControllerIpAddress_Object = MibScalar
mgnt2TrapNodeControllerIpAddress = _Mgnt2TrapNodeControllerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 58),
    _Mgnt2TrapNodeControllerIpAddress_Type()
)
mgnt2TrapNodeControllerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapNodeControllerIpAddress.setStatus("current")
_Mgnt2TrapChassisId_Type = DisplayString
_Mgnt2TrapChassisId_Object = MibScalar
mgnt2TrapChassisId = _Mgnt2TrapChassisId_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 59),
    _Mgnt2TrapChassisId_Type()
)
mgnt2TrapChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2TrapChassisId.setStatus("current")
_Mgnt2SoftwareManagement_ObjectIdentity = ObjectIdentity
mgnt2SoftwareManagement = _Mgnt2SoftwareManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4)
)
_Mgnt2DwlUploadingTable_Object = MibTable
mgnt2DwlUploadingTable = _Mgnt2DwlUploadingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mgnt2DwlUploadingTable.setStatus("deprecated")
_Mgnt2DwlUploadingEntry_Object = MibTableRow
mgnt2DwlUploadingEntry = _Mgnt2DwlUploadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1)
)
mgnt2DwlUploadingEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexUpload"),
)
if mibBuilder.loadTexts:
    mgnt2DwlUploadingEntry.setStatus("deprecated")


class _Mgnt2IndexUpload_Type(Integer32):
    """Custom type mgnt2IndexUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Mgnt2IndexUpload_Type.__name__ = "Integer32"
_Mgnt2IndexUpload_Object = MibTableColumn
mgnt2IndexUpload = _Mgnt2IndexUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 1),
    _Mgnt2IndexUpload_Type()
)
mgnt2IndexUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexUpload.setStatus("deprecated")
_Mgnt2DwlUploadFileName_Type = DisplayString
_Mgnt2DwlUploadFileName_Object = MibTableColumn
mgnt2DwlUploadFileName = _Mgnt2DwlUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 2),
    _Mgnt2DwlUploadFileName_Type()
)
mgnt2DwlUploadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2DwlUploadFileName.setStatus("deprecated")
_Mgnt2ImmediateReplacement_Type = EkiState
_Mgnt2ImmediateReplacement_Object = MibTableColumn
mgnt2ImmediateReplacement = _Mgnt2ImmediateReplacement_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 3),
    _Mgnt2ImmediateReplacement_Type()
)
mgnt2ImmediateReplacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2ImmediateReplacement.setStatus("deprecated")
_Mgnt2FileUpload_Type = EkiOnOff
_Mgnt2FileUpload_Object = MibTableColumn
mgnt2FileUpload = _Mgnt2FileUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 4),
    _Mgnt2FileUpload_Type()
)
mgnt2FileUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2FileUpload.setStatus("deprecated")
_Mgnt2DeletePackageFromRam_Type = EkiOnOff
_Mgnt2DeletePackageFromRam_Object = MibTableColumn
mgnt2DeletePackageFromRam = _Mgnt2DeletePackageFromRam_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 5),
    _Mgnt2DeletePackageFromRam_Type()
)
mgnt2DeletePackageFromRam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DeletePackageFromRam.setStatus("deprecated")
_Mgnt2FlashingInProgress_Type = EkiOnOff
_Mgnt2FlashingInProgress_Object = MibTableColumn
mgnt2FlashingInProgress = _Mgnt2FlashingInProgress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 1, 1, 6),
    _Mgnt2FlashingInProgress_Type()
)
mgnt2FlashingInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2FlashingInProgress.setStatus("deprecated")
_Mgnt2DwlPackageTable_Object = MibTable
mgnt2DwlPackageTable = _Mgnt2DwlPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2)
)
if mibBuilder.loadTexts:
    mgnt2DwlPackageTable.setStatus("deprecated")
_Mgnt2DwlPackageEntry_Object = MibTableRow
mgnt2DwlPackageEntry = _Mgnt2DwlPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1)
)
mgnt2DwlPackageEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexPackage"),
)
if mibBuilder.loadTexts:
    mgnt2DwlPackageEntry.setStatus("deprecated")


class _Mgnt2IndexPackage_Type(Integer32):
    """Custom type mgnt2IndexPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Mgnt2IndexPackage_Type.__name__ = "Integer32"
_Mgnt2IndexPackage_Object = MibTableColumn
mgnt2IndexPackage = _Mgnt2IndexPackage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 1),
    _Mgnt2IndexPackage_Type()
)
mgnt2IndexPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexPackage.setStatus("deprecated")
_Mgnt2DwlPackageFileName_Type = DisplayString
_Mgnt2DwlPackageFileName_Object = MibTableColumn
mgnt2DwlPackageFileName = _Mgnt2DwlPackageFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 2),
    _Mgnt2DwlPackageFileName_Type()
)
mgnt2DwlPackageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2DwlPackageFileName.setStatus("deprecated")
_Mgnt2ExtractedPack_Type = EkiOnOff
_Mgnt2ExtractedPack_Object = MibTableColumn
mgnt2ExtractedPack = _Mgnt2ExtractedPack_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 3),
    _Mgnt2ExtractedPack_Type()
)
mgnt2ExtractedPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ExtractedPack.setStatus("deprecated")
_Mgnt2SwitchTo_Type = EkiOnOff
_Mgnt2SwitchTo_Object = MibTableColumn
mgnt2SwitchTo = _Mgnt2SwitchTo_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 4),
    _Mgnt2SwitchTo_Type()
)
mgnt2SwitchTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2SwitchTo.setStatus("deprecated")
_Mgnt2Immediate_Type = EkiOnOff
_Mgnt2Immediate_Object = MibTableColumn
mgnt2Immediate = _Mgnt2Immediate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 5),
    _Mgnt2Immediate_Type()
)
mgnt2Immediate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2Immediate.setStatus("deprecated")
_Mgnt2DeletePackageFromFlash_Type = EkiOnOff
_Mgnt2DeletePackageFromFlash_Object = MibTableColumn
mgnt2DeletePackageFromFlash = _Mgnt2DeletePackageFromFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 6),
    _Mgnt2DeletePackageFromFlash_Type()
)
mgnt2DeletePackageFromFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DeletePackageFromFlash.setStatus("deprecated")
_Mgnt2PackageExtractionInProgress_Type = EkiOnOff
_Mgnt2PackageExtractionInProgress_Object = MibTableColumn
mgnt2PackageExtractionInProgress = _Mgnt2PackageExtractionInProgress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 2, 1, 7),
    _Mgnt2PackageExtractionInProgress_Type()
)
mgnt2PackageExtractionInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PackageExtractionInProgress.setStatus("deprecated")
_Mgnt2DwlUploadingTableUpdate_Type = EkiOnOff
_Mgnt2DwlUploadingTableUpdate_Object = MibScalar
mgnt2DwlUploadingTableUpdate = _Mgnt2DwlUploadingTableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 3),
    _Mgnt2DwlUploadingTableUpdate_Type()
)
mgnt2DwlUploadingTableUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DwlUploadingTableUpdate.setStatus("deprecated")
_Mgnt2LoadPMTable_Object = MibTable
mgnt2LoadPMTable = _Mgnt2LoadPMTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4)
)
if mibBuilder.loadTexts:
    mgnt2LoadPMTable.setStatus("deprecated")
_Mgnt2LoadPMEntry_Object = MibTableRow
mgnt2LoadPMEntry = _Mgnt2LoadPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1)
)
mgnt2LoadPMEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2LoadPMIndex"),
)
if mibBuilder.loadTexts:
    mgnt2LoadPMEntry.setStatus("deprecated")


class _Mgnt2LoadPMIndex_Type(Integer32):
    """Custom type mgnt2LoadPMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Mgnt2LoadPMIndex_Type.__name__ = "Integer32"
_Mgnt2LoadPMIndex_Object = MibTableColumn
mgnt2LoadPMIndex = _Mgnt2LoadPMIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 1),
    _Mgnt2LoadPMIndex_Type()
)
mgnt2LoadPMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LoadPMIndex.setStatus("deprecated")
_Mgnt2LoadFileName_Type = DisplayString
_Mgnt2LoadFileName_Object = MibTableColumn
mgnt2LoadFileName = _Mgnt2LoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 2),
    _Mgnt2LoadFileName_Type()
)
mgnt2LoadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LoadFileName.setStatus("deprecated")
_Mgnt2LoadFileType_Type = EkiLoadGWSW
_Mgnt2LoadFileType_Object = MibTableColumn
mgnt2LoadFileType = _Mgnt2LoadFileType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 3),
    _Mgnt2LoadFileType_Type()
)
mgnt2LoadFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LoadFileType.setStatus("deprecated")
_Mgnt2LoadState_Type = EkiLoadState
_Mgnt2LoadState_Object = MibTableColumn
mgnt2LoadState = _Mgnt2LoadState_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 4),
    _Mgnt2LoadState_Type()
)
mgnt2LoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LoadState.setStatus("deprecated")


class _Mgnt2LoadModuleNumber_Type(Integer32):
    """Custom type mgnt2LoadModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Mgnt2LoadModuleNumber_Type.__name__ = "Integer32"
_Mgnt2LoadModuleNumber_Object = MibTableColumn
mgnt2LoadModuleNumber = _Mgnt2LoadModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 5),
    _Mgnt2LoadModuleNumber_Type()
)
mgnt2LoadModuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadModuleNumber.setStatus("deprecated")
_Mgnt2LoadResetMethod_Type = EkiLoadPermutMethod
_Mgnt2LoadResetMethod_Object = MibTableColumn
mgnt2LoadResetMethod = _Mgnt2LoadResetMethod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 6),
    _Mgnt2LoadResetMethod_Type()
)
mgnt2LoadResetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadResetMethod.setStatus("deprecated")
_Mgnt2LoadResetMode_Type = EkiLoadPermutMode
_Mgnt2LoadResetMode_Object = MibTableColumn
mgnt2LoadResetMode = _Mgnt2LoadResetMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 7),
    _Mgnt2LoadResetMode_Type()
)
mgnt2LoadResetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadResetMode.setStatus("deprecated")


class _Mgnt2LoadBankNumber_Type(Integer32):
    """Custom type mgnt2LoadBankNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Mgnt2LoadBankNumber_Type.__name__ = "Integer32"
_Mgnt2LoadBankNumber_Object = MibTableColumn
mgnt2LoadBankNumber = _Mgnt2LoadBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 8),
    _Mgnt2LoadBankNumber_Type()
)
mgnt2LoadBankNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadBankNumber.setStatus("deprecated")


class _Mgnt2LoadDownloadProgress_Type(Integer32):
    """Custom type mgnt2LoadDownloadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Mgnt2LoadDownloadProgress_Type.__name__ = "Integer32"
_Mgnt2LoadDownloadProgress_Object = MibTableColumn
mgnt2LoadDownloadProgress = _Mgnt2LoadDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 9),
    _Mgnt2LoadDownloadProgress_Type()
)
mgnt2LoadDownloadProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2LoadDownloadProgress.setStatus("deprecated")
_Mgnt2LoadTransfer_Type = EkiOnOff
_Mgnt2LoadTransfer_Object = MibTableColumn
mgnt2LoadTransfer = _Mgnt2LoadTransfer_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 10),
    _Mgnt2LoadTransfer_Type()
)
mgnt2LoadTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadTransfer.setStatus("deprecated")
_Mgnt2LoadDelete_Type = EkiOnOff
_Mgnt2LoadDelete_Object = MibTableColumn
mgnt2LoadDelete = _Mgnt2LoadDelete_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 4, 1, 11),
    _Mgnt2LoadDelete_Type()
)
mgnt2LoadDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadDelete.setStatus("deprecated")
_Mgnt2LoadPMTableUpdate_Type = EkiOnOff
_Mgnt2LoadPMTableUpdate_Object = MibScalar
mgnt2LoadPMTableUpdate = _Mgnt2LoadPMTableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 5),
    _Mgnt2LoadPMTableUpdate_Type()
)
mgnt2LoadPMTableUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2LoadPMTableUpdate.setStatus("deprecated")
_Mgnt2DwlEkicraftPkgTable_Object = MibTable
mgnt2DwlEkicraftPkgTable = _Mgnt2DwlEkicraftPkgTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6)
)
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftPkgTable.setStatus("deprecated")
_Mgnt2DwlEkicraftPkgEntry_Object = MibTableRow
mgnt2DwlEkicraftPkgEntry = _Mgnt2DwlEkicraftPkgEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1)
)
mgnt2DwlEkicraftPkgEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexEkicraftPkg"),
)
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftPkgEntry.setStatus("deprecated")


class _Mgnt2IndexEkicraftPkg_Type(Integer32):
    """Custom type mgnt2IndexEkicraftPkg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Mgnt2IndexEkicraftPkg_Type.__name__ = "Integer32"
_Mgnt2IndexEkicraftPkg_Object = MibTableColumn
mgnt2IndexEkicraftPkg = _Mgnt2IndexEkicraftPkg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 1),
    _Mgnt2IndexEkicraftPkg_Type()
)
mgnt2IndexEkicraftPkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexEkicraftPkg.setStatus("deprecated")
_Mgnt2DwlEkicraftPkgFileName_Type = DisplayString
_Mgnt2DwlEkicraftPkgFileName_Object = MibTableColumn
mgnt2DwlEkicraftPkgFileName = _Mgnt2DwlEkicraftPkgFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 2),
    _Mgnt2DwlEkicraftPkgFileName_Type()
)
mgnt2DwlEkicraftPkgFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftPkgFileName.setStatus("deprecated")
_Mgnt2DwlEkicraftExtractedPack_Type = EkiOnOff
_Mgnt2DwlEkicraftExtractedPack_Object = MibTableColumn
mgnt2DwlEkicraftExtractedPack = _Mgnt2DwlEkicraftExtractedPack_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 3),
    _Mgnt2DwlEkicraftExtractedPack_Type()
)
mgnt2DwlEkicraftExtractedPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftExtractedPack.setStatus("deprecated")
_Mgnt2DwlEkicraftSwitchTo_Type = EkiOnOff
_Mgnt2DwlEkicraftSwitchTo_Object = MibTableColumn
mgnt2DwlEkicraftSwitchTo = _Mgnt2DwlEkicraftSwitchTo_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 4),
    _Mgnt2DwlEkicraftSwitchTo_Type()
)
mgnt2DwlEkicraftSwitchTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftSwitchTo.setStatus("deprecated")
_Mgnt2DwlEkicraftImmediate_Type = EkiOnOff
_Mgnt2DwlEkicraftImmediate_Object = MibTableColumn
mgnt2DwlEkicraftImmediate = _Mgnt2DwlEkicraftImmediate_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 5),
    _Mgnt2DwlEkicraftImmediate_Type()
)
mgnt2DwlEkicraftImmediate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DwlEkicraftImmediate.setStatus("deprecated")
_Mgnt2DeleteEkicraftPkgFromFlash_Type = EkiOnOff
_Mgnt2DeleteEkicraftPkgFromFlash_Object = MibTableColumn
mgnt2DeleteEkicraftPkgFromFlash = _Mgnt2DeleteEkicraftPkgFromFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 6),
    _Mgnt2DeleteEkicraftPkgFromFlash_Type()
)
mgnt2DeleteEkicraftPkgFromFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2DeleteEkicraftPkgFromFlash.setStatus("deprecated")
_Mgnt2EkicraftPkgExtractionInProgress_Type = EkiOnOff
_Mgnt2EkicraftPkgExtractionInProgress_Object = MibTableColumn
mgnt2EkicraftPkgExtractionInProgress = _Mgnt2EkicraftPkgExtractionInProgress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 4, 6, 1, 7),
    _Mgnt2EkicraftPkgExtractionInProgress_Type()
)
mgnt2EkicraftPkgExtractionInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2EkicraftPkgExtractionInProgress.setStatus("deprecated")
_Mgnt2ConfigManagement_ObjectIdentity = ObjectIdentity
mgnt2ConfigManagement = _Mgnt2ConfigManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5)
)
_Mgnt2CnfUploadConfigFilesTable_Object = MibTable
mgnt2CnfUploadConfigFilesTable = _Mgnt2CnfUploadConfigFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1)
)
if mibBuilder.loadTexts:
    mgnt2CnfUploadConfigFilesTable.setStatus("deprecated")
_Mgnt2CnfUploadConfigFilesEntry_Object = MibTableRow
mgnt2CnfUploadConfigFilesEntry = _Mgnt2CnfUploadConfigFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1)
)
mgnt2CnfUploadConfigFilesEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2CnfUploadConfigIndex"),
)
if mibBuilder.loadTexts:
    mgnt2CnfUploadConfigFilesEntry.setStatus("deprecated")


class _Mgnt2CnfUploadConfigIndex_Type(Integer32):
    """Custom type mgnt2CnfUploadConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mgnt2CnfUploadConfigIndex_Type.__name__ = "Integer32"
_Mgnt2CnfUploadConfigIndex_Object = MibTableColumn
mgnt2CnfUploadConfigIndex = _Mgnt2CnfUploadConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1, 1),
    _Mgnt2CnfUploadConfigIndex_Type()
)
mgnt2CnfUploadConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2CnfUploadConfigIndex.setStatus("deprecated")
_Mgnt2CnfConfigFileName_Type = DisplayString
_Mgnt2CnfConfigFileName_Object = MibTableColumn
mgnt2CnfConfigFileName = _Mgnt2CnfConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1, 2),
    _Mgnt2CnfConfigFileName_Type()
)
mgnt2CnfConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2CnfConfigFileName.setStatus("deprecated")


class _Mgnt2CnfConfigSlot_Type(Integer32):
    """Custom type mgnt2CnfConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Mgnt2CnfConfigSlot_Type.__name__ = "Integer32"
_Mgnt2CnfConfigSlot_Object = MibTableColumn
mgnt2CnfConfigSlot = _Mgnt2CnfConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1, 3),
    _Mgnt2CnfConfigSlot_Type()
)
mgnt2CnfConfigSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfConfigSlot.setStatus("deprecated")
_Mgnt2CnfConfigUpload_Type = EkiOnOff
_Mgnt2CnfConfigUpload_Object = MibTableColumn
mgnt2CnfConfigUpload = _Mgnt2CnfConfigUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1, 4),
    _Mgnt2CnfConfigUpload_Type()
)
mgnt2CnfConfigUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfConfigUpload.setStatus("deprecated")
_Mgnt2CnfDeleteConfigFile_Type = EkiOnOff
_Mgnt2CnfDeleteConfigFile_Object = MibTableColumn
mgnt2CnfDeleteConfigFile = _Mgnt2CnfDeleteConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 1, 1, 5),
    _Mgnt2CnfDeleteConfigFile_Type()
)
mgnt2CnfDeleteConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfDeleteConfigFile.setStatus("deprecated")
_Mgnt2CnfManageConfigFilesTable_Object = MibTable
mgnt2CnfManageConfigFilesTable = _Mgnt2CnfManageConfigFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2)
)
if mibBuilder.loadTexts:
    mgnt2CnfManageConfigFilesTable.setStatus("deprecated")
_Mgnt2CnfManageConfigFilesEntry_Object = MibTableRow
mgnt2CnfManageConfigFilesEntry = _Mgnt2CnfManageConfigFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1)
)
mgnt2CnfManageConfigFilesEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2CnfManageConfigIndex"),
)
if mibBuilder.loadTexts:
    mgnt2CnfManageConfigFilesEntry.setStatus("deprecated")


class _Mgnt2CnfManageConfigIndex_Type(Integer32):
    """Custom type mgnt2CnfManageConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mgnt2CnfManageConfigIndex_Type.__name__ = "Integer32"
_Mgnt2CnfManageConfigIndex_Object = MibTableColumn
mgnt2CnfManageConfigIndex = _Mgnt2CnfManageConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 1),
    _Mgnt2CnfManageConfigIndex_Type()
)
mgnt2CnfManageConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2CnfManageConfigIndex.setStatus("deprecated")
_Mgnt2CnfManageConfigFileID_Type = DisplayString
_Mgnt2CnfManageConfigFileID_Object = MibTableColumn
mgnt2CnfManageConfigFileID = _Mgnt2CnfManageConfigFileID_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 2),
    _Mgnt2CnfManageConfigFileID_Type()
)
mgnt2CnfManageConfigFileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfManageConfigFileID.setStatus("deprecated")
_Mgnt2CnfManageConfigFileName_Type = DisplayString
_Mgnt2CnfManageConfigFileName_Object = MibTableColumn
mgnt2CnfManageConfigFileName = _Mgnt2CnfManageConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 3),
    _Mgnt2CnfManageConfigFileName_Type()
)
mgnt2CnfManageConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfManageConfigFileName.setStatus("deprecated")


class _Mgnt2CnfModuleSlotNumber_Type(Integer32):
    """Custom type mgnt2CnfModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 6),
    )


_Mgnt2CnfModuleSlotNumber_Type.__name__ = "Integer32"
_Mgnt2CnfModuleSlotNumber_Object = MibTableColumn
mgnt2CnfModuleSlotNumber = _Mgnt2CnfModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 4),
    _Mgnt2CnfModuleSlotNumber_Type()
)
mgnt2CnfModuleSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfModuleSlotNumber.setStatus("deprecated")
_Mgnt2CnfBackupConfig_Type = EkiOnOff
_Mgnt2CnfBackupConfig_Object = MibTableColumn
mgnt2CnfBackupConfig = _Mgnt2CnfBackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 5),
    _Mgnt2CnfBackupConfig_Type()
)
mgnt2CnfBackupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfBackupConfig.setStatus("deprecated")
_Mgnt2CnfRestoreConfig_Type = EkiOnOff
_Mgnt2CnfRestoreConfig_Object = MibTableColumn
mgnt2CnfRestoreConfig = _Mgnt2CnfRestoreConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 6),
    _Mgnt2CnfRestoreConfig_Type()
)
mgnt2CnfRestoreConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfRestoreConfig.setStatus("deprecated")
_Mgnt2CnfExportConfig_Type = EkiOnOff
_Mgnt2CnfExportConfig_Object = MibTableColumn
mgnt2CnfExportConfig = _Mgnt2CnfExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 7),
    _Mgnt2CnfExportConfig_Type()
)
mgnt2CnfExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfExportConfig.setStatus("deprecated")
_Mgnt2CnfDeleteConfig_Type = EkiOnOff
_Mgnt2CnfDeleteConfig_Object = MibTableColumn
mgnt2CnfDeleteConfig = _Mgnt2CnfDeleteConfig_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 5, 2, 1, 8),
    _Mgnt2CnfDeleteConfig_Type()
)
mgnt2CnfDeleteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2CnfDeleteConfig.setStatus("deprecated")
_Mgnt2RemoteInventory_ObjectIdentity = ObjectIdentity
mgnt2RemoteInventory = _Mgnt2RemoteInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6)
)
_Mgnt2RinvHwPlatform_Type = DisplayString
_Mgnt2RinvHwPlatform_Object = MibScalar
mgnt2RinvHwPlatform = _Mgnt2RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 1),
    _Mgnt2RinvHwPlatform_Type()
)
mgnt2RinvHwPlatform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvHwPlatform.setStatus("current")
_Mgnt2RinvSoftwarePackage_Type = DisplayString
_Mgnt2RinvSoftwarePackage_Object = MibScalar
mgnt2RinvSoftwarePackage = _Mgnt2RinvSoftwarePackage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 2),
    _Mgnt2RinvSoftwarePackage_Type()
)
mgnt2RinvSoftwarePackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvSoftwarePackage.setStatus("current")
_Mgnt2RinvGateware_Type = DisplayString
_Mgnt2RinvGateware_Object = MibScalar
mgnt2RinvGateware = _Mgnt2RinvGateware_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 3),
    _Mgnt2RinvGateware_Type()
)
mgnt2RinvGateware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvGateware.setStatus("current")
_Mgnt2RinvAgent_Type = DisplayString
_Mgnt2RinvAgent_Object = MibScalar
mgnt2RinvAgent = _Mgnt2RinvAgent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 4),
    _Mgnt2RinvAgent_Type()
)
mgnt2RinvAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvAgent.setStatus("current")
_Mgnt2RinvCraft_Type = DisplayString
_Mgnt2RinvCraft_Object = MibScalar
mgnt2RinvCraft = _Mgnt2RinvCraft_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 5),
    _Mgnt2RinvCraft_Type()
)
mgnt2RinvCraft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvCraft.setStatus("current")
_Mgnt2RinvLinux_Type = DisplayString
_Mgnt2RinvLinux_Object = MibScalar
mgnt2RinvLinux = _Mgnt2RinvLinux_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 6),
    _Mgnt2RinvLinux_Type()
)
mgnt2RinvLinux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvLinux.setStatus("current")
_Mgnt2GigmPlugInTable_Object = MibTable
mgnt2GigmPlugInTable = _Mgnt2GigmPlugInTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7)
)
if mibBuilder.loadTexts:
    mgnt2GigmPlugInTable.setStatus("current")
_Mgnt2GigmPlugInEntry_Object = MibTableRow
mgnt2GigmPlugInEntry = _Mgnt2GigmPlugInEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7, 1)
)
mgnt2GigmPlugInEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexPlugIns"),
)
if mibBuilder.loadTexts:
    mgnt2GigmPlugInEntry.setStatus("current")


class _Mgnt2IndexPlugIns_Type(Integer32):
    """Custom type mgnt2IndexPlugIns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2IndexPlugIns_Type.__name__ = "Integer32"
_Mgnt2IndexPlugIns_Object = MibTableColumn
mgnt2IndexPlugIns = _Mgnt2IndexPlugIns_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7, 1, 1),
    _Mgnt2IndexPlugIns_Type()
)
mgnt2IndexPlugIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexPlugIns.setStatus("current")
_Mgnt2PlugInRinv_Type = DisplayString
_Mgnt2PlugInRinv_Object = MibTableColumn
mgnt2PlugInRinv = _Mgnt2PlugInRinv_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7, 1, 2),
    _Mgnt2PlugInRinv_Type()
)
mgnt2PlugInRinv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PlugInRinv.setStatus("current")
_Mgnt2PollingPresent_Type = EkiPlugInState
_Mgnt2PollingPresent_Object = MibTableColumn
mgnt2PollingPresent = _Mgnt2PollingPresent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7, 1, 3),
    _Mgnt2PollingPresent_Type()
)
mgnt2PollingPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PollingPresent.setStatus("current")
_Mgnt2SnmpPresent_Type = EkiPlugInState
_Mgnt2SnmpPresent_Object = MibTableColumn
mgnt2SnmpPresent = _Mgnt2SnmpPresent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 7, 1, 4),
    _Mgnt2SnmpPresent_Type()
)
mgnt2SnmpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2SnmpPresent.setStatus("current")
_Mgnt2RinvBackpanel_Type = DisplayString
_Mgnt2RinvBackpanel_Object = MibScalar
mgnt2RinvBackpanel = _Mgnt2RinvBackpanel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 8),
    _Mgnt2RinvBackpanel_Type()
)
mgnt2RinvBackpanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvBackpanel.setStatus("current")
_Mgnt2RinvFan_Type = DisplayString
_Mgnt2RinvFan_Object = MibScalar
mgnt2RinvFan = _Mgnt2RinvFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 9),
    _Mgnt2RinvFan_Type()
)
mgnt2RinvFan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvFan.setStatus("current")
_Mgnt2RinvUboot_Type = DisplayString
_Mgnt2RinvUboot_Object = MibScalar
mgnt2RinvUboot = _Mgnt2RinvUboot_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 6, 10),
    _Mgnt2RinvUboot_Type()
)
mgnt2RinvUboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2RinvUboot.setStatus("current")
_Mgnt2ErrorCounters_ObjectIdentity = ObjectIdentity
mgnt2ErrorCounters = _Mgnt2ErrorCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7)
)
_Mgnt2GigmErrorCounterTable_Object = MibTable
mgnt2GigmErrorCounterTable = _Mgnt2GigmErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 1)
)
if mibBuilder.loadTexts:
    mgnt2GigmErrorCounterTable.setStatus("current")
_Mgnt2GigmErrorCounterEntry_Object = MibTableRow
mgnt2GigmErrorCounterEntry = _Mgnt2GigmErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 1, 1)
)
mgnt2GigmErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2IndexErrorCounter"),
)
if mibBuilder.loadTexts:
    mgnt2GigmErrorCounterEntry.setStatus("current")


class _Mgnt2IndexErrorCounter_Type(Integer32):
    """Custom type mgnt2IndexErrorCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2IndexErrorCounter_Type.__name__ = "Integer32"
_Mgnt2IndexErrorCounter_Object = MibTableColumn
mgnt2IndexErrorCounter = _Mgnt2IndexErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 1, 1, 1),
    _Mgnt2IndexErrorCounter_Type()
)
mgnt2IndexErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2IndexErrorCounter.setStatus("current")
_Mgnt2ErrorCounterSlotNumber_Type = Integer32
_Mgnt2ErrorCounterSlotNumber_Object = MibTableColumn
mgnt2ErrorCounterSlotNumber = _Mgnt2ErrorCounterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 1, 1, 2),
    _Mgnt2ErrorCounterSlotNumber_Type()
)
mgnt2ErrorCounterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ErrorCounterSlotNumber.setStatus("current")
_Mgnt2ErrorCounterValue_Type = Integer32
_Mgnt2ErrorCounterValue_Object = MibTableColumn
mgnt2ErrorCounterValue = _Mgnt2ErrorCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 1, 1, 3),
    _Mgnt2ErrorCounterValue_Type()
)
mgnt2ErrorCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2ErrorCounterValue.setStatus("current")
_Mgnt2GigmResetErrorCounters_Type = EkiOnOff
_Mgnt2GigmResetErrorCounters_Object = MibScalar
mgnt2GigmResetErrorCounters = _Mgnt2GigmResetErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 7, 2),
    _Mgnt2GigmResetErrorCounters_Type()
)
mgnt2GigmResetErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmResetErrorCounters.setStatus("current")
_Mgnt2Perf_ObjectIdentity = ObjectIdentity
mgnt2Perf = _Mgnt2Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8)
)
_Mgnt2PerfCapabilityTable_Object = MibTable
mgnt2PerfCapabilityTable = _Mgnt2PerfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1)
)
if mibBuilder.loadTexts:
    mgnt2PerfCapabilityTable.setStatus("current")
_Mgnt2PerfCapabilityEntry_Object = MibTableRow
mgnt2PerfCapabilityEntry = _Mgnt2PerfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1)
)
mgnt2PerfCapabilityEntry.setIndexNames(
    (0, "EKINOPS-MGNT2-MIB", "mgnt2PerfCapIndexBoards"),
)
if mibBuilder.loadTexts:
    mgnt2PerfCapabilityEntry.setStatus("current")


class _Mgnt2PerfCapIndexBoards_Type(Integer32):
    """Custom type mgnt2PerfCapIndexBoards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2PerfCapIndexBoards_Type.__name__ = "Integer32"
_Mgnt2PerfCapIndexBoards_Object = MibTableColumn
mgnt2PerfCapIndexBoards = _Mgnt2PerfCapIndexBoards_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1, 1),
    _Mgnt2PerfCapIndexBoards_Type()
)
mgnt2PerfCapIndexBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PerfCapIndexBoards.setStatus("current")


class _Mgnt2PerfCapPosition_Type(Integer32):
    """Custom type mgnt2PerfCapPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Mgnt2PerfCapPosition_Type.__name__ = "Integer32"
_Mgnt2PerfCapPosition_Object = MibTableColumn
mgnt2PerfCapPosition = _Mgnt2PerfCapPosition_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1, 2),
    _Mgnt2PerfCapPosition_Type()
)
mgnt2PerfCapPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PerfCapPosition.setStatus("current")
_Mgnt2PerfCapName_Type = DisplayString
_Mgnt2PerfCapName_Object = MibTableColumn
mgnt2PerfCapName = _Mgnt2PerfCapName_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1, 3),
    _Mgnt2PerfCapName_Type()
)
mgnt2PerfCapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PerfCapName.setStatus("current")
_Mgnt2PerfCapStatus_Type = EkiOnOff
_Mgnt2PerfCapStatus_Object = MibTableColumn
mgnt2PerfCapStatus = _Mgnt2PerfCapStatus_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1, 4),
    _Mgnt2PerfCapStatus_Type()
)
mgnt2PerfCapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PerfCapStatus.setStatus("current")
_Mgnt2PerfCapOidEnable_Type = ObjectIdentifier
_Mgnt2PerfCapOidEnable_Object = MibTableColumn
mgnt2PerfCapOidEnable = _Mgnt2PerfCapOidEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 1, 1, 5),
    _Mgnt2PerfCapOidEnable_Type()
)
mgnt2PerfCapOidEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgnt2PerfCapOidEnable.setStatus("current")
_Mgnt2GigmPerf15minSync_Type = EkiOnOff
_Mgnt2GigmPerf15minSync_Object = MibScalar
mgnt2GigmPerf15minSync = _Mgnt2GigmPerf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 2),
    _Mgnt2GigmPerf15minSync_Type()
)
mgnt2GigmPerf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmPerf15minSync.setStatus("current")
_Mgnt2GigmPerf24hSync_Type = EkiOnOff
_Mgnt2GigmPerf24hSync_Object = MibScalar
mgnt2GigmPerf24hSync = _Mgnt2GigmPerf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 3),
    _Mgnt2GigmPerf24hSync_Type()
)
mgnt2GigmPerf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2GigmPerf24hSync.setStatus("current")
_Mgnt2PerfResyncNMS_Type = Mgnt2PerfResyncValues
_Mgnt2PerfResyncNMS_Object = MibScalar
mgnt2PerfResyncNMS = _Mgnt2PerfResyncNMS_Object(
    (1, 3, 6, 1, 4, 1, 20044, 7, 8, 4),
    _Mgnt2PerfResyncNMS_Type()
)
mgnt2PerfResyncNMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgnt2PerfResyncNMS.setStatus("current")

# Managed Objects groups


# Notification objects

mgnt2TrapApi = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 1)
)
mgnt2TrapApi.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmapiErrorCode"))
)
if mibBuilder.loadTexts:
    mgnt2TrapApi.setStatus(
        "current"
    )

mgnt2TrapSwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 2)
)
mgnt2TrapSwError.setObjects(
    ("EKINOPS-MGNT2-MIB", "mgnt2AlmFifoCmdError")
)
if mibBuilder.loadTexts:
    mgnt2TrapSwError.setStatus(
        "current"
    )

mgnt2TrapBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 4)
)
mgnt2TrapBoardInserted.setObjects(
    ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber")
)
if mibBuilder.loadTexts:
    mgnt2TrapBoardInserted.setStatus(
        "current"
    )

mgnt2TrapBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 5)
)
mgnt2TrapBoardRemoved.setObjects(
    ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber")
)
if mibBuilder.loadTexts:
    mgnt2TrapBoardRemoved.setStatus(
        "current"
    )

mgnt2TrapRestoreConfDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 6)
)
mgnt2TrapRestoreConfDone.setObjects(
    ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber")
)
if mibBuilder.loadTexts:
    mgnt2TrapRestoreConfDone.setStatus(
        "current"
    )

mgnt2TrapGlobalPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 8)
)
mgnt2TrapGlobalPowerFail.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2AlmDef48b"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmDef48a"))
)
if mibBuilder.loadTexts:
    mgnt2TrapGlobalPowerFail.setStatus(
        "current"
    )

mgnt2TrapFanPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 9)
)
mgnt2TrapFanPowerFail.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2AlmFanDefFuseB"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmFanDefFuseA"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmFanPwrFail1"))
)
if mibBuilder.loadTexts:
    mgnt2TrapFanPowerFail.setStatus(
        "current"
    )

mgnt2TrapGigmPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 10)
)
mgnt2TrapGigmPowerFail.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2AlmMgntDefFuseA"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmMgntDefFuseB"))
)
if mibBuilder.loadTexts:
    mgnt2TrapGigmPowerFail.setStatus(
        "current"
    )

mgnt2TrapFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 11)
)
mgnt2TrapFanFail.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan1Fail"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan2Fail"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan3Fail"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan4Fail"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan5Fail"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmPbFan6Fail"))
)
if mibBuilder.loadTexts:
    mgnt2TrapFanFail.setStatus(
        "current"
    )

mgnt2TrapLogFileFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 20)
)
mgnt2TrapLogFileFull.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmLog80Full"),
        ("EKINOPS-MGNT2-MIB", "mgnt2AlmLogFileFull"))
)
if mibBuilder.loadTexts:
    mgnt2TrapLogFileFull.setStatus(
        "current"
    )

mgnt2TrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 30)
)
mgnt2TrapAlarm.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapSeverity"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePm"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortType"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceLabel"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceValue"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapAlarm.setStatus(
        "current"
    )

mgnt2TrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 31)
)
mgnt2TrapEvent.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapEventLabel"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapEvent.setStatus(
        "current"
    )

mgnt2TrapControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 32)
)
mgnt2TrapControl.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePm"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortType"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceLabel"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceValue"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapControl.setStatus(
        "current"
    )

mgnt2TrapConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 7, 3, 33)
)
mgnt2TrapConfig.setObjects(
      *(("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePm"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapBoardNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortType"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourcePortNumber"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceLabel"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapSourceValue"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapNodeControllerIpAddress"),
        ("EKINOPS-MGNT2-MIB", "mgnt2TrapChassisId"))
)
if mibBuilder.loadTexts:
    mgnt2TrapConfig.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-MGNT2-MIB",
    **{"Mgnt2CliAccessValues": Mgnt2CliAccessValues,
       "Mgnt2CraftAccessValues": Mgnt2CraftAccessValues,
       "Mgnt2DccAccessValues": Mgnt2DccAccessValues,
       "Mgnt2TrapModeValues": Mgnt2TrapModeValues,
       "Mgnt2AckMode": Mgnt2AckMode,
       "Mgnt2PerfResyncValues": Mgnt2PerfResyncValues,
       "Mgnt2NetMode": Mgnt2NetMode,
       "Mgnt2MasterEthMode": Mgnt2MasterEthMode,
       "Mgnt2SubnetEthMode": Mgnt2SubnetEthMode,
       "Mgnt2AuthTypeValues": Mgnt2AuthTypeValues,
       "Mgnt2LogFileMode": Mgnt2LogFileMode,
       "Mgnt2SlotStatus": Mgnt2SlotStatus,
       "EkiPlugInState": EkiPlugInState,
       "mgnt2": mgnt2,
       "mgnt2SNMPAgentData": mgnt2SNMPAgentData,
       "mgnt2IPmanagment": mgnt2IPmanagment,
       "mgnt2GigmManagerIpAddressTable": mgnt2GigmManagerIpAddressTable,
       "mgnt2GigmManagerIpAddressEntry": mgnt2GigmManagerIpAddressEntry,
       "mgnt2GigmManagerIpIndex": mgnt2GigmManagerIpIndex,
       "mgnt2GigmManagerIpAddress": mgnt2GigmManagerIpAddress,
       "mgnt2GigmManagerIpAddressTableRowStatus": mgnt2GigmManagerIpAddressTableRowStatus,
       "mgnt2GigmManagerTrapPort": mgnt2GigmManagerTrapPort,
       "mgnt2GigmManagerEnableCtrl": mgnt2GigmManagerEnableCtrl,
       "mgnt2GigmManagerEnableConfig": mgnt2GigmManagerEnableConfig,
       "mgnt2GigmManagerEnableEvent": mgnt2GigmManagerEnableEvent,
       "mgnt2GigmManagerEnableAlarmCrit": mgnt2GigmManagerEnableAlarmCrit,
       "mgnt2GigmManagerEnableAlarmMajor": mgnt2GigmManagerEnableAlarmMajor,
       "mgnt2GigmManagerEnableAlarmMinor": mgnt2GigmManagerEnableAlarmMinor,
       "mgnt2GigmManagerRegistrationTimeout": mgnt2GigmManagerRegistrationTimeout,
       "mgnt2GigmManagerEnableAlarmWarning": mgnt2GigmManagerEnableAlarmWarning,
       "mgnt2GigmManagerEnableAlarmIndeterminate": mgnt2GigmManagerEnableAlarmIndeterminate,
       "mgnt2GigmBoardIpAddress": mgnt2GigmBoardIpAddress,
       "mgnt2GigmIPAddresByDHCP": mgnt2GigmIPAddresByDHCP,
       "mgnt2GigmNetmask": mgnt2GigmNetmask,
       "mgnt2GigmGatewayAddressTable": mgnt2GigmGatewayAddressTable,
       "mgnt2GigmGatewayAddressEntry": mgnt2GigmGatewayAddressEntry,
       "mgnt2GigmGatewayIndex": mgnt2GigmGatewayIndex,
       "mgnt2GigmGatewayAddress": mgnt2GigmGatewayAddress,
       "mgnt2GigmGatewayOrder": mgnt2GigmGatewayOrder,
       "mgnt2GigmSyslog": mgnt2GigmSyslog,
       "mgnt2GigmNtpServer": mgnt2GigmNtpServer,
       "mgnt2GigmNodeIpAddress": mgnt2GigmNodeIpAddress,
       "mgnt2ModulesManagement": mgnt2ModulesManagement,
       "mgnt2GigmBoardTable": mgnt2GigmBoardTable,
       "mgnt2GigmBoardEntry": mgnt2GigmBoardEntry,
       "mgnt2IndexBoards": mgnt2IndexBoards,
       "mgnt2Position": mgnt2Position,
       "mgnt2Name": mgnt2Name,
       "mgnt2PortNumber": mgnt2PortNumber,
       "mgnt2LineNumber": mgnt2LineNumber,
       "mgnt2GroupNumber": mgnt2GroupNumber,
       "mgnt2RootOIDInventory": mgnt2RootOIDInventory,
       "mgnt2SlotOcc": mgnt2SlotOcc,
       "mgnt2SubFunctionLabel": mgnt2SubFunctionLabel,
       "mgnt2SlotStatus": mgnt2SlotStatus,
       "mgnt2GigmSelectedBoard": mgnt2GigmSelectedBoard,
       "mgnt2GigmMibsTable": mgnt2GigmMibsTable,
       "mgnt2GigmMibsEntry": mgnt2GigmMibsEntry,
       "mgnt2IndexMibs": mgnt2IndexMibs,
       "mgnt2MibName": mgnt2MibName,
       "mgnt2MibPartNumber": mgnt2MibPartNumber,
       "mgnt2GigmLogicalName": mgnt2GigmLogicalName,
       "mgnt2GigmEqptType": mgnt2GigmEqptType,
       "mgnt2GigmTrapCount": mgnt2GigmTrapCount,
       "mgnt2GigmTrapCounter": mgnt2GigmTrapCounter,
       "mgnt2GigmResetTrapCounter": mgnt2GigmResetTrapCounter,
       "mgnt2GigmSecurity": mgnt2GigmSecurity,
       "mgnt2GigmRoCommunity": mgnt2GigmRoCommunity,
       "mgnt2GigmRwCommunity": mgnt2GigmRwCommunity,
       "mgnt2GigmTrapCommunity": mgnt2GigmTrapCommunity,
       "mgnt2GigmTime": mgnt2GigmTime,
       "mgnt2GigmCurrentHour": mgnt2GigmCurrentHour,
       "mgnt2GigmCurrentMinute": mgnt2GigmCurrentMinute,
       "mgnt2GigmCurrentYear": mgnt2GigmCurrentYear,
       "mgnt2GigmCurrentMonth": mgnt2GigmCurrentMonth,
       "mgnt2GigmCurrentDay": mgnt2GigmCurrentDay,
       "mgnt2Authentication": mgnt2Authentication,
       "mgnt2GigmRadiusServer": mgnt2GigmRadiusServer,
       "mgnt2GigmRadiusPort": mgnt2GigmRadiusPort,
       "mgnt2GigmRadiusSecret": mgnt2GigmRadiusSecret,
       "mgnt2GigmLdapHost": mgnt2GigmLdapHost,
       "mgnt2GigmLdapPort": mgnt2GigmLdapPort,
       "mgnt2GigmLdapBase": mgnt2GigmLdapBase,
       "mgnt2GigmLdapVersion": mgnt2GigmLdapVersion,
       "mgnt2GigmLdapBindDn": mgnt2GigmLdapBindDn,
       "mgnt2GigmLdapBindPw": mgnt2GigmLdapBindPw,
       "mgnt2GigmLdapScope": mgnt2GigmLdapScope,
       "mgnt2GigmLdapPamPasswd": mgnt2GigmLdapPamPasswd,
       "mgnt2GigmAuthenticationType": mgnt2GigmAuthenticationType,
       "mgnt2Hardware": mgnt2Hardware,
       "mgnt2alarms": mgnt2alarms,
       "mgnt2AlmsynthAlm0": mgnt2AlmsynthAlm0,
       "mgnt2AlmAbsFailure": mgnt2AlmAbsFailure,
       "mgnt2AlmFansFailure": mgnt2AlmFansFailure,
       "mgnt2AlmDef48a": mgnt2AlmDef48a,
       "mgnt2AlmDef48b": mgnt2AlmDef48b,
       "mgnt2AlmMgntDefFuseA": mgnt2AlmMgntDefFuseA,
       "mgnt2AlmMgntDefFuseB": mgnt2AlmMgntDefFuseB,
       "mgnt2AlmsynthAlm1": mgnt2AlmsynthAlm1,
       "mgnt2AlmNurgVisual": mgnt2AlmNurgVisual,
       "mgnt2AlmUrgVisual": mgnt2AlmUrgVisual,
       "mgnt2AlmCritVisual": mgnt2AlmCritVisual,
       "mgnt2AlmAcknowledge": mgnt2AlmAcknowledge,
       "mgnt2AlmboardMgmntSet1": mgnt2AlmboardMgmntSet1,
       "mgnt2AlmPmSlot1Absent": mgnt2AlmPmSlot1Absent,
       "mgnt2AlmPmSlot2Absent": mgnt2AlmPmSlot2Absent,
       "mgnt2AlmPmSlot3Absent": mgnt2AlmPmSlot3Absent,
       "mgnt2AlmPmSlot4Absent": mgnt2AlmPmSlot4Absent,
       "mgnt2AlmPmSlot5Absent": mgnt2AlmPmSlot5Absent,
       "mgnt2AlmPmSlot6Absent": mgnt2AlmPmSlot6Absent,
       "mgnt2AlmPmSlot7Absent": mgnt2AlmPmSlot7Absent,
       "mgnt2AlmPmSlot8Absent": mgnt2AlmPmSlot8Absent,
       "mgnt2AlmPmSlot9Absent": mgnt2AlmPmSlot9Absent,
       "mgnt2AlmPmSlot10Absent": mgnt2AlmPmSlot10Absent,
       "mgnt2AlmPmSlot11Absent": mgnt2AlmPmSlot11Absent,
       "mgnt2AlmPmFanAbsent": mgnt2AlmPmFanAbsent,
       "mgnt2AlmboardMgmntSet2": mgnt2AlmboardMgmntSet2,
       "mgnt2AlmPmSlot12Absent": mgnt2AlmPmSlot12Absent,
       "mgnt2AlmPmSlot13Absent": mgnt2AlmPmSlot13Absent,
       "mgnt2AlmPmSlot14Absent": mgnt2AlmPmSlot14Absent,
       "mgnt2AlmPmSlot15Absent": mgnt2AlmPmSlot15Absent,
       "mgnt2AlmPmSlot16Absent": mgnt2AlmPmSlot16Absent,
       "mgnt2AlmPmSlot17Absent": mgnt2AlmPmSlot17Absent,
       "mgnt2AlmPmSlot18Absent": mgnt2AlmPmSlot18Absent,
       "mgnt2AlmPmSlot19Absent": mgnt2AlmPmSlot19Absent,
       "mgnt2AlmPmSlot20Absent": mgnt2AlmPmSlot20Absent,
       "mgnt2AlmfanMgmnt": mgnt2AlmfanMgmnt,
       "mgnt2AlmPbFan1Fail": mgnt2AlmPbFan1Fail,
       "mgnt2AlmPbFan2Fail": mgnt2AlmPbFan2Fail,
       "mgnt2AlmPbFan3Fail": mgnt2AlmPbFan3Fail,
       "mgnt2AlmPbFan4Fail": mgnt2AlmPbFan4Fail,
       "mgnt2AlmPbFan5Fail": mgnt2AlmPbFan5Fail,
       "mgnt2AlmPbFan6Fail": mgnt2AlmPbFan6Fail,
       "mgnt2AlmFanFilterAbsent": mgnt2AlmFanFilterAbsent,
       "mgnt2AlmfanPwrMgmnt": mgnt2AlmfanPwrMgmnt,
       "mgnt2AlmFanPwrProtOn": mgnt2AlmFanPwrProtOn,
       "mgnt2AlmFanPwrFail1": mgnt2AlmFanPwrFail1,
       "mgnt2AlmFanDefFuseA": mgnt2AlmFanDefFuseA,
       "mgnt2AlmFanDefFuseB": mgnt2AlmFanDefFuseB,
       "mgnt2AlmremoveablefanModuleFail": mgnt2AlmremoveablefanModuleFail,
       "mgnt2AlmFan1ModuleAbsent": mgnt2AlmFan1ModuleAbsent,
       "mgnt2AlmFan2ModuleAbsent": mgnt2AlmFan2ModuleAbsent,
       "mgnt2AlmFan3ModuleAbsent": mgnt2AlmFan3ModuleAbsent,
       "mgnt2AlmFan4ModuleAbsent": mgnt2AlmFan4ModuleAbsent,
       "mgnt2AlmremoveableFanModuleMgmnt": mgnt2AlmremoveableFanModuleMgmnt,
       "mgnt2AlmFan1ModuleFail": mgnt2AlmFan1ModuleFail,
       "mgnt2AlmFan2ModuleFail": mgnt2AlmFan2ModuleFail,
       "mgnt2AlmFan3ModuleFail": mgnt2AlmFan3ModuleFail,
       "mgnt2AlmFan4ModuleFail": mgnt2AlmFan4ModuleFail,
       "mgnt2AlmswAlarm1": mgnt2AlmswAlarm1,
       "mgnt2AlmApiError": mgnt2AlmApiError,
       "mgnt2AlmFifoCmdError": mgnt2AlmFifoCmdError,
       "mgnt2AlmPollingManagerError": mgnt2AlmPollingManagerError,
       "mgnt2AlmapiErrorCode": mgnt2AlmapiErrorCode,
       "mgnt2AlmlogMgmnt": mgnt2AlmlogMgmnt,
       "mgnt2AlmLogFileFull": mgnt2AlmLogFileFull,
       "mgnt2AlmLog80Full": mgnt2AlmLog80Full,
       "mgnt2AlmntpSyncLoss": mgnt2AlmntpSyncLoss,
       "mgnt2AlmNtpSyncLoss": mgnt2AlmNtpSyncLoss,
       "mgnt2AlmCpuTempOverRange": mgnt2AlmCpuTempOverRange,
       "mgnt2controls": mgnt2controls,
       "mgnt2Ctrlsynth5": mgnt2Ctrlsynth5,
       "mgnt2CtrlChassisShutdown": mgnt2CtrlChassisShutdown,
       "mgnt2CtrlChassisWarmReset": mgnt2CtrlChassisWarmReset,
       "mgnt2CtrlChassisColdReset": mgnt2CtrlChassisColdReset,
       "mgnt2CtrltestLed": mgnt2CtrltestLed,
       "mgnt2CtrlGreenLed": mgnt2CtrlGreenLed,
       "mgnt2CtrlRedLed": mgnt2CtrlRedLed,
       "mgnt2CtrlLedOff": mgnt2CtrlLedOff,
       "mgnt2CtrllogFile": mgnt2CtrllogFile,
       "mgnt2CtrlLogFileReset": mgnt2CtrlLogFileReset,
       "mgnt2CtrlmgntSaveConfig": mgnt2CtrlmgntSaveConfig,
       "mgnt2CtrlSaveConfig": mgnt2CtrlSaveConfig,
       "mgnt2CtrlmgntGetGlobalConfig": mgnt2CtrlmgntGetGlobalConfig,
       "mgnt2CtrlGetGlobalConfig": mgnt2CtrlGetGlobalConfig,
       "mgnt2CtrlmgntPutGlobalConfig": mgnt2CtrlmgntPutGlobalConfig,
       "mgnt2CtrlPutGlobalConfig": mgnt2CtrlPutGlobalConfig,
       "mgnt2CtrlmgntAcknowledge": mgnt2CtrlmgntAcknowledge,
       "mgnt2CtrlAcknowledge": mgnt2CtrlAcknowledge,
       "mgnt2config": mgnt2config,
       "mgnt2CfgethPort2": mgnt2CfgethPort2,
       "mgnt2CfgEthPort2Disable": mgnt2CfgEthPort2Disable,
       "mgnt2CfgChassisEthernetSplit": mgnt2CfgChassisEthernetSplit,
       "mgnt2CfgmgntDccEnable": mgnt2CfgmgntDccEnable,
       "mgnt2CfgpmTrapEnable": mgnt2CfgpmTrapEnable,
       "mgnt2CfgPmCriticalTrapEn": mgnt2CfgPmCriticalTrapEn,
       "mgnt2CfgPmMajorTrapEn": mgnt2CfgPmMajorTrapEn,
       "mgnt2CfgPmMinorTrapEn": mgnt2CfgPmMinorTrapEn,
       "mgnt2CfgPmControlTrapEn": mgnt2CfgPmControlTrapEn,
       "mgnt2CfgPmConfigTrapEn": mgnt2CfgPmConfigTrapEn,
       "mgnt2CfgmgntTrapEnable": mgnt2CfgmgntTrapEnable,
       "mgnt2CfgMgntCriticalTrapEn": mgnt2CfgMgntCriticalTrapEn,
       "mgnt2CfgMgntMajorTrapEn": mgnt2CfgMgntMajorTrapEn,
       "mgnt2CfgMgntMinorTrapEn": mgnt2CfgMgntMinorTrapEn,
       "mgnt2CfgMgntControlTrapEn": mgnt2CfgMgntControlTrapEn,
       "mgnt2CfgMgntConfigTrapEn": mgnt2CfgMgntConfigTrapEn,
       "mgnt2CfgMgntEventTrapEn": mgnt2CfgMgntEventTrapEn,
       "mgnt2CfgmgntTrapMode": mgnt2CfgmgntTrapMode,
       "mgnt2CfgsyslogEnable": mgnt2CfgsyslogEnable,
       "mgnt2CfgSyslogEventEn": mgnt2CfgSyslogEventEn,
       "mgnt2CfgSyslogConfigEn": mgnt2CfgSyslogConfigEn,
       "mgnt2CfgSyslogCtrlEn": mgnt2CfgSyslogCtrlEn,
       "mgnt2CfgSyslogAlarmEn": mgnt2CfgSyslogAlarmEn,
       "mgnt2CfgntpTimeZone": mgnt2CfgntpTimeZone,
       "mgnt2CfgpmConfEnable": mgnt2CfgpmConfEnable,
       "mgnt2CfgPmBackupEnable": mgnt2CfgPmBackupEnable,
       "mgnt2CfgPmRestoreEnable": mgnt2CfgPmRestoreEnable,
       "mgnt2CfginactivityTimeout": mgnt2CfginactivityTimeout,
       "mgnt2CfgcliAccess": mgnt2CfgcliAccess,
       "mgnt2CfgcraftAccess": mgnt2CfgcraftAccess,
       "mgnt2CfgperfModes1": mgnt2CfgperfModes1,
       "mgnt2CfgalarmModelActiv": mgnt2CfgalarmModelActiv,
       "mgnt2CfgnetworkInput": mgnt2CfgnetworkInput,
       "mgnt2CfgmasterEthMode": mgnt2CfgmasterEthMode,
       "mgnt2CfgsubnetMode": mgnt2CfgsubnetMode,
       "mgnt2CfgrstpMode": mgnt2CfgrstpMode,
       "mgnt2CfgRstpEnable": mgnt2CfgRstpEnable,
       "mgnt2CfglldpMode": mgnt2CfglldpMode,
       "mgnt2CfgLldpEnable": mgnt2CfgLldpEnable,
       "mgnt2CfglogMode": mgnt2CfglogMode,
       "mgnt2CfgnodeMode": mgnt2CfgnodeMode,
       "mgnt2CfgNodeControllerEnable": mgnt2CfgNodeControllerEnable,
       "mgnt2CfgunprivilegedUsersMode": mgnt2CfgunprivilegedUsersMode,
       "mgnt2CfgRestrictUnprivilegeUsers": mgnt2CfgRestrictUnprivilegeUsers,
       "mgnt2CfgoscDccLinkUpThreshold": mgnt2CfgoscDccLinkUpThreshold,
       "mgnt2CfgoscDccLinkDownThreshold": mgnt2CfgoscDccLinkDownThreshold,
       "mgnt2CfgaccountAutoLock": mgnt2CfgaccountAutoLock,
       "mgnt2CfgfailCountReset": mgnt2CfgfailCountReset,
       "mgnt2CfgftpMode": mgnt2CfgftpMode,
       "mgnt2CfgFtpEnable": mgnt2CfgFtpEnable,
       "mgnt2CfgtftpMode": mgnt2CfgtftpMode,
       "mgnt2CfgTftpEnable": mgnt2CfgTftpEnable,
       "mgnt2Traps": mgnt2Traps,
       "mgnt2TrapApi": mgnt2TrapApi,
       "mgnt2TrapSwError": mgnt2TrapSwError,
       "mgnt2TrapBoardInserted": mgnt2TrapBoardInserted,
       "mgnt2TrapBoardRemoved": mgnt2TrapBoardRemoved,
       "mgnt2TrapRestoreConfDone": mgnt2TrapRestoreConfDone,
       "mgnt2TrapGlobalPowerFail": mgnt2TrapGlobalPowerFail,
       "mgnt2TrapFanPowerFail": mgnt2TrapFanPowerFail,
       "mgnt2TrapGigmPowerFail": mgnt2TrapGigmPowerFail,
       "mgnt2TrapFanFail": mgnt2TrapFanFail,
       "mgnt2TrapLogFileFull": mgnt2TrapLogFileFull,
       "mgnt2TrapAlarm": mgnt2TrapAlarm,
       "mgnt2TrapEvent": mgnt2TrapEvent,
       "mgnt2TrapControl": mgnt2TrapControl,
       "mgnt2TrapConfig": mgnt2TrapConfig,
       "mgnt2TrapBoardNumber": mgnt2TrapBoardNumber,
       "mgnt2TrapSeverity": mgnt2TrapSeverity,
       "mgnt2TrapSourcePm": mgnt2TrapSourcePm,
       "mgnt2TrapSourcePortType": mgnt2TrapSourcePortType,
       "mgnt2TrapSourcePortNumber": mgnt2TrapSourcePortNumber,
       "mgnt2TrapSourceLabel": mgnt2TrapSourceLabel,
       "mgnt2TrapSourceValue": mgnt2TrapSourceValue,
       "mgnt2TrapEventLabel": mgnt2TrapEventLabel,
       "mgnt2TrapNodeControllerIpAddress": mgnt2TrapNodeControllerIpAddress,
       "mgnt2TrapChassisId": mgnt2TrapChassisId,
       "mgnt2SoftwareManagement": mgnt2SoftwareManagement,
       "mgnt2DwlUploadingTable": mgnt2DwlUploadingTable,
       "mgnt2DwlUploadingEntry": mgnt2DwlUploadingEntry,
       "mgnt2IndexUpload": mgnt2IndexUpload,
       "mgnt2DwlUploadFileName": mgnt2DwlUploadFileName,
       "mgnt2ImmediateReplacement": mgnt2ImmediateReplacement,
       "mgnt2FileUpload": mgnt2FileUpload,
       "mgnt2DeletePackageFromRam": mgnt2DeletePackageFromRam,
       "mgnt2FlashingInProgress": mgnt2FlashingInProgress,
       "mgnt2DwlPackageTable": mgnt2DwlPackageTable,
       "mgnt2DwlPackageEntry": mgnt2DwlPackageEntry,
       "mgnt2IndexPackage": mgnt2IndexPackage,
       "mgnt2DwlPackageFileName": mgnt2DwlPackageFileName,
       "mgnt2ExtractedPack": mgnt2ExtractedPack,
       "mgnt2SwitchTo": mgnt2SwitchTo,
       "mgnt2Immediate": mgnt2Immediate,
       "mgnt2DeletePackageFromFlash": mgnt2DeletePackageFromFlash,
       "mgnt2PackageExtractionInProgress": mgnt2PackageExtractionInProgress,
       "mgnt2DwlUploadingTableUpdate": mgnt2DwlUploadingTableUpdate,
       "mgnt2LoadPMTable": mgnt2LoadPMTable,
       "mgnt2LoadPMEntry": mgnt2LoadPMEntry,
       "mgnt2LoadPMIndex": mgnt2LoadPMIndex,
       "mgnt2LoadFileName": mgnt2LoadFileName,
       "mgnt2LoadFileType": mgnt2LoadFileType,
       "mgnt2LoadState": mgnt2LoadState,
       "mgnt2LoadModuleNumber": mgnt2LoadModuleNumber,
       "mgnt2LoadResetMethod": mgnt2LoadResetMethod,
       "mgnt2LoadResetMode": mgnt2LoadResetMode,
       "mgnt2LoadBankNumber": mgnt2LoadBankNumber,
       "mgnt2LoadDownloadProgress": mgnt2LoadDownloadProgress,
       "mgnt2LoadTransfer": mgnt2LoadTransfer,
       "mgnt2LoadDelete": mgnt2LoadDelete,
       "mgnt2LoadPMTableUpdate": mgnt2LoadPMTableUpdate,
       "mgnt2DwlEkicraftPkgTable": mgnt2DwlEkicraftPkgTable,
       "mgnt2DwlEkicraftPkgEntry": mgnt2DwlEkicraftPkgEntry,
       "mgnt2IndexEkicraftPkg": mgnt2IndexEkicraftPkg,
       "mgnt2DwlEkicraftPkgFileName": mgnt2DwlEkicraftPkgFileName,
       "mgnt2DwlEkicraftExtractedPack": mgnt2DwlEkicraftExtractedPack,
       "mgnt2DwlEkicraftSwitchTo": mgnt2DwlEkicraftSwitchTo,
       "mgnt2DwlEkicraftImmediate": mgnt2DwlEkicraftImmediate,
       "mgnt2DeleteEkicraftPkgFromFlash": mgnt2DeleteEkicraftPkgFromFlash,
       "mgnt2EkicraftPkgExtractionInProgress": mgnt2EkicraftPkgExtractionInProgress,
       "mgnt2ConfigManagement": mgnt2ConfigManagement,
       "mgnt2CnfUploadConfigFilesTable": mgnt2CnfUploadConfigFilesTable,
       "mgnt2CnfUploadConfigFilesEntry": mgnt2CnfUploadConfigFilesEntry,
       "mgnt2CnfUploadConfigIndex": mgnt2CnfUploadConfigIndex,
       "mgnt2CnfConfigFileName": mgnt2CnfConfigFileName,
       "mgnt2CnfConfigSlot": mgnt2CnfConfigSlot,
       "mgnt2CnfConfigUpload": mgnt2CnfConfigUpload,
       "mgnt2CnfDeleteConfigFile": mgnt2CnfDeleteConfigFile,
       "mgnt2CnfManageConfigFilesTable": mgnt2CnfManageConfigFilesTable,
       "mgnt2CnfManageConfigFilesEntry": mgnt2CnfManageConfigFilesEntry,
       "mgnt2CnfManageConfigIndex": mgnt2CnfManageConfigIndex,
       "mgnt2CnfManageConfigFileID": mgnt2CnfManageConfigFileID,
       "mgnt2CnfManageConfigFileName": mgnt2CnfManageConfigFileName,
       "mgnt2CnfModuleSlotNumber": mgnt2CnfModuleSlotNumber,
       "mgnt2CnfBackupConfig": mgnt2CnfBackupConfig,
       "mgnt2CnfRestoreConfig": mgnt2CnfRestoreConfig,
       "mgnt2CnfExportConfig": mgnt2CnfExportConfig,
       "mgnt2CnfDeleteConfig": mgnt2CnfDeleteConfig,
       "mgnt2RemoteInventory": mgnt2RemoteInventory,
       "mgnt2RinvHwPlatform": mgnt2RinvHwPlatform,
       "mgnt2RinvSoftwarePackage": mgnt2RinvSoftwarePackage,
       "mgnt2RinvGateware": mgnt2RinvGateware,
       "mgnt2RinvAgent": mgnt2RinvAgent,
       "mgnt2RinvCraft": mgnt2RinvCraft,
       "mgnt2RinvLinux": mgnt2RinvLinux,
       "mgnt2GigmPlugInTable": mgnt2GigmPlugInTable,
       "mgnt2GigmPlugInEntry": mgnt2GigmPlugInEntry,
       "mgnt2IndexPlugIns": mgnt2IndexPlugIns,
       "mgnt2PlugInRinv": mgnt2PlugInRinv,
       "mgnt2PollingPresent": mgnt2PollingPresent,
       "mgnt2SnmpPresent": mgnt2SnmpPresent,
       "mgnt2RinvBackpanel": mgnt2RinvBackpanel,
       "mgnt2RinvFan": mgnt2RinvFan,
       "mgnt2RinvUboot": mgnt2RinvUboot,
       "mgnt2ErrorCounters": mgnt2ErrorCounters,
       "mgnt2GigmErrorCounterTable": mgnt2GigmErrorCounterTable,
       "mgnt2GigmErrorCounterEntry": mgnt2GigmErrorCounterEntry,
       "mgnt2IndexErrorCounter": mgnt2IndexErrorCounter,
       "mgnt2ErrorCounterSlotNumber": mgnt2ErrorCounterSlotNumber,
       "mgnt2ErrorCounterValue": mgnt2ErrorCounterValue,
       "mgnt2GigmResetErrorCounters": mgnt2GigmResetErrorCounters,
       "mgnt2Perf": mgnt2Perf,
       "mgnt2PerfCapabilityTable": mgnt2PerfCapabilityTable,
       "mgnt2PerfCapabilityEntry": mgnt2PerfCapabilityEntry,
       "mgnt2PerfCapIndexBoards": mgnt2PerfCapIndexBoards,
       "mgnt2PerfCapPosition": mgnt2PerfCapPosition,
       "mgnt2PerfCapName": mgnt2PerfCapName,
       "mgnt2PerfCapStatus": mgnt2PerfCapStatus,
       "mgnt2PerfCapOidEnable": mgnt2PerfCapOidEnable,
       "mgnt2GigmPerf15minSync": mgnt2GigmPerf15minSync,
       "mgnt2GigmPerf24hSync": mgnt2GigmPerf24hSync,
       "mgnt2PerfResyncNMS": mgnt2PerfResyncNMS}
)
