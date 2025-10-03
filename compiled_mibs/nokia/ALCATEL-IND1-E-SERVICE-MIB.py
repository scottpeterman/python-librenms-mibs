# SNMP MIB module (ALCATEL-IND1-E-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-E-SERVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:17 2025
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

(softentIND1eService,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1eService")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1EServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIB.setRevisions(
        ("2010-01-20 00:00",
         "2009-12-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaEServiceUNIProfileProtocolTreatment(TextualConvention, Integer32):
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
        *(("tunnel", 1),
          ("drop", 2),
          ("peer", 3),
          ("macTunnel", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1eServiceMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1eServiceMIBObjects = _AlcatelIND1eServiceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1eServiceMIBObjects.setStatus("current")
_AlaEService_ObjectIdentity = ObjectIdentity
alaEService = _AlaEService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1)
)
_AlaEServiceInfo_ObjectIdentity = ObjectIdentity
alaEServiceInfo = _AlaEServiceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1)
)


class _AlaEServiceMode_Type(Integer32):
    """Custom type alaEServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacyMode", 1),
          ("eServiceMode", 2))
    )


_AlaEServiceMode_Type.__name__ = "Integer32"
_AlaEServiceMode_Object = MibScalar
alaEServiceMode = _AlaEServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 1),
    _AlaEServiceMode_Type()
)
alaEServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceMode.setStatus("current")


class _AlaEServiceStatReset_Type(Integer32):
    """Custom type alaEServiceStatReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceStatReset_Type.__name__ = "Integer32"
_AlaEServiceStatReset_Object = MibScalar
alaEServiceStatReset = _AlaEServiceStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 2),
    _AlaEServiceStatReset_Type()
)
alaEServiceStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceStatReset.setStatus("current")
_AlaEServiceSapProfileTable_Object = MibTable
alaEServiceSapProfileTable = _AlaEServiceSapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileTable.setStatus("current")
_AlaEServiceSapProfileEntry_Object = MibTableRow
alaEServiceSapProfileEntry = _AlaEServiceSapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1)
)
alaEServiceSapProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileEntry.setStatus("current")


class _AlaEServiceSapProfileID_Type(DisplayString):
    """Custom type alaEServiceSapProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceSapProfileID_Type.__name__ = "DisplayString"
_AlaEServiceSapProfileID_Object = MibTableColumn
alaEServiceSapProfileID = _AlaEServiceSapProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 1),
    _AlaEServiceSapProfileID_Type()
)
alaEServiceSapProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapProfileID.setStatus("current")


class _AlaEServiceSapProfileCVLANTreatment_Type(Integer32):
    """Custom type alaEServiceSapProfileCVLANTreatment based on Integer32"""
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
        *(("stackSVLAN", 1),
          ("translate", 2),
          ("changeCVLAN", 3))
    )


_AlaEServiceSapProfileCVLANTreatment_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCVLANTreatment_Object = MibTableColumn
alaEServiceSapProfileCVLANTreatment = _AlaEServiceSapProfileCVLANTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 2),
    _AlaEServiceSapProfileCVLANTreatment_Type()
)
alaEServiceSapProfileCVLANTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCVLANTreatment.setStatus("current")


class _AlaEServiceSapProfileReplacementCVLAN_Type(Integer32):
    """Custom type alaEServiceSapProfileReplacementCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSapProfileReplacementCVLAN_Type.__name__ = "Integer32"
_AlaEServiceSapProfileReplacementCVLAN_Object = MibTableColumn
alaEServiceSapProfileReplacementCVLAN = _AlaEServiceSapProfileReplacementCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 3),
    _AlaEServiceSapProfileReplacementCVLAN_Type()
)
alaEServiceSapProfileReplacementCVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileReplacementCVLAN.setStatus("current")


class _AlaEServiceSapProfilePriorityMapMode_Type(Integer32):
    """Custom type alaEServiceSapProfilePriorityMapMode based on Integer32"""
    defaultValue = 3

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
        *(("notAssigned", 0),
          ("mapInnerPtoOuterP", 1),
          ("mapInnerDscpToOuterP", 2),
          ("fixedP", 3))
    )


_AlaEServiceSapProfilePriorityMapMode_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePriorityMapMode_Object = MibTableColumn
alaEServiceSapProfilePriorityMapMode = _AlaEServiceSapProfilePriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 4),
    _AlaEServiceSapProfilePriorityMapMode_Type()
)
alaEServiceSapProfilePriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePriorityMapMode.setStatus("current")


class _AlaEServiceSapProfileFixedPriority_Type(Integer32):
    """Custom type alaEServiceSapProfileFixedPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaEServiceSapProfileFixedPriority_Type.__name__ = "Integer32"
_AlaEServiceSapProfileFixedPriority_Object = MibTableColumn
alaEServiceSapProfileFixedPriority = _AlaEServiceSapProfileFixedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 5),
    _AlaEServiceSapProfileFixedPriority_Type()
)
alaEServiceSapProfileFixedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileFixedPriority.setStatus("current")
_AlaEServiceSapProfileIngressBW_Type = Integer32
_AlaEServiceSapProfileIngressBW_Object = MibTableColumn
alaEServiceSapProfileIngressBW = _AlaEServiceSapProfileIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 6),
    _AlaEServiceSapProfileIngressBW_Type()
)
alaEServiceSapProfileIngressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileIngressBW.setStatus("current")


class _AlaEServiceSapProfileBandwidthShare_Type(Integer32):
    """Custom type alaEServiceSapProfileBandwidthShare based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 0),
          ("shared", 1),
          ("notShared", 2),
          ("notAssigned", 3))
    )


