# SNMP MIB module (LINKSYS-STORMCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-STORMCTRL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:02 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlStormCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77)
)
if mibBuilder.loadTexts:
    rlStormCtrl.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions



class RlStormCtrlRateUnit(Integer32):
    """Custom type RlStormCtrlRateUnit based on Integer32"""
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
        *(("packetsPerSecond", 1),
          ("bytesPerSecond", 2),
          ("framesPerBuffer", 3),
          ("precentages", 4),
          ("kiloBytesPerSecond", 5),
          ("kiloBitsPerSecond", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlStormCtrlSupport_Type = TruthValue
_RlStormCtrlSupport_Object = MibScalar
rlStormCtrlSupport = _RlStormCtrlSupport_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 1),
    _RlStormCtrlSupport_Type()
)
rlStormCtrlSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlSupport.setStatus("current")
_RlStormCtrlMibVersion_Type = Integer32
_RlStormCtrlMibVersion_Object = MibScalar
rlStormCtrlMibVersion = _RlStormCtrlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 2),
    _RlStormCtrlMibVersion_Type()
)
rlStormCtrlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlMibVersion.setStatus("current")


class _RlStormCtrlRateUnitTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlRateUnitTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlStormCtrlRateUnitTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlRateUnitTypeSupport_Object = MibScalar
rlStormCtrlRateUnitTypeSupport = _RlStormCtrlRateUnitTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 3),
    _RlStormCtrlRateUnitTypeSupport_Type()
)
rlStormCtrlRateUnitTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateUnitTypeSupport.setStatus("current")


class _RlStormCtrlTypeSupport_Type(OctetString):
    """Custom type rlStormCtrlTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlStormCtrlTypeSupport_Type.__name__ = "OctetString"
_RlStormCtrlTypeSupport_Object = MibScalar
rlStormCtrlTypeSupport = _RlStormCtrlTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 4),
    _RlStormCtrlTypeSupport_Type()
)
rlStormCtrlTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlTypeSupport.setStatus("current")


class _RlStormCtrlRateSupportPerType_Type(OctetString):
    """Custom type rlStormCtrlRateSupportPerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlStormCtrlRateSupportPerType_Type.__name__ = "OctetString"
_RlStormCtrlRateSupportPerType_Object = MibScalar
rlStormCtrlRateSupportPerType = _RlStormCtrlRateSupportPerType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 5),
    _RlStormCtrlRateSupportPerType_Type()
)
rlStormCtrlRateSupportPerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateSupportPerType.setStatus("current")


class _RlStormCtrlEnbaleDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlEnbaleDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlStormCtrlEnbaleDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlEnbaleDependencyBetweenTypes_Object = MibScalar
rlStormCtrlEnbaleDependencyBetweenTypes = _RlStormCtrlEnbaleDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 6),
    _RlStormCtrlEnbaleDependencyBetweenTypes_Type()
)
rlStormCtrlEnbaleDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlEnbaleDependencyBetweenTypes.setStatus("current")


class _RlStormCtrlRateDependencyBetweenTypes_Type(OctetString):
    """Custom type rlStormCtrlRateDependencyBetweenTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RlStormCtrlRateDependencyBetweenTypes_Type.__name__ = "OctetString"
_RlStormCtrlRateDependencyBetweenTypes_Object = MibScalar
rlStormCtrlRateDependencyBetweenTypes = _RlStormCtrlRateDependencyBetweenTypes_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 7),
    _RlStormCtrlRateDependencyBetweenTypes_Type()
)
rlStormCtrlRateDependencyBetweenTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlRateDependencyBetweenTypes.setStatus("current")
_RlStormCtrlTable_Object = MibTable
rlStormCtrlTable = _RlStormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8)
)
if mibBuilder.loadTexts:
    rlStormCtrlTable.setStatus("current")
_RlStormCtrlEntry_Object = MibTableRow
rlStormCtrlEntry = _RlStormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1)
)
rlStormCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlEntry.setStatus("current")
_RlStormCtrlRateType_Type = RlStormCtrlRateUnit
_RlStormCtrlRateType_Object = MibTableColumn
rlStormCtrlRateType = _RlStormCtrlRateType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 1),
    _RlStormCtrlRateType_Type()
)
rlStormCtrlRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlRateType.setStatus("current")


class _RlStormCtrlUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownUnicastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlUnknownUnicastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlUnknownUnicastEnable = _RlStormCtrlUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 2),
    _RlStormCtrlUnknownUnicastEnable_Type()
)
rlStormCtrlUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastEnable.setStatus("current")


class _RlStormCtrlUnknownUnicastRate_Type(Unsigned32):
    """Custom type rlStormCtrlUnknownUnicastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlUnknownUnicastRate_Type.__name__ = "Unsigned32"
_RlStormCtrlUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlUnknownUnicastRate = _RlStormCtrlUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 3),
    _RlStormCtrlUnknownUnicastRate_Type()
)
rlStormCtrlUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownUnicastRate.setStatus("current")


class _RlStormCtrlUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlUnknownMulticastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlUnknownMulticastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlUnknownMulticastEnable = _RlStormCtrlUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 4),
    _RlStormCtrlUnknownMulticastEnable_Type()
)
rlStormCtrlUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastEnable.setStatus("current")


class _RlStormCtrlUnknownMulticastRate_Type(Unsigned32):
    """Custom type rlStormCtrlUnknownMulticastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlUnknownMulticastRate_Type.__name__ = "Unsigned32"
_RlStormCtrlUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlUnknownMulticastRate = _RlStormCtrlUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 5),
    _RlStormCtrlUnknownMulticastRate_Type()
)
rlStormCtrlUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlUnknownMulticastRate.setStatus("current")


class _RlStormCtrlBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlBroadcastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlBroadcastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlBroadcastEnable_Object = MibTableColumn
rlStormCtrlBroadcastEnable = _RlStormCtrlBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 6),
    _RlStormCtrlBroadcastEnable_Type()
)
rlStormCtrlBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastEnable.setStatus("current")


class _RlStormCtrlBroadcastRate_Type(Unsigned32):
    """Custom type rlStormCtrlBroadcastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlBroadcastRate_Type.__name__ = "Unsigned32"
_RlStormCtrlBroadcastRate_Object = MibTableColumn
rlStormCtrlBroadcastRate = _RlStormCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 7),
    _RlStormCtrlBroadcastRate_Type()
)
rlStormCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastRate.setStatus("current")


class _RlStormCtrlMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlMulticastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlMulticastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlMulticastEnable_Object = MibTableColumn
rlStormCtrlMulticastEnable = _RlStormCtrlMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 8),
    _RlStormCtrlMulticastEnable_Type()
)
rlStormCtrlMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastEnable.setStatus("current")


class _RlStormCtrlMulticastRate_Type(Unsigned32):
    """Custom type rlStormCtrlMulticastRate based on Unsigned32"""
    defaultValue = 0


_RlStormCtrlMulticastRate_Type.__name__ = "Unsigned32"
_RlStormCtrlMulticastRate_Object = MibTableColumn
rlStormCtrlMulticastRate = _RlStormCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 9),
    _RlStormCtrlMulticastRate_Type()
)
rlStormCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlMulticastRate.setStatus("current")


class _RlStormCtrlSetDefaultRateType_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultRateType based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultRateType_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultRateType_Object = MibTableColumn
rlStormCtrlSetDefaultRateType = _RlStormCtrlSetDefaultRateType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 10),
    _RlStormCtrlSetDefaultRateType_Type()
)
rlStormCtrlSetDefaultRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultRateType.setStatus("current")


class _RlStormCtrlSetDefaultUnknownUnicastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultUnknownUnicastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultUnknownUnicastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastEnable = _RlStormCtrlSetDefaultUnknownUnicastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 11),
    _RlStormCtrlSetDefaultUnknownUnicastEnable_Type()
)
rlStormCtrlSetDefaultUnknownUnicastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastEnable.setStatus("current")


class _RlStormCtrlSetDefaultUnknownUnicastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownUnicastRate based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultUnknownUnicastRate_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultUnknownUnicastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownUnicastRate = _RlStormCtrlSetDefaultUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 12),
    _RlStormCtrlSetDefaultUnknownUnicastRate_Type()
)
rlStormCtrlSetDefaultUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownUnicastRate.setStatus("current")


class _RlStormCtrlSetDefaultUnknownMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultUnknownMulticastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultUnknownMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastEnable = _RlStormCtrlSetDefaultUnknownMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 13),
    _RlStormCtrlSetDefaultUnknownMulticastEnable_Type()
)
rlStormCtrlSetDefaultUnknownMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastEnable.setStatus("current")


class _RlStormCtrlSetDefaultUnknownMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultUnknownMulticastRate based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultUnknownMulticastRate_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultUnknownMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultUnknownMulticastRate = _RlStormCtrlSetDefaultUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 14),
    _RlStormCtrlSetDefaultUnknownMulticastRate_Type()
)
rlStormCtrlSetDefaultUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultUnknownMulticastRate.setStatus("current")


class _RlStormCtrlSetDefaultBroadcastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultBroadcastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultBroadcastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastEnable = _RlStormCtrlSetDefaultBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 15),
    _RlStormCtrlSetDefaultBroadcastEnable_Type()
)
rlStormCtrlSetDefaultBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastEnable.setStatus("current")


class _RlStormCtrlSetDefaultBroadcastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultBroadcastRate based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultBroadcastRate_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultBroadcastRate_Object = MibTableColumn
rlStormCtrlSetDefaultBroadcastRate = _RlStormCtrlSetDefaultBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 16),
    _RlStormCtrlSetDefaultBroadcastRate_Type()
)
rlStormCtrlSetDefaultBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultBroadcastRate.setStatus("current")


class _RlStormCtrlSetDefaultMulticastEnable_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastEnable based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultMulticastEnable_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultMulticastEnable_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastEnable = _RlStormCtrlSetDefaultMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 17),
    _RlStormCtrlSetDefaultMulticastEnable_Type()
)
rlStormCtrlSetDefaultMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastEnable.setStatus("current")


class _RlStormCtrlSetDefaultMulticastRate_Type(TruthValue):
    """Custom type rlStormCtrlSetDefaultMulticastRate based on TruthValue"""
    defaultValue = 2


