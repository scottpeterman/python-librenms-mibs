# SNMP MIB module (TROPIC-ACCESSPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-ACCESSPORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:20 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifEntry",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnAccessPortMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAccessPortMIB",
    "tnPortModules")

(AluWdmFecMode,
 AluWdmTnIfType,
 TnCommand,
 TropicLEDColorType,
 TropicLEDStateType,
 TropicOperationalCapabilityType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmFecMode",
    "AluWdmTnIfType",
    "TnCommand",
    "TropicLEDColorType",
    "TropicLEDStateType",
    "TropicOperationalCapabilityType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnAccessPortMibModules = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortMibModules.setRevisions(
        ("2022-07-08 12:00",
         "2021-12-03 12:00",
         "2020-12-11 12:00",
         "2020-11-27 12:00",
         "2020-05-01 12:00",
         "2020-04-03 12:00",
         "2020-03-27 12:00",
         "2020-03-20 12:00",
         "2020-02-28 12:00",
         "2020-02-21 12:00",
         "2020-01-24 12:00",
         "2019-12-27 12:00",
         "2019-10-18 12:00",
         "2019-09-06 12:00",
         "2019-08-09 12:00",
         "2019-05-17 12:00",
         "2019-03-08 12:00",
         "2019-01-11 12:00",
         "2018-11-02 12:00",
         "2018-08-03 12:00",
         "2018-07-20 12:00",
         "2018-06-08 12:00",
         "2018-05-11 12:00",
         "2018-04-20 12:00",
         "2018-02-23 12:00",
         "2018-01-05 12:00",
         "2017-12-29 12:00",
         "2017-10-06 12:00",
         "2017-04-07 12:00",
         "2017-01-13 12:00",
         "2016-12-28 12:00",
         "2016-11-22 12:00",
         "2016-11-16 12:00",
         "2016-10-19 12:00",
         "2016-08-24 12:00",
         "2016-05-11 12:00",
         "2015-10-05 12:00",
         "2015-09-28 12:00",
         "2015-07-03 12:00",
         "2015-05-18 12:00",
         "2015-05-15 12:00",
         "2015-01-22 12:00",
         "2014-11-24 12:00",
         "2014-05-18 12:00",
         "2014-03-18 12:00",
         "2014-02-26 12:00",
         "2013-06-13 12:00",
         "2013-05-21 12:00",
         "2013-04-12 12:00",
         "2013-03-15 12:00",
         "2012-12-17 12:00",
         "2012-09-27 12:00",
         "2012-09-06 12:00",
         "2012-08-06 12:00",
         "2012-04-25 12:00",
         "2012-02-28 12:00",
         "2011-11-16 12:00",
         "2011-09-30 12:00",
         "2010-10-19 12:00",
         "2010-09-20 12:00",
         "2010-06-28 12:00",
         "2010-06-04 12:00",
         "2010-05-10 12:00",
         "2010-01-15 12:00",
         "2010-01-04 12:00",
         "2009-11-01 12:00",
         "2009-07-10 12:00",
         "2009-07-08 12:00",
         "2009-06-07 12:00",
         "2009-03-31 12:00",
         "2009-03-22 12:00",
         "2009-03-10 12:00",
         "2009-03-03 12:00",
         "2009-02-11 12:00",
         "2008-03-20 12:00",
         "2008-03-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnAccessPortConf_ObjectIdentity = ObjectIdentity
tnAccessPortConf = _TnAccessPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1)
)
_TnAccessPortGroups_ObjectIdentity = ObjectIdentity
tnAccessPortGroups = _TnAccessPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1)
)
_TnAccessPortCompliances_ObjectIdentity = ObjectIdentity
tnAccessPortCompliances = _TnAccessPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 2)
)
_TnAccessPortObjs_ObjectIdentity = ObjectIdentity
tnAccessPortObjs = _TnAccessPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2)
)
_TnAccessPortTable_Object = MibTable
tnAccessPortTable = _TnAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortTable.setStatus("current")
_TnAccessPortEntry_Object = MibTableRow
tnAccessPortEntry = _TnAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1)
)
tnAccessPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAccessPortEntry.setStatus("current")


class _TnAccessPortDescr_Type(SnmpAdminString):
    """Custom type tnAccessPortDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAccessPortDescr_Type.__name__ = "SnmpAdminString"
_TnAccessPortDescr_Object = MibTableColumn
tnAccessPortDescr = _TnAccessPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 1),
    _TnAccessPortDescr_Type()
)
tnAccessPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortDescr.setStatus("current")
_TnAccessPortStatusLEDColor_Type = TropicLEDColorType
_TnAccessPortStatusLEDColor_Object = MibTableColumn
tnAccessPortStatusLEDColor = _TnAccessPortStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 2),
    _TnAccessPortStatusLEDColor_Type()
)
tnAccessPortStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStatusLEDColor.setStatus("current")
_TnAccessPortStatusLEDState_Type = TropicLEDStateType
_TnAccessPortStatusLEDState_Object = MibTableColumn
tnAccessPortStatusLEDState = _TnAccessPortStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 3),
    _TnAccessPortStatusLEDState_Type()
)
tnAccessPortStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStatusLEDState.setStatus("current")


class _TnAccessPortOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnAccessPortOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnAccessPortOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnAccessPortOperationalCapability_Object = MibTableColumn
tnAccessPortOperationalCapability = _TnAccessPortOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 4),
    _TnAccessPortOperationalCapability_Type()
)
tnAccessPortOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortOperationalCapability.setStatus("current")


class _TnAccessPortStateQualifier_Type(TropicStateQualifierType):
    """Custom type tnAccessPortStateQualifier based on TropicStateQualifierType"""
    defaultBinValue = "0"


_TnAccessPortStateQualifier_Type.__name__ = "TropicStateQualifierType"
_TnAccessPortStateQualifier_Object = MibTableColumn
tnAccessPortStateQualifier = _TnAccessPortStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 5),
    _TnAccessPortStateQualifier_Type()
)
tnAccessPortStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStateQualifier.setStatus("current")


class _TnAccessPortFarEndAddress_Type(SnmpAdminString):
    """Custom type tnAccessPortFarEndAddress based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnAccessPortFarEndAddress_Type.__name__ = "SnmpAdminString"
