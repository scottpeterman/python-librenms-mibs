# SNMP MIB module (DCP-LINKVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-LINKVIEW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:23 2025
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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(InterfaceStatus,
 OpticalPower1Decimal) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "InterfaceStatus",
    "OpticalPower1Decimal")


# MODULE-IDENTITY

dcpLinkview = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dcpLinkview.setRevisions(
        ("2021-02-25 12:00",
         "2018-10-08 14:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DcpFiberLoss(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class DcpFiberAttenuation(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )



class DcpFiberLength(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )



# MIB Managed Objects in the order of their OIDs

_DcpLinkviewObjects_ObjectIdentity = ObjectIdentity
dcpLinkviewObjects = _DcpLinkviewObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1)
)
_DcpLinkviewTable_Object = MibTable
dcpLinkviewTable = _DcpLinkviewTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dcpLinkviewTable.setStatus("current")
_DcpLinkviewEntry_Object = MibTableRow
dcpLinkviewEntry = _DcpLinkviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1)
)
dcpLinkviewEntry.setIndexNames(
    (0, "DCP-LINKVIEW-MIB", "dcpLinkviewIndex"),
)
if mibBuilder.loadTexts:
    dcpLinkviewEntry.setStatus("current")


class _DcpLinkviewIndex_Type(Unsigned32):
    """Custom type dcpLinkviewIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpLinkviewIndex_Type.__name__ = "Unsigned32"
_DcpLinkviewIndex_Object = MibTableColumn
dcpLinkviewIndex = _DcpLinkviewIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 1),
    _DcpLinkviewIndex_Type()
)
dcpLinkviewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpLinkviewIndex.setStatus("current")
_DcpLinkviewLocalHostname_Type = DisplayString
_DcpLinkviewLocalHostname_Object = MibTableColumn
dcpLinkviewLocalHostname = _DcpLinkviewLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 2),
    _DcpLinkviewLocalHostname_Type()
)
dcpLinkviewLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewLocalHostname.setStatus("current")
_DcpLinkviewLocalName_Type = DisplayString
_DcpLinkviewLocalName_Object = MibTableColumn
dcpLinkviewLocalName = _DcpLinkviewLocalName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 3),
    _DcpLinkviewLocalName_Type()
)
dcpLinkviewLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewLocalName.setStatus("current")
_DcpLinkviewLocalStatus_Type = InterfaceStatus
_DcpLinkviewLocalStatus_Object = MibTableColumn
dcpLinkviewLocalStatus = _DcpLinkviewLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 4),
    _DcpLinkviewLocalStatus_Type()
)
dcpLinkviewLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewLocalStatus.setStatus("current")
_DcpLinkviewLocalPower_Type = OpticalPower1Decimal
_DcpLinkviewLocalPower_Object = MibTableColumn
dcpLinkviewLocalPower = _DcpLinkviewLocalPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 5),
    _DcpLinkviewLocalPower_Type()
)
dcpLinkviewLocalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewLocalPower.setStatus("current")
_DcpLinkviewFiberLoss_Type = DcpFiberLoss
_DcpLinkviewFiberLoss_Object = MibTableColumn
dcpLinkviewFiberLoss = _DcpLinkviewFiberLoss_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 6),
    _DcpLinkviewFiberLoss_Type()
)
dcpLinkviewFiberLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberLoss.setStatus("current")
_DcpLinkviewFiberAttenuation_Type = DcpFiberAttenuation
_DcpLinkviewFiberAttenuation_Object = MibTableColumn
dcpLinkviewFiberAttenuation = _DcpLinkviewFiberAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 7),
    _DcpLinkviewFiberAttenuation_Type()
)
dcpLinkviewFiberAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberAttenuation.setStatus("current")
_DcpLinkviewFiberLength_Type = DcpFiberLength
_DcpLinkviewFiberLength_Object = MibTableColumn
dcpLinkviewFiberLength = _DcpLinkviewFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 8),
    _DcpLinkviewFiberLength_Type()
)
dcpLinkviewFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberLength.setStatus("current")


class _DcpLinkviewFiberDispersion_Type(Unsigned32):
    """Custom type dcpLinkviewFiberDispersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_DcpLinkviewFiberDispersion_Type.__name__ = "Unsigned32"
_DcpLinkviewFiberDispersion_Object = MibTableColumn
dcpLinkviewFiberDispersion = _DcpLinkviewFiberDispersion_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 9),
    _DcpLinkviewFiberDispersion_Type()
)
dcpLinkviewFiberDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberDispersion.setStatus("current")
_DcpLinkviewFiberType_Type = DisplayString
_DcpLinkviewFiberType_Object = MibTableColumn
dcpLinkviewFiberType = _DcpLinkviewFiberType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 10),
    _DcpLinkviewFiberType_Type()
)
dcpLinkviewFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberType.setStatus("current")


class _DcpLinkviewFiberDispComp_Type(Integer32):
    """Custom type dcpLinkviewFiberDispComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_DcpLinkviewFiberDispComp_Type.__name__ = "Integer32"
_DcpLinkviewFiberDispComp_Object = MibTableColumn
dcpLinkviewFiberDispComp = _DcpLinkviewFiberDispComp_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 11),
    _DcpLinkviewFiberDispComp_Type()
)
dcpLinkviewFiberDispComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberDispComp.setStatus("current")


class _DcpLinkviewFiberDispFinal_Type(Integer32):
    """Custom type dcpLinkviewFiberDispFinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_DcpLinkviewFiberDispFinal_Type.__name__ = "Integer32"