_AlaEServiceSapProfileBandwidthShare_Type.__name__ = "Integer32"
_AlaEServiceSapProfileBandwidthShare_Object = MibTableColumn
alaEServiceSapProfileBandwidthShare = _AlaEServiceSapProfileBandwidthShare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 7),
    _AlaEServiceSapProfileBandwidthShare_Type()
)
alaEServiceSapProfileBandwidthShare.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileBandwidthShare.setStatus("current")
_AlaEServiceSapProfileRowStatus_Type = RowStatus
_AlaEServiceSapProfileRowStatus_Object = MibTableColumn
alaEServiceSapProfileRowStatus = _AlaEServiceSapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 8),
    _AlaEServiceSapProfileRowStatus_Type()
)
alaEServiceSapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileRowStatus.setStatus("current")


class _AlaEServiceSapProfileEgressBW_Type(Integer32):
    """Custom type alaEServiceSapProfileEgressBW based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileEgressBW_Type.__name__ = "Integer32"
_AlaEServiceSapProfileEgressBW_Object = MibTableColumn
alaEServiceSapProfileEgressBW = _AlaEServiceSapProfileEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 9),
    _AlaEServiceSapProfileEgressBW_Type()
)
alaEServiceSapProfileEgressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileEgressBW.setStatus("current")


class _AlaEServiceSapProfileCIR_Type(Integer32):
    """Custom type alaEServiceSapProfileCIR based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileCIR_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCIR_Object = MibTableColumn
alaEServiceSapProfileCIR = _AlaEServiceSapProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 10),
    _AlaEServiceSapProfileCIR_Type()
)
alaEServiceSapProfileCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCIR.setStatus("current")


class _AlaEServiceSapProfileCBS_Type(Integer32):
    """Custom type alaEServiceSapProfileCBS based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileCBS_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCBS_Object = MibTableColumn
alaEServiceSapProfileCBS = _AlaEServiceSapProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 11),
    _AlaEServiceSapProfileCBS_Type()
)
alaEServiceSapProfileCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCBS.setStatus("current")


class _AlaEServiceSapProfilePIR_Type(Integer32):
    """Custom type alaEServiceSapProfilePIR based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfilePIR_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePIR_Object = MibTableColumn
alaEServiceSapProfilePIR = _AlaEServiceSapProfilePIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 12),
    _AlaEServiceSapProfilePIR_Type()
)
alaEServiceSapProfilePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePIR.setStatus("current")


class _AlaEServiceSapProfilePBS_Type(Integer32):
    """Custom type alaEServiceSapProfilePBS based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfilePBS_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePBS_Object = MibTableColumn
alaEServiceSapProfilePBS = _AlaEServiceSapProfilePBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 13),
    _AlaEServiceSapProfilePBS_Type()
)
alaEServiceSapProfilePBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePBS.setStatus("current")
_AlaEServiceUNIProfileTable_Object = MibTable
alaEServiceUNIProfileTable = _AlaEServiceUNIProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileTable.setStatus("current")
_AlaEServiceUNIProfileEntry_Object = MibTableRow
alaEServiceUNIProfileEntry = _AlaEServiceUNIProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1)
)
alaEServiceUNIProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileEntry.setStatus("current")


class _AlaEServiceUNIProfileID_Type(DisplayString):
    """Custom type alaEServiceUNIProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileID_Type.__name__ = "DisplayString"
_AlaEServiceUNIProfileID_Object = MibTableColumn
alaEServiceUNIProfileID = _AlaEServiceUNIProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 1),
    _AlaEServiceUNIProfileID_Type()
)
alaEServiceUNIProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileID.setStatus("current")


class _AlaEServiceUNIProfileStpBpduTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileStpBpduTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileStpBpduTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileStpBpduTreatment_Object = MibTableColumn
alaEServiceUNIProfileStpBpduTreatment = _AlaEServiceUNIProfileStpBpduTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 2),
    _AlaEServiceUNIProfileStpBpduTreatment_Type()
)
alaEServiceUNIProfileStpBpduTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileStpBpduTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021xTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021xTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfile8021xTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8021xTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021xTreatment = _AlaEServiceUNIProfile8021xTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 3),
    _AlaEServiceUNIProfile8021xTreatment_Type()
)
alaEServiceUNIProfile8021xTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021xTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021ABTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021ABTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfile8021ABTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8021ABTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021ABTreatment = _AlaEServiceUNIProfile8021ABTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 4),
    _AlaEServiceUNIProfile8021ABTreatment_Type()
)
alaEServiceUNIProfile8021ABTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021ABTreatment.setStatus("current")


class _AlaEServiceUNIProfile8023adTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8023adTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfile8023adTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8023adTreatment_Object = MibTableColumn
alaEServiceUNIProfile8023adTreatment = _AlaEServiceUNIProfile8023adTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 5),
    _AlaEServiceUNIProfile8023adTreatment_Type()
)
alaEServiceUNIProfile8023adTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8023adTreatment.setStatus("current")


class _AlaEServiceUNIProfileGvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileGvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileGvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileGvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileGvrpTreatment = _AlaEServiceUNIProfileGvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 6),
    _AlaEServiceUNIProfileGvrpTreatment_Type()
)
alaEServiceUNIProfileGvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGvrpTreatment.setStatus("current")


class _AlaEServiceUNIProfileAmapTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileAmapTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileAmapTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileAmapTreatment_Object = MibTableColumn
alaEServiceUNIProfileAmapTreatment = _AlaEServiceUNIProfileAmapTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 7),
    _AlaEServiceUNIProfileAmapTreatment_Type()
)
alaEServiceUNIProfileAmapTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileAmapTreatment.setStatus("current")
_AlaEServiceUNIProfileRowStatus_Type = RowStatus
_AlaEServiceUNIProfileRowStatus_Object = MibTableColumn
alaEServiceUNIProfileRowStatus = _AlaEServiceUNIProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 8),
    _AlaEServiceUNIProfileRowStatus_Type()
)
alaEServiceUNIProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileRowStatus.setStatus("current")


class _AlaEServiceUNIProfileMvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileMvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileMvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileMvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileMvrpTreatment = _AlaEServiceUNIProfileMvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 9),
    _AlaEServiceUNIProfileMvrpTreatment_Type()
)
alaEServiceUNIProfileMvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileMvrpTreatment.setStatus("current")
_AlaEServiceUNIProfileTunnelMac_Type = MacAddress
_AlaEServiceUNIProfileTunnelMac_Object = MibTableColumn
alaEServiceUNIProfileTunnelMac = _AlaEServiceUNIProfileTunnelMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 10),
    _AlaEServiceUNIProfileTunnelMac_Type()
)
alaEServiceUNIProfileTunnelMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileTunnelMac.setStatus("current")


class _AlaEServiceUNIProfileLacpMarkerTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileLacpMarkerTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfileLacpMarkerTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileLacpMarkerTreatment_Object = MibTableColumn
alaEServiceUNIProfileLacpMarkerTreatment = _AlaEServiceUNIProfileLacpMarkerTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 11),
    _AlaEServiceUNIProfileLacpMarkerTreatment_Type()
)
alaEServiceUNIProfileLacpMarkerTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileLacpMarkerTreatment.setStatus("current")


class _AlaEServiceUNIProfileOamTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileOamTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfileOamTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileOamTreatment_Object = MibTableColumn
alaEServiceUNIProfileOamTreatment = _AlaEServiceUNIProfileOamTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 12),
    _AlaEServiceUNIProfileOamTreatment_Type()
)
alaEServiceUNIProfileOamTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileOamTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoPagpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoPagpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoPagpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoPagpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoPagpTreatment = _AlaEServiceUNIProfileCiscoPagpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 13),
    _AlaEServiceUNIProfileCiscoPagpTreatment_Type()
)
alaEServiceUNIProfileCiscoPagpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoPagpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoUdldTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoUdldTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoUdldTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoUdldTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoUdldTreatment = _AlaEServiceUNIProfileCiscoUdldTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 14),
    _AlaEServiceUNIProfileCiscoUdldTreatment_Type()
)
alaEServiceUNIProfileCiscoUdldTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoUdldTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoCdpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoCdpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoCdpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoCdpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoCdpTreatment = _AlaEServiceUNIProfileCiscoCdpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 15),
    _AlaEServiceUNIProfileCiscoCdpTreatment_Type()
)
alaEServiceUNIProfileCiscoCdpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoCdpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoVtpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoVtpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoVtpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoVtpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoVtpTreatment = _AlaEServiceUNIProfileCiscoVtpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 16),
    _AlaEServiceUNIProfileCiscoVtpTreatment_Type()
)
alaEServiceUNIProfileCiscoVtpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoVtpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoDtpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoDtpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoDtpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoDtpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoDtpTreatment = _AlaEServiceUNIProfileCiscoDtpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 17),
    _AlaEServiceUNIProfileCiscoDtpTreatment_Type()
)
alaEServiceUNIProfileCiscoDtpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoDtpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoPvstTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoPvstTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoPvstTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoPvstTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoPvstTreatment = _AlaEServiceUNIProfileCiscoPvstTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 18),
    _AlaEServiceUNIProfileCiscoPvstTreatment_Type()
)
alaEServiceUNIProfileCiscoPvstTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoPvstTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoVlanTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoVlanTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoVlanTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoVlanTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoVlanTreatment = _AlaEServiceUNIProfileCiscoVlanTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 19),
    _AlaEServiceUNIProfileCiscoVlanTreatment_Type()
)
alaEServiceUNIProfileCiscoVlanTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoVlanTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoUplinkTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoUplinkTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoUplinkTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoUplinkTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoUplinkTreatment = _AlaEServiceUNIProfileCiscoUplinkTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 20),
    _AlaEServiceUNIProfileCiscoUplinkTreatment_Type()
)
alaEServiceUNIProfileCiscoUplinkTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoUplinkTreatment.setStatus("current")
_AlaEServiceTable_Object = MibTable
alaEServiceTable = _AlaEServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaEServiceTable.setStatus("current")
_AlaEServiceEntry_Object = MibTableRow
alaEServiceEntry = _AlaEServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1)
)
alaEServiceEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceID"),
)
if mibBuilder.loadTexts:
    alaEServiceEntry.setStatus("current")


class _AlaEServiceID_Type(DisplayString):
    """Custom type alaEServiceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceID_Type.__name__ = "DisplayString"
_AlaEServiceID_Object = MibTableColumn
alaEServiceID = _AlaEServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 1),
    _AlaEServiceID_Type()
)
alaEServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceID.setStatus("current")


class _AlaEServiceSVLAN_Type(Integer32):
    """Custom type alaEServiceSVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSVLAN_Type.__name__ = "Integer32"
_AlaEServiceSVLAN_Object = MibTableColumn
alaEServiceSVLAN = _AlaEServiceSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 2),
    _AlaEServiceSVLAN_Type()
)
alaEServiceSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSVLAN.setStatus("current")


