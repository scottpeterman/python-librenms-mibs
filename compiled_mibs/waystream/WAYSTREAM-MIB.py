# SNMP MIB module (WAYSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:01 2025
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

(wsExperiment,
 wsMgmt) = mibBuilder.importSymbols(
    "WAYSTREAM-SMI",
    "wsExperiment",
    "wsMgmt")


# MODULE-IDENTITY

ibos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1)
)
if mibBuilder.loadTexts:
    ibos.setRevisions(
        ("2017-10-23 11:00",
         "2017-09-18 11:00",
         "2017-02-10 11:00",
         "2012-07-05 19:30",
         "2011-12-20 09:08",
         "2011-12-06 09:34",
         "2011-01-11 17:55",
         "2009-04-17 15:29",
         "2009-03-23 11:02",
         "2008-04-30 14:26",
         "2007-10-03 18:35",
         "2007-06-13 14:37",
         "2006-10-18 13:41",
         "2006-08-23 11:00",
         "2006-01-25 13:30",
         "2005-05-10 11:24",
         "2005-02-01 09:11",
         "2005-01-14 15:00",
         "2004-10-20 14:34",
         "2004-05-14 11:55")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsSystem_ObjectIdentity = ObjectIdentity
wsSystem = _WsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wsSystem.setStatus("current")


class _WsWritedummy_Type(Integer32):
    """Custom type wsWritedummy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsWritedummy_Type.__name__ = "Integer32"
_WsWritedummy_Object = MibScalar
wsWritedummy = _WsWritedummy_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1, 1),
    _WsWritedummy_Type()
)
wsWritedummy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsWritedummy.setStatus("current")


class _WsReload_Type(Integer32):
    """Custom type wsReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsReload_Type.__name__ = "Integer32"
_WsReload_Object = MibScalar
wsReload = _WsReload_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1, 2),
    _WsReload_Type()
)
wsReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsReload.setStatus("current")


class _WsVersion_Type(Integer32):
    """Custom type wsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsVersion_Type.__name__ = "Integer32"
_WsVersion_Object = MibScalar
wsVersion = _WsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1, 3),
    _WsVersion_Type()
)
wsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVersion.setStatus("current")


class _WsAsrRevision_Type(Integer32):
    """Custom type wsAsrRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsAsrRevision_Type.__name__ = "Integer32"
_WsAsrRevision_Object = MibScalar
wsAsrRevision = _WsAsrRevision_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1, 4),
    _WsAsrRevision_Type()
)
wsAsrRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAsrRevision.setStatus("current")
_WsVersionString_Type = DisplayString
_WsVersionString_Object = MibScalar
wsVersionString = _WsVersionString_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 1, 5),
    _WsVersionString_Type()
)
wsVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVersionString.setStatus("current")
_WsEnvironment_ObjectIdentity = ObjectIdentity
wsEnvironment = _WsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wsEnvironment.setStatus("current")
_WsIbosEnvironmentNotifications_ObjectIdentity = ObjectIdentity
wsIbosEnvironmentNotifications = _WsIbosEnvironmentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0)
)
_WsTempTable_Object = MibTable
wsTempTable = _WsTempTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wsTempTable.setStatus("current")
_WsTempEntry_Object = MibTableRow
wsTempEntry = _WsTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1)
)
wsTempEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsTempSensor"),
)
if mibBuilder.loadTexts:
    wsTempEntry.setStatus("current")
_WsTempSensor_Type = Unsigned32
_WsTempSensor_Object = MibTableColumn
wsTempSensor = _WsTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 1),
    _WsTempSensor_Type()
)
wsTempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempSensor.setStatus("current")
_WsTempMeasured_Type = Integer32
_WsTempMeasured_Object = MibTableColumn
wsTempMeasured = _WsTempMeasured_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 2),
    _WsTempMeasured_Type()
)
wsTempMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempMeasured.setStatus("current")
_WsTempTOS_Type = Integer32
_WsTempTOS_Object = MibTableColumn
wsTempTOS = _WsTempTOS_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 3),
    _WsTempTOS_Type()
)
wsTempTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempTOS.setStatus("current")
_WsTempTHYST_Type = Integer32
_WsTempTHYST_Object = MibTableColumn
wsTempTHYST = _WsTempTHYST_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 4),
    _WsTempTHYST_Type()
)
wsTempTHYST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempTHYST.setStatus("current")
_WsTempThresholdLow_Type = Integer32
_WsTempThresholdLow_Object = MibTableColumn
wsTempThresholdLow = _WsTempThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 5),
    _WsTempThresholdLow_Type()
)
wsTempThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempThresholdLow.setStatus("current")
_WsTempThresholdHigh_Type = Integer32
_WsTempThresholdHigh_Object = MibTableColumn
wsTempThresholdHigh = _WsTempThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 6),
    _WsTempThresholdHigh_Type()
)
wsTempThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempThresholdHigh.setStatus("current")


class _WsTempStatus_Type(Integer32):
    """Custom type wsTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", -1),
          ("ok", 0),
          ("high", 1),
          ("low", 2),
          ("disabled", 4))
    )


_WsTempStatus_Type.__name__ = "Integer32"
_WsTempStatus_Object = MibTableColumn
wsTempStatus = _WsTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 1, 1, 7),
    _WsTempStatus_Type()
)
wsTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTempStatus.setStatus("current")
_WsVoltTable_Object = MibTable
wsVoltTable = _WsVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wsVoltTable.setStatus("current")
_WsVoltEntry_Object = MibTableRow
wsVoltEntry = _WsVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1)
)
wsVoltEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsVoltChannel"),
)
if mibBuilder.loadTexts:
    wsVoltEntry.setStatus("current")
_WsVoltChannel_Type = Unsigned32
_WsVoltChannel_Object = MibTableColumn
wsVoltChannel = _WsVoltChannel_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 1),
    _WsVoltChannel_Type()
)
wsVoltChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltChannel.setStatus("current")
_WsVoltNominal_Type = Integer32
_WsVoltNominal_Object = MibTableColumn
wsVoltNominal = _WsVoltNominal_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 2),
    _WsVoltNominal_Type()
)
wsVoltNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltNominal.setStatus("current")
_WsVoltMeasured_Type = Integer32
_WsVoltMeasured_Object = MibTableColumn
wsVoltMeasured = _WsVoltMeasured_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 3),
    _WsVoltMeasured_Type()
)
wsVoltMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltMeasured.setStatus("current")
_WsVoltThresholdLow_Type = Integer32
_WsVoltThresholdLow_Object = MibTableColumn
wsVoltThresholdLow = _WsVoltThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 4),
    _WsVoltThresholdLow_Type()
)
wsVoltThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltThresholdLow.setStatus("current")
_WsVoltThresholdHigh_Type = Integer32
_WsVoltThresholdHigh_Object = MibTableColumn
wsVoltThresholdHigh = _WsVoltThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 5),
    _WsVoltThresholdHigh_Type()
)
wsVoltThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltThresholdHigh.setStatus("current")


class _WsVoltStatus_Type(Integer32):
    """Custom type wsVoltStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", -3),
          ("failed", -1),
          ("ok", 0),
          ("high", 1),
          ("low", 2),
          ("notPresent", 3),
          ("disabled", 4))
    )


_WsVoltStatus_Type.__name__ = "Integer32"
_WsVoltStatus_Object = MibTableColumn
wsVoltStatus = _WsVoltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 2, 1, 6),
    _WsVoltStatus_Type()
)
wsVoltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsVoltStatus.setStatus("current")
_WsFanTable_Object = MibTable
wsFanTable = _WsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wsFanTable.setStatus("current")
_WsFanEntry_Object = MibTableRow
wsFanEntry = _WsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 3, 1)
)
wsFanEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsFanNumber"),
)
if mibBuilder.loadTexts:
    wsFanEntry.setStatus("current")
_WsFanNumber_Type = Unsigned32
_WsFanNumber_Object = MibTableColumn
wsFanNumber = _WsFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 3, 1, 1),
    _WsFanNumber_Type()
)
wsFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFanNumber.setStatus("current")
_WsFanRPM_Type = Integer32
_WsFanRPM_Object = MibTableColumn
wsFanRPM = _WsFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 3, 1, 2),
    _WsFanRPM_Type()
)
wsFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFanRPM.setStatus("current")
_WsFanVoltage_Type = Integer32
_WsFanVoltage_Object = MibScalar
wsFanVoltage = _WsFanVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 4),
    _WsFanVoltage_Type()
)
wsFanVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsFanVoltage.setStatus("current")


class _WsIbosEnvironmentTrapEnable_Type(Integer32):
    """Custom type wsIbosEnvironmentTrapEnable based on Integer32"""
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


_WsIbosEnvironmentTrapEnable_Type.__name__ = "Integer32"
_WsIbosEnvironmentTrapEnable_Object = MibScalar
wsIbosEnvironmentTrapEnable = _WsIbosEnvironmentTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 5),
    _WsIbosEnvironmentTrapEnable_Type()
)
wsIbosEnvironmentTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsIbosEnvironmentTrapEnable.setStatus("current")
_WsPFDP_ObjectIdentity = ObjectIdentity
wsPFDP = _WsPFDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3)
)
if mibBuilder.loadTexts:
    wsPFDP.setStatus("current")
_WsNeighboursTable_Object = MibTable
wsNeighboursTable = _WsNeighboursTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wsNeighboursTable.setStatus("current")
_WsNeighboursEntry_Object = MibTableRow
wsNeighboursEntry = _WsNeighboursEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1)
)
wsNeighboursEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsNeighbourIfIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourNIndex"),
)
if mibBuilder.loadTexts:
    wsNeighboursEntry.setStatus("current")