_RlStormCtrlSetDefaultMulticastRate_Type.__name__ = "TruthValue"
_RlStormCtrlSetDefaultMulticastRate_Object = MibTableColumn
rlStormCtrlSetDefaultMulticastRate = _RlStormCtrlSetDefaultMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 18),
    _RlStormCtrlSetDefaultMulticastRate_Type()
)
rlStormCtrlSetDefaultMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlStormCtrlSetDefaultMulticastRate.setStatus("current")
_RlStormCtrlBroadcastOperRate_Type = Unsigned32
_RlStormCtrlBroadcastOperRate_Object = MibTableColumn
rlStormCtrlBroadcastOperRate = _RlStormCtrlBroadcastOperRate_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 8, 1, 19),
    _RlStormCtrlBroadcastOperRate_Type()
)
rlStormCtrlBroadcastOperRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlBroadcastOperRate.setStatus("current")
_RlStormCtrlGroupTable_Object = MibTable
rlStormCtrlGroupTable = _RlStormCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9)
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupTable.setStatus("current")
_RlStormCtrlGroupEntry_Object = MibTableRow
rlStormCtrlGroupEntry = _RlStormCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9, 1)
)
rlStormCtrlGroupEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlStormCtrlGroupEntry.setStatus("current")
_RlStormCtrlGroupUnknownUnicastId_Type = Integer32
_RlStormCtrlGroupUnknownUnicastId_Object = MibTableColumn
rlStormCtrlGroupUnknownUnicastId = _RlStormCtrlGroupUnknownUnicastId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9, 1, 1),
    _RlStormCtrlGroupUnknownUnicastId_Type()
)
rlStormCtrlGroupUnknownUnicastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownUnicastId.setStatus("current")
_RlStormCtrlGroupUnknownMulticastId_Type = Integer32
_RlStormCtrlGroupUnknownMulticastId_Object = MibTableColumn
rlStormCtrlGroupUnknownMulticastId = _RlStormCtrlGroupUnknownMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9, 1, 2),
    _RlStormCtrlGroupUnknownMulticastId_Type()
)
rlStormCtrlGroupUnknownMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupUnknownMulticastId.setStatus("current")
_RlStormCtrlGroupBroadcastId_Type = Integer32
_RlStormCtrlGroupBroadcastId_Object = MibTableColumn
rlStormCtrlGroupBroadcastId = _RlStormCtrlGroupBroadcastId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9, 1, 3),
    _RlStormCtrlGroupBroadcastId_Type()
)
rlStormCtrlGroupBroadcastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupBroadcastId.setStatus("current")
_RlStormCtrlGroupMulticastId_Type = Integer32
_RlStormCtrlGroupMulticastId_Object = MibTableColumn
rlStormCtrlGroupMulticastId = _RlStormCtrlGroupMulticastId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 77, 9, 1, 4),
    _RlStormCtrlGroupMulticastId_Type()
)
rlStormCtrlGroupMulticastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlStormCtrlGroupMulticastId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-STORMCTRL-MIB",
    **{"RlStormCtrlRateUnit": RlStormCtrlRateUnit,
       "rlStormCtrl": rlStormCtrl,
       "rlStormCtrlSupport": rlStormCtrlSupport,
       "rlStormCtrlMibVersion": rlStormCtrlMibVersion,
       "rlStormCtrlRateUnitTypeSupport": rlStormCtrlRateUnitTypeSupport,
       "rlStormCtrlTypeSupport": rlStormCtrlTypeSupport,
       "rlStormCtrlRateSupportPerType": rlStormCtrlRateSupportPerType,
       "rlStormCtrlEnbaleDependencyBetweenTypes": rlStormCtrlEnbaleDependencyBetweenTypes,
       "rlStormCtrlRateDependencyBetweenTypes": rlStormCtrlRateDependencyBetweenTypes,
       "rlStormCtrlTable": rlStormCtrlTable,
       "rlStormCtrlEntry": rlStormCtrlEntry,
       "rlStormCtrlRateType": rlStormCtrlRateType,
       "rlStormCtrlUnknownUnicastEnable": rlStormCtrlUnknownUnicastEnable,
       "rlStormCtrlUnknownUnicastRate": rlStormCtrlUnknownUnicastRate,
       "rlStormCtrlUnknownMulticastEnable": rlStormCtrlUnknownMulticastEnable,
       "rlStormCtrlUnknownMulticastRate": rlStormCtrlUnknownMulticastRate,
       "rlStormCtrlBroadcastEnable": rlStormCtrlBroadcastEnable,
       "rlStormCtrlBroadcastRate": rlStormCtrlBroadcastRate,
       "rlStormCtrlMulticastEnable": rlStormCtrlMulticastEnable,
       "rlStormCtrlMulticastRate": rlStormCtrlMulticastRate,
       "rlStormCtrlSetDefaultRateType": rlStormCtrlSetDefaultRateType,
       "rlStormCtrlSetDefaultUnknownUnicastEnable": rlStormCtrlSetDefaultUnknownUnicastEnable,
       "rlStormCtrlSetDefaultUnknownUnicastRate": rlStormCtrlSetDefaultUnknownUnicastRate,
       "rlStormCtrlSetDefaultUnknownMulticastEnable": rlStormCtrlSetDefaultUnknownMulticastEnable,
       "rlStormCtrlSetDefaultUnknownMulticastRate": rlStormCtrlSetDefaultUnknownMulticastRate,
       "rlStormCtrlSetDefaultBroadcastEnable": rlStormCtrlSetDefaultBroadcastEnable,
       "rlStormCtrlSetDefaultBroadcastRate": rlStormCtrlSetDefaultBroadcastRate,
       "rlStormCtrlSetDefaultMulticastEnable": rlStormCtrlSetDefaultMulticastEnable,
       "rlStormCtrlSetDefaultMulticastRate": rlStormCtrlSetDefaultMulticastRate,
       "rlStormCtrlBroadcastOperRate": rlStormCtrlBroadcastOperRate,
       "rlStormCtrlGroupTable": rlStormCtrlGroupTable,
       "rlStormCtrlGroupEntry": rlStormCtrlGroupEntry,
       "rlStormCtrlGroupUnknownUnicastId": rlStormCtrlGroupUnknownUnicastId,
       "rlStormCtrlGroupUnknownMulticastId": rlStormCtrlGroupUnknownMulticastId,
       "rlStormCtrlGroupBroadcastId": rlStormCtrlGroupBroadcastId,
       "rlStormCtrlGroupMulticastId": rlStormCtrlGroupMulticastId}
)
