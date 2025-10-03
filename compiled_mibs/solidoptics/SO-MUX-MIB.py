# SNMP MIB module (SO-MUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\solidoptics\SO-MUX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:42 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

solidOptics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 51628)
)
if mibBuilder.loadTexts:
    solidOptics.setRevisions(
        ("2020-07-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EdfaMux_ObjectIdentity = ObjectIdentity
edfaMux = _EdfaMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51628, 1)
)


class _DcmDistance_Type(Integer32):
    """Custom type dcmDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_DcmDistance_Type.__name__ = "Integer32"
_DcmDistance_Object = MibScalar
dcmDistance = _DcmDistance_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 1),
    _DcmDistance_Type()
)
dcmDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmDistance.setStatus("current")
_PreEdfaSeqTable_Object = MibTable
preEdfaSeqTable = _PreEdfaSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2)
)
if mibBuilder.loadTexts:
    preEdfaSeqTable.setStatus("current")
_PreEdfaSeqEntry_Object = MibTableRow
preEdfaSeqEntry = _PreEdfaSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1)
)
preEdfaSeqEntry.setIndexNames(
    (0, "SO-MUX-MIB", "preIndex"),
)
if mibBuilder.loadTexts:
    preEdfaSeqEntry.setStatus("current")


class _PreIndex_Type(Integer32):
    """Custom type preIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PreIndex_Type.__name__ = "Integer32"
_PreIndex_Object = MibTableColumn
preIndex = _PreIndex_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1, 1),
    _PreIndex_Type()
)
preIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    preIndex.setStatus("current")
_PrePowerGainValue_Type = OctetString
_PrePowerGainValue_Object = MibTableColumn
prePowerGainValue = _PrePowerGainValue_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1, 2),
    _PrePowerGainValue_Type()
)
prePowerGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prePowerGainValue.setStatus("current")
_PrePowerIn_Type = OctetString
_PrePowerIn_Object = MibTableColumn
prePowerIn = _PrePowerIn_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1, 3),
    _PrePowerIn_Type()
)
prePowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prePowerIn.setStatus("current")
_PrePowerOut_Type = OctetString
_PrePowerOut_Object = MibTableColumn
prePowerOut = _PrePowerOut_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1, 4),
    _PrePowerOut_Type()
)
prePowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prePowerOut.setStatus("current")
_PreTemperature_Type = OctetString
_PreTemperature_Object = MibTableColumn
preTemperature = _PreTemperature_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 2, 1, 5),
    _PreTemperature_Type()
)
preTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preTemperature.setStatus("current")
_PostEdfaSeqTable_Object = MibTable
postEdfaSeqTable = _PostEdfaSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3)
)
if mibBuilder.loadTexts:
    postEdfaSeqTable.setStatus("current")
_PostEdfaSeqEntry_Object = MibTableRow
postEdfaSeqEntry = _PostEdfaSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1)
)
postEdfaSeqEntry.setIndexNames(
    (0, "SO-MUX-MIB", "postIndex"),
)
if mibBuilder.loadTexts:
    postEdfaSeqEntry.setStatus("current")


class _PostIndex_Type(Integer32):
    """Custom type postIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PostIndex_Type.__name__ = "Integer32"
_PostIndex_Object = MibTableColumn
postIndex = _PostIndex_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1, 1),
    _PostIndex_Type()
)
postIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    postIndex.setStatus("current")
_PostPowerGainValue_Type = OctetString
_PostPowerGainValue_Object = MibTableColumn
postPowerGainValue = _PostPowerGainValue_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1, 2),
    _PostPowerGainValue_Type()
)
postPowerGainValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postPowerGainValue.setStatus("current")
_PostPowerIn_Type = OctetString
_PostPowerIn_Object = MibTableColumn
postPowerIn = _PostPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1, 3),
    _PostPowerIn_Type()
)
postPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postPowerIn.setStatus("current")
_PostPowerOut_Type = OctetString
_PostPowerOut_Object = MibTableColumn
postPowerOut = _PostPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1, 4),
    _PostPowerOut_Type()
)
postPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postPowerOut.setStatus("current")
_PostTemperature_Type = OctetString
_PostTemperature_Object = MibTableColumn
postTemperature = _PostTemperature_Object(
    (1, 3, 6, 1, 4, 1, 51628, 1, 3, 1, 5),
    _PostTemperature_Type()
)
postTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postTemperature.setStatus("current")
_EdfaConformance_ObjectIdentity = ObjectIdentity
edfaConformance = _EdfaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51628, 1, 4)
)
_EdfaGroups_ObjectIdentity = ObjectIdentity
edfaGroups = _EdfaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51628, 1, 4, 1)
)
_EdfaCompliances_ObjectIdentity = ObjectIdentity
edfaCompliances = _EdfaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51628, 1, 4, 2)
)

# Managed Objects groups

edfaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 51628, 1, 4, 1, 1)
)
edfaGroup.setObjects(
      *(("SO-MUX-MIB", "dcmDistance"),
        ("SO-MUX-MIB", "prePowerGainValue"),
        ("SO-MUX-MIB", "prePowerIn"),
        ("SO-MUX-MIB", "prePowerOut"),
        ("SO-MUX-MIB", "preTemperature"),
        ("SO-MUX-MIB", "postPowerGainValue"),
        ("SO-MUX-MIB", "postPowerIn"),
        ("SO-MUX-MIB", "postPowerOut"),
        ("SO-MUX-MIB", "postTemperature"))
)
if mibBuilder.loadTexts:
    edfaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

edfaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 51628, 1, 4, 2, 1)
)
edfaCompliance.setObjects(
    ("SO-MUX-MIB", "edfaGroup")
)
if mibBuilder.loadTexts:
    edfaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SO-MUX-MIB",
    **{"solidOptics": solidOptics,
       "edfaMux": edfaMux,
       "dcmDistance": dcmDistance,
       "preEdfaSeqTable": preEdfaSeqTable,
       "preEdfaSeqEntry": preEdfaSeqEntry,
       "preIndex": preIndex,
       "prePowerGainValue": prePowerGainValue,
       "prePowerIn": prePowerIn,
       "prePowerOut": prePowerOut,
       "preTemperature": preTemperature,
       "postEdfaSeqTable": postEdfaSeqTable,
       "postEdfaSeqEntry": postEdfaSeqEntry,
       "postIndex": postIndex,
       "postPowerGainValue": postPowerGainValue,
       "postPowerIn": postPowerIn,
       "postPowerOut": postPowerOut,
       "postTemperature": postTemperature,
       "edfaConformance": edfaConformance,
       "edfaGroups": edfaGroups,
       "edfaGroup": edfaGroup,
       "edfaCompliances": edfaCompliances,
       "edfaCompliance": edfaCompliance}
)