class _AlaEServiceVlanType_Type(Integer32):
    """Custom type alaEServiceVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("svlan", 1),
          ("ipmvlan", 2))
    )


_AlaEServiceVlanType_Type.__name__ = "Integer32"
_AlaEServiceVlanType_Object = MibTableColumn
alaEServiceVlanType = _AlaEServiceVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 3),
    _AlaEServiceVlanType_Type()
)
alaEServiceVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceVlanType.setStatus("current")
_AlaEServiceRowStatus_Type = RowStatus
_AlaEServiceRowStatus_Object = MibTableColumn
alaEServiceRowStatus = _AlaEServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 4),
    _AlaEServiceRowStatus_Type()
)
alaEServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceRowStatus.setStatus("current")
_AlaEServiceStatGreenCount_Type = Counter64
_AlaEServiceStatGreenCount_Object = MibTableColumn
alaEServiceStatGreenCount = _AlaEServiceStatGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 5),
    _AlaEServiceStatGreenCount_Type()
)
alaEServiceStatGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatGreenCount.setStatus("current")
_AlaEServiceStatYellowCount_Type = Counter64
_AlaEServiceStatYellowCount_Object = MibTableColumn
alaEServiceStatYellowCount = _AlaEServiceStatYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 6),
    _AlaEServiceStatYellowCount_Type()
)
alaEServiceStatYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatYellowCount.setStatus("current")
_AlaEServiceStatRedCount_Type = Counter64
_AlaEServiceStatRedCount_Object = MibTableColumn
alaEServiceStatRedCount = _AlaEServiceStatRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 7),
    _AlaEServiceStatRedCount_Type()
)
alaEServiceStatRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatRedCount.setStatus("current")
_AlaEServiceSapTable_Object = MibTable
alaEServiceSapTable = _AlaEServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaEServiceSapTable.setStatus("current")
_AlaEServiceSapEntry_Object = MibTableRow
alaEServiceSapEntry = _AlaEServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1)
)
alaEServiceSapEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapEntry.setStatus("current")
_AlaEServiceSapID_Type = Integer32
_AlaEServiceSapID_Object = MibTableColumn
alaEServiceSapID = _AlaEServiceSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 1),
    _AlaEServiceSapID_Type()
)
alaEServiceSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapID.setStatus("current")


class _AlaEServiceSapServiceID_Type(DisplayString):
    """Custom type alaEServiceSapServiceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapServiceID_Type.__name__ = "DisplayString"
_AlaEServiceSapServiceID_Object = MibTableColumn
alaEServiceSapServiceID = _AlaEServiceSapServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 2),
    _AlaEServiceSapServiceID_Type()
)
alaEServiceSapServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapServiceID.setStatus("current")


class _AlaEServiceSapProfile_Type(DisplayString):
    """Custom type alaEServiceSapProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapProfile_Type.__name__ = "DisplayString"
_AlaEServiceSapProfile_Object = MibTableColumn
alaEServiceSapProfile = _AlaEServiceSapProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 3),
    _AlaEServiceSapProfile_Type()
)
alaEServiceSapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfile.setStatus("current")
_AlaEServiceSapRowStatus_Type = RowStatus
_AlaEServiceSapRowStatus_Object = MibTableColumn
alaEServiceSapRowStatus = _AlaEServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 4),
    _AlaEServiceSapRowStatus_Type()
)
alaEServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapRowStatus.setStatus("current")
_AlaEServiceSapCvlanTable_Object = MibTable
alaEServiceSapCvlanTable = _AlaEServiceSapCvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanTable.setStatus("current")
_AlaEServiceSapCvlanEntry_Object = MibTableRow
alaEServiceSapCvlanEntry = _AlaEServiceSapCvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1)
)
alaEServiceSapCvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanSapID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanCvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanEntry.setStatus("current")
_AlaEServiceSapCvlanSapID_Type = Integer32
_AlaEServiceSapCvlanSapID_Object = MibTableColumn
alaEServiceSapCvlanSapID = _AlaEServiceSapCvlanSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 1),
    _AlaEServiceSapCvlanSapID_Type()
)
alaEServiceSapCvlanSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanSapID.setStatus("current")


class _AlaEServiceSapCvlanCvlan_Type(Integer32):
    """Custom type alaEServiceSapCvlanCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaEServiceSapCvlanCvlan_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanCvlan_Object = MibTableColumn
alaEServiceSapCvlanCvlan = _AlaEServiceSapCvlanCvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 2),
    _AlaEServiceSapCvlanCvlan_Type()
)
alaEServiceSapCvlanCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanCvlan.setStatus("current")


class _AlaEServiceSapCvlanMapType_Type(Integer32):
    """Custom type alaEServiceSapCvlanMapType based on Integer32"""
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
        *(("single", 1),
          ("all", 2),
          ("untaggedOnly", 3))
    )


_AlaEServiceSapCvlanMapType_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanMapType_Object = MibTableColumn
alaEServiceSapCvlanMapType = _AlaEServiceSapCvlanMapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 3),
    _AlaEServiceSapCvlanMapType_Type()
)
alaEServiceSapCvlanMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanMapType.setStatus("current")
_AlaEServiceSapCvlanRowStatus_Type = RowStatus
_AlaEServiceSapCvlanRowStatus_Object = MibTableColumn
alaEServiceSapCvlanRowStatus = _AlaEServiceSapCvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 4),
    _AlaEServiceSapCvlanRowStatus_Type()
)
alaEServiceSapCvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanRowStatus.setStatus("current")
_AlaEServicePortTable_Object = MibTable
alaEServicePortTable = _AlaEServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaEServicePortTable.setStatus("current")
_AlaEServicePortEntry_Object = MibTableRow
alaEServicePortEntry = _AlaEServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1)
)
alaEServicePortEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortID"),
)
if mibBuilder.loadTexts:
    alaEServicePortEntry.setStatus("current")