_TnAccessPortFarEndAddress_Object = MibTableColumn
tnAccessPortFarEndAddress = _TnAccessPortFarEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 6),
    _TnAccessPortFarEndAddress_Type()
)
tnAccessPortFarEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndAddress.setStatus("current")


class _TnAccessPortFarEndIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortFarEndIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortFarEndIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortFarEndIfIndex_Object = MibTableColumn
tnAccessPortFarEndIfIndex = _TnAccessPortFarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 7),
    _TnAccessPortFarEndIfIndex_Type()
)
tnAccessPortFarEndIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndIfIndex.setStatus("current")


class _TnAccessPortFarEndType_Type(Integer32):
    """Custom type tnAccessPortFarEndType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("internal", 2),
          ("external", 3),
          ("interCompound", 5),
          ("cluster", 6))
    )


_TnAccessPortFarEndType_Type.__name__ = "Integer32"
_TnAccessPortFarEndType_Object = MibTableColumn
tnAccessPortFarEndType = _TnAccessPortFarEndType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 8),
    _TnAccessPortFarEndType_Type()
)
tnAccessPortFarEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndType.setStatus("current")


class _TnAccessPortDirection_Type(Integer32):
    """Custom type tnAccessPortDirection based on Integer32"""
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
        *(("bidirectional", 1),
          ("unidirectionalTx", 2),
          ("unidirectionalRx", 3))
    )


_TnAccessPortDirection_Type.__name__ = "Integer32"
_TnAccessPortDirection_Object = MibTableColumn
tnAccessPortDirection = _TnAccessPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 9),
    _TnAccessPortDirection_Type()
)
tnAccessPortDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortDirection.setStatus("current")


class _TnAccessPortAINS_Type(TruthValue):
    """Custom type tnAccessPortAINS based on TruthValue"""
    defaultValue = 2


_TnAccessPortAINS_Type.__name__ = "TruthValue"
_TnAccessPortAINS_Object = MibTableColumn
tnAccessPortAINS = _TnAccessPortAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 10),
    _TnAccessPortAINS_Type()
)
tnAccessPortAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAINS.setStatus("current")


class _TnAccessPortAINSDebounceTime_Type(Integer32):
    """Custom type tnAccessPortAINSDebounceTime based on Integer32"""
    defaultValue = -1


_TnAccessPortAINSDebounceTime_Type.__name__ = "Integer32"
_TnAccessPortAINSDebounceTime_Object = MibTableColumn
tnAccessPortAINSDebounceTime = _TnAccessPortAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 11),
    _TnAccessPortAINSDebounceTime_Type()
)
tnAccessPortAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTime.setUnits("seconds")
_TnAccessPortUsingSysAINSDebounceTime_Type = TruthValue
_TnAccessPortUsingSysAINSDebounceTime_Object = MibTableColumn
tnAccessPortUsingSysAINSDebounceTime = _TnAccessPortUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 12),
    _TnAccessPortUsingSysAINSDebounceTime_Type()
)
tnAccessPortUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortUsingSysAINSDebounceTime.setStatus("current")


class _TnAccessPortAINSDebounceTimeRemaining_Type(Unsigned32):
    """Custom type tnAccessPortAINSDebounceTimeRemaining based on Unsigned32"""
    defaultValue = 0


_TnAccessPortAINSDebounceTimeRemaining_Type.__name__ = "Unsigned32"
_TnAccessPortAINSDebounceTimeRemaining_Object = MibTableColumn
tnAccessPortAINSDebounceTimeRemaining = _TnAccessPortAINSDebounceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 13),
    _TnAccessPortAINSDebounceTimeRemaining_Type()
)
tnAccessPortAINSDebounceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTimeRemaining.setUnits("seconds")


class _TnAccessPortIsDomainEdgePort_Type(TruthValue):
    """Custom type tnAccessPortIsDomainEdgePort based on TruthValue"""
    defaultValue = 1


_TnAccessPortIsDomainEdgePort_Type.__name__ = "TruthValue"
_TnAccessPortIsDomainEdgePort_Object = MibTableColumn
tnAccessPortIsDomainEdgePort = _TnAccessPortIsDomainEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 14),
    _TnAccessPortIsDomainEdgePort_Type()
)
tnAccessPortIsDomainEdgePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortIsDomainEdgePort.setStatus("current")


class _TnAccessPortFarEndAddressConnFrom_Type(SnmpAdminString):
    """Custom type tnAccessPortFarEndAddressConnFrom based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnAccessPortFarEndAddressConnFrom_Type.__name__ = "SnmpAdminString"
_TnAccessPortFarEndAddressConnFrom_Object = MibTableColumn
tnAccessPortFarEndAddressConnFrom = _TnAccessPortFarEndAddressConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 15),
    _TnAccessPortFarEndAddressConnFrom_Type()
)
tnAccessPortFarEndAddressConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndAddressConnFrom.setStatus("current")


class _TnAccessPortFarEndIfIndexConnFrom_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortFarEndIfIndexConnFrom based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortFarEndIfIndexConnFrom_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortFarEndIfIndexConnFrom_Object = MibTableColumn
tnAccessPortFarEndIfIndexConnFrom = _TnAccessPortFarEndIfIndexConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 16),
    _TnAccessPortFarEndIfIndexConnFrom_Type()
)
tnAccessPortFarEndIfIndexConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndIfIndexConnFrom.setStatus("current")


