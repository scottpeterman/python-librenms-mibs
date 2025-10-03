# SNMP MIB module (UBNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubnt\UBNT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:37 2025
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

ubntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1)
)
if mibBuilder.loadTexts:
    ubntMIB.setRevisions(
        ("2021-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ubnt_ObjectIdentity = ObjectIdentity
ubnt = _Ubnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112)
)
_UbntORTable_Object = MibTable
ubntORTable = _UbntORTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1)
)
if mibBuilder.loadTexts:
    ubntORTable.setStatus("current")
_UbntOREntry_Object = MibTableRow
ubntOREntry = _UbntOREntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1)
)
ubntOREntry.setIndexNames(
    (0, "UBNT-MIB", "ubntORIndex"),
)
if mibBuilder.loadTexts:
    ubntOREntry.setStatus("current")


class _UbntORIndex_Type(Integer32):
    """Custom type ubntORIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntORIndex_Type.__name__ = "Integer32"
_UbntORIndex_Object = MibTableColumn
ubntORIndex = _UbntORIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 1),
    _UbntORIndex_Type()
)
ubntORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntORIndex.setStatus("current")
_UbntORID_Type = ObjectIdentifier
_UbntORID_Object = MibTableColumn
ubntORID = _UbntORID_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 2),
    _UbntORID_Type()
)
ubntORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORID.setStatus("current")
_UbntORDescr_Type = DisplayString
_UbntORDescr_Object = MibTableColumn
ubntORDescr = _UbntORDescr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 3),
    _UbntORDescr_Type()
)
ubntORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORDescr.setStatus("current")
_UbntSnmpInfo_ObjectIdentity = ObjectIdentity
ubntSnmpInfo = _UbntSnmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2)
)
_UbntSnmpGroups_ObjectIdentity = ObjectIdentity
ubntSnmpGroups = _UbntSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1)
)
_UbntAirosGroups_ObjectIdentity = ObjectIdentity
ubntAirosGroups = _UbntAirosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2)
)
_UbntAirFiberGroups_ObjectIdentity = ObjectIdentity
ubntAirFiberGroups = _UbntAirFiberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 3)
)
_UbntEdgeMaxGroups_ObjectIdentity = ObjectIdentity
ubntEdgeMaxGroups = _UbntEdgeMaxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 4)
)
_UbntUniFiGroups_ObjectIdentity = ObjectIdentity
ubntUniFiGroups = _UbntUniFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5)
)
_UbntAirVisionGroups_ObjectIdentity = ObjectIdentity
ubntAirVisionGroups = _UbntAirVisionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 6)
)
_UbntMFiGroups_ObjectIdentity = ObjectIdentity
ubntMFiGroups = _UbntMFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 7)
)
_UbntUniTelGroups_ObjectIdentity = ObjectIdentity
ubntUniTelGroups = _UbntUniTelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 8)
)
_UbntAFLTUGroups_ObjectIdentity = ObjectIdentity
ubntAFLTUGroups = _UbntAFLTUGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9)
)
_UiAF60Groups_ObjectIdentity = ObjectIdentity
uiAF60Groups = _UiAF60Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 10)
)
_UbntAirFIBER_ObjectIdentity = ObjectIdentity
ubntAirFIBER = _UbntAirFIBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3)
)
_UbntEdgeMax_ObjectIdentity = ObjectIdentity
ubntEdgeMax = _UbntEdgeMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5)
)
_UbntUniFi_ObjectIdentity = ObjectIdentity
ubntUniFi = _UbntUniFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6)
)
_UbntAirVision_ObjectIdentity = ObjectIdentity
ubntAirVision = _UbntAirVision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 7)
)
_UbntMFi_ObjectIdentity = ObjectIdentity
ubntMFi = _UbntMFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 8)
)
_UbntUniTel_ObjectIdentity = ObjectIdentity
ubntUniTel = _UbntUniTel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 9)
)
_UbntAFLTU_ObjectIdentity = ObjectIdentity
ubntAFLTU = _UbntAFLTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10)
)
_UiAF60_ObjectIdentity = ObjectIdentity
uiAF60 = _UiAF60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11)
)

# Managed Objects groups

ubntORInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 1)
)
ubntORInfoGroup.setObjects(
      *(("UBNT-MIB", "ubntORID"),
        ("UBNT-MIB", "ubntORDescr"))
)
if mibBuilder.loadTexts:
    ubntORInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubntORCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 2)
)
ubntORCompliance.setObjects(
    ("UBNT-MIB", "ubntORInfoGroup")
)
if mibBuilder.loadTexts:
    ubntORCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-MIB",
    **{"ubnt": ubnt,
       "ubntMIB": ubntMIB,
       "ubntORTable": ubntORTable,
       "ubntOREntry": ubntOREntry,
       "ubntORIndex": ubntORIndex,
       "ubntORID": ubntORID,
       "ubntORDescr": ubntORDescr,
       "ubntSnmpInfo": ubntSnmpInfo,
       "ubntSnmpGroups": ubntSnmpGroups,
       "ubntORInfoGroup": ubntORInfoGroup,
       "ubntORCompliance": ubntORCompliance,
       "ubntAirosGroups": ubntAirosGroups,
       "ubntAirFiberGroups": ubntAirFiberGroups,
       "ubntEdgeMaxGroups": ubntEdgeMaxGroups,
       "ubntUniFiGroups": ubntUniFiGroups,
       "ubntAirVisionGroups": ubntAirVisionGroups,
       "ubntMFiGroups": ubntMFiGroups,
       "ubntUniTelGroups": ubntUniTelGroups,
       "ubntAFLTUGroups": ubntAFLTUGroups,
       "uiAF60Groups": uiAF60Groups,
       "ubntAirFIBER": ubntAirFIBER,
       "ubntEdgeMax": ubntEdgeMax,
       "ubntUniFi": ubntUniFi,
       "ubntAirVision": ubntAirVision,
       "ubntMFi": ubntMFi,
       "ubntUniTel": ubntUniTel,
       "ubntAFLTU": ubntAFLTU,
       "uiAF60": uiAF60}
)