_AlaEServicePortID_Type = InterfaceIndex
_AlaEServicePortID_Object = MibTableColumn
alaEServicePortID = _AlaEServicePortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 1),
    _AlaEServicePortID_Type()
)
alaEServicePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServicePortID.setStatus("current")


class _AlaEServicePortType_Type(Integer32):
    """Custom type alaEServicePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni", 1),
          ("nni", 3))
    )


_AlaEServicePortType_Type.__name__ = "Integer32"
_AlaEServicePortType_Object = MibTableColumn
alaEServicePortType = _AlaEServicePortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 2),
    _AlaEServicePortType_Type()
)
alaEServicePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortType.setStatus("current")


class _AlaEServicePortVendorTpid_Type(Integer32):
    """Custom type alaEServicePortVendorTpid based on Integer32"""
    defaultValue = 33024


_AlaEServicePortVendorTpid_Type.__name__ = "Integer32"
_AlaEServicePortVendorTpid_Object = MibTableColumn
alaEServicePortVendorTpid = _AlaEServicePortVendorTpid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 3),
    _AlaEServicePortVendorTpid_Type()
)
alaEServicePortVendorTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortVendorTpid.setStatus("current")


class _AlaEServicePortLegacyStpBpdu_Type(Integer32):
    """Custom type alaEServicePortLegacyStpBpdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyStpBpdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyStpBpdu_Object = MibTableColumn
alaEServicePortLegacyStpBpdu = _AlaEServicePortLegacyStpBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 4),
    _AlaEServicePortLegacyStpBpdu_Type()
)
alaEServicePortLegacyStpBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyStpBpdu.setStatus("current")


class _AlaEServicePortLegacyGvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyGvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyGvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyGvrpPdu_Object = MibTableColumn
alaEServicePortLegacyGvrpPdu = _AlaEServicePortLegacyGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 5),
    _AlaEServicePortLegacyGvrpPdu_Type()
)
alaEServicePortLegacyGvrpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyGvrpPdu.setStatus("current")


class _AlaEServicePortUniProfile_Type(DisplayString):
    """Custom type alaEServicePortUniProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServicePortUniProfile_Type.__name__ = "DisplayString"
_AlaEServicePortUniProfile_Object = MibTableColumn
alaEServicePortUniProfile = _AlaEServicePortUniProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 6),
    _AlaEServicePortUniProfile_Type()
)
alaEServicePortUniProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortUniProfile.setStatus("current")


class _AlaEServicePortTransBridging_Type(Integer32):
    """Custom type alaEServicePortTransBridging based on Integer32"""
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


_AlaEServicePortTransBridging_Type.__name__ = "Integer32"
_AlaEServicePortTransBridging_Object = MibTableColumn
alaEServicePortTransBridging = _AlaEServicePortTransBridging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 7),
    _AlaEServicePortTransBridging_Type()
)
alaEServicePortTransBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortTransBridging.setStatus("current")


class _AlaEServicePortLegacyMvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyMvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyMvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyMvrpPdu_Object = MibTableColumn
alaEServicePortLegacyMvrpPdu = _AlaEServicePortLegacyMvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 8),
    _AlaEServicePortLegacyMvrpPdu_Type()
)
alaEServicePortLegacyMvrpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyMvrpPdu.setStatus("current")
_AlaEServiceSapUniTable_Object = MibTable
alaEServiceSapUniTable = _AlaEServiceSapUniTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaEServiceSapUniTable.setStatus("current")
_AlaEServiceSapUniEntry_Object = MibTableRow
alaEServiceSapUniEntry = _AlaEServiceSapUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1)
)
alaEServiceSapUniEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniSap"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniUni"),
)
if mibBuilder.loadTexts:
    alaEServiceSapUniEntry.setStatus("current")
_AlaEServiceSapUniSap_Type = Integer32
_AlaEServiceSapUniSap_Object = MibTableColumn
alaEServiceSapUniSap = _AlaEServiceSapUniSap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 1),
    _AlaEServiceSapUniSap_Type()
)
alaEServiceSapUniSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniSap.setStatus("current")
_AlaEServiceSapUniUni_Type = InterfaceIndex
_AlaEServiceSapUniUni_Object = MibTableColumn
alaEServiceSapUniUni = _AlaEServiceSapUniUni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 2),
    _AlaEServiceSapUniUni_Type()
)
alaEServiceSapUniUni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniUni.setStatus("current")
_AlaEServiceSapUniRowStatus_Type = RowStatus
_AlaEServiceSapUniRowStatus_Object = MibTableColumn
alaEServiceSapUniRowStatus = _AlaEServiceSapUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 3),
    _AlaEServiceSapUniRowStatus_Type()
)
alaEServiceSapUniRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapUniRowStatus.setStatus("current")
_AlaEServiceNniSvlanTable_Object = MibTable
alaEServiceNniSvlanTable = _AlaEServiceNniSvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanTable.setStatus("current")
_AlaEServiceNniSvlanEntry_Object = MibTableRow
alaEServiceNniSvlanEntry = _AlaEServiceNniSvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1)
)
alaEServiceNniSvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanNni"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanSvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanEntry.setStatus("current")
_AlaEServiceNniSvlanNni_Type = InterfaceIndex
_AlaEServiceNniSvlanNni_Object = MibTableColumn
alaEServiceNniSvlanNni = _AlaEServiceNniSvlanNni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 1),
    _AlaEServiceNniSvlanNni_Type()
)
alaEServiceNniSvlanNni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanNni.setStatus("current")


class _AlaEServiceNniSvlanSvlan_Type(Integer32):
    """Custom type alaEServiceNniSvlanSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaEServiceNniSvlanSvlan_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanSvlan_Object = MibTableColumn