class _TnAccessPortFarEndTypeConnFrom_Type(Integer32):
    """Custom type tnAccessPortFarEndTypeConnFrom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("internal", 2),
          ("external", 3),
          ("interCompound", 5),
          ("cluster", 6))
    )


_TnAccessPortFarEndTypeConnFrom_Type.__name__ = "Integer32"
_TnAccessPortFarEndTypeConnFrom_Object = MibTableColumn
tnAccessPortFarEndTypeConnFrom = _TnAccessPortFarEndTypeConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 17),
    _TnAccessPortFarEndTypeConnFrom_Type()
)
tnAccessPortFarEndTypeConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndTypeConnFrom.setStatus("current")


class _TnAccessPortExtAmpIpAddressIn_Type(IpAddress):
    """Custom type tnAccessPortExtAmpIpAddressIn based on IpAddress"""
    defaultHexValue = "00000000"


_TnAccessPortExtAmpIpAddressIn_Type.__name__ = "IpAddress"
_TnAccessPortExtAmpIpAddressIn_Object = MibTableColumn
tnAccessPortExtAmpIpAddressIn = _TnAccessPortExtAmpIpAddressIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 18),
    _TnAccessPortExtAmpIpAddressIn_Type()
)
tnAccessPortExtAmpIpAddressIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortExtAmpIpAddressIn.setStatus("current")


class _TnAccessPortExtAmpIpAddressOut_Type(IpAddress):
    """Custom type tnAccessPortExtAmpIpAddressOut based on IpAddress"""
    defaultHexValue = "00000000"


_TnAccessPortExtAmpIpAddressOut_Type.__name__ = "IpAddress"
_TnAccessPortExtAmpIpAddressOut_Object = MibTableColumn
tnAccessPortExtAmpIpAddressOut = _TnAccessPortExtAmpIpAddressOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 19),
    _TnAccessPortExtAmpIpAddressOut_Type()
)
tnAccessPortExtAmpIpAddressOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortExtAmpIpAddressOut.setStatus("current")


class _TnAccessPortWtocmConnLoss_Type(Integer32):
    """Custom type tnAccessPortWtocmConnLoss based on Integer32"""
    defaultValue = 0


_TnAccessPortWtocmConnLoss_Type.__name__ = "Integer32"
_TnAccessPortWtocmConnLoss_Object = MibTableColumn
tnAccessPortWtocmConnLoss = _TnAccessPortWtocmConnLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 20),
    _TnAccessPortWtocmConnLoss_Type()
)
tnAccessPortWtocmConnLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnLoss.setUnits("mB")


class _TnAccessPortWtocmConnAddress_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortWtocmConnAddress based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortWtocmConnAddress_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortWtocmConnAddress_Object = MibTableColumn
tnAccessPortWtocmConnAddress = _TnAccessPortWtocmConnAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 21),
    _TnAccessPortWtocmConnAddress_Type()
)
tnAccessPortWtocmConnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnAddress.setStatus("current")


class _TnAccessPortOppDirectionPortAddress_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortOppDirectionPortAddress based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortOppDirectionPortAddress_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortOppDirectionPortAddress_Object = MibTableColumn
tnAccessPortOppDirectionPortAddress = _TnAccessPortOppDirectionPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 22),
    _TnAccessPortOppDirectionPortAddress_Type()
)
tnAccessPortOppDirectionPortAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortOppDirectionPortAddress.setStatus("current")


class _TnAccessPortIsValidInternalOTSXcEndpoint_Type(TruthValue):
    """Custom type tnAccessPortIsValidInternalOTSXcEndpoint based on TruthValue"""
    defaultValue = 2


_TnAccessPortIsValidInternalOTSXcEndpoint_Type.__name__ = "TruthValue"
_TnAccessPortIsValidInternalOTSXcEndpoint_Object = MibTableColumn
tnAccessPortIsValidInternalOTSXcEndpoint = _TnAccessPortIsValidInternalOTSXcEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 23),
    _TnAccessPortIsValidInternalOTSXcEndpoint_Type()
)
tnAccessPortIsValidInternalOTSXcEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortIsValidInternalOTSXcEndpoint.setStatus("current")


class _TnAccessPortWtDomainNumber_Type(Integer32):
    """Custom type tnAccessPortWtDomainNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnAccessPortWtDomainNumber_Type.__name__ = "Integer32"
_TnAccessPortWtDomainNumber_Object = MibTableColumn
tnAccessPortWtDomainNumber = _TnAccessPortWtDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 24),
    _TnAccessPortWtDomainNumber_Type()
)
tnAccessPortWtDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtDomainNumber.setStatus("current")
_TnAccessPortHasMpoConnector_Type = TruthValue
_TnAccessPortHasMpoConnector_Object = MibTableColumn
tnAccessPortHasMpoConnector = _TnAccessPortHasMpoConnector_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 25),
    _TnAccessPortHasMpoConnector_Type()
)
tnAccessPortHasMpoConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortHasMpoConnector.setStatus("current")
_TnAccessPortMpoConnectorPortOutIfIndex_Type = InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortOutIfIndex_Object = MibTableColumn
tnAccessPortMpoConnectorPortOutIfIndex = _TnAccessPortMpoConnectorPortOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 26),
    _TnAccessPortMpoConnectorPortOutIfIndex_Type()
)
tnAccessPortMpoConnectorPortOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortMpoConnectorPortOutIfIndex.setStatus("current")
_TnAccessPortMpoConnectorPortInIfIndex_Type = InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortInIfIndex_Object = MibTableColumn
tnAccessPortMpoConnectorPortInIfIndex = _TnAccessPortMpoConnectorPortInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 27),
    _TnAccessPortMpoConnectorPortInIfIndex_Type()
)
tnAccessPortMpoConnectorPortInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortMpoConnectorPortInIfIndex.setStatus("current")
_TnAccessPortIsMpo_Type = TruthValue
_TnAccessPortIsMpo_Object = MibTableColumn
tnAccessPortIsMpo = _TnAccessPortIsMpo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 28),
    _TnAccessPortIsMpo_Type()
)
tnAccessPortIsMpo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortIsMpo.setStatus("current")