_WsNeighbourIfIndex_Type = Unsigned32
_WsNeighbourIfIndex_Object = MibTableColumn
wsNeighbourIfIndex = _WsNeighbourIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 1),
    _WsNeighbourIfIndex_Type()
)
wsNeighbourIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourIfIndex.setStatus("current")
_WsNeighbourNIndex_Type = Unsigned32
_WsNeighbourNIndex_Object = MibTableColumn
wsNeighbourNIndex = _WsNeighbourNIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 2),
    _WsNeighbourNIndex_Type()
)
wsNeighbourNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourNIndex.setStatus("current")
_WsNeighbourHostname_Type = DisplayString
_WsNeighbourHostname_Object = MibTableColumn
wsNeighbourHostname = _WsNeighbourHostname_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 3),
    _WsNeighbourHostname_Type()
)
wsNeighbourHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourHostname.setStatus("current")
_WsNeighbourLocalIf_Type = DisplayString
_WsNeighbourLocalIf_Object = MibTableColumn
wsNeighbourLocalIf = _WsNeighbourLocalIf_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 4),
    _WsNeighbourLocalIf_Type()
)
wsNeighbourLocalIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourLocalIf.setStatus("current")
_WsNeighbourRemoteIf_Type = DisplayString
_WsNeighbourRemoteIf_Object = MibTableColumn
wsNeighbourRemoteIf = _WsNeighbourRemoteIf_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 5),
    _WsNeighbourRemoteIf_Type()
)
wsNeighbourRemoteIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourRemoteIf.setStatus("current")
_WsNeighbourModel_Type = DisplayString
_WsNeighbourModel_Object = MibTableColumn
wsNeighbourModel = _WsNeighbourModel_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 6),
    _WsNeighbourModel_Type()
)
wsNeighbourModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourModel.setStatus("current")
_WsNeighbourLastAct_Type = Integer32
_WsNeighbourLastAct_Object = MibTableColumn
wsNeighbourLastAct = _WsNeighbourLastAct_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 7),
    _WsNeighbourLastAct_Type()
)
wsNeighbourLastAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourLastAct.setStatus("current")
_WsNeighbourOSVersion_Type = DisplayString
_WsNeighbourOSVersion_Object = MibTableColumn
wsNeighbourOSVersion = _WsNeighbourOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 8),
    _WsNeighbourOSVersion_Type()
)
wsNeighbourOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourOSVersion.setStatus("current")
_WsNeighbourSNPA_Type = OctetString
_WsNeighbourSNPA_Object = MibTableColumn
wsNeighbourSNPA = _WsNeighbourSNPA_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 9),
    _WsNeighbourSNPA_Type()
)
wsNeighbourSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourSNPA.setStatus("current")
_WsNeighbourUptime_Type = Unsigned32
_WsNeighbourUptime_Object = MibTableColumn
wsNeighbourUptime = _WsNeighbourUptime_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 10),
    _WsNeighbourUptime_Type()
)
wsNeighbourUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourUptime.setStatus("current")