alaEServiceNniSvlanSvlan = _AlaEServiceNniSvlanSvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 2),
    _AlaEServiceNniSvlanSvlan_Type()
)
alaEServiceNniSvlanSvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanSvlan.setStatus("current")
_AlaEServiceNniSvlanRowStatus_Type = RowStatus
_AlaEServiceNniSvlanRowStatus_Object = MibTableColumn
alaEServiceNniSvlanRowStatus = _AlaEServiceNniSvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 3),
    _AlaEServiceNniSvlanRowStatus_Type()
)
alaEServiceNniSvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanRowStatus.setStatus("current")


class _AlaEServiceNniSvlanVpaType_Type(Integer32):
    """Custom type alaEServiceNniSvlanVpaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("erp", 2))
    )


_AlaEServiceNniSvlanVpaType_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanVpaType_Object = MibTableColumn
alaEServiceNniSvlanVpaType = _AlaEServiceNniSvlanVpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 4),
    _AlaEServiceNniSvlanVpaType_Type()
)
alaEServiceNniSvlanVpaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanVpaType.setStatus("current")
_AlaEServiceSapCvlanPortStatTable_Object = MibTable
alaEServiceSapCvlanPortStatTable = _AlaEServiceSapCvlanPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatTable.setStatus("current")
_AlaEServiceSapCvlanPortStatEntry_Object = MibTableRow
alaEServiceSapCvlanPortStatEntry = _AlaEServiceSapCvlanPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1)
)
alaEServiceSapCvlanPortStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatSapID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatCvlanID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatPortID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatEntry.setStatus("current")
_AlaEServiceSapCvlanPortStatSapID_Type = Integer32
_AlaEServiceSapCvlanPortStatSapID_Object = MibTableColumn
alaEServiceSapCvlanPortStatSapID = _AlaEServiceSapCvlanPortStatSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 1),
    _AlaEServiceSapCvlanPortStatSapID_Type()
)
alaEServiceSapCvlanPortStatSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatSapID.setStatus("current")


class _AlaEServiceSapCvlanPortStatCvlanID_Type(Integer32):
    """Custom type alaEServiceSapCvlanPortStatCvlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaEServiceSapCvlanPortStatCvlanID_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanPortStatCvlanID_Object = MibTableColumn
alaEServiceSapCvlanPortStatCvlanID = _AlaEServiceSapCvlanPortStatCvlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 2),
    _AlaEServiceSapCvlanPortStatCvlanID_Type()
)
alaEServiceSapCvlanPortStatCvlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatCvlanID.setStatus("current")
_AlaEServiceSapCvlanPortStatPortID_Type = InterfaceIndex
_AlaEServiceSapCvlanPortStatPortID_Object = MibTableColumn
alaEServiceSapCvlanPortStatPortID = _AlaEServiceSapCvlanPortStatPortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 3),
    _AlaEServiceSapCvlanPortStatPortID_Type()
)
alaEServiceSapCvlanPortStatPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatPortID.setStatus("current")
_AlaEServiceSapCvlanPortStatGreenCount_Type = Counter64
_AlaEServiceSapCvlanPortStatGreenCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatGreenCount = _AlaEServiceSapCvlanPortStatGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 4),
    _AlaEServiceSapCvlanPortStatGreenCount_Type()
)
alaEServiceSapCvlanPortStatGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatGreenCount.setStatus("current")
_AlaEServiceSapCvlanPortStatYellowCount_Type = Counter64
_AlaEServiceSapCvlanPortStatYellowCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatYellowCount = _AlaEServiceSapCvlanPortStatYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 5),
    _AlaEServiceSapCvlanPortStatYellowCount_Type()
)
alaEServiceSapCvlanPortStatYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatYellowCount.setStatus("current")
_AlaEServiceSapCvlanPortStatRedCount_Type = Counter64
_AlaEServiceSapCvlanPortStatRedCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatRedCount = _AlaEServiceSapCvlanPortStatRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 6),
    _AlaEServiceSapCvlanPortStatRedCount_Type()
)
alaEServiceSapCvlanPortStatRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatRedCount.setStatus("current")
_AlcatelIND1EServiceMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBConformance = _AlcatelIND1EServiceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBConformance.setStatus("current")
_AlcatelIND1EServiceMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBGroups = _AlcatelIND1EServiceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBGroups.setStatus("current")
_AlcatelIND1EServiceMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBCompliances = _AlcatelIND1EServiceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliances.setStatus("current")

# Managed Objects groups

alaEServiceSapProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 1)
)
alaEServiceSapProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCVLANTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileReplacementCVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePriorityMapMode"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileFixedPriority"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileIngressBW"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileBandwidthShare"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileEgressBW"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCIR"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCBS"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePIR"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePBS"))
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileGroup.setStatus("current")

alaEServiceUNIProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 2)
)
alaEServiceUNIProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileStpBpduTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021xTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021ABTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8023adTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileGvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileAmapTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileMvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileTunnelMac"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileLacpMarkerTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileOamTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoPagpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoUdldTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoCdpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoVtpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoDtpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoPvstTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoVlanTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoUplinkTreatment"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGroup.setStatus("current")

alaEServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 3)
)
alaEServiceGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceVlanType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatGreenCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatYellowCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatRedCount"))
)
if mibBuilder.loadTexts:
    alaEServiceGroup.setStatus("current")

alaEServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 4)
)
alaEServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapServiceID"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapGroup.setStatus("current")

alaEServiceSapCvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 5)
)
alaEServiceSapCvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanMapType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanGroup.setStatus("current")

alaEServicePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 6)
)
alaEServicePortGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortVendorTpid"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyStpBpdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyGvrpPdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortUniProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortTransBridging"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyMvrpPdu"))
)
if mibBuilder.loadTexts:
    alaEServicePortGroup.setStatus("current")

alaEServiceSapUniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 7)
)
alaEServiceSapUniGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniRowStatus")
)
if mibBuilder.loadTexts:
    alaEServiceSapUniGroup.setStatus("current")

alaEServiceNniSvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 8)
)
alaEServiceNniSvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanVpaType"))
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanGroup.setStatus("current")

alaEServiceSapCvlanPortStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 9)
)
alaEServiceSapCvlanPortStatGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatGreenCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatYellowCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatRedCount"))
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatGroup.setStatus("current")

alaEServiceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 10)
)
alaEServiceInfoGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceMode"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatReset"))
)
if mibBuilder.loadTexts:
    alaEServiceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1EServiceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 2, 1)
)
alcatelIND1EServiceMIBCompliance.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceInfoGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-E-SERVICE-MIB",
    **{"AlaEServiceUNIProfileProtocolTreatment": AlaEServiceUNIProfileProtocolTreatment,
       "alcatelIND1EServiceMIB": alcatelIND1EServiceMIB,
       "alcatelIND1eServiceMIBObjects": alcatelIND1eServiceMIBObjects,
       "alaEService": alaEService,
       "alaEServiceInfo": alaEServiceInfo,
       "alaEServiceMode": alaEServiceMode,
       "alaEServiceStatReset": alaEServiceStatReset,
       "alaEServiceSapProfileTable": alaEServiceSapProfileTable,
       "alaEServiceSapProfileEntry": alaEServiceSapProfileEntry,
       "alaEServiceSapProfileID": alaEServiceSapProfileID,
       "alaEServiceSapProfileCVLANTreatment": alaEServiceSapProfileCVLANTreatment,
       "alaEServiceSapProfileReplacementCVLAN": alaEServiceSapProfileReplacementCVLAN,
       "alaEServiceSapProfilePriorityMapMode": alaEServiceSapProfilePriorityMapMode,
       "alaEServiceSapProfileFixedPriority": alaEServiceSapProfileFixedPriority,
       "alaEServiceSapProfileIngressBW": alaEServiceSapProfileIngressBW,
       "alaEServiceSapProfileBandwidthShare": alaEServiceSapProfileBandwidthShare,
       "alaEServiceSapProfileRowStatus": alaEServiceSapProfileRowStatus,
       "alaEServiceSapProfileEgressBW": alaEServiceSapProfileEgressBW,
       "alaEServiceSapProfileCIR": alaEServiceSapProfileCIR,
       "alaEServiceSapProfileCBS": alaEServiceSapProfileCBS,
       "alaEServiceSapProfilePIR": alaEServiceSapProfilePIR,
       "alaEServiceSapProfilePBS": alaEServiceSapProfilePBS,
       "alaEServiceUNIProfileTable": alaEServiceUNIProfileTable,
       "alaEServiceUNIProfileEntry": alaEServiceUNIProfileEntry,
       "alaEServiceUNIProfileID": alaEServiceUNIProfileID,
       "alaEServiceUNIProfileStpBpduTreatment": alaEServiceUNIProfileStpBpduTreatment,
       "alaEServiceUNIProfile8021xTreatment": alaEServiceUNIProfile8021xTreatment,
       "alaEServiceUNIProfile8021ABTreatment": alaEServiceUNIProfile8021ABTreatment,
       "alaEServiceUNIProfile8023adTreatment": alaEServiceUNIProfile8023adTreatment,
       "alaEServiceUNIProfileGvrpTreatment": alaEServiceUNIProfileGvrpTreatment,
       "alaEServiceUNIProfileAmapTreatment": alaEServiceUNIProfileAmapTreatment,
       "alaEServiceUNIProfileRowStatus": alaEServiceUNIProfileRowStatus,
       "alaEServiceUNIProfileMvrpTreatment": alaEServiceUNIProfileMvrpTreatment,
       "alaEServiceUNIProfileTunnelMac": alaEServiceUNIProfileTunnelMac,
       "alaEServiceUNIProfileLacpMarkerTreatment": alaEServiceUNIProfileLacpMarkerTreatment,
       "alaEServiceUNIProfileOamTreatment": alaEServiceUNIProfileOamTreatment,
       "alaEServiceUNIProfileCiscoPagpTreatment": alaEServiceUNIProfileCiscoPagpTreatment,
       "alaEServiceUNIProfileCiscoUdldTreatment": alaEServiceUNIProfileCiscoUdldTreatment,
       "alaEServiceUNIProfileCiscoCdpTreatment": alaEServiceUNIProfileCiscoCdpTreatment,
       "alaEServiceUNIProfileCiscoVtpTreatment": alaEServiceUNIProfileCiscoVtpTreatment,
       "alaEServiceUNIProfileCiscoDtpTreatment": alaEServiceUNIProfileCiscoDtpTreatment,
       "alaEServiceUNIProfileCiscoPvstTreatment": alaEServiceUNIProfileCiscoPvstTreatment,
       "alaEServiceUNIProfileCiscoVlanTreatment": alaEServiceUNIProfileCiscoVlanTreatment,
       "alaEServiceUNIProfileCiscoUplinkTreatment": alaEServiceUNIProfileCiscoUplinkTreatment,
       "alaEServiceTable": alaEServiceTable,
       "alaEServiceEntry": alaEServiceEntry,
       "alaEServiceID": alaEServiceID,
       "alaEServiceSVLAN": alaEServiceSVLAN,
       "alaEServiceVlanType": alaEServiceVlanType,
       "alaEServiceRowStatus": alaEServiceRowStatus,
       "alaEServiceStatGreenCount": alaEServiceStatGreenCount,
       "alaEServiceStatYellowCount": alaEServiceStatYellowCount,
       "alaEServiceStatRedCount": alaEServiceStatRedCount,
       "alaEServiceSapTable": alaEServiceSapTable,
       "alaEServiceSapEntry": alaEServiceSapEntry,
       "alaEServiceSapID": alaEServiceSapID,
       "alaEServiceSapServiceID": alaEServiceSapServiceID,
       "alaEServiceSapProfile": alaEServiceSapProfile,
       "alaEServiceSapRowStatus": alaEServiceSapRowStatus,
       "alaEServiceSapCvlanTable": alaEServiceSapCvlanTable,
       "alaEServiceSapCvlanEntry": alaEServiceSapCvlanEntry,
       "alaEServiceSapCvlanSapID": alaEServiceSapCvlanSapID,
       "alaEServiceSapCvlanCvlan": alaEServiceSapCvlanCvlan,
       "alaEServiceSapCvlanMapType": alaEServiceSapCvlanMapType,
       "alaEServiceSapCvlanRowStatus": alaEServiceSapCvlanRowStatus,
       "alaEServicePortTable": alaEServicePortTable,
       "alaEServicePortEntry": alaEServicePortEntry,
       "alaEServicePortID": alaEServicePortID,
       "alaEServicePortType": alaEServicePortType,
       "alaEServicePortVendorTpid": alaEServicePortVendorTpid,
       "alaEServicePortLegacyStpBpdu": alaEServicePortLegacyStpBpdu,
       "alaEServicePortLegacyGvrpPdu": alaEServicePortLegacyGvrpPdu,
       "alaEServicePortUniProfile": alaEServicePortUniProfile,
       "alaEServicePortTransBridging": alaEServicePortTransBridging,
       "alaEServicePortLegacyMvrpPdu": alaEServicePortLegacyMvrpPdu,
       "alaEServiceSapUniTable": alaEServiceSapUniTable,
       "alaEServiceSapUniEntry": alaEServiceSapUniEntry,
       "alaEServiceSapUniSap": alaEServiceSapUniSap,
       "alaEServiceSapUniUni": alaEServiceSapUniUni,
       "alaEServiceSapUniRowStatus": alaEServiceSapUniRowStatus,
       "alaEServiceNniSvlanTable": alaEServiceNniSvlanTable,
       "alaEServiceNniSvlanEntry": alaEServiceNniSvlanEntry,
       "alaEServiceNniSvlanNni": alaEServiceNniSvlanNni,
       "alaEServiceNniSvlanSvlan": alaEServiceNniSvlanSvlan,
       "alaEServiceNniSvlanRowStatus": alaEServiceNniSvlanRowStatus,
       "alaEServiceNniSvlanVpaType": alaEServiceNniSvlanVpaType,
       "alaEServiceSapCvlanPortStatTable": alaEServiceSapCvlanPortStatTable,
       "alaEServiceSapCvlanPortStatEntry": alaEServiceSapCvlanPortStatEntry,
       "alaEServiceSapCvlanPortStatSapID": alaEServiceSapCvlanPortStatSapID,
       "alaEServiceSapCvlanPortStatCvlanID": alaEServiceSapCvlanPortStatCvlanID,
       "alaEServiceSapCvlanPortStatPortID": alaEServiceSapCvlanPortStatPortID,
       "alaEServiceSapCvlanPortStatGreenCount": alaEServiceSapCvlanPortStatGreenCount,
       "alaEServiceSapCvlanPortStatYellowCount": alaEServiceSapCvlanPortStatYellowCount,
       "alaEServiceSapCvlanPortStatRedCount": alaEServiceSapCvlanPortStatRedCount,
       "alcatelIND1EServiceMIBConformance": alcatelIND1EServiceMIBConformance,
       "alcatelIND1EServiceMIBGroups": alcatelIND1EServiceMIBGroups,
       "alaEServiceSapProfileGroup": alaEServiceSapProfileGroup,
       "alaEServiceUNIProfileGroup": alaEServiceUNIProfileGroup,
       "alaEServiceGroup": alaEServiceGroup,
       "alaEServiceSapGroup": alaEServiceSapGroup,
       "alaEServiceSapCvlanGroup": alaEServiceSapCvlanGroup,
       "alaEServicePortGroup": alaEServicePortGroup,
       "alaEServiceSapUniGroup": alaEServiceSapUniGroup,
       "alaEServiceNniSvlanGroup": alaEServiceNniSvlanGroup,
       "alaEServiceSapCvlanPortStatGroup": alaEServiceSapCvlanPortStatGroup,
       "alaEServiceInfoGroup": alaEServiceInfoGroup,
       "alcatelIND1EServiceMIBCompliances": alcatelIND1EServiceMIBCompliances,
       "alcatelIND1EServiceMIBCompliance": alcatelIND1EServiceMIBCompliance}
)