class _TnAccessPortMonOcmConnAddress_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortMonOcmConnAddress based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortMonOcmConnAddress_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortMonOcmConnAddress_Object = MibTableColumn
tnAccessPortMonOcmConnAddress = _TnAccessPortMonOcmConnAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 29),
    _TnAccessPortMonOcmConnAddress_Type()
)
tnAccessPortMonOcmConnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortMonOcmConnAddress.setStatus("current")


class _TnAccessPortAlmProfName_Type(OctetString):
    """Custom type tnAccessPortAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnAccessPortAlmProfName_Type.__name__ = "OctetString"
_TnAccessPortAlmProfName_Object = MibTableColumn
tnAccessPortAlmProfName = _TnAccessPortAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 30),
    _TnAccessPortAlmProfName_Type()
)
tnAccessPortAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAlmProfName.setStatus("current")
_TnAccessPortmfcTemperature_Type = Integer32
_TnAccessPortmfcTemperature_Object = MibTableColumn
tnAccessPortmfcTemperature = _TnAccessPortmfcTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 31),
    _TnAccessPortmfcTemperature_Type()
)
tnAccessPortmfcTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortmfcTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortmfcTemperature.setUnits("Celsius")


class _TnAccessPortmfcNominalPressure_Type(Integer32):
    """Custom type tnAccessPortmfcNominalPressure based on Integer32"""
    defaultValue = 0


_TnAccessPortmfcNominalPressure_Type.__name__ = "Integer32"
_TnAccessPortmfcNominalPressure_Object = MibTableColumn
tnAccessPortmfcNominalPressure = _TnAccessPortmfcNominalPressure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 32),
    _TnAccessPortmfcNominalPressure_Type()
)
tnAccessPortmfcNominalPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortmfcNominalPressure.setStatus("current")


class _TnAccessPortmfcDifferentialPressure_Type(Integer32):
    """Custom type tnAccessPortmfcDifferentialPressure based on Integer32"""
    defaultValue = 0


_TnAccessPortmfcDifferentialPressure_Type.__name__ = "Integer32"
_TnAccessPortmfcDifferentialPressure_Object = MibTableColumn
tnAccessPortmfcDifferentialPressure = _TnAccessPortmfcDifferentialPressure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 33),
    _TnAccessPortmfcDifferentialPressure_Type()
)
tnAccessPortmfcDifferentialPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortmfcDifferentialPressure.setStatus("current")
_TnAccessFilterAmbientTemperature_Type = Integer32
_TnAccessFilterAmbientTemperature_Object = MibTableColumn
tnAccessFilterAmbientTemperature = _TnAccessFilterAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 34),
    _TnAccessFilterAmbientTemperature_Type()
)
tnAccessFilterAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterAmbientTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessFilterAmbientTemperature.setUnits("Celsius")
_TnAccessFilterPressure_Type = Integer32
_TnAccessFilterPressure_Object = MibTableColumn
tnAccessFilterPressure = _TnAccessFilterPressure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 35),
    _TnAccessFilterPressure_Type()
)
tnAccessFilterPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterPressure.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessFilterPressure.setUnits("Pa")
_TnAccessFilterRecorded_Type = Integer32
_TnAccessFilterRecorded_Object = MibTableColumn
tnAccessFilterRecorded = _TnAccessFilterRecorded_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 36),
    _TnAccessFilterRecorded_Type()
)
tnAccessFilterRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterRecorded.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessFilterRecorded.setUnits("Pa")
_TnAccessFilterCalibrated_Type = Integer32
_TnAccessFilterCalibrated_Object = MibTableColumn
tnAccessFilterCalibrated = _TnAccessFilterCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 37),
    _TnAccessFilterCalibrated_Type()
)
tnAccessFilterCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterCalibrated.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessFilterCalibrated.setUnits("Pa")
_TnAccessFilterAltitude_Type = Integer32
_TnAccessFilterAltitude_Object = MibTableColumn
tnAccessFilterAltitude = _TnAccessFilterAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 38),
    _TnAccessFilterAltitude_Type()
)
tnAccessFilterAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterAltitude.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessFilterAltitude.setUnits("kilometers")
_TnAccessFilterRecordTime_Type = TimeTicks
_TnAccessFilterRecordTime_Object = MibTableColumn
tnAccessFilterRecordTime = _TnAccessFilterRecordTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 39),
    _TnAccessFilterRecordTime_Type()
)
tnAccessFilterRecordTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterRecordTime.setStatus("current")
_TnAccessFilterCalibrateTime_Type = TimeTicks
_TnAccessFilterCalibrateTime_Object = MibTableColumn
tnAccessFilterCalibrateTime = _TnAccessFilterCalibrateTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 40),
    _TnAccessFilterCalibrateTime_Type()
)
tnAccessFilterCalibrateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterCalibrateTime.setStatus("current")
_TnAccessFilterScheduledTime_Type = TimeTicks
_TnAccessFilterScheduledTime_Object = MibTableColumn
tnAccessFilterScheduledTime = _TnAccessFilterScheduledTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 41),
    _TnAccessFilterScheduledTime_Type()
)
tnAccessFilterScheduledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessFilterScheduledTime.setStatus("current")
_TnAccessPortL2FarEndIfIndex_Type = InterfaceIndexOrZero
_TnAccessPortL2FarEndIfIndex_Object = MibTableColumn
tnAccessPortL2FarEndIfIndex = _TnAccessPortL2FarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 42),
    _TnAccessPortL2FarEndIfIndex_Type()
)
tnAccessPortL2FarEndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortL2FarEndIfIndex.setStatus("current")
_TnAccessPortL2FarEndMacAddress_Type = MacAddress
_TnAccessPortL2FarEndMacAddress_Object = MibTableColumn
tnAccessPortL2FarEndMacAddress = _TnAccessPortL2FarEndMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 43),
    _TnAccessPortL2FarEndMacAddress_Type()
)
tnAccessPortL2FarEndMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortL2FarEndMacAddress.setStatus("current")


class _TnAccessPortDirectionCapability_Type(Integer32):
    """Custom type tnAccessPortDirectionCapability based on Integer32"""
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
        *(("notInstalled", 0),
          ("singleBidi", 1),
          ("dualBidi", 2),
          ("rxOnly", 3),
          ("txOnly", 4),
          ("rxAndTx", 5))
    )


_TnAccessPortDirectionCapability_Type.__name__ = "Integer32"
_TnAccessPortDirectionCapability_Object = MibTableColumn
tnAccessPortDirectionCapability = _TnAccessPortDirectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 44),
    _TnAccessPortDirectionCapability_Type()
)
tnAccessPortDirectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortDirectionCapability.setStatus("current")


class _TnAccessPortCpriMappingType_Type(Integer32):
    """Custom type tnAccessPortCpriMappingType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("tunneling", 6),
          ("linecodeAware", 7),
          ("structureAware", 8),
          ("structureAwareControl", 9),
          ("nomapping", 10))
    )