class _WsNeighbourState_Type(Integer32):
    """Custom type wsNeighbourState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_WsNeighbourState_Type.__name__ = "Integer32"
_WsNeighbourState_Object = MibTableColumn
wsNeighbourState = _WsNeighbourState_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 11),
    _WsNeighbourState_Type()
)
wsNeighbourState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourState.setStatus("current")
_WsNeighbourDBCount_Type = Unsigned32
_WsNeighbourDBCount_Object = MibTableColumn
wsNeighbourDBCount = _WsNeighbourDBCount_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 12),
    _WsNeighbourDBCount_Type()
)
wsNeighbourDBCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourDBCount.setStatus("current")
_WsNeighbourCreated_Type = TimeTicks
_WsNeighbourCreated_Object = MibTableColumn
wsNeighbourCreated = _WsNeighbourCreated_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 13),
    _WsNeighbourCreated_Type()
)
wsNeighbourCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourCreated.setStatus("current")
_WsNeighbourPacketsIn_Type = Unsigned32
_WsNeighbourPacketsIn_Object = MibTableColumn
wsNeighbourPacketsIn = _WsNeighbourPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 14),
    _WsNeighbourPacketsIn_Type()
)
wsNeighbourPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPacketsIn.setStatus("current")
_WsNeighbourPacketErrorsrIn_Type = Unsigned32
_WsNeighbourPacketErrorsrIn_Object = MibTableColumn
wsNeighbourPacketErrorsrIn = _WsNeighbourPacketErrorsrIn_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 1, 1, 15),
    _WsNeighbourPacketErrorsrIn_Type()
)
wsNeighbourPacketErrorsrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPacketErrorsrIn.setStatus("current")
_WsNeighbourPortsTable_Object = MibTable
wsNeighbourPortsTable = _WsNeighbourPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wsNeighbourPortsTable.setStatus("current")
_WsNeighbourPortsEntry_Object = MibTableRow
wsNeighbourPortsEntry = _WsNeighbourPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1)
)
wsNeighbourPortsEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsNeighbourPortIfIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourPortNIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourPortPIndex"),
)
if mibBuilder.loadTexts:
    wsNeighbourPortsEntry.setStatus("current")
_WsNeighbourPortIfIndex_Type = Unsigned32
_WsNeighbourPortIfIndex_Object = MibTableColumn
wsNeighbourPortIfIndex = _WsNeighbourPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 1),
    _WsNeighbourPortIfIndex_Type()
)
wsNeighbourPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortIfIndex.setStatus("current")
_WsNeighbourPortNIndex_Type = Unsigned32
_WsNeighbourPortNIndex_Object = MibTableColumn
wsNeighbourPortNIndex = _WsNeighbourPortNIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 2),
    _WsNeighbourPortNIndex_Type()
)
wsNeighbourPortNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortNIndex.setStatus("current")
_WsNeighbourPortPIndex_Type = Unsigned32
_WsNeighbourPortPIndex_Object = MibTableColumn
wsNeighbourPortPIndex = _WsNeighbourPortPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 3),
    _WsNeighbourPortPIndex_Type()
)
wsNeighbourPortPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPIndex.setStatus("current")
_WsNeighbourPortName_Type = DisplayString
_WsNeighbourPortName_Object = MibTableColumn
wsNeighbourPortName = _WsNeighbourPortName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 4),
    _WsNeighbourPortName_Type()
)
wsNeighbourPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortName.setStatus("current")


class _WsNeighbourPortState_Type(Bits):
    """Custom type wsNeighbourPortState based on Bits"""
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("vlaninfo", 4),
          ("s100mbit", 5),
          ("fullduplex", 6),
          ("up", 7))
    )

_WsNeighbourPortState_Type.__name__ = "Bits"
_WsNeighbourPortState_Object = MibTableColumn
wsNeighbourPortState = _WsNeighbourPortState_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 5),
    _WsNeighbourPortState_Type()
)
wsNeighbourPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortState.setStatus("current")
_WsNeighbourPortTxOctets_Type = Counter64
_WsNeighbourPortTxOctets_Object = MibTableColumn
wsNeighbourPortTxOctets = _WsNeighbourPortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 6),
    _WsNeighbourPortTxOctets_Type()
)
wsNeighbourPortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxOctets.setStatus("current")
_WsNeighbourPortTxDropPkts_Type = Unsigned32
_WsNeighbourPortTxDropPkts_Object = MibTableColumn
wsNeighbourPortTxDropPkts = _WsNeighbourPortTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 7),
    _WsNeighbourPortTxDropPkts_Type()
)
wsNeighbourPortTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxDropPkts.setStatus("current")
_WsNeighbourPortTxBroadcastPkts_Type = Unsigned32
_WsNeighbourPortTxBroadcastPkts_Object = MibTableColumn
wsNeighbourPortTxBroadcastPkts = _WsNeighbourPortTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 8),
    _WsNeighbourPortTxBroadcastPkts_Type()
)
wsNeighbourPortTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxBroadcastPkts.setStatus("current")
_WsNeighbourPortTxMulticastPkts_Type = Unsigned32
_WsNeighbourPortTxMulticastPkts_Object = MibTableColumn
wsNeighbourPortTxMulticastPkts = _WsNeighbourPortTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 9),
    _WsNeighbourPortTxMulticastPkts_Type()
)
wsNeighbourPortTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxMulticastPkts.setStatus("current")
_WsNeighbourPortTxUnicastPkts_Type = Unsigned32
_WsNeighbourPortTxUnicastPkts_Object = MibTableColumn
wsNeighbourPortTxUnicastPkts = _WsNeighbourPortTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 10),
    _WsNeighbourPortTxUnicastPkts_Type()
)
wsNeighbourPortTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxUnicastPkts.setStatus("current")
_WsNeighbourPortTxCollisions_Type = Unsigned32
_WsNeighbourPortTxCollisions_Object = MibTableColumn
wsNeighbourPortTxCollisions = _WsNeighbourPortTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 11),
    _WsNeighbourPortTxCollisions_Type()
)
wsNeighbourPortTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxCollisions.setStatus("current")
_WsNeighbourPortTxDeferredTransmit_Type = Unsigned32
_WsNeighbourPortTxDeferredTransmit_Object = MibTableColumn
wsNeighbourPortTxDeferredTransmit = _WsNeighbourPortTxDeferredTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 12),
    _WsNeighbourPortTxDeferredTransmit_Type()
)
wsNeighbourPortTxDeferredTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxDeferredTransmit.setStatus("current")
_WsNeighbourPortTxFrameInDisc_Type = Unsigned32
_WsNeighbourPortTxFrameInDisc_Object = MibTableColumn
wsNeighbourPortTxFrameInDisc = _WsNeighbourPortTxFrameInDisc_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 13),
    _WsNeighbourPortTxFrameInDisc_Type()
)
wsNeighbourPortTxFrameInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortTxFrameInDisc.setStatus("current")
_WsNeighbourPortRxOctets_Type = Counter64
_WsNeighbourPortRxOctets_Object = MibTableColumn
wsNeighbourPortRxOctets = _WsNeighbourPortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 14),
    _WsNeighbourPortRxOctets_Type()
)
wsNeighbourPortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxOctets.setStatus("current")
_WsNeighbourPortRxUndersizePkts_Type = Unsigned32
_WsNeighbourPortRxUndersizePkts_Object = MibTableColumn
wsNeighbourPortRxUndersizePkts = _WsNeighbourPortRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 15),
    _WsNeighbourPortRxUndersizePkts_Type()
)
wsNeighbourPortRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxUndersizePkts.setStatus("current")
_WsNeighbourPortPkts64Octets_Type = Unsigned32
_WsNeighbourPortPkts64Octets_Object = MibTableColumn
wsNeighbourPortPkts64Octets = _WsNeighbourPortPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 16),
    _WsNeighbourPortPkts64Octets_Type()
)
wsNeighbourPortPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts64Octets.setStatus("current")
_WsNeighbourPortPkts65to127Octets_Type = Unsigned32
_WsNeighbourPortPkts65to127Octets_Object = MibTableColumn
wsNeighbourPortPkts65to127Octets = _WsNeighbourPortPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 17),
    _WsNeighbourPortPkts65to127Octets_Type()
)
wsNeighbourPortPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts65to127Octets.setStatus("current")
_WsNeighbourPortPkts128to255Octets_Type = Unsigned32
_WsNeighbourPortPkts128to255Octets_Object = MibTableColumn
wsNeighbourPortPkts128to255Octets = _WsNeighbourPortPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 18),
    _WsNeighbourPortPkts128to255Octets_Type()
)
wsNeighbourPortPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts128to255Octets.setStatus("current")
_WsNeighbourPortPkts256to511Octets_Type = Unsigned32
_WsNeighbourPortPkts256to511Octets_Object = MibTableColumn
wsNeighbourPortPkts256to511Octets = _WsNeighbourPortPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 19),
    _WsNeighbourPortPkts256to511Octets_Type()
)
wsNeighbourPortPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts256to511Octets.setStatus("current")
_WsNeighbourPortPkts512to1023Octets_Type = Unsigned32
_WsNeighbourPortPkts512to1023Octets_Object = MibTableColumn
wsNeighbourPortPkts512to1023Octets = _WsNeighbourPortPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 20),
    _WsNeighbourPortPkts512to1023Octets_Type()
)
wsNeighbourPortPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts512to1023Octets.setStatus("current")
_WsNeighbourPortPkts1024to1522Octets_Type = Unsigned32
_WsNeighbourPortPkts1024to1522Octets_Object = MibTableColumn
wsNeighbourPortPkts1024to1522Octets = _WsNeighbourPortPkts1024to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 21),
    _WsNeighbourPortPkts1024to1522Octets_Type()
)
wsNeighbourPortPkts1024to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortPkts1024to1522Octets.setStatus("current")
_WsNeighbourPortRxOversizePkts_Type = Unsigned32
_WsNeighbourPortRxOversizePkts_Object = MibTableColumn
wsNeighbourPortRxOversizePkts = _WsNeighbourPortRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 22),
    _WsNeighbourPortRxOversizePkts_Type()
)
wsNeighbourPortRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxOversizePkts.setStatus("current")
_WsNeighbourPortRxJabbers_Type = Unsigned32
_WsNeighbourPortRxJabbers_Object = MibTableColumn
wsNeighbourPortRxJabbers = _WsNeighbourPortRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 23),
    _WsNeighbourPortRxJabbers_Type()
)
wsNeighbourPortRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxJabbers.setStatus("current")
_WsNeighbourPortRxAlignmentErrors_Type = Unsigned32
_WsNeighbourPortRxAlignmentErrors_Object = MibTableColumn
wsNeighbourPortRxAlignmentErrors = _WsNeighbourPortRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 24),
    _WsNeighbourPortRxAlignmentErrors_Type()
)
wsNeighbourPortRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxAlignmentErrors.setStatus("current")
_WsNeighbourPortRxFCSErrors_Type = Unsigned32
_WsNeighbourPortRxFCSErrors_Object = MibTableColumn
wsNeighbourPortRxFCSErrors = _WsNeighbourPortRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 25),
    _WsNeighbourPortRxFCSErrors_Type()
)
wsNeighbourPortRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxFCSErrors.setStatus("current")
_WsNeighbourPortRxGoodOctets_Type = Counter64
_WsNeighbourPortRxGoodOctets_Object = MibTableColumn
wsNeighbourPortRxGoodOctets = _WsNeighbourPortRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 26),
    _WsNeighbourPortRxGoodOctets_Type()
)
wsNeighbourPortRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxGoodOctets.setStatus("current")
_WsNeighbourPortRxDropPkts_Type = Unsigned32
_WsNeighbourPortRxDropPkts_Object = MibTableColumn
wsNeighbourPortRxDropPkts = _WsNeighbourPortRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 27),
    _WsNeighbourPortRxDropPkts_Type()
)
wsNeighbourPortRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxDropPkts.setStatus("current")
_WsNeighbourPortRxUnicastPkts_Type = Unsigned32
_WsNeighbourPortRxUnicastPkts_Object = MibTableColumn
wsNeighbourPortRxUnicastPkts = _WsNeighbourPortRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 28),
    _WsNeighbourPortRxUnicastPkts_Type()
)
wsNeighbourPortRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxUnicastPkts.setStatus("current")
_WsNeighbourPortRxMulticastPkts_Type = Unsigned32
_WsNeighbourPortRxMulticastPkts_Object = MibTableColumn
wsNeighbourPortRxMulticastPkts = _WsNeighbourPortRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 29),
    _WsNeighbourPortRxMulticastPkts_Type()
)
wsNeighbourPortRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxMulticastPkts.setStatus("current")
_WsNeighbourPortRxBroadcastPkts_Type = Unsigned32
_WsNeighbourPortRxBroadcastPkts_Object = MibTableColumn
wsNeighbourPortRxBroadcastPkts = _WsNeighbourPortRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 30),
    _WsNeighbourPortRxBroadcastPkts_Type()
)
wsNeighbourPortRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxBroadcastPkts.setStatus("current")
_WsNeighbourPortRxFragments_Type = Unsigned32
_WsNeighbourPortRxFragments_Object = MibTableColumn
wsNeighbourPortRxFragments = _WsNeighbourPortRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 31),
    _WsNeighbourPortRxFragments_Type()
)
wsNeighbourPortRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxFragments.setStatus("current")
_WsNeighbourPortRxExcessSizeDisc_Type = Unsigned32
_WsNeighbourPortRxExcessSizeDisc_Object = MibTableColumn
wsNeighbourPortRxExcessSizeDisc = _WsNeighbourPortRxExcessSizeDisc_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 32),
    _WsNeighbourPortRxExcessSizeDisc_Type()
)
wsNeighbourPortRxExcessSizeDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxExcessSizeDisc.setStatus("current")
_WsNeighbourPortRxSymbolError_Type = Unsigned32
_WsNeighbourPortRxSymbolError_Object = MibTableColumn
wsNeighbourPortRxSymbolError = _WsNeighbourPortRxSymbolError_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 2, 1, 33),
    _WsNeighbourPortRxSymbolError_Type()
)
wsNeighbourPortRxSymbolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortRxSymbolError.setStatus("current")
_WsNeighbourPortSNPATable_Object = MibTable
wsNeighbourPortSNPATable = _WsNeighbourPortSNPATable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wsNeighbourPortSNPATable.setStatus("current")
_WsNeighbourPortSNPAEntry_Object = MibTableRow
wsNeighbourPortSNPAEntry = _WsNeighbourPortSNPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1)
)
wsNeighbourPortSNPAEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsNeighbourPortSNPAIfIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourPortSNPANIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourPortSNPAPIndex"),
    (0, "WAYSTREAM-MIB", "wsNeighbourPortSNPASIndex"),
)
if mibBuilder.loadTexts:
    wsNeighbourPortSNPAEntry.setStatus("current")
_WsNeighbourPortSNPAIfIndex_Type = Unsigned32
_WsNeighbourPortSNPAIfIndex_Object = MibTableColumn
wsNeighbourPortSNPAIfIndex = _WsNeighbourPortSNPAIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 1),
    _WsNeighbourPortSNPAIfIndex_Type()
)
wsNeighbourPortSNPAIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPAIfIndex.setStatus("current")
_WsNeighbourPortSNPANIndex_Type = Unsigned32
_WsNeighbourPortSNPANIndex_Object = MibTableColumn
wsNeighbourPortSNPANIndex = _WsNeighbourPortSNPANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 2),
    _WsNeighbourPortSNPANIndex_Type()
)
wsNeighbourPortSNPANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPANIndex.setStatus("current")
_WsNeighbourPortSNPAPIndex_Type = Unsigned32
_WsNeighbourPortSNPAPIndex_Object = MibTableColumn
wsNeighbourPortSNPAPIndex = _WsNeighbourPortSNPAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 3),
    _WsNeighbourPortSNPAPIndex_Type()
)
wsNeighbourPortSNPAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPAPIndex.setStatus("current")
_WsNeighbourPortSNPASIndex_Type = Unsigned32
_WsNeighbourPortSNPASIndex_Object = MibTableColumn
wsNeighbourPortSNPASIndex = _WsNeighbourPortSNPASIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 4),
    _WsNeighbourPortSNPASIndex_Type()
)
wsNeighbourPortSNPASIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPASIndex.setStatus("current")
_WsNeighbourPortSNPASMCast_Type = Integer32
_WsNeighbourPortSNPASMCast_Object = MibTableColumn
wsNeighbourPortSNPASMCast = _WsNeighbourPortSNPASMCast_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 5),
    _WsNeighbourPortSNPASMCast_Type()
)
wsNeighbourPortSNPASMCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPASMCast.setStatus("current")
_WsNeighbourPortSNPA_Type = OctetString
_WsNeighbourPortSNPA_Object = MibTableColumn
wsNeighbourPortSNPA = _WsNeighbourPortSNPA_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 3, 3, 1, 6),
    _WsNeighbourPortSNPA_Type()
)
wsNeighbourPortSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNeighbourPortSNPA.setStatus("current")
_WsSFPTable_Object = MibTable
wsSFPTable = _WsSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4)
)
if mibBuilder.loadTexts:
    wsSFPTable.setStatus("current")
_WsSFPEntry_Object = MibTableRow
wsSFPEntry = _WsSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1)
)
wsSFPEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsSFPIndex"),
)
if mibBuilder.loadTexts:
    wsSFPEntry.setStatus("current")
_WsSFPIndex_Type = Unsigned32
_WsSFPIndex_Object = MibTableColumn
wsSFPIndex = _WsSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 1),
    _WsSFPIndex_Type()
)
wsSFPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPIndex.setStatus("current")


class _WsSFPStatus_Type(Integer32):
    """Custom type wsSFPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("missing", 1),
          ("invalid", 2))
    )


