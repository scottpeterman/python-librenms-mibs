# SNMP MIB module (NETELASTIC-FLEXBNG-IPPOOL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netelastic\NETELASTIC-FLEXBNG-IPPOOL
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:43 2025
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

(bras,) = mibBuilder.importSymbols(
    "NETELASTIC-FLEXBNG-MIB",
    "bras")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ippoolMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ippoolMib.setRevisions(
        ("2015-11-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1)
)
groupEntry.setIndexNames(
    (0, "NETELASTIC-FLEXBNG-IPPOOL", "groupName"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")
_GroupName_Type = String
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1, 1),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_VrfName_Type = String
_VrfName_Object = MibTableColumn
vrfName = _VrfName_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1, 2),
    _VrfName_Type()
)
vrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrfName.setStatus("current")
_GroupValidIpNumber_Type = Unsigned32
_GroupValidIpNumber_Object = MibTableColumn
groupValidIpNumber = _GroupValidIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1, 3),
    _GroupValidIpNumber_Type()
)
groupValidIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupValidIpNumber.setStatus("current")
_GroupUsedIpNumber_Type = Unsigned32
_GroupUsedIpNumber_Object = MibTableColumn
groupUsedIpNumber = _GroupUsedIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1, 4),
    _GroupUsedIpNumber_Type()
)
groupUsedIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUsedIpNumber.setStatus("current")
_GroupAllocatePercent_Type = Unsigned32
_GroupAllocatePercent_Object = MibTableColumn
groupAllocatePercent = _GroupAllocatePercent_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 1, 1, 5),
    _GroupAllocatePercent_Type()
)
groupAllocatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAllocatePercent.setStatus("current")
_SectionTable_Object = MibTable
sectionTable = _SectionTable_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sectionTable.setStatus("current")
_SectionEntry_Object = MibTableRow
sectionEntry = _SectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1)
)
sectionEntry.setIndexNames(
    (0, "NETELASTIC-FLEXBNG-IPPOOL", "groupName"),
    (0, "NETELASTIC-FLEXBNG-IPPOOL", "startIP"),
    (0, "NETELASTIC-FLEXBNG-IPPOOL", "endIP"),
)
if mibBuilder.loadTexts:
    sectionEntry.setStatus("current")
_StartIP_Type = IpAddress
_StartIP_Object = MibTableColumn
startIP = _StartIP_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1, 1),
    _StartIP_Type()
)
startIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startIP.setStatus("current")
_EndIP_Type = IpAddress
_EndIP_Object = MibTableColumn
endIP = _EndIP_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1, 2),
    _EndIP_Type()
)
endIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endIP.setStatus("current")
_SectionTotalIpNumber_Type = Unsigned32
_SectionTotalIpNumber_Object = MibTableColumn
sectionTotalIpNumber = _SectionTotalIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1, 3),
    _SectionTotalIpNumber_Type()
)
sectionTotalIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionTotalIpNumber.setStatus("current")
_SectionIpAllocateNumber_Type = Unsigned32
_SectionIpAllocateNumber_Object = MibTableColumn
sectionIpAllocateNumber = _SectionIpAllocateNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1, 4),
    _SectionIpAllocateNumber_Type()
)
sectionIpAllocateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionIpAllocateNumber.setStatus("current")
_SectionIpAllocatePercent_Type = Unsigned32
_SectionIpAllocatePercent_Object = MibTableColumn
sectionIpAllocatePercent = _SectionIpAllocatePercent_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 2, 1, 5),
    _SectionIpAllocatePercent_Type()
)
sectionIpAllocatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sectionIpAllocatePercent.setStatus("current")
_AllocateStatus_ObjectIdentity = ObjectIdentity
allocateStatus = _AllocateStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 3)
)
_TotalValidIpNumber_Type = Unsigned32
_TotalValidIpNumber_Object = MibScalar
totalValidIpNumber = _TotalValidIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 3, 1),
    _TotalValidIpNumber_Type()
)
totalValidIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalValidIpNumber.setStatus("current")
_TotalUsedIpNumber_Type = Unsigned32
_TotalUsedIpNumber_Object = MibScalar
totalUsedIpNumber = _TotalUsedIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 3, 2),
    _TotalUsedIpNumber_Type()
)
totalUsedIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalUsedIpNumber.setStatus("current")
_TotalAllocatePercent_Type = Unsigned32
_TotalAllocatePercent_Object = MibScalar
totalAllocatePercent = _TotalAllocatePercent_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 2, 3, 3),
    _TotalAllocatePercent_Type()
)
totalAllocatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAllocatePercent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETELASTIC-FLEXBNG-IPPOOL",
    **{"String": String,
       "ippoolMib": ippoolMib,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupName": groupName,
       "vrfName": vrfName,
       "groupValidIpNumber": groupValidIpNumber,
       "groupUsedIpNumber": groupUsedIpNumber,
       "groupAllocatePercent": groupAllocatePercent,
       "sectionTable": sectionTable,
       "sectionEntry": sectionEntry,
       "startIP": startIP,
       "endIP": endIP,
       "sectionTotalIpNumber": sectionTotalIpNumber,
       "sectionIpAllocateNumber": sectionIpAllocateNumber,
       "sectionIpAllocatePercent": sectionIpAllocatePercent,
       "allocateStatus": allocateStatus,
       "totalValidIpNumber": totalValidIpNumber,
       "totalUsedIpNumber": totalUsedIpNumber,
       "totalAllocatePercent": totalAllocatePercent}
)