_TnAccessPortCpriMappingType_Type.__name__ = "Integer32"
_TnAccessPortCpriMappingType_Object = MibTableColumn
tnAccessPortCpriMappingType = _TnAccessPortCpriMappingType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 45),
    _TnAccessPortCpriMappingType_Type()
)
tnAccessPortCpriMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortCpriMappingType.setStatus("current")


class _TnAccessPortFecType_Type(AluWdmFecMode):
    """Custom type tnAccessPortFecType based on AluWdmFecMode"""
    defaultValue = 1


_TnAccessPortFecType_Type.__name__ = "AluWdmFecMode"
_TnAccessPortFecType_Object = MibTableColumn
tnAccessPortFecType = _TnAccessPortFecType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 46),
    _TnAccessPortFecType_Type()
)
tnAccessPortFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFecType.setStatus("current")


class _TnAccessPortFecBypassInd_Type(TruthValue):
    """Custom type tnAccessPortFecBypassInd based on TruthValue"""
    defaultValue = 2


_TnAccessPortFecBypassInd_Type.__name__ = "TruthValue"
_TnAccessPortFecBypassInd_Object = MibTableColumn
tnAccessPortFecBypassInd = _TnAccessPortFecBypassInd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 47),
    _TnAccessPortFecBypassInd_Type()
)
tnAccessPortFecBypassInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFecBypassInd.setStatus("current")


class _TnAccessPortCpriRole_Type(Integer32):
    """Custom type tnAccessPortCpriRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("none", 3))
    )


_TnAccessPortCpriRole_Type.__name__ = "Integer32"
_TnAccessPortCpriRole_Object = MibTableColumn
tnAccessPortCpriRole = _TnAccessPortCpriRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 48),
    _TnAccessPortCpriRole_Type()
)
tnAccessPortCpriRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortCpriRole.setStatus("current")


class _TnAccessPortAseMode_Type(Integer32):
    """Custom type tnAccessPortAseMode based on Integer32"""
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
        *(("unconfigured", 1),
          ("noNoise", 2),
          ("low", 3),
          ("standard", 4))
    )


_TnAccessPortAseMode_Type.__name__ = "Integer32"
_TnAccessPortAseMode_Object = MibTableColumn
tnAccessPortAseMode = _TnAccessPortAseMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 49),
    _TnAccessPortAseMode_Type()
)
tnAccessPortAseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAseMode.setStatus("current")


class _TnAccessPortRole_Type(Integer32):
    """Custom type tnAccessPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 1),
          ("in", 2),
          ("out", 3))
    )


_TnAccessPortRole_Type.__name__ = "Integer32"
_TnAccessPortRole_Object = MibTableColumn
tnAccessPortRole = _TnAccessPortRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 50),
    _TnAccessPortRole_Type()
)
tnAccessPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortRole.setStatus("current")


class _TnAccessPortFacilityDescriptorName_Type(SnmpAdminString):
    """Custom type tnAccessPortFacilityDescriptorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnAccessPortFacilityDescriptorName_Type.__name__ = "SnmpAdminString"
_TnAccessPortFacilityDescriptorName_Object = MibTableColumn
tnAccessPortFacilityDescriptorName = _TnAccessPortFacilityDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 51),
    _TnAccessPortFacilityDescriptorName_Type()
)
tnAccessPortFacilityDescriptorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFacilityDescriptorName.setStatus("current")


class _TnAccessPortFacilityDescriptorDesc_Type(SnmpAdminString):
    """Custom type tnAccessPortFacilityDescriptorDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAccessPortFacilityDescriptorDesc_Type.__name__ = "SnmpAdminString"
_TnAccessPortFacilityDescriptorDesc_Object = MibTableColumn
tnAccessPortFacilityDescriptorDesc = _TnAccessPortFacilityDescriptorDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 52),
    _TnAccessPortFacilityDescriptorDesc_Type()
)
tnAccessPortFacilityDescriptorDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFacilityDescriptorDesc.setStatus("current")