_WsSFPStatus_Type.__name__ = "Integer32"
_WsSFPStatus_Object = MibTableColumn
wsSFPStatus = _WsSFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 2),
    _WsSFPStatus_Type()
)
wsSFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPStatus.setStatus("current")


class _WsSFPConnector_Type(Integer32):
    """Custom type wsSFPConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              10,
              11,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("sc", 1),
          ("fiberJack", 6),
          ("lc", 7),
          ("mtrj", 8),
          ("mu", 9),
          ("sg", 10),
          ("opticalPigtail", 11),
          ("hssdcii", 32),
          ("copperPigtail", 33))
    )


_WsSFPConnector_Type.__name__ = "Integer32"
_WsSFPConnector_Object = MibTableColumn
wsSFPConnector = _WsSFPConnector_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 3),
    _WsSFPConnector_Type()
)
wsSFPConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPConnector.setStatus("current")


class _WsSFPTransceiver_Type(Bits):
    """Custom type wsSFPTransceiver based on Bits"""
    namedValues = NamedValues(
        *(("sBasePX", 0),
          ("sBaseBX10", 1),
          ("s100BaseFX", 2),
          ("s100BaseLX", 3),
          ("s1000BaseT", 4),
          ("s1000BaseCX", 5),
          ("s1000BaseLX", 6),
          ("s1000BaseSX", 7))
    )

_WsSFPTransceiver_Type.__name__ = "Bits"
_WsSFPTransceiver_Object = MibTableColumn
wsSFPTransceiver = _WsSFPTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 4),
    _WsSFPTransceiver_Type()
)
wsSFPTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTransceiver.setStatus("current")


class _WsSFPEncoding_Type(Integer32):
    """Custom type wsSFPEncoding based on Integer32"""
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
        *(("e8B10B", 1),
          ("e4B5B", 2),
          ("eNRZ", 3),
          ("eManchester", 4))
    )


_WsSFPEncoding_Type.__name__ = "Integer32"
_WsSFPEncoding_Object = MibTableColumn
wsSFPEncoding = _WsSFPEncoding_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 5),
    _WsSFPEncoding_Type()
)
wsSFPEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPEncoding.setStatus("current")
_WsSFPBitrate_Type = Unsigned32
_WsSFPBitrate_Object = MibTableColumn
wsSFPBitrate = _WsSFPBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 6),
    _WsSFPBitrate_Type()
)
wsSFPBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPBitrate.setStatus("current")
_WsSFPSingleModeLen_Type = Unsigned32
_WsSFPSingleModeLen_Object = MibTableColumn
wsSFPSingleModeLen = _WsSFPSingleModeLen_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 7),
    _WsSFPSingleModeLen_Type()
)
wsSFPSingleModeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPSingleModeLen.setStatus("current")
_WsSFPMultiMode50Len_Type = Unsigned32
_WsSFPMultiMode50Len_Object = MibTableColumn
wsSFPMultiMode50Len = _WsSFPMultiMode50Len_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 8),
    _WsSFPMultiMode50Len_Type()
)
wsSFPMultiMode50Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPMultiMode50Len.setStatus("current")
_WsSFPMultiMode625Len_Type = Unsigned32
_WsSFPMultiMode625Len_Object = MibTableColumn
wsSFPMultiMode625Len = _WsSFPMultiMode625Len_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 9),
    _WsSFPMultiMode625Len_Type()
)
wsSFPMultiMode625Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPMultiMode625Len.setStatus("current")
_WsSFPCopperLen_Type = Unsigned32
_WsSFPCopperLen_Object = MibTableColumn
wsSFPCopperLen = _WsSFPCopperLen_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 10),
    _WsSFPCopperLen_Type()
)
wsSFPCopperLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPCopperLen.setStatus("current")


class _WsSFPTempStatus_Type(Integer32):
    """Custom type wsSFPTempStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsSFPTempStatus_Type.__name__ = "Integer32"
_WsSFPTempStatus_Object = MibTableColumn
wsSFPTempStatus = _WsSFPTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 11),
    _WsSFPTempStatus_Type()
)
wsSFPTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTempStatus.setStatus("current")
_WsSFPTemp_Type = Integer32
_WsSFPTemp_Object = MibTableColumn
wsSFPTemp = _WsSFPTemp_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 12),
    _WsSFPTemp_Type()
)
wsSFPTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTemp.setStatus("current")


class _WsSFPVoltStatus_Type(Integer32):
    """Custom type wsSFPVoltStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsSFPVoltStatus_Type.__name__ = "Integer32"
_WsSFPVoltStatus_Object = MibTableColumn
wsSFPVoltStatus = _WsSFPVoltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 13),
    _WsSFPVoltStatus_Type()
)
wsSFPVoltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVoltStatus.setStatus("current")
_WsSFPVolt_Type = Integer32
_WsSFPVolt_Object = MibTableColumn
wsSFPVolt = _WsSFPVolt_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 14),
    _WsSFPVolt_Type()
)
wsSFPVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVolt.setStatus("current")


class _WsSFPTXCurrentStatus_Type(Integer32):
    """Custom type wsSFPTXCurrentStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsSFPTXCurrentStatus_Type.__name__ = "Integer32"
_WsSFPTXCurrentStatus_Object = MibTableColumn
wsSFPTXCurrentStatus = _WsSFPTXCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 15),
    _WsSFPTXCurrentStatus_Type()
)
wsSFPTXCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrentStatus.setStatus("current")
_WsSFPTXCurrent_Type = Integer32
_WsSFPTXCurrent_Object = MibTableColumn
wsSFPTXCurrent = _WsSFPTXCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 16),
    _WsSFPTXCurrent_Type()
)
wsSFPTXCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrent.setStatus("current")


class _WsSFPTXPowerStatus_Type(Integer32):
    """Custom type wsSFPTXPowerStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsSFPTXPowerStatus_Type.__name__ = "Integer32"
_WsSFPTXPowerStatus_Object = MibTableColumn
wsSFPTXPowerStatus = _WsSFPTXPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 17),
    _WsSFPTXPowerStatus_Type()
)
wsSFPTXPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXPowerStatus.setStatus("current")
_WsSFPTXPower_Type = Integer32
_WsSFPTXPower_Object = MibTableColumn
wsSFPTXPower = _WsSFPTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 18),
    _WsSFPTXPower_Type()
)
wsSFPTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXPower.setStatus("current")


class _WsSFPRXPowerStatus_Type(Integer32):
    """Custom type wsSFPRXPowerStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsSFPRXPowerStatus_Type.__name__ = "Integer32"
_WsSFPRXPowerStatus_Object = MibTableColumn
wsSFPRXPowerStatus = _WsSFPRXPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 19),
    _WsSFPRXPowerStatus_Type()
)
wsSFPRXPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXPowerStatus.setStatus("current")
_WsSFPRXPower_Type = Integer32
_WsSFPRXPower_Object = MibTableColumn
wsSFPRXPower = _WsSFPRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 20),
    _WsSFPRXPower_Type()
)
wsSFPRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXPower.setStatus("current")


class _WsSFPTransceiverExt_Type(Bits):
    """Custom type wsSFPTransceiverExt based on Bits"""
    namedValues = NamedValues(
        *(("s10000BaseER", 0),
          ("s10000BaseLRM", 1),
          ("s10000BaseLR", 2),
          ("s10000BaseSR", 3),
          ("sActiveCable", 4),
          ("sPassiveCable", 5),
          ("reserved6", 6),
          ("reserved7", 7))
    )

