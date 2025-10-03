# SNMP MIB module (GUDEADS-ETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gude\GUDEADS-ETS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:03 2025
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

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
if mibBuilder.loadTexts:
    gudeads.setRevisions(
        ("2007-05-23 12:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsETS_ObjectIdentity = ObjectIdentity
gadsETS = _GadsETS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4)
)
_EtsEvents_ObjectIdentity = ObjectIdentity
etsEvents = _EtsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 0)
)
_EtsObjects_ObjectIdentity = ObjectIdentity
etsObjects = _EtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1)
)
_EtsSNMPaccess_ObjectIdentity = ObjectIdentity
etsSNMPaccess = _EtsSNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1)
)


class _EtsTrapCtrl_Type(Integer32):
    """Custom type etsTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EtsTrapCtrl_Type.__name__ = "Integer32"
_EtsTrapCtrl_Object = MibScalar
etsTrapCtrl = _EtsTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 1),
    _EtsTrapCtrl_Type()
)
etsTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsTrapCtrl.setStatus("current")
_EtsTrapIPTable_Object = MibTable
etsTrapIPTable = _EtsTrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsTrapIPTable.setStatus("current")
_EtsTrapIPEntry_Object = MibTableRow
etsTrapIPEntry = _EtsTrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1)
)
etsTrapIPEntry.setIndexNames(
    (0, "GUDEADS-ETS-MIB", "etsTrapIPIndex"),
)
if mibBuilder.loadTexts:
    etsTrapIPEntry.setStatus("current")


class _EtsTrapIPIndex_Type(Integer32):
    """Custom type etsTrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EtsTrapIPIndex_Type.__name__ = "Integer32"
_EtsTrapIPIndex_Object = MibTableColumn
etsTrapIPIndex = _EtsTrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 1),
    _EtsTrapIPIndex_Type()
)
etsTrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsTrapIPIndex.setStatus("current")


class _EtsTrapIPAddr_Type(IpAddress):
    """Custom type etsTrapIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_EtsTrapIPAddr_Type.__name__ = "IpAddress"
_EtsTrapIPAddr_Object = MibTableColumn
etsTrapIPAddr = _EtsTrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 2),
    _EtsTrapIPAddr_Type()
)
etsTrapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsTrapIPAddr.setStatus("current")


class _EtsTrapIPPort_Type(Integer32):
    """Custom type etsTrapIPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_EtsTrapIPPort_Type.__name__ = "Integer32"
_EtsTrapIPPort_Object = MibTableColumn
etsTrapIPPort = _EtsTrapIPPort_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 3),
    _EtsTrapIPPort_Type()
)
etsTrapIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsTrapIPPort.setStatus("current")
_EtsPrimPowAvail_Type = Integer32
_EtsPrimPowAvail_Object = MibScalar
etsPrimPowAvail = _EtsPrimPowAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 2),
    _EtsPrimPowAvail_Type()
)
etsPrimPowAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsPrimPowAvail.setStatus("current")
_EtsSecPowAvail_Type = Integer32
_EtsSecPowAvail_Object = MibScalar
etsSecPowAvail = _EtsSecPowAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 3),
    _EtsSecPowAvail_Type()
)
etsSecPowAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsSecPowAvail.setStatus("current")
_EtsSecManualSelect_Type = Integer32
_EtsSecManualSelect_Object = MibScalar
etsSecManualSelect = _EtsSecManualSelect_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 4),
    _EtsSecManualSelect_Type()
)
etsSecManualSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsSecManualSelect.setStatus("current")
_EtsPowerSelect_Type = Integer32
_EtsPowerSelect_Object = MibScalar
etsPowerSelect = _EtsPowerSelect_Object(
    (1, 3, 6, 1, 4, 1, 28507, 4, 1, 5),
    _EtsPowerSelect_Type()
)
etsPowerSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsPowerSelect.setStatus("current")
_EtsConf_ObjectIdentity = ObjectIdentity
etsConf = _EtsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 3)
)
_EtsGroups_ObjectIdentity = ObjectIdentity
etsGroups = _EtsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 3, 1)
)
_EtsCompls_ObjectIdentity = ObjectIdentity
etsCompls = _EtsCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 4, 3, 2)
)