_DcpLinkviewFiberDispFinal_Object = MibTableColumn
dcpLinkviewFiberDispFinal = _DcpLinkviewFiberDispFinal_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 12),
    _DcpLinkviewFiberDispFinal_Type()
)
dcpLinkviewFiberDispFinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberDispFinal.setStatus("current")


class _DcpLinkviewFiberUtilization_Type(Gauge32):
    """Custom type dcpLinkviewFiberUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DcpLinkviewFiberUtilization_Type.__name__ = "Gauge32"
_DcpLinkviewFiberUtilization_Object = MibTableColumn
dcpLinkviewFiberUtilization = _DcpLinkviewFiberUtilization_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 13),
    _DcpLinkviewFiberUtilization_Type()
)
dcpLinkviewFiberUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewFiberUtilization.setStatus("current")
_DcpLinkviewRemotePower_Type = OpticalPower1Decimal
_DcpLinkviewRemotePower_Object = MibTableColumn
dcpLinkviewRemotePower = _DcpLinkviewRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 14),
    _DcpLinkviewRemotePower_Type()
)
dcpLinkviewRemotePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewRemotePower.setStatus("current")
_DcpLinkviewRemoteName_Type = DisplayString
_DcpLinkviewRemoteName_Object = MibTableColumn
dcpLinkviewRemoteName = _DcpLinkviewRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 15),
    _DcpLinkviewRemoteName_Type()
)
dcpLinkviewRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewRemoteName.setStatus("current")
_DcpLinkviewRemoteHostname_Type = DisplayString
_DcpLinkviewRemoteHostname_Object = MibTableColumn
dcpLinkviewRemoteHostname = _DcpLinkviewRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 1, 1, 1, 16),
    _DcpLinkviewRemoteHostname_Type()
)
dcpLinkviewRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpLinkviewRemoteHostname.setStatus("current")
_DcpLinkviewMIBCompliance_ObjectIdentity = ObjectIdentity
dcpLinkviewMIBCompliance = _DcpLinkviewMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2)
)
_DcpLinkviewMIBGroups_ObjectIdentity = ObjectIdentity
dcpLinkviewMIBGroups = _DcpLinkviewMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 1)
)
_DcpLinkviewMIBCompliances_ObjectIdentity = ObjectIdentity
dcpLinkviewMIBCompliances = _DcpLinkviewMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 2)
)

# Managed Objects groups

dcpLinkviewTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 1, 1)
)
dcpLinkviewTableGroupV1.setObjects(
      *(("DCP-LINKVIEW-MIB", "dcpLinkviewLocalHostname"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalName"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalStatus"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewLocalPower"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberLoss"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberAttenuation"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberLength"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispersion"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberType"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispComp"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberDispFinal"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewFiberUtilization"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewRemotePower"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewRemoteName"),
        ("DCP-LINKVIEW-MIB", "dcpLinkviewRemoteHostname"))
)
if mibBuilder.loadTexts:
    dcpLinkviewTableGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcpLinkviewBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 3, 2, 2, 1)
)
dcpLinkviewBasicComplV1.setObjects(
    ("DCP-LINKVIEW-MIB", "dcpLinkviewTableGroupV1")
)
if mibBuilder.loadTexts:
    dcpLinkviewBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-LINKVIEW-MIB",
    **{"DcpFiberLoss": DcpFiberLoss,
       "DcpFiberAttenuation": DcpFiberAttenuation,
       "DcpFiberLength": DcpFiberLength,
       "dcpLinkview": dcpLinkview,
       "dcpLinkviewObjects": dcpLinkviewObjects,
       "dcpLinkviewTable": dcpLinkviewTable,
       "dcpLinkviewEntry": dcpLinkviewEntry,
       "dcpLinkviewIndex": dcpLinkviewIndex,
       "dcpLinkviewLocalHostname": dcpLinkviewLocalHostname,
       "dcpLinkviewLocalName": dcpLinkviewLocalName,
       "dcpLinkviewLocalStatus": dcpLinkviewLocalStatus,
       "dcpLinkviewLocalPower": dcpLinkviewLocalPower,
       "dcpLinkviewFiberLoss": dcpLinkviewFiberLoss,
       "dcpLinkviewFiberAttenuation": dcpLinkviewFiberAttenuation,
       "dcpLinkviewFiberLength": dcpLinkviewFiberLength,
       "dcpLinkviewFiberDispersion": dcpLinkviewFiberDispersion,
       "dcpLinkviewFiberType": dcpLinkviewFiberType,
       "dcpLinkviewFiberDispComp": dcpLinkviewFiberDispComp,
       "dcpLinkviewFiberDispFinal": dcpLinkviewFiberDispFinal,
       "dcpLinkviewFiberUtilization": dcpLinkviewFiberUtilization,
       "dcpLinkviewRemotePower": dcpLinkviewRemotePower,
       "dcpLinkviewRemoteName": dcpLinkviewRemoteName,
       "dcpLinkviewRemoteHostname": dcpLinkviewRemoteHostname,
       "dcpLinkviewMIBCompliance": dcpLinkviewMIBCompliance,
       "dcpLinkviewMIBGroups": dcpLinkviewMIBGroups,
       "dcpLinkviewTableGroupV1": dcpLinkviewTableGroupV1,
       "dcpLinkviewMIBCompliances": dcpLinkviewMIBCompliances,
       "dcpLinkviewBasicComplV1": dcpLinkviewBasicComplV1}
)