_WsSFPTransceiverExt_Type.__name__ = "Bits"
_WsSFPTransceiverExt_Object = MibTableColumn
wsSFPTransceiverExt = _WsSFPTransceiverExt_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 21),
    _WsSFPTransceiverExt_Type()
)
wsSFPTransceiverExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTransceiverExt.setStatus("current")
_WsSFPTXdBmPower_Type = Integer32
_WsSFPTXdBmPower_Object = MibTableColumn
wsSFPTXdBmPower = _WsSFPTXdBmPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 22),
    _WsSFPTXdBmPower_Type()
)
wsSFPTXdBmPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXdBmPower.setStatus("current")
_WsSFPRXdBmPower_Type = Integer32
_WsSFPRXdBmPower_Object = MibTableColumn
wsSFPRXdBmPower = _WsSFPRXdBmPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 23),
    _WsSFPRXdBmPower_Type()
)
wsSFPRXdBmPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXdBmPower.setStatus("current")
_WsSFPTempNormalLow_Type = Integer32
_WsSFPTempNormalLow_Object = MibTableColumn
wsSFPTempNormalLow = _WsSFPTempNormalLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 24),
    _WsSFPTempNormalLow_Type()
)
wsSFPTempNormalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTempNormalLow.setStatus("current")
_WsSFPTempNormalHigh_Type = Integer32
_WsSFPTempNormalHigh_Object = MibTableColumn
wsSFPTempNormalHigh = _WsSFPTempNormalHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 25),
    _WsSFPTempNormalHigh_Type()
)
wsSFPTempNormalHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTempNormalHigh.setStatus("current")
_WsSFPTempWarningLow_Type = Integer32
_WsSFPTempWarningLow_Object = MibTableColumn
wsSFPTempWarningLow = _WsSFPTempWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 26),
    _WsSFPTempWarningLow_Type()
)
wsSFPTempWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTempWarningLow.setStatus("current")
_WsSFPTempWarningHigh_Type = Integer32
_WsSFPTempWarningHigh_Object = MibTableColumn
wsSFPTempWarningHigh = _WsSFPTempWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 27),
    _WsSFPTempWarningHigh_Type()
)
wsSFPTempWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTempWarningHigh.setStatus("current")
_WsSFPVoltNormalLow_Type = Integer32
_WsSFPVoltNormalLow_Object = MibTableColumn
wsSFPVoltNormalLow = _WsSFPVoltNormalLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 28),
    _WsSFPVoltNormalLow_Type()
)
wsSFPVoltNormalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVoltNormalLow.setStatus("current")
_WsSFPVoltNormalHigh_Type = Integer32
_WsSFPVoltNormalHigh_Object = MibTableColumn
wsSFPVoltNormalHigh = _WsSFPVoltNormalHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 29),
    _WsSFPVoltNormalHigh_Type()
)
wsSFPVoltNormalHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVoltNormalHigh.setStatus("current")
_WsSFPVoltWarningLow_Type = Integer32
_WsSFPVoltWarningLow_Object = MibTableColumn
wsSFPVoltWarningLow = _WsSFPVoltWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 30),
    _WsSFPVoltWarningLow_Type()
)
wsSFPVoltWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVoltWarningLow.setStatus("current")
_WsSFPVoltWarningHigh_Type = Integer32
_WsSFPVoltWarningHigh_Object = MibTableColumn
wsSFPVoltWarningHigh = _WsSFPVoltWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 31),
    _WsSFPVoltWarningHigh_Type()
)
wsSFPVoltWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPVoltWarningHigh.setStatus("current")
_WsSFPTXCurrentNormalLow_Type = Integer32
_WsSFPTXCurrentNormalLow_Object = MibTableColumn
wsSFPTXCurrentNormalLow = _WsSFPTXCurrentNormalLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 32),
    _WsSFPTXCurrentNormalLow_Type()
)
wsSFPTXCurrentNormalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrentNormalLow.setStatus("current")
_WsSFPTXCurrentNormalHigh_Type = Integer32
_WsSFPTXCurrentNormalHigh_Object = MibTableColumn
wsSFPTXCurrentNormalHigh = _WsSFPTXCurrentNormalHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 33),
    _WsSFPTXCurrentNormalHigh_Type()
)
wsSFPTXCurrentNormalHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrentNormalHigh.setStatus("current")
_WsSFPTXCurrentWarningLow_Type = Integer32
_WsSFPTXCurrentWarningLow_Object = MibTableColumn
wsSFPTXCurrentWarningLow = _WsSFPTXCurrentWarningLow_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 34),
    _WsSFPTXCurrentWarningLow_Type()
)
wsSFPTXCurrentWarningLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrentWarningLow.setStatus("current")
_WsSFPTXCurrentWarningHigh_Type = Integer32
_WsSFPTXCurrentWarningHigh_Object = MibTableColumn
wsSFPTXCurrentWarningHigh = _WsSFPTXCurrentWarningHigh_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 35),
    _WsSFPTXCurrentWarningHigh_Type()
)
wsSFPTXCurrentWarningHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXCurrentWarningHigh.setStatus("current")
_WsSFPTXOutputPowNormalLowuW_Type = Integer32
_WsSFPTXOutputPowNormalLowuW_Object = MibTableColumn
wsSFPTXOutputPowNormalLowuW = _WsSFPTXOutputPowNormalLowuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 36),
    _WsSFPTXOutputPowNormalLowuW_Type()
)
wsSFPTXOutputPowNormalLowuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowNormalLowuW.setStatus("current")
_WsSFPTXOutputPowNormalHighuW_Type = Integer32
_WsSFPTXOutputPowNormalHighuW_Object = MibTableColumn
wsSFPTXOutputPowNormalHighuW = _WsSFPTXOutputPowNormalHighuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 37),
    _WsSFPTXOutputPowNormalHighuW_Type()
)
wsSFPTXOutputPowNormalHighuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowNormalHighuW.setStatus("current")
_WsSFPTXOutputPowWarningLowuW_Type = Integer32
_WsSFPTXOutputPowWarningLowuW_Object = MibTableColumn
wsSFPTXOutputPowWarningLowuW = _WsSFPTXOutputPowWarningLowuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 38),
    _WsSFPTXOutputPowWarningLowuW_Type()
)
wsSFPTXOutputPowWarningLowuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowWarningLowuW.setStatus("current")
_WsSFPTXOutputPowWarningHighuW_Type = Integer32
_WsSFPTXOutputPowWarningHighuW_Object = MibTableColumn
wsSFPTXOutputPowWarningHighuW = _WsSFPTXOutputPowWarningHighuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 39),
    _WsSFPTXOutputPowWarningHighuW_Type()
)
wsSFPTXOutputPowWarningHighuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowWarningHighuW.setStatus("current")
_WsSFPTXOutputPowNormalLowdBm_Type = Integer32
_WsSFPTXOutputPowNormalLowdBm_Object = MibTableColumn
wsSFPTXOutputPowNormalLowdBm = _WsSFPTXOutputPowNormalLowdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 40),
    _WsSFPTXOutputPowNormalLowdBm_Type()
)
wsSFPTXOutputPowNormalLowdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowNormalLowdBm.setStatus("current")
_WsSFPTXOutputPowNormalHighdBm_Type = Integer32
_WsSFPTXOutputPowNormalHighdBm_Object = MibTableColumn
wsSFPTXOutputPowNormalHighdBm = _WsSFPTXOutputPowNormalHighdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 41),
    _WsSFPTXOutputPowNormalHighdBm_Type()
)
wsSFPTXOutputPowNormalHighdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowNormalHighdBm.setStatus("current")
_WsSFPTXOutputPowWarningLowdBm_Type = Integer32
_WsSFPTXOutputPowWarningLowdBm_Object = MibTableColumn
wsSFPTXOutputPowWarningLowdBm = _WsSFPTXOutputPowWarningLowdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 42),
    _WsSFPTXOutputPowWarningLowdBm_Type()
)
wsSFPTXOutputPowWarningLowdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowWarningLowdBm.setStatus("current")
_WsSFPTXOutputPowWarningHighdBm_Type = Integer32
_WsSFPTXOutputPowWarningHighdBm_Object = MibTableColumn
wsSFPTXOutputPowWarningHighdBm = _WsSFPTXOutputPowWarningHighdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 43),
    _WsSFPTXOutputPowWarningHighdBm_Type()
)
wsSFPTXOutputPowWarningHighdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPTXOutputPowWarningHighdBm.setStatus("current")
_WsSFPRXInputPowNormalLowuW_Type = Integer32
_WsSFPRXInputPowNormalLowuW_Object = MibTableColumn
wsSFPRXInputPowNormalLowuW = _WsSFPRXInputPowNormalLowuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 44),
    _WsSFPRXInputPowNormalLowuW_Type()
)
wsSFPRXInputPowNormalLowuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowNormalLowuW.setStatus("current")
_WsSFPRXInputPowNormalHighuW_Type = Integer32
_WsSFPRXInputPowNormalHighuW_Object = MibTableColumn
wsSFPRXInputPowNormalHighuW = _WsSFPRXInputPowNormalHighuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 45),
    _WsSFPRXInputPowNormalHighuW_Type()
)
wsSFPRXInputPowNormalHighuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowNormalHighuW.setStatus("current")
_WsSFPRXInputPowWarningLowuW_Type = Integer32
_WsSFPRXInputPowWarningLowuW_Object = MibTableColumn
wsSFPRXInputPowWarningLowuW = _WsSFPRXInputPowWarningLowuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 46),
    _WsSFPRXInputPowWarningLowuW_Type()
)
wsSFPRXInputPowWarningLowuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowWarningLowuW.setStatus("current")
_WsSFPRXInputPowWarningHighuW_Type = Integer32
_WsSFPRXInputPowWarningHighuW_Object = MibTableColumn
wsSFPRXInputPowWarningHighuW = _WsSFPRXInputPowWarningHighuW_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 47),
    _WsSFPRXInputPowWarningHighuW_Type()
)
wsSFPRXInputPowWarningHighuW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowWarningHighuW.setStatus("current")
_WsSFPRXInputPowNormalLowdBm_Type = Integer32
_WsSFPRXInputPowNormalLowdBm_Object = MibTableColumn
wsSFPRXInputPowNormalLowdBm = _WsSFPRXInputPowNormalLowdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 48),
    _WsSFPRXInputPowNormalLowdBm_Type()
)
wsSFPRXInputPowNormalLowdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowNormalLowdBm.setStatus("current")
_WsSFPRXInputPowNormalHighdBm_Type = Integer32
_WsSFPRXInputPowNormalHighdBm_Object = MibTableColumn
wsSFPRXInputPowNormalHighdBm = _WsSFPRXInputPowNormalHighdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 49),
    _WsSFPRXInputPowNormalHighdBm_Type()
)
wsSFPRXInputPowNormalHighdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowNormalHighdBm.setStatus("current")
_WsSFPRXInputPowWarningLowdBm_Type = Integer32
_WsSFPRXInputPowWarningLowdBm_Object = MibTableColumn
wsSFPRXInputPowWarningLowdBm = _WsSFPRXInputPowWarningLowdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 50),
    _WsSFPRXInputPowWarningLowdBm_Type()
)
wsSFPRXInputPowWarningLowdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowWarningLowdBm.setStatus("current")
_WsSFPRXInputPowWarningHighdBm_Type = Integer32
_WsSFPRXInputPowWarningHighdBm_Object = MibTableColumn
wsSFPRXInputPowWarningHighdBm = _WsSFPRXInputPowWarningHighdBm_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 51),
    _WsSFPRXInputPowWarningHighdBm_Type()
)
wsSFPRXInputPowWarningHighdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPRXInputPowWarningHighdBm.setStatus("current")