# Managed Objects groups

etsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 4, 3, 1, 1)
)
etsBasicGroup.setObjects(
      *(("GUDEADS-ETS-MIB", "etsPrimPowAvail"),
        ("GUDEADS-ETS-MIB", "etsSecPowAvail"),
        ("GUDEADS-ETS-MIB", "etsSecManualSelect"),
        ("GUDEADS-ETS-MIB", "etsPowerSelect"),
        ("GUDEADS-ETS-MIB", "etsTrapCtrl"),
        ("GUDEADS-ETS-MIB", "etsTrapIPAddr"),
        ("GUDEADS-ETS-MIB", "etsTrapIPPort"))
)
if mibBuilder.loadTexts:
    etsBasicGroup.setStatus("current")


# Notification objects

etsPrimaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 4, 0, 1)
)
etsPrimaryPowerChangeEvt.setObjects(
    ("GUDEADS-ETS-MIB", "etsPrimPowAvail")
)
if mibBuilder.loadTexts:
    etsPrimaryPowerChangeEvt.setStatus(
        "current"
    )

etsSecondaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 4, 0, 2)
)
etsSecondaryPowerChangeEvt.setObjects(
    ("GUDEADS-ETS-MIB", "etsSecPowAvail")
)
if mibBuilder.loadTexts:
    etsSecondaryPowerChangeEvt.setStatus(
        "current"
    )

etsManualSelectEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 4, 0, 3)
)
etsManualSelectEvt.setObjects(
    ("GUDEADS-ETS-MIB", "etsSecManualSelect")
)
if mibBuilder.loadTexts:
    etsManualSelectEvt.setStatus(
        "current"
    )

etsPowerSelectEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 4, 0, 4)
)
etsPowerSelectEvt.setObjects(
    ("GUDEADS-ETS-MIB", "etsPowerSelect")
)
if mibBuilder.loadTexts:
    etsPowerSelectEvt.setStatus(
        "current"
    )


# Notifications groups

etsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 4, 3, 1, 2)
)
etsNotificationGroup.setObjects(
      *(("GUDEADS-ETS-MIB", "etsPrimaryPowerChangeEvt"),
        ("GUDEADS-ETS-MIB", "etsSecondaryPowerChangeEvt"),
        ("GUDEADS-ETS-MIB", "etsManualSelectEvt"),
        ("GUDEADS-ETS-MIB", "etsPowerSelectEvt"))
)
if mibBuilder.loadTexts:
    etsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ETS-MIB",
    **{"gudeads": gudeads,
       "gadsETS": gadsETS,
       "etsEvents": etsEvents,
       "etsPrimaryPowerChangeEvt": etsPrimaryPowerChangeEvt,
       "etsSecondaryPowerChangeEvt": etsSecondaryPowerChangeEvt,
       "etsManualSelectEvt": etsManualSelectEvt,
       "etsPowerSelectEvt": etsPowerSelectEvt,
       "etsObjects": etsObjects,
       "etsSNMPaccess": etsSNMPaccess,
       "etsTrapCtrl": etsTrapCtrl,
       "etsTrapIPTable": etsTrapIPTable,
       "etsTrapIPEntry": etsTrapIPEntry,
       "etsTrapIPIndex": etsTrapIPIndex,
       "etsTrapIPAddr": etsTrapIPAddr,
       "etsTrapIPPort": etsTrapIPPort,
       "etsPrimPowAvail": etsPrimPowAvail,
       "etsSecPowAvail": etsSecPowAvail,
       "etsSecManualSelect": etsSecManualSelect,
       "etsPowerSelect": etsPowerSelect,
       "etsConf": etsConf,
       "etsGroups": etsGroups,
       "etsBasicGroup": etsBasicGroup,
       "etsNotificationGroup": etsNotificationGroup,
       "etsCompls": etsCompls}
)