class _TnAccessPortFacilityDescriptorCirId_Type(SnmpAdminString):
    """Custom type tnAccessPortFacilityDescriptorCirId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnAccessPortFacilityDescriptorCirId_Type.__name__ = "SnmpAdminString"
_TnAccessPortFacilityDescriptorCirId_Object = MibTableColumn
tnAccessPortFacilityDescriptorCirId = _TnAccessPortFacilityDescriptorCirId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 53),
    _TnAccessPortFacilityDescriptorCirId_Type()
)
tnAccessPortFacilityDescriptorCirId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFacilityDescriptorCirId.setStatus("current")


class _TnAccessPortAlienWavebank_Type(TruthValue):
    """Custom type tnAccessPortAlienWavebank based on TruthValue"""
    defaultValue = 2


_TnAccessPortAlienWavebank_Type.__name__ = "TruthValue"
_TnAccessPortAlienWavebank_Object = MibTableColumn
tnAccessPortAlienWavebank = _TnAccessPortAlienWavebank_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 54),
    _TnAccessPortAlienWavebank_Type()
)
tnAccessPortAlienWavebank.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAlienWavebank.setStatus("current")


class _TnAccessPortModuleReset_Type(Integer32):
    """Custom type tnAccessPortModuleReset based on Integer32"""
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
        *(("noCmd", 1),
          ("warmReset", 2),
          ("coldReset", 3),
          ("forceReset", 4))
    )


_TnAccessPortModuleReset_Type.__name__ = "Integer32"
_TnAccessPortModuleReset_Object = MibTableColumn
tnAccessPortModuleReset = _TnAccessPortModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 55),
    _TnAccessPortModuleReset_Type()
)
tnAccessPortModuleReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortModuleReset.setStatus("current")


class _TnAccessPortFacilityDesCustLifeCycleState_Type(SnmpAdminString):
    """Custom type tnAccessPortFacilityDesCustLifeCycleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnAccessPortFacilityDesCustLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnAccessPortFacilityDesCustLifeCycleState_Object = MibTableColumn
tnAccessPortFacilityDesCustLifeCycleState = _TnAccessPortFacilityDesCustLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 56),
    _TnAccessPortFacilityDesCustLifeCycleState_Type()
)
tnAccessPortFacilityDesCustLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFacilityDesCustLifeCycleState.setStatus("current")
_TnAccessPortSummaryStatusLEDColor_Type = TropicLEDColorType
_TnAccessPortSummaryStatusLEDColor_Object = MibTableColumn
tnAccessPortSummaryStatusLEDColor = _TnAccessPortSummaryStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 57),
    _TnAccessPortSummaryStatusLEDColor_Type()
)
tnAccessPortSummaryStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortSummaryStatusLEDColor.setStatus("current")
_TnAccessPortSummaryStatusLEDState_Type = TropicLEDStateType
_TnAccessPortSummaryStatusLEDState_Object = MibTableColumn
tnAccessPortSummaryStatusLEDState = _TnAccessPortSummaryStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 58),
    _TnAccessPortSummaryStatusLEDState_Type()
)
tnAccessPortSummaryStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortSummaryStatusLEDState.setStatus("current")
_TnIfTable_Object = MibTable
tnIfTable = _TnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnIfTable.setStatus("current")
_TnIfEntry_Object = MibTableRow
tnIfEntry = _TnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnIfEntry.setStatus("current")
_TnIfPhysicalLocation_Type = InterfaceIndex
_TnIfPhysicalLocation_Object = MibTableColumn
tnIfPhysicalLocation = _TnIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 1),
    _TnIfPhysicalLocation_Type()
)
tnIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfPhysicalLocation.setStatus("current")
_TnIfType_Type = AluWdmTnIfType
_TnIfType_Object = MibTableColumn
tnIfType = _TnIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 2),
    _TnIfType_Type()
)
tnIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfType.setStatus("current")


class _TnIfSupportedTypes_Type(Bits):
    """Custom type tnIfSupportedTypes based on Bits"""
    namedValues = NamedValues(
        *(("oc3", 0),
          ("oc12", 1),
          ("oc48", 2),
          ("oc192", 3),
          ("ots", 4),
          ("och", 5),
          ("otu1", 6),
          ("otu2", 7),
          ("gige", 8),
          ("tenGige", 9),
          ("stm1", 10),
          ("stm4", 11),
          ("stm16", 12),
          ("stm64", 13),
          ("fc1g", 14),
          ("fc2g", 15),
          ("fc4g", 16),
          ("fc10g", 17),
          ("cbr2g5", 18),
          ("cbr10g", 19),
          ("anyRate", 20),
          ("hdSdi", 21),
          ("fe", 22),
          ("fddi", 23),
          ("esCon", 24),
          ("dvbAsi", 25),
          ("dvi6000", 26),
          ("otu3", 27),
          ("oc768", 28),
          ("stm256", 29),
          ("otu4", 30),
          ("fc8g", 31),
          ("hundredGige", 32),
          ("sdsdi", 33),
          ("e1", 34),
          ("sdi3g", 35),
          ("dcn", 36),
          ("evoa", 37),
          ("fee", 38),
          ("oduptf", 39),
          ("ds1", 40),
          ("otu3e2", 41),
          ("otu2e", 42),
          ("fortyGige", 43),
          ("sdr", 44),
          ("ddr", 45),
          ("tod", 46),
          ("lagGroup", 47),
          ("otl44", 48),
          ("fc16g", 49),
          ("qdr", 50),
          ("bits", 51),
          ("oneTru", 52),
          ("otu4x2", 53),
          ("otu1f", 54),
          ("cbr10g3", 55),
          ("fortyGigeMLD", 56),
          ("interLaken", 57),
          ("otl410", 58),
          ("otu4x4", 59),
          ("otu4Half", 60),
          ("otu4Halfx5", 61),
          ("sensor", 62),
          ("xfi", 63),
          ("caui", 64),
          ("otu2ewaneth", 65),
          ("otu4waneth", 66),
          ("tengigelaneth", 67),
          ("hundredGigeLaneth", 68),
          ("gigeConv", 69),
          ("otu2eeth", 70),
          ("gigelaneth", 71),
          ("felaneth", 72),
          ("ethman", 73),
          ("ilkpif", 74),
          ("feed", 75),
          ("otu2eNimEth", 76),
          ("twentyFiveGbeLaneth", 77),
          ("otu4x2waneth", 78),
          ("otsi", 79),
          ("fourHundredGige", 80),
          ("cpri3", 81),
          ("cpri5", 82),
          ("cpri6", 83),
          ("cpri7", 84),
          ("cpri8", 85),
          ("cpri10", 86),
          ("obsai8", 87),
          ("obsai4", 88),
          ("tfgige", 89),
          ("cauiV2", 90),
          ("fc32g", 91),
          ("otuc4mld", 92),
          ("equipment", 93),
          ("cpri4", 94),
          ("tengigelaneth2g5ce", 95))
    )