class _WsSFPPartNumber_Type(DisplayString):
    """Custom type wsSFPPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsSFPPartNumber_Type.__name__ = "DisplayString"
_WsSFPPartNumber_Object = MibTableColumn
wsSFPPartNumber = _WsSFPPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 52),
    _WsSFPPartNumber_Type()
)
wsSFPPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPPartNumber.setStatus("current")


class _WsSFPSerialNumber_Type(DisplayString):
    """Custom type wsSFPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WsSFPSerialNumber_Type.__name__ = "DisplayString"
_WsSFPSerialNumber_Object = MibTableColumn
wsSFPSerialNumber = _WsSFPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 4, 1, 53),
    _WsSFPSerialNumber_Type()
)
wsSFPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSFPSerialNumber.setStatus("current")
_WsAccounting_ObjectIdentity = ObjectIdentity
wsAccounting = _WsAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5)
)
if mibBuilder.loadTexts:
    wsAccounting.setStatus("current")
_WsPolicyTable_Object = MibTable
wsPolicyTable = _WsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wsPolicyTable.setStatus("current")
_WsPolicyEntry_Object = MibTableRow
wsPolicyEntry = _WsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1)
)
wsPolicyEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsPolicyIfIndex"),
    (0, "WAYSTREAM-MIB", "wsPolicyName"),
)
if mibBuilder.loadTexts:
    wsPolicyEntry.setStatus("current")
_WsPolicyIfIndex_Type = Unsigned32
_WsPolicyIfIndex_Object = MibTableColumn
wsPolicyIfIndex = _WsPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 1),
    _WsPolicyIfIndex_Type()
)
wsPolicyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyIfIndex.setStatus("current")
_WsPolicyIfName_Type = DisplayString
_WsPolicyIfName_Object = MibTableColumn
wsPolicyIfName = _WsPolicyIfName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 2),
    _WsPolicyIfName_Type()
)
wsPolicyIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyIfName.setStatus("current")
_WsPolicyName_Type = DisplayString
_WsPolicyName_Object = MibTableColumn
wsPolicyName = _WsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 3),
    _WsPolicyName_Type()
)
wsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyName.setStatus("current")
_WsPolicyCookie_Type = DisplayString
_WsPolicyCookie_Object = MibTableColumn
wsPolicyCookie = _WsPolicyCookie_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 4),
    _WsPolicyCookie_Type()
)
wsPolicyCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyCookie.setStatus("current")
_WsPolicyInPkts_Type = Counter64
_WsPolicyInPkts_Object = MibTableColumn
wsPolicyInPkts = _WsPolicyInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 5),
    _WsPolicyInPkts_Type()
)
wsPolicyInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyInPkts.setStatus("current")
_WsPolicyInBytes_Type = Counter64
_WsPolicyInBytes_Object = MibTableColumn
wsPolicyInBytes = _WsPolicyInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 6),
    _WsPolicyInBytes_Type()
)
wsPolicyInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyInBytes.setStatus("current")
_WsPolicyInDrops_Type = Counter64
_WsPolicyInDrops_Object = MibTableColumn
wsPolicyInDrops = _WsPolicyInDrops_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 7),
    _WsPolicyInDrops_Type()
)
wsPolicyInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyInDrops.setStatus("current")
_WsPolicyOutPkts_Type = Counter64
_WsPolicyOutPkts_Object = MibTableColumn
wsPolicyOutPkts = _WsPolicyOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 8),
    _WsPolicyOutPkts_Type()
)
wsPolicyOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyOutPkts.setStatus("current")
_WsPolicyOutBytes_Type = Counter64
_WsPolicyOutBytes_Object = MibTableColumn
wsPolicyOutBytes = _WsPolicyOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 9),
    _WsPolicyOutBytes_Type()
)
wsPolicyOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyOutBytes.setStatus("current")
_WsPolicyOutDrops_Type = Counter64
_WsPolicyOutDrops_Object = MibTableColumn
wsPolicyOutDrops = _WsPolicyOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 10),
    _WsPolicyOutDrops_Type()
)
wsPolicyOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyOutDrops.setStatus("current")
_WsPolicyUsedCnt_Type = Gauge32
_WsPolicyUsedCnt_Object = MibTableColumn
wsPolicyUsedCnt = _WsPolicyUsedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 5, 1, 1, 11),
    _WsPolicyUsedCnt_Type()
)
wsPolicyUsedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPolicyUsedCnt.setStatus("current")
_WsXFPTable_Object = MibTable
wsXFPTable = _WsXFPTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6)
)
if mibBuilder.loadTexts:
    wsXFPTable.setStatus("current")
_WsXFPEntry_Object = MibTableRow
wsXFPEntry = _WsXFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1)
)
wsXFPEntry.setIndexNames(
    (0, "WAYSTREAM-MIB", "wsXFPIndex"),
)
if mibBuilder.loadTexts:
    wsXFPEntry.setStatus("current")
_WsXFPIndex_Type = Unsigned32
_WsXFPIndex_Object = MibTableColumn
wsXFPIndex = _WsXFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 1),
    _WsXFPIndex_Type()
)
wsXFPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPIndex.setStatus("current")


class _WsXFPStatus_Type(Integer32):
    """Custom type wsXFPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("missing", 1),
          ("invalid", 2))
    )


_WsXFPStatus_Type.__name__ = "Integer32"
_WsXFPStatus_Object = MibTableColumn
wsXFPStatus = _WsXFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 2),
    _WsXFPStatus_Type()
)
wsXFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPStatus.setStatus("current")


class _WsXFPConnector_Type(Integer32):
    """Custom type wsXFPConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              9,
              10,
              11,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("sc", 1),
          ("fiberJack", 6),
          ("lc", 7),
          ("mtrj", 8),
          ("mu", 9),
          ("sg", 10),
          ("opticalPigtail", 11),
          ("hssdcii", 32),
          ("copperPigtail", 33))
    )


_WsXFPConnector_Type.__name__ = "Integer32"
_WsXFPConnector_Object = MibTableColumn
wsXFPConnector = _WsXFPConnector_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 3),
    _WsXFPConnector_Type()
)
wsXFPConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPConnector.setStatus("current")


class _WsXFPTransceiver_Type(Bits):
    """Custom type wsXFPTransceiver based on Bits"""
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("s10GBaseEW", 1),
          ("s10GBaseLW", 2),
          ("s10GBaseSW", 3),
          ("s10GBaseLRM", 4),
          ("s10GBaseER", 5),
          ("s10GBaseLR", 6),
          ("s10GBaseSR", 7))
    )

_WsXFPTransceiver_Type.__name__ = "Bits"
_WsXFPTransceiver_Object = MibTableColumn
wsXFPTransceiver = _WsXFPTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 4),
    _WsXFPTransceiver_Type()
)
wsXFPTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTransceiver.setStatus("current")


class _WsXFPEncoding_Type(Bits):
    """Custom type wsXFPEncoding based on Bits"""
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("eRZ", 3),
          ("eNRZ", 4),
          ("eSonetScrambl", 5),
          ("e8B10B", 6),
          ("e64B66B", 7))
    )

_WsXFPEncoding_Type.__name__ = "Bits"
_WsXFPEncoding_Object = MibTableColumn
wsXFPEncoding = _WsXFPEncoding_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 5),
    _WsXFPEncoding_Type()
)
wsXFPEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPEncoding.setStatus("current")
_WsXFPBitrateMin_Type = Unsigned32
_WsXFPBitrateMin_Object = MibTableColumn
wsXFPBitrateMin = _WsXFPBitrateMin_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 6),
    _WsXFPBitrateMin_Type()
)
wsXFPBitrateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPBitrateMin.setStatus("current")
_WsXFPBitrateMax_Type = Unsigned32
_WsXFPBitrateMax_Object = MibTableColumn
wsXFPBitrateMax = _WsXFPBitrateMax_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 7),
    _WsXFPBitrateMax_Type()
)
wsXFPBitrateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPBitrateMax.setStatus("current")
_WsXFPSingleModeLen_Type = Unsigned32
_WsXFPSingleModeLen_Object = MibTableColumn
wsXFPSingleModeLen = _WsXFPSingleModeLen_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 8),
    _WsXFPSingleModeLen_Type()
)
wsXFPSingleModeLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPSingleModeLen.setStatus("current")
_WsXFPMultiMode50Len_Type = Unsigned32
_WsXFPMultiMode50Len_Object = MibTableColumn
wsXFPMultiMode50Len = _WsXFPMultiMode50Len_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 9),
    _WsXFPMultiMode50Len_Type()
)
wsXFPMultiMode50Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPMultiMode50Len.setStatus("current")
_WsXFPMultiMode625Len_Type = Unsigned32
_WsXFPMultiMode625Len_Object = MibTableColumn
wsXFPMultiMode625Len = _WsXFPMultiMode625Len_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 10),
    _WsXFPMultiMode625Len_Type()
)
wsXFPMultiMode625Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPMultiMode625Len.setStatus("current")
_WsXFPCopperLen_Type = Unsigned32
_WsXFPCopperLen_Object = MibTableColumn
wsXFPCopperLen = _WsXFPCopperLen_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 11),
    _WsXFPCopperLen_Type()
)
wsXFPCopperLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPCopperLen.setStatus("current")


class _WsXFPTempStatus_Type(Integer32):
    """Custom type wsXFPTempStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsXFPTempStatus_Type.__name__ = "Integer32"
_WsXFPTempStatus_Object = MibTableColumn
wsXFPTempStatus = _WsXFPTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 12),
    _WsXFPTempStatus_Type()
)
wsXFPTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTempStatus.setStatus("current")
_WsXFPTemp_Type = Integer32
_WsXFPTemp_Object = MibTableColumn
wsXFPTemp = _WsXFPTemp_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 13),
    _WsXFPTemp_Type()
)
wsXFPTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTemp.setStatus("current")


class _WsXFPTXCurrentStatus_Type(Integer32):
    """Custom type wsXFPTXCurrentStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsXFPTXCurrentStatus_Type.__name__ = "Integer32"
_WsXFPTXCurrentStatus_Object = MibTableColumn
wsXFPTXCurrentStatus = _WsXFPTXCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 14),
    _WsXFPTXCurrentStatus_Type()
)
wsXFPTXCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTXCurrentStatus.setStatus("current")
_WsXFPTXCurrent_Type = Integer32
_WsXFPTXCurrent_Object = MibTableColumn
wsXFPTXCurrent = _WsXFPTXCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 15),
    _WsXFPTXCurrent_Type()
)
wsXFPTXCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTXCurrent.setStatus("current")