_TnIfSupportedTypes_Type.__name__ = "Bits"
_TnIfSupportedTypes_Object = MibTableColumn
tnIfSupportedTypes = _TnIfSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 3),
    _TnIfSupportedTypes_Type()
)
tnIfSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfSupportedTypes.setStatus("current")


class _TnIfSupportedTypesAlternate_Type(OctetString):
    """Custom type tnIfSupportedTypesAlternate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnIfSupportedTypesAlternate_Type.__name__ = "OctetString"
_TnIfSupportedTypesAlternate_Object = MibTableColumn
tnIfSupportedTypesAlternate = _TnIfSupportedTypesAlternate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 4),
    _TnIfSupportedTypesAlternate_Type()
)
tnIfSupportedTypesAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfSupportedTypesAlternate.setStatus("current")
_TnIfForceAdminStatus_Type = TnCommand
_TnIfForceAdminStatus_Object = MibTableColumn
tnIfForceAdminStatus = _TnIfForceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 5),
    _TnIfForceAdminStatus_Type()
)
tnIfForceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfForceAdminStatus.setStatus("current")


class _TnIfnumofTimeSlots_Type(Unsigned32):
    """Custom type tnIfnumofTimeSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_TnIfnumofTimeSlots_Type.__name__ = "Unsigned32"
_TnIfnumofTimeSlots_Object = MibTableColumn
tnIfnumofTimeSlots = _TnIfnumofTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 6),
    _TnIfnumofTimeSlots_Type()
)
tnIfnumofTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfnumofTimeSlots.setStatus("current")


class _TnIfAlmProfName_Type(OctetString):
    """Custom type tnIfAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnIfAlmProfName_Type.__name__ = "OctetString"
_TnIfAlmProfName_Object = MibTableColumn
tnIfAlmProfName = _TnIfAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 7),
    _TnIfAlmProfName_Type()
)
tnIfAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfAlmProfName.setStatus("current")
_TnAccessPortScalarObjs_ObjectIdentity = ObjectIdentity
tnAccessPortScalarObjs = _TnAccessPortScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3)
)
_TnSysTopology_ObjectIdentity = ObjectIdentity
tnSysTopology = _TnSysTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3, 1)
)


class _TnSysTopologyAudit_Type(SnmpAdminString):
    """Custom type tnSysTopologyAudit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTopologyAudit_Type.__name__ = "SnmpAdminString"
_TnSysTopologyAudit_Object = MibScalar
tnSysTopologyAudit = _TnSysTopologyAudit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3, 1, 1),
    _TnSysTopologyAudit_Type()
)
tnSysTopologyAudit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTopologyAudit.setStatus("current")
ifEntry.registerAugmentions(
    ("TROPIC-ACCESSPORT-MIB",
     "tnIfEntry")
)
tnIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

tnAccessPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 1)
)
tnAccessPortGroup.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnAccessPortDescr"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStatusLEDColor"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStatusLEDState"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortOperationalCapability"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStateQualifier"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndType"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortDirection"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINS"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINSDebounceTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortUsingSysAINSDebounceTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINSDebounceTimeRemaining"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsDomainEdgePort"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndAddressConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndIfIndexConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndTypeConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortExtAmpIpAddressIn"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortExtAmpIpAddressOut"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtocmConnLoss"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtocmConnAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortOppDirectionPortAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsValidInternalOTSXcEndpoint"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtDomainNumber"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortHasMpoConnector"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortMpoConnectorPortOutIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortMpoConnectorPortInIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsMpo"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortMonOcmConnAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAlmProfName"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortmfcTemperature"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortmfcNominalPressure"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortmfcDifferentialPressure"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterAmbientTemperature"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterPressure"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterRecorded"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterCalibrated"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterAltitude"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterRecordTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterCalibrateTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessFilterScheduledTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortL2FarEndIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortL2FarEndMacAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortDirectionCapability"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortCpriMappingType"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFecType"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFecBypassInd"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortCpriRole"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAseMode"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortRole"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFacilityDescriptorName"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFacilityDescriptorDesc"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFacilityDescriptorCirId"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAlienWavebank"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortModuleReset"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFacilityDesCustLifeCycleState"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortSummaryStatusLEDColor"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortSummaryStatusLEDState"))
)
if mibBuilder.loadTexts:
    tnAccessPortGroup.setStatus("current")

tnIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 2)
)
tnIfGroup.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnIfPhysicalLocation"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfType"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfSupportedTypes"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfSupportedTypesAlternate"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfForceAdminStatus"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfnumofTimeSlots"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfAlmProfName"))
)
if mibBuilder.loadTexts:
    tnIfGroup.setStatus("current")

tnSysTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 3)
)
tnSysTopologyGroup.setObjects(
    ("TROPIC-ACCESSPORT-MIB", "tnSysTopologyAudit")
)
if mibBuilder.loadTexts:
    tnSysTopologyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAccessPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 2, 1)
)
tnAccessPortCompliance.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnAccessPortGroup"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfGroup"),
        ("TROPIC-ACCESSPORT-MIB", "tnSysTopologyGroup"))
)
if mibBuilder.loadTexts:
    tnAccessPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ACCESSPORT-MIB",
    **{"tnAccessPortMibModules": tnAccessPortMibModules,
       "tnAccessPortConf": tnAccessPortConf,
       "tnAccessPortGroups": tnAccessPortGroups,
       "tnAccessPortGroup": tnAccessPortGroup,
       "tnIfGroup": tnIfGroup,
       "tnSysTopologyGroup": tnSysTopologyGroup,
       "tnAccessPortCompliances": tnAccessPortCompliances,
       "tnAccessPortCompliance": tnAccessPortCompliance,
       "tnAccessPortObjs": tnAccessPortObjs,
       "tnAccessPortTable": tnAccessPortTable,
       "tnAccessPortEntry": tnAccessPortEntry,
       "tnAccessPortDescr": tnAccessPortDescr,
       "tnAccessPortStatusLEDColor": tnAccessPortStatusLEDColor,
       "tnAccessPortStatusLEDState": tnAccessPortStatusLEDState,
       "tnAccessPortOperationalCapability": tnAccessPortOperationalCapability,
       "tnAccessPortStateQualifier": tnAccessPortStateQualifier,
       "tnAccessPortFarEndAddress": tnAccessPortFarEndAddress,
       "tnAccessPortFarEndIfIndex": tnAccessPortFarEndIfIndex,
       "tnAccessPortFarEndType": tnAccessPortFarEndType,
       "tnAccessPortDirection": tnAccessPortDirection,
       "tnAccessPortAINS": tnAccessPortAINS,
       "tnAccessPortAINSDebounceTime": tnAccessPortAINSDebounceTime,
       "tnAccessPortUsingSysAINSDebounceTime": tnAccessPortUsingSysAINSDebounceTime,
       "tnAccessPortAINSDebounceTimeRemaining": tnAccessPortAINSDebounceTimeRemaining,
       "tnAccessPortIsDomainEdgePort": tnAccessPortIsDomainEdgePort,
       "tnAccessPortFarEndAddressConnFrom": tnAccessPortFarEndAddressConnFrom,
       "tnAccessPortFarEndIfIndexConnFrom": tnAccessPortFarEndIfIndexConnFrom,
       "tnAccessPortFarEndTypeConnFrom": tnAccessPortFarEndTypeConnFrom,
       "tnAccessPortExtAmpIpAddressIn": tnAccessPortExtAmpIpAddressIn,
       "tnAccessPortExtAmpIpAddressOut": tnAccessPortExtAmpIpAddressOut,
       "tnAccessPortWtocmConnLoss": tnAccessPortWtocmConnLoss,
       "tnAccessPortWtocmConnAddress": tnAccessPortWtocmConnAddress,
       "tnAccessPortOppDirectionPortAddress": tnAccessPortOppDirectionPortAddress,
       "tnAccessPortIsValidInternalOTSXcEndpoint": tnAccessPortIsValidInternalOTSXcEndpoint,
       "tnAccessPortWtDomainNumber": tnAccessPortWtDomainNumber,
       "tnAccessPortHasMpoConnector": tnAccessPortHasMpoConnector,
       "tnAccessPortMpoConnectorPortOutIfIndex": tnAccessPortMpoConnectorPortOutIfIndex,
       "tnAccessPortMpoConnectorPortInIfIndex": tnAccessPortMpoConnectorPortInIfIndex,
       "tnAccessPortIsMpo": tnAccessPortIsMpo,
       "tnAccessPortMonOcmConnAddress": tnAccessPortMonOcmConnAddress,
       "tnAccessPortAlmProfName": tnAccessPortAlmProfName,
       "tnAccessPortmfcTemperature": tnAccessPortmfcTemperature,
       "tnAccessPortmfcNominalPressure": tnAccessPortmfcNominalPressure,
       "tnAccessPortmfcDifferentialPressure": tnAccessPortmfcDifferentialPressure,
       "tnAccessFilterAmbientTemperature": tnAccessFilterAmbientTemperature,
       "tnAccessFilterPressure": tnAccessFilterPressure,
       "tnAccessFilterRecorded": tnAccessFilterRecorded,
       "tnAccessFilterCalibrated": tnAccessFilterCalibrated,
       "tnAccessFilterAltitude": tnAccessFilterAltitude,
       "tnAccessFilterRecordTime": tnAccessFilterRecordTime,
       "tnAccessFilterCalibrateTime": tnAccessFilterCalibrateTime,
       "tnAccessFilterScheduledTime": tnAccessFilterScheduledTime,
       "tnAccessPortL2FarEndIfIndex": tnAccessPortL2FarEndIfIndex,
       "tnAccessPortL2FarEndMacAddress": tnAccessPortL2FarEndMacAddress,
       "tnAccessPortDirectionCapability": tnAccessPortDirectionCapability,
       "tnAccessPortCpriMappingType": tnAccessPortCpriMappingType,
       "tnAccessPortFecType": tnAccessPortFecType,
       "tnAccessPortFecBypassInd": tnAccessPortFecBypassInd,
       "tnAccessPortCpriRole": tnAccessPortCpriRole,
       "tnAccessPortAseMode": tnAccessPortAseMode,
       "tnAccessPortRole": tnAccessPortRole,
       "tnAccessPortFacilityDescriptorName": tnAccessPortFacilityDescriptorName,
       "tnAccessPortFacilityDescriptorDesc": tnAccessPortFacilityDescriptorDesc,
       "tnAccessPortFacilityDescriptorCirId": tnAccessPortFacilityDescriptorCirId,
       "tnAccessPortAlienWavebank": tnAccessPortAlienWavebank,
       "tnAccessPortModuleReset": tnAccessPortModuleReset,
       "tnAccessPortFacilityDesCustLifeCycleState": tnAccessPortFacilityDesCustLifeCycleState,
       "tnAccessPortSummaryStatusLEDColor": tnAccessPortSummaryStatusLEDColor,
       "tnAccessPortSummaryStatusLEDState": tnAccessPortSummaryStatusLEDState,
       "tnIfTable": tnIfTable,
       "tnIfEntry": tnIfEntry,
       "tnIfPhysicalLocation": tnIfPhysicalLocation,
       "tnIfType": tnIfType,
       "tnIfSupportedTypes": tnIfSupportedTypes,
       "tnIfSupportedTypesAlternate": tnIfSupportedTypesAlternate,
       "tnIfForceAdminStatus": tnIfForceAdminStatus,
       "tnIfnumofTimeSlots": tnIfnumofTimeSlots,
       "tnIfAlmProfName": tnIfAlmProfName,
       "tnAccessPortScalarObjs": tnAccessPortScalarObjs,
       "tnSysTopology": tnSysTopology,
       "tnSysTopologyAudit": tnSysTopologyAudit}
)