class _WsXFPTXPowerStatus_Type(Integer32):
    """Custom type wsXFPTXPowerStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsXFPTXPowerStatus_Type.__name__ = "Integer32"
_WsXFPTXPowerStatus_Object = MibTableColumn
wsXFPTXPowerStatus = _WsXFPTXPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 16),
    _WsXFPTXPowerStatus_Type()
)
wsXFPTXPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTXPowerStatus.setStatus("current")
_WsXFPTXPower_Type = Integer32
_WsXFPTXPower_Object = MibTableColumn
wsXFPTXPower = _WsXFPTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 17),
    _WsXFPTXPower_Type()
)
wsXFPTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPTXPower.setStatus("current")


class _WsXFPRXPowerStatus_Type(Integer32):
    """Custom type wsXFPRXPowerStatus based on Integer32"""
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
        *(("unknown", 0),
          ("alarmLow", 1),
          ("warnLow", 2),
          ("ok", 3),
          ("warnHigh", 4),
          ("alarmHigh", 5))
    )


_WsXFPRXPowerStatus_Type.__name__ = "Integer32"
_WsXFPRXPowerStatus_Object = MibTableColumn
wsXFPRXPowerStatus = _WsXFPRXPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 18),
    _WsXFPRXPowerStatus_Type()
)
wsXFPRXPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPRXPowerStatus.setStatus("current")
_WsXFPRXPower_Type = Integer32
_WsXFPRXPower_Object = MibTableColumn
wsXFPRXPower = _WsXFPRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 6, 1, 19),
    _WsXFPRXPower_Type()
)
wsXFPRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsXFPRXPower.setStatus("current")

# Managed Objects groups


# Notification objects

wsIbosTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 1)
)
wsIbosTempLow.setObjects(
      *(("WAYSTREAM-MIB", "wsTempSensor"),
        ("WAYSTREAM-MIB", "wsTempMeasured"),
        ("WAYSTREAM-MIB", "wsTempThresholdLow"),
        ("WAYSTREAM-MIB", "wsTempStatus"))
)
if mibBuilder.loadTexts:
    wsIbosTempLow.setStatus(
        "current"
    )

wsIbosTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 2)
)
wsIbosTempHigh.setObjects(
      *(("WAYSTREAM-MIB", "wsTempSensor"),
        ("WAYSTREAM-MIB", "wsTempMeasured"),
        ("WAYSTREAM-MIB", "wsTempThresholdHigh"),
        ("WAYSTREAM-MIB", "wsTempStatus"))
)
if mibBuilder.loadTexts:
    wsIbosTempHigh.setStatus(
        "current"
    )

wsIbosVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 3)
)
wsIbosVoltLow.setObjects(
      *(("WAYSTREAM-MIB", "wsVoltChannel"),
        ("WAYSTREAM-MIB", "wsVoltMeasured"),
        ("WAYSTREAM-MIB", "wsVoltThresholdLow"),
        ("WAYSTREAM-MIB", "wsVoltStatus"))
)
if mibBuilder.loadTexts:
    wsIbosVoltLow.setStatus(
        "current"
    )

wsIbosVoltHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 4)
)
wsIbosVoltHigh.setObjects(
      *(("WAYSTREAM-MIB", "wsVoltChannel"),
        ("WAYSTREAM-MIB", "wsVoltMeasured"),
        ("WAYSTREAM-MIB", "wsVoltThresholdHigh"),
        ("WAYSTREAM-MIB", "wsVoltStatus"))
)
if mibBuilder.loadTexts:
    wsIbosVoltHigh.setStatus(
        "current"
    )

wsIbosFanRPMLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 5)
)
wsIbosFanRPMLow.setObjects(
      *(("WAYSTREAM-MIB", "wsFanNumber"),
        ("WAYSTREAM-MIB", "wsFanRPM"))
)
if mibBuilder.loadTexts:
    wsIbosFanRPMLow.setStatus(
        "current"
    )

wsIbosFanOutVoltLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 1, 2, 0, 6)
)
wsIbosFanOutVoltLow.setObjects(
    ("WAYSTREAM-MIB", "wsFanVoltage")
)
if mibBuilder.loadTexts:
    wsIbosFanOutVoltLow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-MIB",
    **{"ibos": ibos,
       "wsSystem": wsSystem,
       "wsWritedummy": wsWritedummy,
       "wsReload": wsReload,
       "wsVersion": wsVersion,
       "wsAsrRevision": wsAsrRevision,
       "wsVersionString": wsVersionString,
       "wsEnvironment": wsEnvironment,
       "wsIbosEnvironmentNotifications": wsIbosEnvironmentNotifications,
       "wsIbosTempLow": wsIbosTempLow,
       "wsIbosTempHigh": wsIbosTempHigh,
       "wsIbosVoltLow": wsIbosVoltLow,
       "wsIbosVoltHigh": wsIbosVoltHigh,
       "wsIbosFanRPMLow": wsIbosFanRPMLow,
       "wsIbosFanOutVoltLow": wsIbosFanOutVoltLow,
       "wsTempTable": wsTempTable,
       "wsTempEntry": wsTempEntry,
       "wsTempSensor": wsTempSensor,
       "wsTempMeasured": wsTempMeasured,
       "wsTempTOS": wsTempTOS,
       "wsTempTHYST": wsTempTHYST,
       "wsTempThresholdLow": wsTempThresholdLow,
       "wsTempThresholdHigh": wsTempThresholdHigh,
       "wsTempStatus": wsTempStatus,
       "wsVoltTable": wsVoltTable,
       "wsVoltEntry": wsVoltEntry,
       "wsVoltChannel": wsVoltChannel,
       "wsVoltNominal": wsVoltNominal,
       "wsVoltMeasured": wsVoltMeasured,
       "wsVoltThresholdLow": wsVoltThresholdLow,
       "wsVoltThresholdHigh": wsVoltThresholdHigh,
       "wsVoltStatus": wsVoltStatus,
       "wsFanTable": wsFanTable,
       "wsFanEntry": wsFanEntry,
       "wsFanNumber": wsFanNumber,
       "wsFanRPM": wsFanRPM,
       "wsFanVoltage": wsFanVoltage,
       "wsIbosEnvironmentTrapEnable": wsIbosEnvironmentTrapEnable,
       "wsPFDP": wsPFDP,
       "wsNeighboursTable": wsNeighboursTable,
       "wsNeighboursEntry": wsNeighboursEntry,
       "wsNeighbourIfIndex": wsNeighbourIfIndex,
       "wsNeighbourNIndex": wsNeighbourNIndex,
       "wsNeighbourHostname": wsNeighbourHostname,
       "wsNeighbourLocalIf": wsNeighbourLocalIf,
       "wsNeighbourRemoteIf": wsNeighbourRemoteIf,
       "wsNeighbourModel": wsNeighbourModel,
       "wsNeighbourLastAct": wsNeighbourLastAct,
       "wsNeighbourOSVersion": wsNeighbourOSVersion,
       "wsNeighbourSNPA": wsNeighbourSNPA,
       "wsNeighbourUptime": wsNeighbourUptime,
       "wsNeighbourState": wsNeighbourState,
       "wsNeighbourDBCount": wsNeighbourDBCount,
       "wsNeighbourCreated": wsNeighbourCreated,
       "wsNeighbourPacketsIn": wsNeighbourPacketsIn,
       "wsNeighbourPacketErrorsrIn": wsNeighbourPacketErrorsrIn,
       "wsNeighbourPortsTable": wsNeighbourPortsTable,
       "wsNeighbourPortsEntry": wsNeighbourPortsEntry,
       "wsNeighbourPortIfIndex": wsNeighbourPortIfIndex,
       "wsNeighbourPortNIndex": wsNeighbourPortNIndex,
       "wsNeighbourPortPIndex": wsNeighbourPortPIndex,
       "wsNeighbourPortName": wsNeighbourPortName,
       "wsNeighbourPortState": wsNeighbourPortState,
       "wsNeighbourPortTxOctets": wsNeighbourPortTxOctets,
       "wsNeighbourPortTxDropPkts": wsNeighbourPortTxDropPkts,
       "wsNeighbourPortTxBroadcastPkts": wsNeighbourPortTxBroadcastPkts,
       "wsNeighbourPortTxMulticastPkts": wsNeighbourPortTxMulticastPkts,
       "wsNeighbourPortTxUnicastPkts": wsNeighbourPortTxUnicastPkts,
       "wsNeighbourPortTxCollisions": wsNeighbourPortTxCollisions,
       "wsNeighbourPortTxDeferredTransmit": wsNeighbourPortTxDeferredTransmit,
       "wsNeighbourPortTxFrameInDisc": wsNeighbourPortTxFrameInDisc,
       "wsNeighbourPortRxOctets": wsNeighbourPortRxOctets,
       "wsNeighbourPortRxUndersizePkts": wsNeighbourPortRxUndersizePkts,
       "wsNeighbourPortPkts64Octets": wsNeighbourPortPkts64Octets,
       "wsNeighbourPortPkts65to127Octets": wsNeighbourPortPkts65to127Octets,
       "wsNeighbourPortPkts128to255Octets": wsNeighbourPortPkts128to255Octets,
       "wsNeighbourPortPkts256to511Octets": wsNeighbourPortPkts256to511Octets,
       "wsNeighbourPortPkts512to1023Octets": wsNeighbourPortPkts512to1023Octets,
       "wsNeighbourPortPkts1024to1522Octets": wsNeighbourPortPkts1024to1522Octets,
       "wsNeighbourPortRxOversizePkts": wsNeighbourPortRxOversizePkts,
       "wsNeighbourPortRxJabbers": wsNeighbourPortRxJabbers,
       "wsNeighbourPortRxAlignmentErrors": wsNeighbourPortRxAlignmentErrors,
       "wsNeighbourPortRxFCSErrors": wsNeighbourPortRxFCSErrors,
       "wsNeighbourPortRxGoodOctets": wsNeighbourPortRxGoodOctets,
       "wsNeighbourPortRxDropPkts": wsNeighbourPortRxDropPkts,
       "wsNeighbourPortRxUnicastPkts": wsNeighbourPortRxUnicastPkts,
       "wsNeighbourPortRxMulticastPkts": wsNeighbourPortRxMulticastPkts,
       "wsNeighbourPortRxBroadcastPkts": wsNeighbourPortRxBroadcastPkts,
       "wsNeighbourPortRxFragments": wsNeighbourPortRxFragments,
       "wsNeighbourPortRxExcessSizeDisc": wsNeighbourPortRxExcessSizeDisc,
       "wsNeighbourPortRxSymbolError": wsNeighbourPortRxSymbolError,
       "wsNeighbourPortSNPATable": wsNeighbourPortSNPATable,
       "wsNeighbourPortSNPAEntry": wsNeighbourPortSNPAEntry,
       "wsNeighbourPortSNPAIfIndex": wsNeighbourPortSNPAIfIndex,
       "wsNeighbourPortSNPANIndex": wsNeighbourPortSNPANIndex,
       "wsNeighbourPortSNPAPIndex": wsNeighbourPortSNPAPIndex,
       "wsNeighbourPortSNPASIndex": wsNeighbourPortSNPASIndex,
       "wsNeighbourPortSNPASMCast": wsNeighbourPortSNPASMCast,
       "wsNeighbourPortSNPA": wsNeighbourPortSNPA,
       "wsSFPTable": wsSFPTable,
       "wsSFPEntry": wsSFPEntry,
       "wsSFPIndex": wsSFPIndex,
       "wsSFPStatus": wsSFPStatus,
       "wsSFPConnector": wsSFPConnector,
       "wsSFPTransceiver": wsSFPTransceiver,
       "wsSFPEncoding": wsSFPEncoding,
       "wsSFPBitrate": wsSFPBitrate,
       "wsSFPSingleModeLen": wsSFPSingleModeLen,
       "wsSFPMultiMode50Len": wsSFPMultiMode50Len,
       "wsSFPMultiMode625Len": wsSFPMultiMode625Len,
       "wsSFPCopperLen": wsSFPCopperLen,
       "wsSFPTempStatus": wsSFPTempStatus,
       "wsSFPTemp": wsSFPTemp,
       "wsSFPVoltStatus": wsSFPVoltStatus,
       "wsSFPVolt": wsSFPVolt,
       "wsSFPTXCurrentStatus": wsSFPTXCurrentStatus,
       "wsSFPTXCurrent": wsSFPTXCurrent,
       "wsSFPTXPowerStatus": wsSFPTXPowerStatus,
       "wsSFPTXPower": wsSFPTXPower,
       "wsSFPRXPowerStatus": wsSFPRXPowerStatus,
       "wsSFPRXPower": wsSFPRXPower,
       "wsSFPTransceiverExt": wsSFPTransceiverExt,
       "wsSFPTXdBmPower": wsSFPTXdBmPower,
       "wsSFPRXdBmPower": wsSFPRXdBmPower,
       "wsSFPTempNormalLow": wsSFPTempNormalLow,
       "wsSFPTempNormalHigh": wsSFPTempNormalHigh,
       "wsSFPTempWarningLow": wsSFPTempWarningLow,
       "wsSFPTempWarningHigh": wsSFPTempWarningHigh,
       "wsSFPVoltNormalLow": wsSFPVoltNormalLow,
       "wsSFPVoltNormalHigh": wsSFPVoltNormalHigh,
       "wsSFPVoltWarningLow": wsSFPVoltWarningLow,
       "wsSFPVoltWarningHigh": wsSFPVoltWarningHigh,
       "wsSFPTXCurrentNormalLow": wsSFPTXCurrentNormalLow,
       "wsSFPTXCurrentNormalHigh": wsSFPTXCurrentNormalHigh,
       "wsSFPTXCurrentWarningLow": wsSFPTXCurrentWarningLow,
       "wsSFPTXCurrentWarningHigh": wsSFPTXCurrentWarningHigh,
       "wsSFPTXOutputPowNormalLowuW": wsSFPTXOutputPowNormalLowuW,
       "wsSFPTXOutputPowNormalHighuW": wsSFPTXOutputPowNormalHighuW,
       "wsSFPTXOutputPowWarningLowuW": wsSFPTXOutputPowWarningLowuW,
       "wsSFPTXOutputPowWarningHighuW": wsSFPTXOutputPowWarningHighuW,
       "wsSFPTXOutputPowNormalLowdBm": wsSFPTXOutputPowNormalLowdBm,
       "wsSFPTXOutputPowNormalHighdBm": wsSFPTXOutputPowNormalHighdBm,
       "wsSFPTXOutputPowWarningLowdBm": wsSFPTXOutputPowWarningLowdBm,
       "wsSFPTXOutputPowWarningHighdBm": wsSFPTXOutputPowWarningHighdBm,
       "wsSFPRXInputPowNormalLowuW": wsSFPRXInputPowNormalLowuW,
       "wsSFPRXInputPowNormalHighuW": wsSFPRXInputPowNormalHighuW,
       "wsSFPRXInputPowWarningLowuW": wsSFPRXInputPowWarningLowuW,
       "wsSFPRXInputPowWarningHighuW": wsSFPRXInputPowWarningHighuW,
       "wsSFPRXInputPowNormalLowdBm": wsSFPRXInputPowNormalLowdBm,
       "wsSFPRXInputPowNormalHighdBm": wsSFPRXInputPowNormalHighdBm,
       "wsSFPRXInputPowWarningLowdBm": wsSFPRXInputPowWarningLowdBm,
       "wsSFPRXInputPowWarningHighdBm": wsSFPRXInputPowWarningHighdBm,
       "wsSFPPartNumber": wsSFPPartNumber,
       "wsSFPSerialNumber": wsSFPSerialNumber,
       "wsAccounting": wsAccounting,
       "wsPolicyTable": wsPolicyTable,
       "wsPolicyEntry": wsPolicyEntry,
       "wsPolicyIfIndex": wsPolicyIfIndex,
       "wsPolicyIfName": wsPolicyIfName,
       "wsPolicyName": wsPolicyName,
       "wsPolicyCookie": wsPolicyCookie,
       "wsPolicyInPkts": wsPolicyInPkts,
       "wsPolicyInBytes": wsPolicyInBytes,
       "wsPolicyInDrops": wsPolicyInDrops,
       "wsPolicyOutPkts": wsPolicyOutPkts,
       "wsPolicyOutBytes": wsPolicyOutBytes,
       "wsPolicyOutDrops": wsPolicyOutDrops,
       "wsPolicyUsedCnt": wsPolicyUsedCnt,
       "wsXFPTable": wsXFPTable,
       "wsXFPEntry": wsXFPEntry,
       "wsXFPIndex": wsXFPIndex,
       "wsXFPStatus": wsXFPStatus,
       "wsXFPConnector": wsXFPConnector,
       "wsXFPTransceiver": wsXFPTransceiver,
       "wsXFPEncoding": wsXFPEncoding,
       "wsXFPBitrateMin": wsXFPBitrateMin,
       "wsXFPBitrateMax": wsXFPBitrateMax,
       "wsXFPSingleModeLen": wsXFPSingleModeLen,
       "wsXFPMultiMode50Len": wsXFPMultiMode50Len,
       "wsXFPMultiMode625Len": wsXFPMultiMode625Len,
       "wsXFPCopperLen": wsXFPCopperLen,
       "wsXFPTempStatus": wsXFPTempStatus,
       "wsXFPTemp": wsXFPTemp,
       "wsXFPTXCurrentStatus": wsXFPTXCurrentStatus,
       "wsXFPTXCurrent": wsXFPTXCurrent,
       "wsXFPTXPowerStatus": wsXFPTXPowerStatus,
       "wsXFPTXPower": wsXFPTXPower,
       "wsXFPRXPowerStatus": wsXFPRXPowerStatus,
       "wsXFPRXPower": wsXFPRXPower}
)
